import PIL
from PIL import Image, ImageTk
# import pytesseract
import cv2
from tkinter import *
from image_preprocessing import image_processing, predict

width, height = 400, 300
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

window = Tk()
window.title("ASL CAM")
# window.bind('<Escape>', lambda e: window.quit())
l = Label(window, text="ASL Recognisation", font=("times new roman", 30, "bold"), fg="yellow", bg="black").pack()

lmain = Label(window)
lmain.pack()

start_btn = Button(window, text="Start", font=("times new roman", 25, "bold"), fg="white", bg="grey").place(x=20, y=550)
stop_btn = Button(window, text="Stop", font=("times new roman", 25, "bold"), fg="white", bg="grey").place(x=180, y=550)

word = ''
l1 = Label(window, text="Character", font=("times new roman", 20, "bold")).pack()
l2 = Label(window, text="Word", font=("times new roman", 20, "bold")).pack()
l3 = Label(window, text="Sentence", font=("times new roman", 20, "bold")).pack()
l4 = Label(window)


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.rectangle(frame, (380 - 1, 10), (620 + 1, 280), (255, 0, 0), 1)
    roi = frame[10:280, 380:620]
    img = image_processing(roi)
    result = predict(img)
    print(chr(result + 64))
    word = result
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    l4.configure(text=word, font=("times new roman", 20, "bold"))
    l4.after(10)
    lmain.after(10, show_frame)


show_frame()
while True:
    window.update()
