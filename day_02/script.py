"""
Advent of Code 2024
Day 2: Red-Nosed Reports

Solution written by JJ Nunez.
"""

import os


# Helper functions and classes


# Solver functions

def _solve1(data):
    reports = []
    for datum in data:
        report = datum.split(" ")
        reports.append(report)

    safe_reports = 0
    for report in reports:
        is_safe = True
        is_ascending = False
        is_descending = False
        previous = -1
        current = -1
        for level in report:
            if previous == -1:
                previous = int(level)
                continue
            if previous != -1 and current == -1:
                current = int(level)
                if previous < current:
                    is_ascending = True
                if previous > current:
                    is_descending = True
                difference = previous - current
                if difference == 0 or difference > 3 or difference < -3:
                    is_safe = False
                continue
            if previous != -1 and current != -1:
                previous = current
                current = int(level)
                if previous < current:
                    is_ascending = True
                if previous > current:
                    is_descending = True
                difference = previous - current
                if difference == 0 or difference > 3 or difference < -3:
                    is_safe = False
        if is_ascending == True and is_descending == True:
            is_safe = False
        if is_safe == True:
            safe_reports = safe_reports + 1

    print(safe_reports)


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
    # _solve2(sampleData)

    print(inputFileName)
    _solve1(inputData)
    # _solve2(inputData)


# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()
