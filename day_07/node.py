class Node:

	def __init__(self, name, type, size, parent):
		self.name = name
		self.type = type
		self.size = size
		self.parent = parent
		self.children = []