################################################################################
# Use this script to classify unlabeled squares
################################################################################
from relative_to_absolute_path import get_absolute_path
import cv2 as cv
import tkinter as tk
from PIL import Image, ImageTk
import sys
from os import listdir
from os.path import isfile, join, exists
import os

################################################################################
# Set paths:
input_dataset: str = get_absolute_path("../datasets/unlabeled_squares/", __file__)
assert exists(input_dataset), "'%s' must be a valid directory path" % input_dataset

output_dataset: str = get_absolute_path("../datasets/squares/", __file__)
assert exists(output_dataset), "'%s' must be a valid directory path" % output_dataset
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
    show_image(path + squares[i])
    
    
def show_image(square_path: str):
    imgtk = load_image(square_path)
    label_image.configure(image=imgtk)
    label_image.image = imgtk


def load_image(square_path: str):
    img = cv.imread(square_path)
    b, g, r = cv.split(img)
    img = cv.merge((r, g, b))
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    return imgtk


################################################################################
################################################################################


if len(sys.argv) < 2:
    print("Usage:\npython classify.py [black|white]")
    sys.exit()

path = input_dataset + sys.argv[1]
squares = [f for f in listdir(path) if isfile(join(path, f))]

if len(squares) == 0:
    print("No more files!")
    sys.exit()

path += "/"

root = tk.Tk()
root.minsize(300, 300)

imgtk = load_image(path + squares[i])
label_image = tk.Label(root, image=imgtk)
label_image.pack()

menu = tk.StringVar(root)
menu.set(OPTIONS[0])
option = tk.OptionMenu(*(root, menu) + tuple(OPTIONS))
option.pack()

button = tk.Button(root, text="classify", command=classify)
button.pack()

root.mainloop()
