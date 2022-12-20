"""
Day 5: Supply Stacks

Solution written by JJ Nunez.
"""

import sys
import os

# Debug function to show raw string list
# that we read in from the file
def _debugListContents(message, data):
	print(message)
	for line in data:
		print(line)
	print('================')
	return

# Function to read the input data and return
# a list of the lines of the first half of it
def _getCrateData(data):
	crateData = []
	for line in data:
		if line != '':
			crateData.append(line)
		else:
			return crateData

# Function to find where the raw input data
# is bisected
def _getStartIndexForMoveData(data):
	for index, line in enumerate(data):
		if line != '':
			continue
		else:
			return index+1	

# Function to read the input data and return
# a list of the lines of the second half of it
def _getMoveData(data, startIndexForMoveData):
	moveData = []
	for index, line in enumerate(data):
		if index < startIndexForMoveData:
			continue
		else:
			moveData.append(line)
	return moveData

# Function to get the number of stacks from the raw data
def _getStackCount(crateData):
	lengthOfLastLine = len(crateData[-1])
	return int(''.join(crateData[-1][lengthOfLastLine-2]))

# Function to get a list of indices
# for each stack column
def _getStackColumnIndices(crateData):
	line = crateData[-1]
	indices = []
	for index, character in enumerate(line):
		if ''.join(character).isdigit():
			indices.append(index)
	return indices

# Function to get the stack at a given column index
def _getStack(crateData, columnIndex):
	stack = []
	for rowIndex, line in enumerate(reversed(crateData)):
		if rowIndex == 0:
			continue
		if line[columnIndex].isalpha() == False:
			break
		stack.append(line[columnIndex])
	return stack	

# Function to populate an empty stack data structure
def _populateListOfStacks(crateData):
	# We start from the bottom of the raw input data
	# and move our way up.
	# First determine the indices of each column ID.
	stackColumnIndices = _getStackColumnIndices(crateData)
	listOfStacks = []
	for item in stackColumnIndices:
		stack = _getStack(crateData, item)
		listOfStacks.append(stack)
	return listOfStacks

def _populateListOfMoves(moveData):
	counts = []
	froms = []
	tos = []
	for line in moveData:
		tokens = line.split(' ')
		counts.append(int(tokens[1]))
		froms.append(int(tokens[3]))
		tos.append(int(tokens[5]))
	listOfMoves = [counts, froms, tos]
	return listOfMoves

def _runCraneOperations(listOfStacks, listOfMoves):
	stacks = listOfStacks.copy()
	moves = listOfMoves.copy()
	numberOfMoves = len(moves[0])
	for index in range(numberOfMoves):
		count = moves[0][index]
		source = moves[1][index] - 1
		dest = moves[2][index] - 1
		for _ in range(count):
			crate = stacks[source].pop()
			stacks[dest].append(crate)
	return stacks

def _runCraneOperations2(listOfStacks, listOfMoves):
	stacks = listOfStacks.copy()
	moves = listOfMoves.copy()
	numberOfMoves = len(moves[0])
	for index in range(numberOfMoves):
		count = moves[0][index]
		source = moves[1][index] - 1
		dest = moves[2][index] - 1
		group = []
		for _ in range(count):
			crate = stacks[source].pop()
			group.append(crate)
		group.reverse
		for _ in range(count):
			crate = group.pop()
			stacks[dest].append(crate)
	return stacks

def _printTopsOfStacks(stacks):
	for stack in stacks:
		print(stack[-1], end='')
	print()

def solve1(data):
	crateData = _getCrateData(data)
	startIndexForMoveData = _getStartIndexForMoveData(data)
	moveData = _getMoveData(data, startIndexForMoveData)
	listOfStacks = _populateListOfStacks(crateData)
	listOfMoves = _populateListOfMoves(moveData)
	finalListOfStacks = _runCraneOperations(listOfStacks, listOfMoves)
	_printTopsOfStacks(finalListOfStacks)
	return

def solve2(data):
	crateData = _getCrateData(data)
	startIndexForMoveData = _getStartIndexForMoveData(data)
	moveData = _getMoveData(data, startIndexForMoveData)
	listOfStacks = _populateListOfStacks(crateData)
	listOfMoves = _populateListOfMoves(moveData)
	finalListOfStacks = _runCraneOperations2(listOfStacks, listOfMoves)
	_printTopsOfStacks(finalListOfStacks)
	return

def main():
	# Get list of lines from file
	filepath = os.path.realpath(os.path.dirname(__file__)) + '\\' + ''.join(sys.argv[1:])
	with open(filepath, 'r', encoding='utf-8') as file:
		lines = file.readlines()

	# Trim newline characters off the ends
	data = []
	for line in lines:
		data.append(line.replace('\n', ''))

	solve1(data)
	solve2(data)

# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()