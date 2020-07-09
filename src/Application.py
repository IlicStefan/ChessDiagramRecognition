import tkinter as tk
from PIL import Image, ImageTk


def load_pieces() -> dict:
    return {
        "bB": ImageTk.PhotoImage(
            Image.open("resources/pieces/bB.png").resize((70, 70))
        ),
        "bK": ImageTk.PhotoImage(
            Image.open("resources/pieces/bK.png").resize((70, 70))
        ),
        "bN": ImageTk.PhotoImage(
            Image.open("resources/pieces/bN.png").resize((70, 70))
        ),
        "bP": ImageTk.PhotoImage(
            Image.open("resources/pieces/bP.png").resize((70, 70))
        ),
        "bQ": ImageTk.PhotoImage(
            Image.open("resources/pieces/bQ.png").resize((70, 70))
        ),
        "bR": ImageTk.PhotoImage(
            Image.open("resources/pieces/bR.png").resize((70, 70))
        ),
        "wB": ImageTk.PhotoImage(
            Image.open("resources/pieces/wB.png").resize((70, 70))
        ),
        "wK": ImageTk.PhotoImage(
            Image.open("resources/pieces/wK.png").resize((70, 70))
        ),
        "wN": ImageTk.PhotoImage(
            Image.open("resources/pieces/wN.png").resize((70, 70))
        ),
        "wP": ImageTk.PhotoImage(
            Image.open("resources/pieces/wP.png").resize((70, 70))
        ),
        "wQ": ImageTk.PhotoImage(
            Image.open("resources/pieces/wQ.png").resize((70, 70))
        ),
        "wR": ImageTk.PhotoImage(
            Image.open("resources/pieces/wR.png").resize((70, 70))
        ),
    }


class ChessBoard(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.canvas = tk.Canvas(self, width=560, height=560)
        self.canvas.place(x=20, y=20)

        self.board_image = ImageTk.PhotoImage(Image.open("resources/board.jpg").resize((560, 560)))
        self.canvas.create_image(0, 0, image=self.board_image, anchor=tk.NW)

        self.pieces = load_pieces()
        self.rook = self.pieces["wR"]
        self.canvas.create_image(0, 0, image=self.rook, anchor=tk.NW)



################################################################################
################################################################################


class Application(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        self.root = root
        self.root.title("Chess Diagram Recognition")
        
        self.left_side = tk.Frame(self.root, height=600, width=600, background="Red")
        self.left_side.place(x=0, y=0)

        self.chess_board = ChessBoard(self.root, height=600, width=600)
        self.chess_board.place(x=600, y=0)


################################################################################
################################################################################


def main():
    root = tk.Tk()
    Application(root)
    root.minsize(height=600, width=1200)
    root.maxsize(height=600, width=1200)
    root.mainloop()

################################################################################
################################################################################


main()
