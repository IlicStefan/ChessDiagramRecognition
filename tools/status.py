################################################################################
# Print number of files for each dataset
################################################################################

from os import listdir, rename
from os.path import isfile, join

################################################################################
# Set paths:
dataset_diagrams = '../datasets/diagrams'
dataset_squares = '../datasets/squares'
################################################################################

def printStatusDiagrams(dataset):
    print '************************************************************'
    print 'D I A G R A M S'
    print ''
    print 'diaagrams: ' + str(len([f for f in listdir(dataset)
                                    if isfile(join(dataset, f))]))
    print '************************************************************'


def printStatusSquares(dataset):
    print '************************************************************'
    print 'S Q U A R E S'
    print ''
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
        "white_rook"
    ]
    printStatusForSquares(dataset, 'black_square', options)
    printStatusForSquares(dataset, 'white_square', options)
    print '************************************************************'

def printStatusForSquares(dataset, color, options):
    print color
    for option in options:
        print '\t' + \
              option + \
              ': ' + \
              str(len([f for f in listdir(dataset + '/' + color + '/' + option) \
                      if isfile(join(dataset + '/' + color + '/' + option, f))]))
    
################################################################################
################################################################################

printStatusDiagrams(dataset_diagrams)
printStatusSquares(dataset_squares)
