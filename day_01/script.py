"""
Advent of Code 2023
Day 1: Trebuchet?!

Solution written by JJ Nunez.
"""

import os


# Helper functions
dictNumericCharacters = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '0': 0,
}

dictNumericStrings = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven':7, 'eight': 8, 'nine': 9, 'zero': 0,
}

dictNumericStringsReversed = {
    'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5,
    'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9, 'orez':0,
}

def _getFirstDigit(datum):
    for character in datum:
        if character.isdigit():
            return character

def _getFirstDigit2(datum):
    lowestNumericString = ''
    lowestIndex = -1
    for string in dictNumericStrings.items():
		index = datum.find
		if datum.find(string) != -1:
			if lowestIndex == -1:

# Solver functions


def _solve1(data):
    digitPairs = []
    for datum in data:
        pair = []
        pair.append(_getFirstDigit(datum))
        pair.append(_getFirstDigit(reversed(datum)))
        digitPairs.append(pair)
    values = []
    for pair in digitPairs:
        value = int(pair[0] + pair[1])
        values.append(value)
    sum = 0
    for value in values:
        sum += value
    print(sum)


def _solve2(data):

	datum = data[0]
	numericStringIndices = []
	for string in numericStrings:
        

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

    print(inputFileName)
    _solve1(inputData)


# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()
