from relative_to_absolute_path import get_absolute_path
from squares_ids import get_id_to_square_dict
from os.path import exists
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
################################################################################
# Set paths:
dataset_squares: str = "../datasets/squares.csv"
################################################################################


def get_square_name_from_id(identifier: int) -> str:
    d = get_id_to_square_dict()
    return d[identifier]


def load_data():
    absolute_path = get_absolute_path(dataset_squares, __file__)
    assert exists(absolute_path), "'%s' must be a valid directory path" % absolute_path
    squares_data = np.genfromtxt(absolute_path, delimiter=",", dtype=np.uint8)
    return squares_data


class Application(tk.Frame):
    def __init__(self, root):
        squares_data = load_data()
        self.X = squares_data[:, 1:].reshape((-1, 32, 32))
        self.Y = squares_data[:, 0]
        self.root = root
        self.root.title("Squares")
        self.root.geometry("300x200")

        # entry
        self.entry_widget = tk.Entry(root)
        self.entry_widget.insert(tk.END, "0")
        self.entry_widget.place(x=140, y=70, width=100)

        # button
        self.show_image_button = tk.Button(
            self.root,
            text="Show Image",
            command=lambda: self.show_image(self.entry_widget.get())
        )
        self.show_image_button.place(x=140, y=100, width=100)

        # image
        self.canvas = tk.Canvas(self.root, width=32, height=32)
        self.canvas.place(x=10, y=10)
        self.image = ImageTk.PhotoImage(
            image=Image.fromarray(self.X[0, :], "L")
        )
        self.image_on_canvas = self.canvas.create_image(
            0, 0, anchor="nw", image=self.image
        )

        # label
        self.label = tk.Label(
            self.root, text="Square id:\n" + get_square_name_from_id(self.Y[0])
        )
        self.label.place(x=70, y=10)

    def show_image(self, index_str: str):
        m: int = self.X.shape[0]
        if not (str.isdecimal(index_str) and 0 <= int(index_str) < m):
            print("'%s' must be a decimal string between 0 and %d" % (index_str, m-1))
            return

        index_int = int(index_str)
        self.image = ImageTk.PhotoImage(
            image=Image.fromarray(
                self.X[index_int, :],
                "L"
            )
        )
        self.canvas.itemconfig(self.image_on_canvas, image=self.image)
        self.label["text"] = "Square id:\n" + get_square_name_from_id(self.Y[index_int])


def main():
    root = tk.Tk()
    Application(root)
    root.mainloop()


main()
