model.save("cnn7.model")

import cv2
import tensorflow as tf 
import numpy as np 

def prepare(filepath):
    IMG_SIZE = 90
    gambarArray = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    gambarArray = np.array(gambarArray).astype(np.float32)
    arraybaru = cv2.resize(gambarArray, (IMG_SIZE, IMG_SIZE))
    return arraybaru.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model("cnn7.model")

prediksi = model.predict([prepare('testkucing3.jpg')])
print(prediksi)
print((CATEGORIES[int(prediksi[0][0])]))