"""
Day 3: Rucksack Reorganization

Solution written by JJ Nunez.
"""

import sys

def getFirstHalfOfString(line):
	half_length = len(line)//2
	return line[0:half_length]

def getSecondHalfOfString(line):
	half_length = len(line)//2
	length = len(line)
	return line[half_length:length]

def getSharedItemType1(firstCompartment, secondCompartment):
	for char1 in firstCompartment:
		for char2 in secondCompartment:
			if char1 == char2:
				return char1

def getSharedItemType2(firstRucksack, secondRucksack, thirdRucksack):
	for char1 in firstRucksack:
		for char2 in secondRucksack:
			if char1 == char2:
				for char3 in thirdRucksack:
					if char2 == char3:
						return char1

def getValue(itemType):
	if (itemType.isupper()):
		return ord(itemType) - ord('A') + 26 + 1
	return ord(itemType) - ord('a') + 1

def solve1(data):
	sharedItemTypes = []
	for line in data:
		firstCompartment = getFirstHalfOfString(line)
		secondCompartment = getSecondHalfOfString(line)
		sharedItemType = getSharedItemType1(firstCompartment, secondCompartment)
		sharedItemTypes.append(sharedItemType)

	values = []
	for itemType in sharedItemTypes:
		value = getValue(itemType)
		values.append(value)
	
	sum = 0
	for value in values:
		sum += value	
	
	print("The total summed value of each duplicate item type from each rucksack altogether is", sum)	
	return

def solve2(data):
	firstRucksacks = []
	secondRucksacks = []
	thirdRucksacks = []
	for index, line in enumerate(data):
		if index % 3 == 0:
			firstRucksacks.append(line)
		if index % 3 == 1:
			secondRucksacks.append(line)
		if index % 3 == 2:
			thirdRucksacks.append(line)
		
	sharedItemTypes = []
	for index, firstRucksack in enumerate(firstRucksacks):
		secondRucksack = secondRucksacks[index]
		thirdRucksack = thirdRucksacks[index]
		sharedItemType = getSharedItemType2(firstRucksack, secondRucksack, thirdRucksack)
		sharedItemTypes.append(sharedItemType)
	
	values = []
	for itemType in sharedItemTypes:
		value = getValue(itemType)
		values.append(value)
	
	sum = 0
	for value in values:
		sum += value	
	
	print("The total summed value of every group of three's badges is", sum)	
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
    
    # Get your answers
    solve1(data)
    solve2(data)

# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()