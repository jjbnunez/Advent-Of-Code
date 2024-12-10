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


def _xmas_string_exists(data, x_start, y_start, x_step, y_step):

    # Check if parameters are good before doing work

    if x_step > 1 or x_step < -1:
        print("ERROR: horizontal step is invalid")
        return 0

    if y_step > 1 or y_step < -1:
        print("ERROR: vertical step is invalid")
        return 0

    y_bound = len(data) - 1
    if y_start > y_bound or y_start < 0:
        print("ERROR: vertical starting point is out of bounds")
        return 0

    x_bound = len(data[y_start]) - 1
    if x_start > x_bound or x_start < 0:
        print("ERROR: horizontal starting point is out of bounds")
        return 0

    # Stop doing work if things will come out of bounds

    if x_step == 1 and x_start + 3 > x_bound:
        return 0
    if x_step == -1 and x_start - 3 < 0:
        return 0
    if y_step == 1 and y_start + 3 > y_bound:
        return 0
    if y_step == -1 and y_start - 3 < 0:
        return 0

    string = ""
    for i in range(4):
        x = x_start + (i * x_step) if x_step != 0 else x_start
        y = y_start + (i * y_step) if y_step != 0 else y_start
        string = string + data[y][x]

    if string == "XMAS":
        return 1
    else:
        return 0


def _cross_mas_string_exists(data, x_start, y_start):

    # check if parameters are good before doing work

    y_bound = len(data) - 1
    if y_start >= y_bound or y_start < 1:
        # print("ERROR: vertical starting point puts grid out of bounds")
        return 0

    x_bound = len(data[y_start]) - 1
    if x_start >= x_bound or x_start < 1:
        # print("ERROR: horizontal starting point puts grid out of bounds")
        return 0

    # do work

    string1 = data[y_start - 1][x_start - 1]
    string1 = string1 + data[y_start][x_start]
    string1 = string1 + data[y_start + 1][x_start + 1]

    string2 = data[y_start + 1][x_start - 1]
    string2 = string2 + data[y_start][x_start]
    string2 = string2 + data[y_start - 1][x_start + 1]

    if string1 == "MAS" or string1 == "SAM":
        if string2 == "MAS" or string2 == "SAM":
            return 1
    return 0


################################################
#                                              #
#               Solver functions               #
#                                              #
################################################


def _solve1(data):
    data_copy = deepcopy(data)
    xmas_occurrences = 0
    for y in range(len(data_copy)):
        for x in range(len(data_copy[y])):
            if data[y][x] != "X":
                continue
            # straight right
            xmas_occurrences = xmas_occurrences + \
                _xmas_string_exists(data_copy, x, y, 1, 0)
            # down right
            xmas_occurrences = xmas_occurrences + \
                _xmas_string_exists(data_copy, x, y, 1, 1)
            # straight down
            xmas_occurrences = xmas_occurrences + \
                _xmas_string_exists(data_copy, x, y, 0, 1)
            # down left
            xmas_occurrences = xmas_occurrences + \
                _xmas_string_exists(data_copy, x, y, -1, 1)
            # straight left
            xmas_occurrences = xmas_occurrences + \
                _xmas_string_exists(data_copy, x, y, -1, 0)
            # up left
            xmas_occurrences = xmas_occurrences + \
                _xmas_string_exists(data_copy, x, y, -1, -1)
            # straight up
            xmas_occurrences = xmas_occurrences + \
                _xmas_string_exists(data_copy, x, y, 0, -1)
            # up right
            xmas_occurrences = xmas_occurrences + \
                _xmas_string_exists(data_copy, x, y, 1, -1)

    print("TOTAL XMAS OCCURRENCES ", xmas_occurrences)


def _solve2(data):
    data_copy = deepcopy(data)
    cross_mas_occurrences = 0
    for y in range(len(data_copy)):
        for x in range(len(data_copy[y])):
            if data[y][x] != "A":
                continue
            cross_mas_occurrences = cross_mas_occurrences + \
                _cross_mas_string_exists(data_copy, x, y)

    print("TOTAL CROSSMAS OCCURRENCES", cross_mas_occurrences)

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
    _solve2(sampleData)

    print(inputFileName)
    _solve1(inputData)
    _solve2(inputData)


# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()
