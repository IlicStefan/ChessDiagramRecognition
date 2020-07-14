################################################################################
# Crop 'diagrams' from 'raw_diagrams'
################################################################################
from relative_to_absolute_path import get_absolute_path

import sys
sys.path.insert(0, get_absolute_path("../src", __file__))

import cv2 as cv
from os import listdir, remove
from os.path import isfile, join, exists
from detection import get_diagram_position
################################################################################
################################################################################
# Set paths:
input_dataset: str = get_absolute_path("../datasets/raw_diagrams", __file__)
assert exists(input_dataset), "'%s' must be a valid directory path" % input_dataset

output_dataset: str = get_absolute_path("../datasets/unused_diagrams", __file__)
assert exists(output_dataset), "'%s' must be a valid directory path" % output_dataset
################################################################################
################################################################################


# Read 'count' from file
def get_counter() -> int:
    with open(get_absolute_path("count_diagrams.txt", __file__), "r") as counter_file:
        return int(counter_file.readline().strip())


################################################################################
################################################################################


# Save 'count'
def save_counter(count: int) -> None:
    with open(get_absolute_path("count_diagrams.txt", __file__), "w") as counter_file:
        counter_file.write(str(count) + "\n")


################################################################################
################################################################################


def main():
    counter = get_counter()

    files = [f for f in listdir(input_dataset) if isfile(join(input_dataset, f))]
    for f in files:
        raw_diagram = cv.imread(input_dataset + "/" + f)
        diagram_image = get_diagram_position(raw_diagram)
        name_of_file = output_dataset + "/d" + str(counter + 1) + ".jpg"
        cv.imwrite(name_of_file, diagram_image[2: -2, 2: -2])
        remove(input_dataset + "/" + f)
        counter += 1

    save_counter(counter)


################################################################################
################################################################################


main()
