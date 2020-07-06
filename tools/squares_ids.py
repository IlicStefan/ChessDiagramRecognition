################################################################################
from relative_to_absolute_path import get_absolute_path
import json

################################################################################
################################################################################
# Set paths:
dataset_squares: str = "../datasets/squares"
################################################################################
################################################################################


def get_id_to_square_dict() -> dict:
    result = {}
    squares_ids = get_squares_ids()
    for square_color, pieces in squares_ids.items():
        for piece, piece_id in pieces.items():
            result[piece_id] = square_color + "_" + piece

    return result


################################################################################
################################################################################


def get_squares_ids() -> dict:
    """
    :return: squares_ids.json as python dict
    """
    with open(get_absolute_path("squares_ids.json", __file__), encoding="utf-8") as file:
        return json.loads(file.read())


################################################################################
################################################################################


def get_squares_ids_absolute_paths() -> dict:
    squares_ids: dict = get_squares_ids()
    result: dict = {}
    for square_color, pieces in squares_ids.items():
        for piece, piece_id in pieces.items():
            relative_path = dataset_squares + "/" + square_color + "/" + piece
            result[get_absolute_path(relative_path, __file__)] = piece_id

    return result


################################################################################
################################################################################
