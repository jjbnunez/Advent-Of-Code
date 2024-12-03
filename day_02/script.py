"""
Advent of Code 2024
Day 2: Red-Nosed Reports

Solution written by JJ Nunez.
"""

import os


# Helper functions and classes


# Solver functions

def _solve1(data):
    print(data[0])


def _solve2(data):
    print(data[0])

    # Execution and File I/O


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
