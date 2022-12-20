"""
Day 5: Supply Stacks

Solution written by JJ Nunez.
"""

import sys

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

# Function to prepare an empty stack data structure
def _getEmptyListOfStacks(crateData):
	# This function assumes that the second-to-last
	# character of the last crate data line is a
	# single-digit integer value
	stackCount = _getStackCount(crateData)
	listOfStacks = []
	for _ in range(stackCount):
		stack = []
		listOfStacks.append(stack)

# Function to get a list of indices
# for each stack column
def _getStackColumnIndices(crateData):
	line = crateData[-1]
	indices = []
	for index, character in line:
		if ''.join(character).isdigit():
			indices.append(index)

# Function to get the stack at a given column index
def _getStack(crateData, stackColumnIndex):
	stack = []
	for rowIndex, line in reversed(crateData):
		if rowIndex == 0:
			continue
		stack.append(''.join(line[stackColumnIndex]))
	print("DEBUG: stack at", rowIndex, stackColumnIndex, "is", stack)

# Function to populate an empty stack data structure
def _populateListOfStacks(crateData, emptyListOfStacks):
	# We start from the bottom of the raw input data
	# and move our way up.
	# First determine the indices of each column ID.
	listOfStacks = emptyListOfStacks.copy()	
	stackColumnIndices = _getStackColumnIndices(crateData)
	_getStack(crateData, stackColumnIndices[0])

def solve1(data):
	crateData = _getCrateData(data)
	startIndexForMoveData = _getStartIndexForMoveData(data)
	moveData = _getMoveData(data, startIndexForMoveData)
	emptyListOfStacks = _getEmptyListOfStacks(crateData)
	listOfStacks = _populateListOfStacks(crateData, emptyListOfStacks)

	return

def solve2(data):
	return

def main():
	# Get arg from command line
	args = sys.argv[1:]

	# Get list of lines from file
	with open(args[0], 'r', encoding='utf-8') as file:
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