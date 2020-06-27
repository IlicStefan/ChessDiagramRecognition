################################################################################
# Use this script to classify unlabeled squares
################################################################################

import cv2 as cv
import tkinter as tk
from PIL import Image, ImageTk
import sys
from os import listdir
from os.path import isfile, join
import os

################################################################################
# Set paths:
input_dataset = "../datasets/unlabeled_squares/"
output_dataset = "../datasets/squares/"
################################################################################

OPTIONS = [
    "empty",
    "black_bishop",
    "black_king",
    "black_knight",
    "black_pawn",
    "black_queen",
    "black_rook",
    "white_bishop",
    "white_king",
    "white_knight",
    "white_pawn",
    "white_queen",
    "white_rook"
]

i = 0
################################################################################


def classify():
    global i
    output = output_dataset + sys.argv[1] + "_square/" + menu.get() + "/"
    os.rename(path + squares[i], output + squares[i])
    i = i + 1
    if i >= len(squares):
        print("No more files!")
        sys.exit()
    else:
        print(i, "/", len(squares))
    showImage(path + squares[i])
    
    
def showImage(squarePath):
    imgtk = loadImage(squarePath)
    labelImage.configure(image = imgtk)
    labelImage.image = imgtk


def loadImage(squarePath):
    img = cv.imread(squarePath)
    b, g, r = cv.split(img)
    img = cv.merge((r, g, b))
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    return imgtk

################################################################################
################################################################################
if len(sys.argv) < 2:
    prin("Usage:\npython classify.py [black|white]")
    sys.exit()

path = input_dataset + sys.argv[1]
squares = [f for f in listdir(path) if isfile(join(path, f))]

if len(squares) == 0:
    print("No more files!")
    sys.exit()

path += "/"

root = tkinter.Tk()
root.minsize(300, 300)

imgtk = loadImage(path + squares[i])
labelImage = Tkinter.Label(root, image = imgtk)
labelImage.pack()

menu = Tkinter.StringVar(root)
menu.set(OPTIONS[0])
option = apply(Tkinter.OptionMenu, (root, menu) + tuple(OPTIONS))
option.pack()

button = Tkinter.Button(root, text="classify", command=classify)
button.pack()

root.mainloop()
