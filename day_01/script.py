"""
Advent of Code 2024
Day 1: Historian Hysteria

Solution written by JJ Nunez.
"""

import os


# Helper functions and classes
class Location:
    def __init__(self, id):
        self.id = id

# Solver functions


def _solve1(data):
    # Create two empty lists
    list0 = []
    list1 = []

    # Populate the lists with unsorted data
    for datum in data:
        pair = datum.split("   ")
        list0.append(pair[0])
        list1.append(pair[1])

    # Sort the lists
    list0.sort()
    list1.sort()

    # Create an empty "distances" list
    distances = []

    # Iterate over the two lists and calculate distances
    for item0, item1 in zip(list0, list1):
        distance = int(item0) - int(item1)
        if distance < 0:
            distance = 0 - distance
        distances.append(distance)

    # Display the sum
    print(sum(distances))


def _solve2(data):
    # Create two empty lists
    list0 = []
    list1 = []

    # Populate the lists with unsorted data
    for datum in data:
        pair = datum.split("   ")
        list0.append(pair[0])
        list1.append(pair[1])

    # Set up the similarity score
    similarity_score = 0

    # Iterate over both lists
    for item in list0:
        instances = 0
        for comparator in list1:
            if item == comparator:
                instances = instances + 1
        current_score = int(item) * instances
        similarity_score = similarity_score + current_score

    # Print results
    print(similarity_score)

# Execution and File I/O


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
