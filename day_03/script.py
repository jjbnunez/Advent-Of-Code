"""
Advent of Code 2024
Day 3: Mull It Over

Solution written by JJ Nunez.
"""

import os
import re
from copy import deepcopy

################################################
#                                              #
#         Helper functions and classes         #
#                                              #
################################################


def _getValidMulOperator(datum_substring):
    regex_pattern = "^mul\([0-9]{1,3},[0-9]{1,3}\)"
    match_found = re.search(regex_pattern, datum_substring)
    if match_found:
        return match_found.group(0)
    else:
        return None


def _getMulOperands(mul_string):
    regex_pattern = "[0-9]{1,3},[0-9]{1,3}"
    pairing = re.search(regex_pattern, mul_string).group(0)
    return pairing.split(",")


# def _isReportSafe(report):

################################################
#                                              #
#               Solver functions               #
#                                              #
################################################


def _solve1(data):
    data_copy = deepcopy(data)

    list_of_operands = []
    for datum in data_copy:
        while len(datum) > 7:
            search_result = _getValidMulOperator(datum)
            if search_result == None:
                datum = datum[1:]
                continue
            operands = _getMulOperands(search_result)
            if operands == None:
                datum = datum[1:]
                continue
            list_of_operands.append(operands)
            datum = datum[1:]

    sum_of_multiplications = 0

    for pair in list_of_operands:
        operand0 = int(pair[0])
        operand1 = int(pair[1])
        result = operand0 * operand1
        sum_of_multiplications = sum_of_multiplications + result

    print(sum_of_multiplications)


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
    _solve1(inputData)
    # _solve2(inputData)


# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()
