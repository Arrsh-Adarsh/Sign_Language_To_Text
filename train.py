# Loading libraries

from tensorflow import keras
# from keras.models import Sequential
# from keras.layers import Convolution2D
# from keras.layers import MaxPooling2D
# from keras.layers import Flatten
# from keras.layers import Dense, Dropout
import os,sys
import cv2
import pandas as pd
import numpy as np
import string


BASEPATH = 'data/model 2'
sys.path.insert(0, BASEPATH)
os.chdir(BASEPATH)

size = 128

# Loading dataset

Xtrain = np.load('Xtrain.npy')
Xtest = np.load('Xtest.npy')
ytrain = pd.read_csv('ytrain.csv')['Symbol']
ytest = pd.read_csv('ytest.csv')['Symbol']

ytrain = pd.get_dummies(ytrain).values
ytest = pd.get_dummies(ytest).values

# CNN model

model = keras.Sequential([
    keras.layers.Conv2D(
        filters=64,
        kernel_size=3,
        activation='relu',
        input_shape=(128, 128, 1)
    ),  # conv2d 1
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(
        filters=64,
        kernel_size=3,
        activation='relu',
        input_shape=(128, 128, 1)
    ),  # conv2d 2
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    keras.layers.Dropout(0.5),

    keras.layers.Conv2D(
        filters=128,
        kernel_size=3,
        activation='relu',
        input_shape=(128, 128, 1)
    ),  # conv2d 3
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(
        filters=128,
        kernel_size=3,
        activation='relu',
        input_shape=(128, 128, 1)
    ),  # conv2d 4
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    keras.layers.Dropout(0.5),

    keras.layers.Conv2D(
        filters=256,
        kernel_size=3,
        activation='relu',
        input_shape=(128, 128, 1)
    ),  # conv2d 5
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(
        filters=256,
        kernel_size=3,
        activation='relu',
        input_shape=(128, 128, 1)
    ),  # conv2d 6
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    keras.layers.Dropout(0.5),

    keras.layers.Conv2D(
        filters=512,
        kernel_size=3,
        activation='relu',
        input_shape=(128, 128, 1)
    ),  # conv2d 7
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(
        filters=512,
        kernel_size=3,
        activation='relu',
        input_shape=(128, 128, 1)
    ),  # conv2d 8
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    keras.layers.Dropout(0.5),

    keras.layers.Flatten(),

    keras.layers.Dense(
        units=256,
        activation='relu'
    ),  # dense 1
    keras.layers.Dropout(0.4),

    keras.layers.Dense(
        units=128,
        activation='relu'
    ),  # dense 2
    keras.layers.Dropout(0.4),

    keras.layers.Dense(
        units=64,
        activation='relu'
    ),  # dense 3
    keras.layers.Dropout(0.5),

    keras.layers.Dense(27, activation='softmax')  # output layer
])

model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x = Xtrain,
               y = ytrain,
               epochs=50,
               batch_size = 32,
               validation_data=(Xtest, ytest))

# Saving the trained model
model.save('Classifier_A_Z.h5')