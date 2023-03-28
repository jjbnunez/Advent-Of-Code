"""
Advent of Code 2022
Day 8: Treetop Tree House

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
		for char in row:
			print(char, end="")
		print("")
	print("")
	return

def _getRow(data, rowNum):
	row = []
	for char in data[rowNum]:
		row.append(char)
	return row

def _getColumn(data, colNum):
	column = []
	for line in data:
		column.append(line[colNum])
	return column

def _createVisionMatrix(data):
	matrix = []
	for i, line in enumerate(data):
		matrix.append([])
		for char in line:
			matrix[i].append('n')
	return matrix	

def _observeRowFromLeft(data, matrix, rowNum):
	max_height = -1
	row = _getRow(data, rowNum)
	for i, char in enumerate(row):
		val = int(char)
		if val > max_height:
			max_height = val
			matrix[rowNum][i] = 'y'
	return matrix

def _observeRowFromRight(data, matrix, rowNum):
	max_height = -1
	row = _getRow(data, rowNum)
	reversedRow = row[::-1]
	size = len(matrix[rowNum])
	for j, char in enumerate(reversedRow):
		val = int(char)
		if val > max_height:
			max_height = val
			matrix[rowNum][size-j-1] = 'y'
	return matrix

def _observeColumnFromTop(data, matrix, colNum):
	max_height = -1
	column = _getColumn(data, colNum)
	for i, char in enumerate(column):
		val = int(char)
		if val > max_height:
			max_height = val
			matrix[i][colNum] = 'y'
	return matrix

def _observeColumnFromBottom(data, matrix, colNum):
	max_height = -1
	column = _getColumn(data, colNum)
	reversedColumn = column[::-1]
	size = len(reversedColumn)
	for i, char in enumerate(reversedColumn):
		val = int(char)
		if val > max_height:
			max_height = val
			matrix[size-i-1][colNum] = 'y'
	return matrix

def _observeFromTop(data, matrix):
	return matrix

"""
Solver functions
"""
def _solve(data):
	matrix = _createVisionMatrix(data)

	for i, row in enumerate(data):
		matrix = _observeRowFromLeft(data, matrix, i)
		matrix = _observeRowFromRight(data, matrix, i)
	
	for i in range(len(data[0])):
		matrix = _observeColumnFromTop(data, matrix, i)
		matrix = _observeColumnFromBottom(data, matrix, i)

	# PROBLEM 1 SOLUTION
	total_visible_trees = 0
	for i, row in enumerate(matrix):
		for j, column in enumerate(matrix):
			if matrix[i][j] == 'y':
				total_visible_trees += 1
	print("The number of trees visible from outside the grid is:", total_visible_trees)

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