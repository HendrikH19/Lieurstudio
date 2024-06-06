import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.utils import to_categorical

# Fungsi untuk memuat data gambar dari folder
def load_data_from_folder(folder_path):
    images = []
    labels = []
    for label in os.listdir(folder_path):
        label_path = os.path.join(folder_path, label)
        for image_filename in os.listdir(label_path):
            image_path = os.path.join(label_path, image_filename)
            image = cv2.imread(image_path)
            image = cv2.resize(image, (100, 100))  # Ubah ukuran gambar sesuai kebutuhan Anda
            image = img_to_array(image)
            images.append(image)
            labels.append(label)
    return np.array(images), np.array(labels)

# Lokasi folder data train dan data test
train_folder = r'D:\SKRIPSI\deteksimuka-nama-dataset\dataset\Train'
test_folder = r'D:\SKRIPSI\deteksimuka-nama-dataset\dataset\Testing'

# Memuat data train dan test dari folder
train_images, train_labels = load_data_from_folder(train_folder)
test_images, test_labels = load_data_from_folder(test_folder)

# Normalisasi data gambar
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Mengubah label menjadi one-hot encoding
num_classes = len(np.unique(train_labels))
train_labels = to_categorical(train_labels, num_classes)
test_labels = to_categorical(test_labels, num_classes)

# Membagi data train menjadi data train dan validasi
train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.2, random_state=42)

# Membuat model CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Menampilkan arsitektur model
model.summary()

# Mengkompilasi model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Melatih model dengan data gambar
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(val_images, val_labels))
