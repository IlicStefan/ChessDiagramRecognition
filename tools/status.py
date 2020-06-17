################################################################################
# Print number of files for each dataset
################################################################################

from os import listdir
from os.path import isfile, isdir, join, abspath, dirname

################################################################################
# Set paths:
dataset_diagrams = "../datasets/diagrams"
dataset_squares = "../datasets/squares"
################################################################################


def get_absolute_path(relative_path):
    assert type(relative_path) is str, "relative_path must be a string"
    absolute_path = abspath(dirname(__file__)) + "/" + relative_path
    assert isdir(absolute_path), "'%s' must be a valid directory path" % absolute_path
    return absolute_path


def print_status_diagrams(dataset):
    print("************************************************************")
    print("D I A G R A M S")
    print()
    number_of_diagrams = len(
        [f for f in listdir(dataset) if isfile(join(dataset, f))]
    )
    print("diagrams: " + str(number_of_diagrams))
    print("************************************************************")


def print_status_squares(dataset):
    print("************************************************************")
    print("S Q U A R E S")
    print()
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
    print_status_for_squares(dataset, "black_square", options)
    print_status_for_squares(dataset, "white_square", options)
    print("************************************************************")


def print_status_for_squares(dataset, color, options):
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

################################################################################
################################################################################


def main():
    print_status_diagrams(get_absolute_path(dataset_diagrams))
    print_status_squares(get_absolute_path(dataset_squares))


main()
