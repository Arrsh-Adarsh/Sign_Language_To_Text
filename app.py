import cv2
import operator
import numpy as np
import tkinter as tk
from string import ascii_uppercase
from PIL import Image, ImageTk
from keras.models import load_model

from image_preprocessing import image_processing


class Main:
    def __init__(self):
        self.vc = cv2.VideoCapture(0)
        self.models_directory = 'model/'
        self.current_image = None
        self.current_image2 = None
        self.ct = {'blank': 0}
        self.blank_flag = 0
        for i in ascii_uppercase:
            self.ct[i] = 0

        self.model = load_model(self.models_directory + 'Classifer_A_Z.h5')

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

        self.bt2 = tk.Button(self.root, command=self.about, height=2, width=8, bg='#89ABD9')
        self.bt2.config(text='Start', font=("times new roman", 15, "bold"))
        self.bt2.place(x=920, y=200)

        self.bt3 = tk.Button(self.root, command=self.about, height=2, width=8, bg='#88bde3')
        self.bt3.config(text='Stop', font=("times new roman", 15, "bold"))
        self.bt3.place(x=920, y=350)

        self.bt4 = tk.Button(self.root, command=self.about, height=2, width=8, bg='#89ABD9')
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
        self.root.destroy()

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
            self.predicts(img)

            self.current_image2 = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=self.current_image2)

            self.panel2.imgtk = imgtk
            self.panel2.config(image=imgtk)
            self.panel3.config(text=self.current_symbol, font=("times new roman", 25, "bold"))
            self.panel4.config(text=self.word, font=("times new roman", 25, "bold"))
            self.panel5.config(text=self.sent, font=("times new roman", 25, "bold"))

        self.root.after(30, self.display_video)

    def predicts(self, image):
        image = cv2.resize(image, (128, 128))
        result = np.argmax(self.model.predict(image.reshape(1, 128, 128, 1)), axis=1)[0]
        print(result)

        self.current_symbol = chr(result + 64)
        if self.current_symbol == '@': self.current_symbol = 'blank'

        if self.current_symbol == 'blank':
            for i in ascii_uppercase:
                self.ct[i] = 0
        self.ct[self.current_symbol] += 1
        if self.ct[self.current_symbol] > 50:
            for i in ascii_uppercase:
                if i == self.current_symbol:
                    continue
                tmp = self.ct[self.current_symbol] - self.ct[i]
                if tmp < 0:
                    tmp *= -1
                if tmp <= 20:
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
                if len(self.sent) > 16:
                    self.sent = ""
                self.blank_flag = 0
                self.word += self.current_symbol

    def about(self):
        pass


print('Application Starting...')
start = Main()
start.root.mainloop()
