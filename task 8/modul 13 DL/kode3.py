import numpy as np 
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "Hewan"
CATEGORIES = ["Anjing", "Kucing"]

for kategori in CATEGORIES:
    masukDirektori = os.path.join(DATADIR, kategori)

    for gambar in os.listdir(masukDirektori):
        gambarArray= cv2.imread(os.path.join(masukDirektori,gambar), cv2.IMREAD.GRAYSCALE)
        arraybaru = cv2.resize(gambarArray, (UKURAN_GAMBAR, UKURAN_GAMBAR))
        plt.imshow(arraybaru, cmap="gray")
        plt.show()