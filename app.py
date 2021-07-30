# Loading libraries

import cv2
import operator
import numpy as np
import tkinter as tk
from string import ascii_uppercase
from PIL import Image, ImageTk
from keras.models import load_model
from image_preprocessing import image_processing

# Main Class (Driver Class)

class Main:
    # Constructor
    def __init__(self):
        self.vc = cv2.VideoCapture(0)
        self.models_directory = 'model/'
        self.current_image = None
        self.current_image2 = None
        self.ct = {'blank': 0}
        self.blank_flag = 0
        self.access = False
        for i in ascii_uppercase:
            self.ct[i] = 0

        # Loading Models

        self.model1 = load_model(self.models_directory + 'Classifier_A_Z_5.h5')
        self.model3 = load_model(self.models_directory + 'Classifier_A_Z_4.h5')
        self.model_mnst = load_model(self.models_directory + 'Classifier_mnst.h5')
        self.model_dru = load_model(self.models_directory + 'Classifier_dru.h5')

        # Building User Interface

        self.root = tk.Tk()
        self.root.title('Sign Language to Text Converter')
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.configure(bg='#D9D9D9')
        self.root.geometry("1100x780")
        self.panel = tk.Label(self.root, bg='#D9D9D9')
        self.panel.place(x=140, y=10, width=780, height=640)
        self.panel2 = tk.Label(self.root)
        self.panel2.place(x=545, y=100, width=300, height=300)

        self.T = tk.Label(self.root)
        self.T.place(x=410, y=17)
        self.T.config(text="ASL to TEXT", font=("times new roman", 30, "bold"), bg='#D9D9D9')

        self.sb = tk.Scrollbar(self.root)

        self.T1 = tk.Label(self.root)
        self.T1.place(x=10, y=640)
        self.T1.config(text='Character : ', font=("times new roman", 25, "bold"), bg='#D9D9D9')
        self.panel3 = tk.Label(self.root, bg='#D9D9D9')  # current Symbol
        self.panel3.place(x=500, y=640)

        self.T2 = tk.Label(self.root)
        self.T2.place(x=10, y=680)
        self.T2.config(text='Word : ', font=("times new roman", 25, "bold"), bg='#D9D9D9')
        self.panel4 = tk.Label(self.root, bg='#D9D9D9')  # Word
        self.panel4.place(x=500, y=680)

        self.T3 = tk.Label(self.root)
        self.T3.place(x=10, y=720)
        self.T3.config(text='Sentence : ', font=("times new roman", 25, "bold"), bg='#D9D9D9')
        self.panel5 = tk.Label(self.root, bg='#D9D9D9')  # Word
        self.panel5.place(x=500, y=720)

        self.bt1 = tk.Button(self.root, command=self.about, height=0, width=8)
        self.bt1.config(text='About', font=("times new roman", 15, "bold"))
        self.bt1.place(x=980, y=5)

        self.bt2 = tk.Button(self.root, command=self.start, height=2, width=8, bg='#89ABD9')
        self.bt2.config(text='Start', font=("times new roman", 15, "bold"))
        self.bt2.place(x=920, y=200)

        self.bt3 = tk.Button(self.root, command=self.stop, height=2, width=8, bg='#88bde3')
        self.bt3.config(text='Stop', font=("times new roman", 15, "bold"))
        self.bt3.place(x=920, y=350)

        self.bt4 = tk.Button(self.root, command=self.reset, height=2, width=8, bg='#89ABD9')
        self.bt4.config(text='Reset', font=("times new roman", 15, "bold"))
        self.bt4.place(x=920, y=500)

        self.sent = ''
        self.word = ''
        self.current_symbol = 'Empty'
        self.photo = 'Empty'
        self.display_video()

    def destructor(self):
        print("Closing Application...")
        self.root.destroy()
        self.vc.release()
        cv2.destroyAllWindows()

    def destructor1(self):
        print("Closing Application...")
        self.root1.destroy()

    # Function to show video from webcam

    def display_video(self):
        ret, frame = self.vc.read()
        if ret:
            frame = cv2.flip(frame, 1)
            cv2.rectangle(frame, (335 - 1, 10 - 1), (635 + 1, 310 + 1), (255, 0, 0), 1)

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(image)
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)

            roi = frame[10:310, 335:635]
            img = image_processing(roi)
            if self.access:
                self.predicts(img)

            self.current_image2 = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=self.current_image2)

            self.panel2.imgtk = imgtk
            self.panel2.config(image=imgtk)
            self.panel3.config(text=self.current_symbol, font=("times new roman", 25, "bold"))
            self.panel4.config(text=self.word, font=("times new roman", 25, "bold"))
            self.panel5.config(text=self.sent, font=("times new roman", 25, "bold"))

        self.root.after(10, self.display_video)

    # Predicting and printing the Result

    def predicts(self, image):
        image = cv2.resize(image, (128, 128))

        list1 = ['A', 'B', 'C', 'E', 'F', 'K', 'L', 'T', 'O', 'Q', 'P', 'S', 'T']

        result1 = chr(64 + np.argmax(self.model1.predict(image.reshape(1, 128, 128, 1)), axis=1)[0])
        result3 = chr(64 + np.argmax(self.model3.predict(image.reshape(1, 128, 128, 1)), axis=1)[0])
        result_mnst = np.argmax(self.model_mnst.predict(image.reshape(1, 128, 128, 1)), axis=1)[0]
        result_dru = np.argmax(self.model_dru.predict(image.reshape(1, 128, 128, 1)), axis=1)[0]

        if result3 in ['I', 'J', 'Z', 'Y', 'X']:
            self.current_symbol = result3
        elif result1 in list1:
            self.current_symbol = result1
        else:
            self.current_symbol = result3

        # self.current_symbol = result1
        if self.current_symbol == '@':
            self.current_symbol = 'blank'
        if self.current_symbol in ['M', 'N', 'S', 'T']:
            self.current_symbol = ['M', 'N', 'S', 'T'][result_mnst]
        if self.current_symbol in ['D', 'R', 'U']:
            self.current_symbol = ['D', 'R', 'U'][result_dru]

        # Formatting Output String (word, sentence)

        if self.current_symbol == 'blank':
            for i in ascii_uppercase:
                self.ct[i] = 0
        self.ct[self.current_symbol] += 1
        if self.ct[self.current_symbol] > 25:
            for i in ascii_uppercase:
                if i == self.current_symbol:
                    continue
                tmp = self.ct[self.current_symbol] - self.ct[i]
                if tmp < 0:
                    tmp *= -1
                if tmp <= 10:
                    self.ct['blank'] = 0
                    for i in ascii_uppercase:
                        self.ct[i] = 0
                    return
            self.ct['blank'] = 0
            for i in ascii_uppercase:
                self.ct[i] = 0
            if self.current_symbol == 'blank':
                if self.blank_flag == 0:
                    self.blank_flag = 1
                    if len(self.sent) > 0:
                        self.sent += " "
                    self.sent += self.word
                    self.word = ""
            else:
                if len(self.sent) > 26:
                    self.sent = ""
                self.blank_flag = 0
                self.word += self.current_symbol

    # Member details Window

    def about(self):
        self.root1 = tk.Toplevel(self.root)
        self.root1.title("About")
        self.root1.protocol('WM_SELETE_WINDOW', self.destructor1)
        self.root1.geometry("1100x780")

        self.tx = tk.Label(self.root1)
        self.tx.place(x=450, y=20)
        self.tx.config(text="MEMBERS", fg="red", font=("times new roman", 20, "bold"))

        self.photo1 = tk.PhotoImage(file='pictures/abhay.png')
        self.member1 = tk.Label(self.root1, image=self.photo1)
        self.member1.place(x=80, y=120)
        self.txt1 = tk.Label(self.root1)
        self.txt1.place(x=120, y=330)
        self.txt1.config(text="Abhay Kumar\n1711001", font=("times new roman", 15, "bold"))

        self.photo2 = tk.PhotoImage(file='pictures/adarsh.png')
        self.member2 = tk.Label(self.root1, image=self.photo2)
        self.member2.place(x=420, y=120)
        self.txt2 = tk.Label(self.root1)
        self.txt2.place(x=460, y=330)
        self.txt2.config(text="Adarsh Kumar\n1711002", font=("times new roman", 15, "bold"))

        self.photo3 = tk.PhotoImage(file='pictures/amit.png')
        self.member3 = tk.Label(self.root1, image=self.photo3)
        self.member3.place(x=760, y=120)
        self.txt3 = tk.Label(self.root1)
        self.txt3.place(x=810, y=330)
        self.txt3.config(text="Amit Oraon\n1711003", font=("times new roman", 15, "bold"))

        self.photo4 = tk.PhotoImage(file='pictures/ani.png')
        self.member4 = tk.Label(self.root1, image=self.photo4)
        self.member4.place(x=80, y=420)
        self.txt4 = tk.Label(self.root1)
        self.txt4.place(x=110, y=630)
        self.txt4.config(text="Anibrato Adhikari\n1711004", font=("times new roman", 15, "bold"))

        self.photo5 = tk.PhotoImage(file='pictures/ranjan.png')
        self.member5 = tk.Label(self.root1, image=self.photo5)
        self.member5.place(x=420, y=420)
        self.txt5 = tk.Label(self.root1)
        self.txt5.place(x=440, y=630)
        self.txt5.config(text="Ranjan Kr. Choubey\n1711025", font=("times new roman", 15, "bold"))

        self.photo6 = tk.PhotoImage(file='pictures/tanveer.png')
        self.member6 = tk.Label(self.root1, image=self.photo6)
        self.member6.place(x=760, y=420)
        self.txt6 = tk.Label(self.root1)
        self.txt6.place(x=780, y=630)
        self.txt6.config(text="Tanveer Azam Ansari\n1711038", font=("times new roman", 15, "bold"))

    # To start the prediction

    def start(self):
        self.access = True

    # To stop the prediction

    def stop(self):
        self.current_symbol = 'Empty'
        self.access = False

    # To Reset the predicted strings

    def reset(self):
        self.sent = ''
        self.word = ''
        self.current_symbol = 'Empty'
        self.access = False


# Making Object Of Main Class and Excuting

print('Application Starting...')
start = Main()
start.root.mainloop()
