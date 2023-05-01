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

pickleIn = open("X.pickle", "rb")
X =  pickle.load(pickleIn)
X[1]