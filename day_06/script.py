"""
Advent of Code 2022
Day 6: Tuning Trouble

Solution written by JJ Nunez.
"""

import os

"""
Helper functions
"""
def _allFourCharsAreUnique(first, second, third, fourth):
	if first == second:
		return False
	if first == third:
		return False
	if first == fourth:
		return False
	if second == third:
		return False
	if second == fourth:
		return False
	if third == fourth:
		return False
	return True

"""
Solver functions
"""
def _solve1(data):
	for line in data:
		for index, character in enumerate(line):
			if index >= 3:
				first = line[index-3]
				second = line[index-2]
				third = line[index-1]
				fourth = character
				if _allFourCharsAreUnique(first, second, third, fourth):
					print('Characters processed before start-of-packet marker:', index+1)	
					break

def _solve2(data):
	bag = set()

	for line in data:
		for index in range(0, len(line)-14+1):
			substring = line[index:14+index]
			for character in substring:
				bag.add(character)
			if len(bag) == 14:
				print('First marker after character ', index+14)
				bag.clear()
				break
			else:
				bag.clear()
				continue
	
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