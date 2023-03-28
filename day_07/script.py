"""
Advent of Code 2022
Day 7: No Space Left On Device

Solution written by JJ Nunez.
"""

import os

"""
Custom classes
"""
class Node:

	def __init__(self, name, type, size, parent):
		self.name = name
		self.type = type
		self.size = size
		self.parent = parent
		self.children = []

"""
Helper functions
"""
def _calculateSize(node):
	for child in node.children:
		if child.type == "file":
			node.size += child.size
		elif child.type == "dir":
			node.size += _calculateSize(child)
	return node.size

def _findSizesUnderLimit(node, limit, dictionary):
	if node.size <= limit:
		dictionary[node.name] = node.size
	for child in node.children:
		if child.type == "dir":
			dictionary = _findSizesUnderLimit(child, limit, dictionary)
	return dictionary

"""
Solver functions
"""
def _solve1(data):

	# Using custom node class to build a directory tree
	root = Node("/", "dir", 0, None)
	c_node = root

	# Iterate over the list
	for line in data:
		
		# Reset position to filesystem root
		if (line == "$ cd /"):
			c_node = root

		# Go up one directory
		elif (line == "$ cd .."):
			c_node = c_node.parent
		
		# Go into a directory
		elif line[:4] == "$ cd":
			c_node.children.append(Node(line[5:], "dir", 0, c_node))
			c_node = c_node.children[-1]

		# List files in directory, ignorable line	
		elif (line == "$ ls"):
			continue

		# Encountered a directory, just ignore
		elif (line[0] == "d"):
			continue

		# Encountered a file to place in the file list
		elif (line[0].isdigit()):
			split_line = line.split(" ")
			file_name = split_line[1]
			file_size = split_line[0]
			c_node.children.append(Node(file_name, "file", int(file_size), c_node))

	_calculateSize(root)
	dictionary = _findSizesUnderLimit(root, 100000, {})

	total = 0
	for size in dictionary.values():
		total += size
	
	print("The sum of the total sizes of all directories with a size of at most 100000:", total)

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