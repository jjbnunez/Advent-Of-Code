"""
Advent of Code 2022
Day 7: No Space Left On Device

Solution written by JJ Nunez.
"""

"""
Import statements
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

def _findSizesUnderLimit(node, limit, list):
	if node.size <= limit:
		list.append(node)
	for child in node.children:
		if child.type == "dir":
			list = _findSizesUnderLimit(child, limit, list)
	return list

"""
Solver functions
"""
def _solve(data):

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

	# Recursively calculate the directory sizes
	_calculateSize(root)

	# Find all directory nodes at or below 100000 in size
	directory_list = _findSizesUnderLimit(root, 100000, [])

	# PROBLEM 1 SOLUTION
	total = 0
	for node in directory_list:
		total += node.size
	print("The sum of the total sizes of all directories with a size of at most 100000:", total)

	# Determine disk space, required space, and other parameters
	disk_space = 70000000
	required_space = 30000000
	available_space = disk_space - root.size
	minimum_delete_size = required_space - available_space

	# Find all directories in the filesystem tree
	directory_list = _findSizesUnderLimit(root, disk_space, [])

	# Mark those which can be deleted to free up enough space for an update
	candidates_for_deletion = []
	for node in directory_list:
		if node.size >= minimum_delete_size:
			candidates_for_deletion.append(node)

	# Find the smallest among delection candidates
	for index, node in enumerate(candidates_for_deletion):
		if index == 0:
			smallest = node
			continue
		if node.size <= smallest.size:
				smallest = node

	# PROBLEM 2 SOLUTION
	print("The smallest directory that, if deleted, would free up enough space on the filesystem to run the update is:", smallest.name, "at size", smallest.size)

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