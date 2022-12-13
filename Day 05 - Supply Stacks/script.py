"""
Day 5: Supply Stacks

Solution written by JJ Nunez.
"""

import sys

def _debugListContents(message, data):
	print(message)
	for line in data:
		print(line)
	print('================')
	return


def _getCrateData(data):
	crateData = []
	for line in data:
		if line != '':
			crateData.append(line)
		else:
			return crateData

def _getStartIndexForMoveData(data):
	for index, line in enumerate(data):
		if line != '':
			continue
		else:
			return index+1	

def _getMoveData(data, startIndexForMoveData):
	moveData = []
	for index, line in enumerate(data):
		if index < startIndexForMoveData:
			continue
		else:
			moveData.append(line)
	return moveData

def _getEmptyListOfStacks(crateData):
	# This function assumes that the second-to-last
	# character of the last crate data line is a
	# single-digit integer value
	lengthOfLastLine = len(crateData[-1])
	stackCount = int(''.join(crateData[lengthOfLastLine-2]))
	listOfStacks = []
	for _ in range(stackCount):
		stack = []
		listOfStacks.append(stack)



def solve1(data):
	crateData = _getCrateData(data)
	startIndexForMoveData = _getStartIndexForMoveData(data)
	moveData = _getMoveData(data, startIndexForMoveData)
	listOfStacks = _getEmptyListOfStacks(crateData)

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