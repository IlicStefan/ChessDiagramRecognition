################################################################################
# For all diagrams in 'diagrams' crop each square
# and put all squares in 'unlabeled squares'
################################################################################

import cv2
from os import listdir, rename
from os.path import isfile, join

################################################################################
# Set paths:
input_dataset = "../datasets/diagrams/unused"
output_dataset_diagrams = "../datasets/diagrams"
output_dataset = "../datasets/unlabeled_squares"
output_dataset_black = output_dataset + "/black"
output_dataset_white = output_dataset + "/white"
################################################################################


def split(d):
    l = [0]
    i = d / 8
    r = d % 8
    for k in range(8):
        if r > 0:
            l.append((k+1)*i + 1)
            r -= 1
        else:
            l.append((k+1)*i)
    return l


def get_squares(diagram):
    height, width, channels = diagram.shape

    # lists with 9 elements each ( (begin,end) pairs )
    hList = split(height)
    wList = split(width)

    black_squares = []
    white_squares = []

    for i in range(8):
        for j in range(8):
            elem = diagram[hList[i]:hList[i+1], wList[j]:wList[j+1]]
            if (i + j) % 2 == 1:
                black_squares.append(elem)
            else:
                white_squares.append(elem)
                
    return black_squares, white_squares

################################################################################
################################################################################


# Read 'count' from file
count_file = open("count_squares.txt", "r")
count = int(count_file.readline().strip())
count_file.close()
################################################################################

files = [f for f in listdir(input_dataset) if isfile(join(input_dataset, f))]

for f in files:
    diagram = cv2.imread(input_dataset + '/' + f)
    black_squares, white_squares = get_squares(diagram)
    for square in black_squares:
        smallSquare = cv2.resize(square, (32, 32))
        nameOfFile = output_dataset_black + "/square" + str(count + 1) + ".jpg"
        cv2.imwrite(nameOfFile, smallSquare)
        count += 1
    for square in white_squares:
        smallSquare = cv2.resize(square, (32, 32))
        nameOfFile = output_dataset_white + "/square" + str(count + 1) + ".jpg"
        cv2.imwrite(nameOfFile, smallSquare)
        count += 1
    rename(input_dataset + '/' + f,
           output_dataset_diagrams + '/' + f)

################################################################################
# Save counter

countFile = open("count_squares.txt", "w")
countFile.write(str(count))
countFile.close()
################################################################################
