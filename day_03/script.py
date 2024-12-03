"""
Advent of Code 2024
Day 3: Mull It Over

Solution written by JJ Nunez.
"""

import os
from copy import deepcopy

################################################
#                                              #
#         Helper functions and classes         #
#                                              #
################################################


def _identifyMulStarter(datum_substring):
    print(datum_substring)
    for index, character in enumerate(datum_substring):
        if index == 0 and character != "m":
            return False
        if index == 1 and character != "u":
            return False
        if index == 2 and character != "l":
            return False
        if index == 3 and character != "(":
            return False
    return True


def _identifyValidOperator(datum_substring):
    for index, character in enumerate(datum_substring):

        # def _isReportSafe(report):

        ################################################
        #                                              #
        #               Solver functions               #
        #                                              #
        ################################################


def _solve1(data):
    data_copy = deepcopy(data)

    for datum in data_copy:
        while len(datum) > 7:
            if _identifyMulStarter(datum):
                print("DEBUG: 'mul(' starter encountered!!!")
                _identifyValidOperator(datum)

            datum = datum[1:]


# def _solve2(data):
#     print(data[0])

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
