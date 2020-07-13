################################################################################
# Create "squares.csv" file
################################################################################
from squares_ids import get_squares_ids_absolute_paths
from relative_to_absolute_path import get_absolute_path
from os import listdir
from os.path import isfile, join
import numpy as np
import cv2 as cv

################################################################################
################################################################################
# Set paths:
output_file: str = "../datasets/squares.csv"
################################################################################
################################################################################


def get_number_of_squares() -> int:
    result: int = 0
    paths: dict = get_squares_ids_absolute_paths()
    for path in paths:
        result += len(
            [f for f in listdir(path) if isfile(join(path, f))]
        )
    return result


################################################################################
################################################################################


def save_data_as_csv(X, Y, f) -> None:
    np.savetxt(f, np.hstack((Y, X)), fmt="%d", delimiter=",")


################################################################################
################################################################################


def get_data():
    m: int = get_number_of_squares()
    X = np.empty((m, 32 * 32), dtype=np.uint8)
    Y = np.empty((m, 1), dtype=np.uint8)
    paths: dict = get_squares_ids_absolute_paths()
    index: int = 0
    for path, square_id in paths.items():
        for f in listdir(path):
            image = join(path, f)
            assert isfile(image), "'%s' is not a file" % image
            image_np = cv.imread(image, cv.IMREAD_GRAYSCALE)
            X[index, :] = image_np.reshape(1, 32 * 32)
            Y[index, 0] = square_id
            index += 1

    return X, Y


################################################################################
################################################################################


def main():
    X, Y = get_data()
    save_data_as_csv(X, Y, get_absolute_path(output_file, __file__))


################################################################################
################################################################################


main()
