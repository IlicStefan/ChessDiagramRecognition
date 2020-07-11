################################################################################
# Print number of files for each dataset
################################################################################
from squares_ids import get_squares_ids_absolute_paths
from relative_to_absolute_path import get_absolute_path
from os import listdir
from os.path import isfile, join, basename

################################################################################
################################################################################
# Set paths:
dataset_diagrams: str = get_absolute_path("../datasets/diagrams", __file__)
################################################################################
################################################################################


def print_status_squares() -> None:
    print("************************************************************")
    print("S Q U A R E S")
    print()
    paths: dict = get_squares_ids_absolute_paths()
    count_all: int = 0

    print("black_square:")
    for path in paths:
        if "black_square" in path:
            number_of_squares = len(
                [f for f in listdir(path) if isfile(join(path, f))]
            )
            count_all += number_of_squares
            print("\t" + basename(path), ":", number_of_squares)

    print("white_square:")
    for path in paths:
        if "white_square" in path:
            number_of_squares = len(
                [f for f in listdir(path) if isfile(join(path, f))]
            )
            count_all += number_of_squares
            print("\t" + basename(path), ":", number_of_squares)

    print()
    print("All squares:", count_all)
    print("************************************************************")


################################################################################
################################################################################


def print_status_diagrams(dataset) -> None:
    print("************************************************************")
    print("D I A G R A M S")
    print()
    number_of_diagrams: int = len(
        [f for f in listdir(dataset) if isfile(join(dataset, f))]
    )
    print("diagrams: " + str(number_of_diagrams))
    print("************************************************************")


################################################################################
################################################################################


def main():
    print_status_diagrams(dataset_diagrams)
    print_status_squares()


################################################################################
################################################################################


main()
