"""
Advent of Code 2024
Day 4: Ceres Search

Solution written by JJ Nunez.
"""

import os
from copy import deepcopy

################################################
#                                              #
#         Helper functions and classes         #
#                                              #
################################################


def _getStraightRight(data, horizontal_start, vertical_start):
    horizontal_bound = len(data[0])-1
    horizontal_position_1 = horizontal_start
    horizontal_position_2 = horizontal_start + 1
    horizontal_position_3 = horizontal_start + 2
    horizontal_position_4 = horizontal_start + 3
    vertical_bound = len(data) - 1
    if vertical_start > vertical_bound or vertical_start < 0:
        print("ERROR: vertical starting point is out of bounds")
        return ""


################################################
#                                              #
#               Solver functions               #
#                                              #
################################################


def _solve1(data):
    data_copy = deepcopy(data)


def _solve2(data):
    data_copy = deepcopy(data)

################################################
#                                              #
#            Execution and File I/O            #
#                                              #
################################################


def _readFile(fileName):
    scriptDirectory = os.path.dirname(__file__)
    filePath = os.path.join(scriptDirectory, fileName)
    with open(filePath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        data.append(line.replace('\n', ''))
    return data


def main():
    sampleFileName = 'sample.txt'
    inputFileName = 'input.txt'
    sampleData = _readFile(sampleFileName)
    inputData = _readFile(inputFileName)

    print(sampleFileName)
    _solve1(sampleData)
    # _solve2(sampleData)

    print(inputFileName)
    # _solve1(inputData)
    # _solve2(inputData)


# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()
