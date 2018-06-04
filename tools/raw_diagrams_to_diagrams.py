################################################################################
# Crop 'diagrams' from 'raw_diagrams'
################################################################################

import numpy as np
import cv2
from os import listdir
from os.path import isfile, join
import sys

sys.path.insert(0, '../src')
from detection import getDiagramPosition
################################################################################
# Set paths:
input_dataset = '../datasets/raw_diagrams'
output_dataset = '../datasets/diagrams'
################################################################################

# functions

################################################################################
################################################################################
# Read 'count' from file

countFile = open(("count_diagrams.txt"), 'r')
count = int(countFile.readline().strip())
countFile.close()
################################################################################

files = [f for f in listdir(input_dataset) if isfile(join(input_dataset, f))]
for f in files:
    raw_diagram = cv2.imread(input_dataset + '/' + f)
    x, y, w, h = getDiagramPosition(raw_diagram)
    nameOfFile = output_dataset + "/d" + str(count + 1) + ".jpg"
    cv2.imwrite(nameOfFile, raw_diagram[y+1:y+h-1, x+1:x+w-1])
    count += 1
    
################################################################################
# Save counter

countFile = open(("count_diagrams.txt"), 'w')
countFile.write(str(count))
countFile.close()
################################################################################
