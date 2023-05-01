DATADIR = "Hewan"
CATEGORIES = ["Anjing", "Kucing"]

dataTraining = []
def buatDataTraining():
    for kategori in CATEGORIES:
        masukDirektori = os.path.join(DATADIR, kategori)
        nomorKlasifikasi = CATEGORIES.index(kategori)
        for gambar in os.listdir(masukDirektori):
            try:
                gambarArray = cv2.imread(os.path.join(masukDirektori,gambar),
                 cv2.IMREAD_GRAYSCALE)
                arraybaru = cv2.resize(gambarArray, (UKURAN_GAMBAR, UKURAN_GAMBAR))
                dataTraining.append([arraybaru, nomorKlasifikasi])
            except Exception as e:
                pass
buatDataTraining()
import random

random.shuffle(dataTraining)

X= []
Y= []

for features, label in dataTraining:
    x.append(features)
    y.append(label)

X = np.array(X).reshape(-1, UKURAN_GAMBAR, UKURAN_GAMBAR,1)

import pickle

pickleOut =  open("X.pickle", "wb")
pickle.dump(X, pickleOut)
pickleOut.close()

pickleOut= open("Y.pickle", "wb")
pickle.dump(Y, pickleOut)
pickleOut.close()

import tensorflow as tf 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flattern
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.advanced_activations import LeakyReLU
import pickle

X = pickle.load(open("X.pickle", "rb"))
Y = pickle.load(open("Y.pickle", "rb"))

X=X/255.0

model = Sequential()

model.add(Conv2D(64, (3,3), input_shape = X.shape [1:]))

model.add(Activation("relu"))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flattern())

model.add(Dense(64))
model.add(Dense(1))

model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, Y, batch_size=32, epochs=12, validation_split=0.2)
