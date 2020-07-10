################################################################################
# Main application
################################################################################
from os.path import abspath, dirname, join
import sys
sys.path.insert(0, join(abspath(dirname(__file__)), "../tools"))

from relative_to_absolute_path import get_absolute_path
import tkinter as tk
from PIL import Image, ImageTk
import pytesseract
import cv2 as cv

################################################################################
################################################################################


def load_pieces() -> dict:
    return {
        "bB": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bB.png", __file__)).resize((70, 70))
        ),
        "bK": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bK.png", __file__)).resize((70, 70))
        ),
        "bN": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bN.png", __file__)).resize((70, 70))
        ),
        "bP": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bP.png", __file__)).resize((70, 70))
        ),
        "bQ": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bQ.png", __file__)).resize((70, 70))
        ),
        "bR": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bR.png", __file__)).resize((70, 70))
        ),
        "wB": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wB.png", __file__)).resize((70, 70))
        ),
        "wK": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wK.png", __file__)).resize((70, 70))
        ),
        "wN": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wN.png", __file__)).resize((70, 70))
        ),
        "wP": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wP.png", __file__)).resize((70, 70))
        ),
        "wQ": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wQ.png", __file__)).resize((70, 70))
        ),
        "wR": ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wR.png", __file__)).resize((70, 70))
        ),
    }

################################################################################
################################################################################


class ChessBoard(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.canvas = tk.Canvas(self, width=560, height=560)
        self.canvas.place(x=20, y=20)

        self.board_image = ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/board.jpg", __file__)).resize((560, 560))
        )
        self.canvas.create_image(0, 0, image=self.board_image, anchor=tk.NW)

        # self.pieces = load_pieces()
        # self.showed_pieces = self.pieces["wR"]
        # self.canvas.create_image(0, 0, image=self.rook, anchor=tk.NW)


################################################################################
################################################################################


class LeftSide(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.camera_button = tk.Button(self, text="Open camera", command=self.show_frame)
        self.camera_button.place(x=50, y=20)

        self.browse_button = tk.Button(self, text="Browse file", command=self.show_image)
        self.browse_button.place(x=200, y=20)

        self.image_on_canvas = None
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.place(x=50, y=150)

        self.cv_video_capture = None
        self.video_camera_on = False

    def show_frame(self):
        self.video_camera_on = True
        self.show_video_frame()

    def show_video_frame(self):
        if not self.video_camera_on:
            return
        if not self.cv_video_capture:
            self.cv_video_capture = cv.VideoCapture(0)
            self.cv_video_capture.set(cv.CAP_PROP_FRAME_WIDTH, 400)
            self.cv_video_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 400)

        _, frame = self.cv_video_capture.read()
        frame = cv.flip(frame, 1)
        cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        image = Image.fromarray(cv2image)
        image_tk = ImageTk.PhotoImage(image=image)
        self.canvas.delete(tk.ALL)
        self.canvas.image_tk = image_tk
        self.canvas.create_image(0, 0, image=image_tk, anchor=tk.NW)
        if self.cv_video_capture:
            self.canvas.after(10, self.show_video_frame)

    def show_image(self):
        self.video_camera_on = False
        if self.cv_video_capture:
            self.cv_video_capture = self.cv_video_capture.release()
        self.canvas.delete(tk.ALL)
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(title="Select file")
        image_tk = ImageTk.PhotoImage(
            Image.open(file_path).resize((400, 400))
        )
        self.canvas.image_tk = image_tk
        self.canvas.create_image(0, 0, image=image_tk, anchor=tk.NW)


################################################################################
################################################################################


class Application(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.root = root
        self.root.title("Chess Diagram Recognition")
        
        self.left_side = LeftSide(self.root, height=600, width=600)
        self.left_side.place(x=0, y=0)

        self.chess_board = ChessBoard(self.root, height=600, width=600)
        self.chess_board.place(x=600, y=0)


################################################################################
################################################################################


def main():
    root = tk.Tk()
    root.bind("<Escape>", lambda e: root.quit())
    Application(root)
    root.minsize(height=600, width=1200)
    root.maxsize(height=600, width=1200)
    root.mainloop()

################################################################################
################################################################################


main()
