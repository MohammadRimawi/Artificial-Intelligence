
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


from PIL import Image
import numpy as np
from skimage import transform

# train_datagen = ImageDataGenerator(
#     rotation_range=15, #range for random rotations
#     rescale=1./255, #rescaling factor to transform every pixel value from range [0,255] -> [0,1]
#     shear_range=0.1, #shear intensity, the image will be distorted along an axis
#     zoom_range=0.2, #zoom in an image
#     horizontal_flip=True, #randomly flip inputs horizontally
#     width_shift_range=0.1, #shift horizontally(left or right)
#     height_shift_range=0.1 #shift vertically(up or down)
# )

# def load(filename):
#    np_image = Image.open(filename)
#    np_image = np.array(np_image).astype('float32')/255
#    np_image = transform.resize(np_image, (256, 256, 3))
#    np_image = np.expand_dims(np_image, axis=0)
#    return np_image

def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(300, 300))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]


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

            Dense(6, activation='softmax') #6 because we have 6 categories
        ])
    return model

new_model = get_model()

# new_model = keras.models.load_model('/home/rimawi/Git repos/Artificial-Intelligence/Trash Classification/model_model.h5')
new_model.load_weights('model.h5')
new_model.compile()
# new_model.summary()

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
            imgpath = "static/"+path
            # img = image.load_img(imgpath, target_size=(300, 300))
            # img = load(imgpath)
            # x = image.img_to_array(img)
            # x = np.expand_dims(x, axis=0)

            # images = np.vstack([x])
            # classes = new_model.predict_classes(images)

             # load a single image
            new_image = load_image(imgpath)

            # check prediction
            pred = new_model.predict_classes(new_image)
            print("****************************************")
            # print(images)
            data = {1: 'glass', 3: 'paper', 0: 'cardboard', 4: 'plastic', 2: 'metal', 5: 'trash'}
            pre = data[pred[0]] 
            # pre='hello'
            print(pred[0],pre)

            return render_template("index.html" ,path = path,pre=pre)
    return render_template("index.html",path = "")


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)