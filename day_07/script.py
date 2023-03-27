"""
Advent of Code 2022
Day 7: No Space Left On Device

Solution written by JJ Nunez.
"""

import os
from collections import deque

"""
Helper functions
"""
def _getDirs(data):
	directory_list = []
	for line in data:
		if line[:3] == 'dir':
			directory_list.append(line[4:])

"""
def _execute(sublist, dirname):
	workingdirsize = 0
	# Loop over sublist until "$ cd .."
	for index, line in enumerate(sublist):
		if line == "$ cd ..":
			print("Dir", dirname, "contains", workingdirsize, "bytes") 
			return
		elif line[:4] == "$ cd":
			_execute(sublist[index:], line[5:])
		elif line[0].isdigit():
			splitline = line.split(" ")
			workingdirsize += int(splitline[0])	
	return
"""
	
"""
Solver functions
"""
def _solve1(data):

	# Using a stack to keep track of current working dir	
	working_directory_path = deque()

	# Using a dictionary to keep track of fully qualified file paths
	# and their size in bytes
	file_list = []
	byte_list = []

	# Iterate over the list
	for index, line in enumerate(data):
		
		# Reset position to filesystem root
		if (line == "$ cd /"):
			working_directory_path.clear()
					
		# Go up one directory
		elif (line == "$ cd .."):
			working_directory_path.pop()
		
		# Go into a directory
		elif line[:4] == "$ cd":
			working_directory_path.append(line[5:])

		# List files in directory, ignorable line	
		elif (line == "$ ls"):
			continue

		# Encountered a directory, just ignore
		elif (line[0] == "d"):
			continue

		# Encountered a file to place in the file list
		elif (line[0].isdigit()):
			fully_qualified_file_path = "/"
			for directory in working_directory_path:
				fully_qualified_file_path += directory
				fully_qualified_file_path += "/"
			split_line = line.split(" ")
			fully_qualified_file_path += split_line[1]
			file_list.append(fully_qualified_file_path)
			byte_list.append(int(split_line[0]))

	for index, file in enumerate(file_list):
		print("File: '" + file + "' is '" + str(byte_list[index]) + "' bytes long")
	
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

	#print(inputFileName)
	#_solve1(inputData)
	#_solve2(inputData)

# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()