#imports
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import keras # neural network models

from PIL import Image

# Potentially useful tools - you do not have to use these
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.utils import to_categorical

IMG_HEIGHT = 100
IMG_WIDTH = 100

CATEGORIES = ['airplane','car','cat','dog','flower','fruit','motorbike','person']

def predict_image(img):

    model = load_model("models/model.h5")
    print("model loaded")

    #preprocess image
    img_resized = img.resize((IMG_WIDTH, IMG_HEIGHT))
    print("resized image")

    img_arr = img_to_array(img_resized)
    print("converted image to array")

    #predict
    prediction = model.predict(np.array([img_arr]))
    print("predicted")

    index = np.argmax(prediction[0])
    
    label = CATEGORIES[index] 

    #convert to category
    return label