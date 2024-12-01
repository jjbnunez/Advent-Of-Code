"""
Advent of Code 2022
Day 6: Tuning Trouble

Solution written by JJ Nunez.
"""

import os

"""
Helper functions
"""

def _hasDuplicatesAmongFour(a, b, c, d):
	if a == b:
		return True
	if a == c:
		return True
	if a == d:
		return True
	if b == c:
		return True
	if b == d:
		return True
	if c == d:
		return True
	return False

"""
Solver functions
"""
def _solve1(data):
	return

def _solve2(data):
	return

"""
Execution and File I/O
"""
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