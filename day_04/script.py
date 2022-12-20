"""
Day 4: Camp Cleanup

Solution written by JJ Nunez.
"""

import sys

def _getLeftGroupLowerBound(line):
	leftLowerBoundString = []
	for character in line:
		if character == '-':
			return int(''.join(leftLowerBoundString))
		else:
			leftLowerBoundString.append(character)

def _getLeftGroupUpperBound(line):
	leftUpperBoundString = []
	startingIndex = line.find('-')+1
	for index, character in enumerate(line):
		if index < startingIndex:
			continue
		if character == ',':
			return int(''.join(leftUpperBoundString))
		else:
			leftUpperBoundString.append(character)

def _getRightGroupLowerBound(line):
	rightLowerBoundString = []
	startingIndex = line.find(',')+1
	for index, character in enumerate(line):
		if index < startingIndex:
			continue
		if character == '-':
			return int(''.join(rightLowerBoundString))
		else:
			rightLowerBoundString.append(character)

def _getRightGroupUpperBound(line):
	rightUpperBoundString = []
	startingIndex = line.find(',')+1
	startingIndex = line.find('-', startingIndex)+1
	for index, character in enumerate(line):
		if index < startingIndex:
			continue
		rightUpperBoundString.append(character)
	return int(''.join(rightUpperBoundString))

def _getLeftGroups(data):
	leftGroups = []
	for line in data:
		leftGroup = []
		leftGroupLowerBound = _getLeftGroupLowerBound(line)
		leftGroup.append(leftGroupLowerBound)
		leftGroupUpperBound = _getLeftGroupUpperBound(line)
		leftGroup.append(leftGroupUpperBound)
		leftGroups.append(leftGroup)
	return leftGroups

def _getRightGroups(data):
	rightGroups = []
	for line in data:
		rightGroup = []
		rightGroupLowerBound = _getRightGroupLowerBound(line)
		rightGroup.append(rightGroupLowerBound)
		rightGroupUpperBound = _getRightGroupUpperBound(line)
		rightGroup.append(rightGroupUpperBound)
		rightGroups.append(rightGroup)
	return rightGroups

def _oneGroupContainsTheOther(leftGroup, rightGroup):
	leftLower = leftGroup[0]
	leftUpper = leftGroup[1]
	rightLower = rightGroup[0]
	rightUpper = rightGroup[1]
	if leftLower <= rightLower and leftUpper >= rightUpper:
		return True
	elif rightLower <= leftLower and rightUpper >= leftUpper:
		return True
	return False

def _eitherGroupHasAnyOverlap(leftGroup, rightGroup):
	leftLower = leftGroup[0]
	leftUpper = leftGroup[1]
	rightLower = rightGroup[0]
	rightUpper = rightGroup[1]
	if leftLower == rightLower or leftUpper == rightUpper:
		return True
	if leftLower == rightUpper or rightLower == leftUpper:
		return True
	if leftLower < rightLower and leftUpper >= rightLower:
		return True
	if rightLower < leftLower and rightUpper >= leftLower:
		return True
	return False

def solve1(data):
	leftGroups = _getLeftGroups(data) 
	rightGroups = _getRightGroups(data)
	total = 0
	for index, leftGroup in enumerate(leftGroups):
		rightGroup = rightGroups[index]
		if _oneGroupContainsTheOther(leftGroup, rightGroup):
			total += 1
	print("The total number of assignment pairs where one range fully contains the other is", total)
	return

def solve2(data):
	leftGroups = _getLeftGroups(data)
	rightGroups = _getRightGroups(data)
	total = 0
	for index, leftGroup in enumerate(leftGroups):
		rightGroup = rightGroups[index]
		if _eitherGroupHasAnyOverlap(leftGroup, rightGroup):
			total += 1
	print("The total number of assignment pairs where one range has any kind of overlap with the other is", total)	
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