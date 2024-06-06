import cv2
import numpy as np
from PIL import Image
import os

path = 'dataset'

# Fungsi untuk mengambil data latih wajah
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faceSamples.append(img_numpy)
        ids.append(id)

    return faceSamples, ids

print("Silahkan tunggu...")
faces, ids = getImagesAndLabels(path)

# Membuat recognizer wajah dengan LBPH
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Melatih recognizer dengan data latih
recognizer.train(faces, np.array(ids))

# Menyimpan model recognizer yang telah dilatih
recognizer.save('D:/SKRIPSI/deteksimuka-nama-dataset/trainer/trainer.yml')

print('\nProses selesai. Total data pelatihan:', len(np.unique(ids)))
