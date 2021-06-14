import os, sys
import cv2
import pandas as pd
import numpy as np
import string

BASEPATH = 'data/'
sys.path.insert(0, BASEPATH)
os.chdir(BASEPATH)

Xtrain = [cv2.resize(np.asarray(cv2.imread('train/' + symbol + '/' + file, cv2.IMREAD_GRAYSCALE)), (128, 128),
                     interpolation=cv2.INTER_CUBIC) for symbol in string.ascii_uppercase for file in
          os.listdir('train/' + symbol)]
ytrain = [symbol for symbol in string.ascii_uppercase for _ in range(len(os.listdir('train/' + symbol)))]
Xtrain1 = [cv2.resize(np.asarray(cv2.imread('train/@/' + file, cv2.IMREAD_GRAYSCALE)), (128, 128),
                      interpolation=cv2.INTER_CUBIC) for file in os.listdir('train/@')]
ytrain1 = ['@' for _ in range(len(os.listdir('train/@')))]


Xtest = [cv2.resize(np.asarray(cv2.imread('test/' + symbol + '/' + file, cv2.IMREAD_GRAYSCALE)), (128, 128),
                    interpolation=cv2.INTER_CUBIC) for symbol in string.ascii_uppercase for file in
         os.listdir('test/' + symbol)]
ytest = [symbol for symbol in string.ascii_uppercase for _ in range(len(os.listdir('test/' + symbol)))]
Xtest1 = [cv2.resize(np.asarray(cv2.imread('test/@/' + file, cv2.IMREAD_GRAYSCALE)), (128, 128),
                     interpolation=cv2.INTER_CUBIC) for file in os.listdir('test/@')]
ytest1 = ['@' for _ in range(len(os.listdir('test/@')))]

Xtrain = Xtrain + Xtrain1
ytrain = ytrain + ytrain1
Xtest = Xtest + Xtest1
ytest = ytest + ytest1

dfTrain = pd.DataFrame()
dfTest = pd.DataFrame()
dfTrain['Symbol'] = ytrain
dfTest['Symbol'] = ytest

Xtrain = np.expand_dims(np.asarray(Xtrain), -1)
Xtest = np.expand_dims(np.asarray(Xtest), -1)

folder = 'model 2/'
if not os.path.exists(folder):
    os.makedirs(folder)
np.save(folder + 'Xtrain.npy', Xtrain)
dfTrain['Symbol'].to_csv(folder + 'ytrain.csv')
np.save(folder + 'Xtest.npy', Xtest)
dfTest['Symbol'].to_csv(folder + 'ytest.csv')
