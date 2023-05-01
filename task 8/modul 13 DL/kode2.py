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
        plt.imshow(gambarArray, cmap="gray")
        plt.show()

    break
print(gambarArray.shape)