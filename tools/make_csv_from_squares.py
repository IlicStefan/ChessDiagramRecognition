################################################################################
# Create "squares.csv" file
################################################################################

import numpy as np
from os import listdir
from os.path import isfile, isdir, join, abspath, dirname

################################################################################
# Set paths:
dataset_squares = "../datasets/squares"
output_file = "../datasets/squares.csv"
################################################################################


def print_status_for_square(dataset, color, options):
    print(color)
    for option in options:
        print("\t", end="")
        print(option, end="")
        print(": ", end="")
        directory = dataset + "/" + color + "/" + option
        number_of_squares = len(
            [f for f in listdir(directory) if isfile(join(directory, f))]
        )
        print(number_of_squares)


def print_status_squares(dataset):
    options = [
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
        "white_rook",
    ]
    print_status_for_square(dataset, "black_square", options)
    print_status_for_square(dataset, "white_square", options)
    print("************************************************************")


def print_status_diagrams(dataset):
    number_of_diagrams = len(
        [f for f in listdir(dataset) if isfile(join(dataset, f))]
    )
    print("diagrams: " + str(number_of_diagrams))


def save_data_as_csv(X, Y, output_file):
    pass

def get_data_color(color_path, id):
    return 1, 2


def get_data(path):
    X_black, Y_black = get_data_color(path + "black_square", 0)
    X_white, Y_white = get_data_color(path + "white_square", 13)
    return np.concatenate(X_black, X_white), np.concatenate(Y_black, Y_white)


def get_absolute_path(relative_path):
    assert type(relative_path) is str, "relative_path must be a string"
    absolute_path = abspath(dirname(__file__)) + "/" + relative_path
    assert isdir(absolute_path), "'%s' must be a valid directory path" % absolute_path
    return absolute_path

################################################################################
################################################################################


def main():
    X, Y = get_data(get_absolute_path(dataset_squares))
    save_data_as_csv(X, Y, get_absolute_path(output_file))

main()