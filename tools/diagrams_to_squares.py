################################################################################
# For all diagrams in 'diagrams' crop each square
# and put all squares in 'unlabeled squares'
################################################################################
from relative_to_absolute_path import get_absolute_path
import cv2 as cv
from os import listdir, rename
from os.path import isfile, join

################################################################################
# Set paths:
input_dataset = "../datasets/diagrams/unused"
input_dataset = get_absolute_path(input_dataset, __file__)

output_dataset_diagrams = "../datasets/diagrams"
output_dataset_diagrams = get_absolute_path(output_dataset_diagrams, __file__)

output_dataset = "../datasets/unlabeled_squares"
output_dataset = get_absolute_path(output_dataset, __file__)

output_dataset_black = output_dataset + "/black"
output_dataset_white = output_dataset + "/white"
################################################################################


# Read 'count' from file
def get_counter() -> int:
    count_file = open("count_squares.txt", "r")
    count = int(count_file.readline().strip())
    count_file.close()
    return count


# Save 'count'
def save_counter(count: int) -> None:
    count_file = open("count_squares.txt", "w")
    count_file.write(str(count))
    count_file.close()


def split(d: int) -> list:
    result = [0]
    i = d / 8
    r = d % 8
    for k in range(8):
        if r > 0:
            result.append(int((k + 1) * i + 1))
            r -= 1
        else:
            result.append(int((k + 1) * i))

    return result


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
                black_squares.append(elem)
            else:
                white_squares.append(elem)
                
    return black_squares, white_squares


def main():
    count = get_counter()

    files = [f for f in listdir(input_dataset) if isfile(join(input_dataset, f))]

    for f in files:
        diagram = cv.imread(input_dataset + "/" + f)
        black_squares, white_squares = get_squares(diagram)
        for square in black_squares:
            small_square = cv.resize(square, (32, 32))
            name_of_file = output_dataset_black + "/square" + str(count + 1) + ".jpg"
            cv.imwrite(name_of_file, small_square)
            count += 1
        for square in white_squares:
            small_square = cv.resize(square, (32, 32))
            name_of_file = output_dataset_white + "/square" + str(count + 1) + ".jpg"
            cv.imwrite(name_of_file, small_square)
            count += 1
        rename(input_dataset + "/" + f,
               output_dataset_diagrams + "/" + f)

    save_counter(count)


main()
