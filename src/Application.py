################################################################################
# Main application
################################################################################
import queue
import threading
from os.path import abspath, dirname, join
import tkinter as tk
from PIL import Image, ImageTk, ImageOps, UnidentifiedImageError
import cv2 as cv
import numpy as np
import tensorflow as tf
from tensorflow import keras

import sys
sys.path.insert(0, join(abspath(dirname(__file__)), "../tools"))

from detection import get_diagram_position
from relative_to_absolute_path import get_absolute_path
from diagrams_to_squares import get_squares

################################################################################
################################################################################


def load_pieces() -> dict:
    return {
        4: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bB.png", __file__)).resize((70, 70))
        ),
        6: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bK.png", __file__)).resize((70, 70))
        ),
        3: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bN.png", __file__)).resize((70, 70))
        ),
        1: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bP.png", __file__)).resize((70, 70))
        ),
        5: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bQ.png", __file__)).resize((70, 70))
        ),
        2: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/bR.png", __file__)).resize((70, 70))
        ),
        10: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wB.png", __file__)).resize((70, 70))
        ),
        12: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wK.png", __file__)).resize((70, 70))
        ),
        9: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wN.png", __file__)).resize((70, 70))
        ),
        7: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wP.png", __file__)).resize((70, 70))
        ),
        11: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wQ.png", __file__)).resize((70, 70))
        ),
        8: ImageTk.PhotoImage(
            Image.open(get_absolute_path("../resources/pieces/wR.png", __file__)).resize((70, 70))
        ),
    }


################################################################################
################################################################################


class ProcessImage:
    def __init__(self, a_queue):
        self.a_queue = a_queue
        self.black_model = keras.models.load_model(
            get_absolute_path("../resources/black_model.h5", __file__)
        )
        self.white_model = keras.models.load_model(
            get_absolute_path("../resources/white_model.h5", __file__)
        )

    def process(self, np_image):
        np_diagram = get_diagram_position(np_image)
        # is a diagram large enough
        if np_diagram.shape[0] * 5 < np_image.shape[0] or np_diagram.shape[1] * 5 < np_image.shape[1]:
            print("No diagram")
            return None

        result = []
        black_squares, white_squares = get_squares(np_diagram)

        for image, i, j in black_squares:
            image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            square = cv.resize(image_gray, (32, 32)) / 255.0
            y_prob = self.black_model.predict(square.reshape(1, 32, 32, 1))
            y_classes = y_prob.argmax(axis=-1)
            if y_classes[0] != 0:
                result.append((i, j, y_classes[0]))

        for image, i, j in white_squares:
            image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            square = cv.resize(image_gray, (32, 32)) / 255.0
            y_prob = self.white_model.predict(square.reshape(1, 32, 32, 1))
            y_classes = y_prob.argmax(axis=-1)
            if y_classes[0] != 0:
                result.append((i, j, y_classes[0]))

        self.a_queue.put_nowait(result)


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

        self.pieces = load_pieces()
        self.showed_pieces = []

    def clear_board(self):
        for piece_ref in self.showed_pieces:
            self.canvas.delete(piece_ref)
        self.showed_pieces = []

    def set_piece(self, i, j, piece_id):
        piece_ref = self.canvas.create_image(i * 70, j * 70, image=self.pieces[piece_id], anchor=tk.NW)
        self.showed_pieces.append(piece_ref)


################################################################################
################################################################################


class LeftSide(tk.Frame):
    def __init__(self, root, chess_board, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.camera_button = tk.Button(self, text="Open camera", command=self.show_frame)
        self.camera_button.place(x=50, y=20)

        self.browse_button = tk.Button(self, text="Browse file", command=self.show_image)
        self.browse_button.place(x=200, y=20)

        self.image_on_canvas = None
        self.canvas = tk.Canvas(self, width=450, height=450)
        self.canvas.place(x=50, y=100)

        self.cv_video_capture = None
        self.video_camera_on = False

        self.chess_board = chess_board
        self.a_queue = queue.Queue()
        self.process_image = ProcessImage(self.a_queue)
        self.thread = None

    def show_frame(self):
        self.video_camera_on = True
        self.show_video_frame()

    def show_video_frame(self, counter=1):
        if not self.video_camera_on:
            return
        if not self.cv_video_capture:
            self.cv_video_capture = cv.VideoCapture(0)
            self.cv_video_capture.set(cv.CAP_PROP_FRAME_WIDTH, 450)
            self.cv_video_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 450)

        _, frame = self.cv_video_capture.read()
        # frame = cv.flip(frame, 1)
        cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        if counter == 1:
            self.thread = threading.Thread(target=self.process_image.process, args=(cv2image[..., :3],))
            self.thread.start()
        elif not self.a_queue.empty():
            self.show_pieces(self.a_queue.get(0))
            self.thread = threading.Thread(target=self.process_image.process, args=(cv2image[..., :3],))
            self.thread.start()
        image = Image.fromarray(cv2image)
        image_tk = ImageTk.PhotoImage(image=image)
        self.canvas.delete(tk.ALL)
        self.canvas.image_tk = image_tk
        self.canvas.create_image(0, 0, image=image_tk, anchor=tk.NW)
        if self.cv_video_capture:
            self.canvas.after(20, self.show_video_frame, counter + 1)

    def show_image(self):
        self.video_camera_on = False
        if self.cv_video_capture:
            self.cv_video_capture = self.cv_video_capture.release()
        self.canvas.delete(tk.ALL)
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(title="Select file")
        if file_path:
            try:
                image = Image.open(file_path)
                self.process_image.process(np.array(image)[..., :3])
                self.show_pieces(self.a_queue.get(0))
                image_tk = ImageTk.PhotoImage(image.resize((450, 450)))
                self.canvas.image_tk = image_tk
                self.canvas.create_image(0, 0, image=image_tk, anchor=tk.NW)
            except UnidentifiedImageError:
                pass

    def show_pieces(self, pieces):
        self.chess_board.clear_board()
        for i, j, piece_id in pieces:
            self.chess_board.set_piece(i, j, piece_id)


################################################################################
################################################################################


class Application(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.root = root
        self.root.title("Chess Diagram Recognition")

        self.chess_board = ChessBoard(self.root, height=600, width=600)
        self.chess_board.place(x=600, y=0)

        self.left_side = LeftSide(
            self.root,
            self.chess_board,
            height=600,
            width=600
        )
        self.left_side.place(x=0, y=0)


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
