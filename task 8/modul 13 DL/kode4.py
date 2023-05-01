import numpy as np 
import matplotlib.pyplot as plt
import os
import cv2

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
print(len(dataTraining))