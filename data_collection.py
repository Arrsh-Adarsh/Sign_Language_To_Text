import cv2
import numpy as np
import os
import string
from image_preprocessing import image_processing

# Create the directory structure

if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists("data/train"):
    os.makedirs("data/train")
if not os.path.exists("data/test"):
    os.makedirs("data/test")

if not os.path.exists("data/train/@"):
    os.makedirs("data/train/@")
if not os.path.exists("data/test/@"):
    os.makedirs("data/test/@")

# Directory for Numbers
for i in range(10):
    if not os.path.exists("data/train/" + str(i)):
        os.makedirs("data/train/" + str(i))
    if not os.path.exists("data/test/" + str(i)):
        os.makedirs("data/test/" + str(i))

# Directory for Alphabets
for i in string.ascii_uppercase:
    if not os.path.exists("data/train/" + i):
        os.makedirs("data/train/" + i)
    if not os.path.exists("data/test/" + i):
        os.makedirs("data/test/" + i)

mode = 'train'
directory = 'data/' + mode + '/'
minValue = 70
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open webcam")

while True:
    ret, frame = cap.read()  # read image from video
    frame = cv2.flip(frame, 1)

    cv2.imshow('Live Video (press "ESC" to close)', frame)

    # Forming rectangle
    cv2.rectangle(frame, (350 - 1, 10), (620 + 1, 320), (255, 0, 0), 1)
    roi = frame[10:320, 350:620]

    # Processing image

    # gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(gray, (5, 5), 2)
    # th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # ret, test_image = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    image = image_processing(roi)
    cv2.imshow('processed image', image)
    image = cv2.resize(image, (128, 128))
    img = image

    # Counting number of image in each folder
    # count = {
    #     'zero': len(os.listdir(directory + "/0")),
    #     'one': len(os.listdir(directory + "/1")),
    #     'two': len(os.listdir(directory + "/2")),
    #     'three': len(os.listdir(directory + "/3")),
    #     'four': len(os.listdir(directory + "/4")),
    #     'five': len(os.listdir(directory + "/5")),
    #     'six': len(os.listdir(directory + "/6")),
    #     'seven': len(os.listdir(directory + "/7")),
    #     'eight': len(os.listdir(directory + "/8")),
    #     'nine': len(os.listdir(directory + "/9")),
    #     'a': len(os.listdir(directory + "/A")),
    #     'b': len(os.listdir(directory + "/B")),
    #     'c': len(os.listdir(directory + "/C")),
    #     'd': len(os.listdir(directory + "/D")),
    #     'e': len(os.listdir(directory + "/E")),
    #     'f': len(os.listdir(directory + "/F")),
    #     'g': len(os.listdir(directory + "/G")),
    #     'h': len(os.listdir(directory + "/H")),
    #     'i': len(os.listdir(directory + "/I")),
    #     'j': len(os.listdir(directory + "/J")),
    #     'k': len(os.listdir(directory + "/K")),
    #     'l': len(os.listdir(directory + "/L")),
    #     'm': len(os.listdir(directory + "/M")),
    #     'n': len(os.listdir(directory + "/N")),
    #     'o': len(os.listdir(directory + "/O")),
    #     'p': len(os.listdir(directory + "/P")),
    #     'q': len(os.listdir(directory + "/Q")),
    #     'r': len(os.listdir(directory + "/R")),
    #     's': len(os.listdir(directory + "/S")),
    #     't': len(os.listdir(directory + "/T")),
    #     'u': len(os.listdir(directory + "/U")),
    #     'v': len(os.listdir(directory + "/V")),
    #     'w': len(os.listdir(directory + "/W")),
    #     'x': len(os.listdir(directory + "/X")),
    #     'y': len(os.listdir(directory + "/Y")),
    #     'z': len(os.listdir(directory + "/Z"))
    # }

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # esc key
        break
    if interrupt & 0xFF == ord('@'):
        cv2.imwrite(directory + '@/' + str(len(os.listdir(directory + "/@"))) + '.jpg', img)
        cv2.imwrite(directory + '@/' + str(len(os.listdir(directory + "/@"))) + '.jpg', cv2.flip(img, 1))

    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory + '0/' + str(len(os.listdir(directory + "/0"))) + '.jpg', img)
        cv2.imwrite(directory + '0/' + str(len(os.listdir(directory + "/0"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory + '1/' + str(len(os.listdir(directory + "/1"))) + '.jpg', img)
        cv2.imwrite(directory + '1/' + str(len(os.listdir(directory + "/1"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory + '2/' + str(len(os.listdir(directory + "/2"))) + '.jpg', img)
        cv2.imwrite(directory + '2/' + str(len(os.listdir(directory + "/2"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory + '3/' + str(len(os.listdir(directory + "/3"))) + '.jpg', img)
        cv2.imwrite(directory + '3/' + str(len(os.listdir(directory + "/3"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory + '4/' + str(len(os.listdir(directory + "/4"))) + '.jpg', img)
        cv2.imwrite(directory + '4/' + str(len(os.listdir(directory + "/4"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory + '5/' + str(len(os.listdir(directory + "/5"))) + '.jpg', img)
        cv2.imwrite(directory + '5/' + str(len(os.listdir(directory + "/5"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory + '6/' + str(len(os.listdir(directory + "/6"))) + '.jpg', img)
        cv2.imwrite(directory + '6/' + str(len(os.listdir(directory + "/6"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory + '7/' + str(len(os.listdir(directory + "/7"))) + '.jpg', img)
        cv2.imwrite(directory + '7/' + str(len(os.listdir(directory + "/7"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory + '8/' + str(len(os.listdir(directory + "/8"))) + '.jpg', img)
        cv2.imwrite(directory + '8/' + str(len(os.listdir(directory + "/8"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory + '9/' + str(len(os.listdir(directory + "/9"))) + '.jpg', img)
        cv2.imwrite(directory + '9/' + str(len(os.listdir(directory + "/9"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory + 'A/' + str(len(os.listdir(directory + "/A"))) + '.jpg', img)
        cv2.imwrite(directory + 'A/' + str(len(os.listdir(directory + "/A"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory + 'B/' + str(len(os.listdir(directory + "/B"))) + '.jpg', img)
        cv2.imwrite(directory + 'B/' + str(len(os.listdir(directory + "/B"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory + 'C/' + str(len(os.listdir(directory + "/C"))) + '.jpg', img)
        cv2.imwrite(directory + 'C/' + str(len(os.listdir(directory + "/C"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory + 'D/' + str(len(os.listdir(directory + "/D"))) + '.jpg', img)
        cv2.imwrite(directory + 'D/' + str(len(os.listdir(directory + "/D"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory + 'E/' + str(len(os.listdir(directory + "/E"))) + '.jpg', img)
        cv2.imwrite(directory + 'E/' + str(len(os.listdir(directory + "/E"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory + 'F/' + str(len(os.listdir(directory + "/F"))) + '.jpg', img)
        cv2.imwrite(directory + 'F/' + str(len(os.listdir(directory + "/F"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory + 'G/' + str(len(os.listdir(directory + "/G"))) + '.jpg', img)
        cv2.imwrite(directory + 'G/' + str(len(os.listdir(directory + "/G"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory + 'H/' + str(len(os.listdir(directory + "/H"))) + '.jpg', img)
        cv2.imwrite(directory + 'H/' + str(len(os.listdir(directory + "/H"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory + 'I/' + str(len(os.listdir(directory + "/I"))) + '.jpg', img)
        cv2.imwrite(directory + 'I/' + str(len(os.listdir(directory + "/I"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory + 'J/' + str(len(os.listdir(directory + "/J"))) + '.jpg', img)
        cv2.imwrite(directory + 'J/' + str(len(os.listdir(directory + "/J"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory + 'K/' + str(len(os.listdir(directory + "/K"))) + '.jpg', img)
        cv2.imwrite(directory + 'K/' + str(len(os.listdir(directory + "/K"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory + 'L/' + str(len(os.listdir(directory + "/L"))) + '.jpg', img)
        cv2.imwrite(directory + 'L/' + str(len(os.listdir(directory + "/L"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory + 'M/' + str(len(os.listdir(directory + "/M"))) + '.jpg', img)
        cv2.imwrite(directory + 'M/' + str(len(os.listdir(directory + "/M"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory + 'N/' + str(len(os.listdir(directory + "/N"))) + '.jpg', img)
        cv2.imwrite(directory + 'N/' + str(len(os.listdir(directory + "/N"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory + 'O/' + str(len(os.listdir(directory + "/O"))) + '.jpg', img)
        cv2.imwrite(directory + 'O/' + str(len(os.listdir(directory + "/O"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory + 'P/' + str(len(os.listdir(directory + "/P"))) + '.jpg', img)
        cv2.imwrite(directory + 'P/' + str(len(os.listdir(directory + "/P"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory + 'Q/' + str(len(os.listdir(directory + "/Q"))) + '.jpg', img)
        cv2.imwrite(directory + 'Q/' + str(len(os.listdir(directory + "/Q"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory + 'R/' + str(len(os.listdir(directory + "/R"))) + '.jpg', img)
        cv2.imwrite(directory + 'R/' + str(len(os.listdir(directory + "/R"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory + 'S/' + str(len(os.listdir(directory + "/S"))) + '.jpg', img)
        cv2.imwrite(directory + 'S/' + str(len(os.listdir(directory + "/S"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory + 'T/' + str(len(os.listdir(directory + "/T"))) + '.jpg', img)
        cv2.imwrite(directory + 'T/' + str(len(os.listdir(directory + "/T"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory + 'U/' + str(len(os.listdir(directory + "/U"))) + '.jpg', img)
        cv2.imwrite(directory + 'U/' + str(len(os.listdir(directory + "/U"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory + 'V/' + str(len(os.listdir(directory + "/V"))) + '.jpg', img)
        cv2.imwrite(directory + 'V/' + str(len(os.listdir(directory + "/V"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory + 'W/' + str(len(os.listdir(directory + "/W"))) + '.jpg', img)
        cv2.imwrite(directory + 'W/' + str(len(os.listdir(directory + "/W"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory + 'X/' + str(len(os.listdir(directory + "/X"))) + '.jpg', img)
        cv2.imwrite(directory + 'X/' + str(len(os.listdir(directory + "/X"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory + 'Y/' + str(len(os.listdir(directory + "/Y"))) + '.jpg', img)
        cv2.imwrite(directory + 'Y/' + str(len(os.listdir(directory + "/Y"))) + '.jpg', cv2.flip(img, 1))
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory + 'Z/' + str(len(os.listdir(directory + "/Z"))) + '.jpg', img)
        cv2.imwrite(directory + 'Z/' + str(len(os.listdir(directory + "/Z"))) + '.jpg', cv2.flip(img, 1))

cap.release()
cv2.destroyAllWindows()
