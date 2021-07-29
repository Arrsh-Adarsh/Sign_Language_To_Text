import os, sys
import cv2
import pandas as pd
import numpy as np
import string

BASEPATH = 'data/'
sys.path.insert(0, BASEPATH)
os.chdir(BASEPATH)

# For  {M, N, S, T}

Xtrain = [cv2.resize(np.asarray(cv2.imread('train/' + symbol + '/' + file, cv2.IMREAD_GRAYSCALE)), (128, 128),
                     interpolation=cv2.INTER_CUBIC) for symbol in ['M', 'N', 'S', 'T'] for file in
          os.listdir('train/' + symbol)]
ytrain = [symbol for symbol in ['M', 'N', 'S', 'T'] for _ in range(len(os.listdir('train/' + symbol)))]

Xtest = [cv2.resize(np.asarray(cv2.imread('test/' + symbol + '/' + file, cv2.IMREAD_GRAYSCALE)), (128, 128),
                    interpolation=cv2.INTER_CUBIC) for symbol in ['M', 'N', 'S', 'T'] for file in
         os.listdir('test/' + symbol)]
ytest = [symbol for symbol in ['M', 'N', 'S', 'T'] for _ in range(len(os.listdir('test/' + symbol)))]

# For {D, R, U}

# Xtrain = [cv2.resize(np.asarray(cv2.imread('train/' + symbol + '/' + file, cv2.IMREAD_GRAYSCALE)), (128, 128),
#                      interpolation=cv2.INTER_CUBIC) for symbol in ['D', 'R', 'U'] for file in
#           os.listdir('train/' + symbol)]
# ytrain = [symbol for symbol in ['D', 'R', 'U'] for _ in range(len(os.listdir('train/' + symbol)))]
#
# Xtest = [cv2.resize(np.asarray(cv2.imread('test/' + symbol + '/' + file, cv2.IMREAD_GRAYSCALE)), (128, 128),
#                     interpolation=cv2.INTER_CUBIC) for symbol in ['D', 'R', 'U'] for file in
#          os.listdir('test/' + symbol)]
# ytest = [symbol for symbol in ['D', 'R', 'U'] for _ in range(len(os.listdir('test/' + symbol)))]

dfTrain = pd.DataFrame()
dfTest = pd.DataFrame()
dfTrain['Symbol'] = ytrain
dfTest['Symbol'] = ytest

Xtrain = np.expand_dims(np.asarray(Xtrain), -1)
Xtest = np.expand_dims(np.asarray(Xtest), -1)

folder = 'layer 2/mnst/'                    # For {M, N, S, T}

# folder = 'layer 2/dru/'                   # For {D, R, U}

if not os.path.exists(folder):
    os.makedirs(folder)

np.save(folder + 'Xtrain.npy', Xtrain)
dfTrain['Symbol'].to_csv(folder + 'ytrain.csv')
np.save(folder + 'Xtest.npy', Xtest)
dfTest['Symbol'].to_csv(folder + 'ytest.csv')
