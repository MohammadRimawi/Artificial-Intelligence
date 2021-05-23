
import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

import numpy as np

from tensorflow import keras

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization


def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(300, 300))
    img_tensor = image.img_to_array(img)                   
    img_tensor = np.expand_dims(img_tensor, axis=0)        
    img_tensor /= 255.                                  


    return img_tensor

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

            Dense(6, activation='softmax')
        ])
    return model

new_model = get_model()

new_model.load_weights('model.h5')
new_model.compile()

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
 
        if file.filename == '':
            flash('No selected file')
        if file and allowed_file(file.filename):
            filename =   secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            
            print(filename)
            path = "/uploads/"+str(filename)
            print(path)
            imgpath = "static/"+path

            new_image = load_image(imgpath)


            pred = new_model.predict_classes(new_image)
            print("****************************************")

            data = {1: 'glass', 3: 'paper', 0: 'cardboard', 4: 'plastic', 2: 'metal', 5: 'trash'}
            pre = data[pred[0]] 
            print(pred[0],pre)

            return render_template("index.html" ,path = path,pre=pre)
    return render_template("index.html",path = "")


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)