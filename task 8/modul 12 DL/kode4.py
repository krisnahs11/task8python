import numpy as np 
from google.colab import files
from keras.preprocessing import image
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
%matplotlib inline

upload = files.upload()

for fn in upload.keys():

    path = fn
    img = image.load_img, target_size=(100,150)
    imgplot = plt.imshow(images, batch_size=10)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)

    print(fn)
    if classes[0][0]==1:
        print('rock')
    elif classes[0][1]==1:
        print('paper')
    else:
        print('scissors')