import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model


def image_processing(image):
    minValue = 70
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, test_image = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return test_image


def processing(image):
    return np.expand_dims(np.expand_dims(np.asarray(cv2.resize(image, (128, 128))), 0), -1)


def predict(image):
    img = processing(image)
    model = load_model('model/Classifier_A_Z_5.h5')
    result = np.argmax(model.predict(img), axis=1)[0]
    return result
