# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Inisialisasi objek ImageDataGenerator untuk augmentasi gambar
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

# Memuat dataset training
train_set = train_datagen.flow_from_directory(
    'D:/SKRIPSI/deteksimuka-nama-dataset/dataset/Train',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

# Memuat dataset testing
test_set = test_datagen.flow_from_directory(
    'D:/SKRIPSI/deteksimuka-nama-dataset/dataset/Testing',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

# Inisialisasi model CNN
model = Sequential()

# Menambahkan layer konvolusi
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))

# Menambahkan layer max pooling
model.add(MaxPooling2D(pool_size=(2, 2)))

# Menambahkan layer konvolusi dan max pooling lagi
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Meratakan output menjadi vektor
model.add(Flatten())

# Menambahkan layer dense (fully connected)
model.add(Dense(units=128, activation='relu'))

# Dropout untuk menghindari overfitting
model.add(Dropout(0.5))

# Output layer
model.add(Dense(units=1, activation='sigmoid'))

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Melatih model
model.fit(
    train_set,
    steps_per_epoch=len(train_set),
    epochs=25,
    validation_data=test_set,
    validation_steps=len(test_set))

# Simpan model
model.save('face_verification_model.h5')
