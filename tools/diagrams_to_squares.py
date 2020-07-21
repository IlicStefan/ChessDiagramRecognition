################################################################################
# For all diagrams in 'diagrams' crop each square
# and put all squares in 'unlabeled squares'
################################################################################
from relative_to_absolute_path import get_absolute_path
import cv2 as cv
from os import listdir, rename
from os.path import isfile, join, exists

################################################################################
################################################################################
# Set paths:
input_dataset = get_absolute_path("../datasets/unused_diagrams", __file__)
output_dataset_diagrams = get_absolute_path("../datasets/diagrams", __file__)
output_dataset = get_absolute_path("../datasets/unlabeled_squares", __file__)

output_dataset_black = output_dataset + "/black"
assert exists(output_dataset_black), "'%s' must be a valid directory path" % output_dataset_black

output_dataset_white = output_dataset + "/white"
assert exists(output_dataset_white), "'%s' must be a valid directory path" % output_dataset_white
################################################################################
################################################################################


# Read 'count' from file
def get_counter() -> int:
    with open(get_absolute_path("count_squares.txt", __file__), "r") as counter_file:
        return int(counter_file.readline().strip())


################################################################################
################################################################################


# Save 'count'
def save_counter(count: int) -> None:
    with open(get_absolute_path("count_squares.txt", __file__), "w") as counter_file:
        counter_file.write(str(count) + "\n")


################################################################################
################################################################################


def split(d: int) -> list:
    result = [0]
    i: int = d // 8
    r: int = d % 8
    for k in range(8):
        if r > 0:
            result.append((k + 1) * i + 1)
            r -= 1
        else:
            result.append((k + 1) * i)

    return result


################################################################################
################################################################################


def get_squares(diagram):
    height, width, channels = diagram.shape

    # lists with 9 elements each ( (begin,end) pairs )
    h_list = split(height)
    w_list = split(width)

    black_squares = []
    white_squares = []

    for i in range(8):
        for j in range(8):
            elem = diagram[h_list[i]:h_list[i+1], w_list[j]:w_list[j+1]]
            if (i + j) % 2 == 1:
                black_squares.append((elem, j, i))
            else:
                white_squares.append((elem, j, i))
                
    return black_squares, white_squares


################################################################################
################################################################################


def main():
    counter = get_counter()

    files = [f for f in listdir(input_dataset) if isfile(join(input_dataset, f))]

    for f in files:
        diagram = cv.imread(input_dataset + "/" + f)
        black_squares, white_squares = get_squares(diagram)

        for square, _, _ in black_squares:
            small_square = cv.resize(square, (32, 32))
            name_of_file = output_dataset_black + "/square" + str(counter + 1) + ".jpg"
            cv.imwrite(name_of_file, small_square)
            counter += 1
        for square, _, _ in white_squares:
            small_square = cv.resize(square, (32, 32))
            name_of_file = output_dataset_white + "/square" + str(counter + 1) + ".jpg"
            cv.imwrite(name_of_file, small_square)
            counter += 1

        rename(input_dataset + "/" + f, output_dataset_diagrams + "/" + f)

    save_counter(counter)


################################################################################
################################################################################


main()
