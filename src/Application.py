import tkinter as tk
import cv2 as cv
from PIL import Image, ImageTk


class Application(tk.Frame):
    def __init__(self, root):
        width, height = 800, 600
        self.cap = cv.VideoCapture(0)
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
        self.root = root
        self.root.bind('<Escape>', lambda e: root.quit())
        self.camera_label = tk.Label(root)
        self.camera_label.pack()
        self.show_frame()

    def show_frame(self):
        _, frame = self.cap.read()
        frame = cv.flip(frame, 1)
        cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.camera_label.imgtk = imgtk
        self.camera_label.configure(image=imgtk)
        self.camera_label.after(10, self.show_frame)


def main():
    root = tk.Tk()
    Application(root)
    root.mainloop()


main()