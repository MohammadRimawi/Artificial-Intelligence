
import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

import numpy as np
import pandas as pd 
# import seaborn as sb
from keras.preprocessing.image import ImageDataGenerator, load_img
# from keras.utils import to_categorical
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# import random
import os

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization

from keras.preprocessing import image



def get_model():
    model = Sequential([
            Conv2D(filters=32, kernel_size=3, padding='same', activation='relu', input_shape=(300, 300, 3)),
            BatchNormalization(),
            MaxPooling2D(pool_size=2),
            Dropout(0.25),

            Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'),
            BatchNormalization(),
            MaxPooling2D(pool_size=2),
            Dropout(0.25),
            
            Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'),
            BatchNormalization(),
            MaxPooling2D(pool_size=2),
            Dropout(0.25),
            
            Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'),
            BatchNormalization(),
            MaxPooling2D(pool_size=2),
            Dropout(0.25),

            Flatten(),

            Dense(64, activation='relu'),
            BatchNormalization(),
            Dropout(0.5),

            Dense(6, activation='softmax') #6 because we have 6 categories
        ])
    return model

new_model = get_model()
new_model.compile()
new_model.load_weights('/home/rimawi/Git repos/Artificial-Intelligence/Trash Classification/model.h5')


UPLOAD_FOLDER = '/home/rimawi/Git repos/Artificial-Intelligence/Trash Classification/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
        if file and allowed_file(file.filename):
            filename =   secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            
            print(filename)
            path = "/uploads/"+str(filename)
            print(path)

            img = image.load_img("/home/rimawi/Git repos/Artificial-Intelligence//Trash Classification/static/"+path, target_size=(300, 300))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)

            images = np.vstack([x])
            classes = new_model.predict_classes(images, batch_size=10)
            print("****************************************")
            data = {0: 'glass', 1: 'paper', 2: 'cardboard', 3: 'plastic', 4: 'metal', 5: 'trash'}
            pre = data[classes[0]] 
            print(pre)

            return render_template("index.html" ,path = path,pre=pre)
    return render_template("index.html",path = "")


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)