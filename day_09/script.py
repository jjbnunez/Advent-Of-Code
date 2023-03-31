"""
Advent of Code 2022
Day 9: Rope Bridge

Solution written by JJ Nunez.
"""

"""
Import statements
"""
import os

"""
Custom classes
"""

"""
Helper functions
"""
def _debugPrint2dList(matrix):
	for i, row in enumerate(matrix):
		for element in row:
			print(str(element), end="")
		print("")
	print("")
	return

"""
Solver functions
"""
def _solve(data):
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
	_solve(sampleData)

	print(inputFileName)
	_solve(inputData)

# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()