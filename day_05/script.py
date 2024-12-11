"""
Advent of Code 2024
Day 5: Print Queue

Solution written by JJ Nunez.
"""

import os
from copy import deepcopy

################################################
#                                              #
#         Helper functions and classes         #
#                                              #
################################################


def _print_lines(data: list[str]):
    for line in data:
        print(line)


def _get_ordering_rule_lines(data: list[str]):
    ordering_rule_lines: list[str] = []
    for line in data:
        if line == '':
            break
        else:
            ordering_rule_lines.append(line)
    return ordering_rule_lines


def _get_page_number_lines(data: list[str]):
    page_number_lines: list[str] = []
    encountered_yet: bool = False
    for line in data:
        if line == '':
            encountered_yet = True
            continue
        elif encountered_yet == False:
            continue
        else:
            page_number_lines.append(line)
    return page_number_lines


def _get_ordering_rule_array(lines: list[str]):
    ordering_rules: list[list[int]] = []
    for line in lines:
        split_string = line.split("|")
        pair: list[int] = []
        for item in split_string:
            pair.append(int(item))
        ordering_rules.append(pair)
    return ordering_rules


def _get_page_number_array(lines: list[str]):
    page_numbers: list[list[int]] = []
    for line in lines:
        split_string = line.split(",")
        group: list[int] = []
        for item in split_string:
            group.append(int(item))
        page_numbers.append(group)
    return page_numbers

################################################
#                                              #
#               Solver functions               #
#                                              #
################################################


def _solve1(data: list[str]):

    # Process the data into structures
    data_copy = deepcopy(data)
    ordering_rule_lines = _get_ordering_rule_lines(data_copy)
    page_number_lines = _get_page_number_lines(data_copy)
    ordering_rules = _get_ordering_rule_array(ordering_rule_lines)
    page_numbers = _get_page_number_array(page_number_lines)

    # I am considering an associative array here
    before_dictionary: dict = {}
    after_dictionary: dict = {}
    for pair in ordering_rules:
        if before_dictionary.get(pair[1]) == None:
            before_dictionary[pair[1]] = set()
        if after_dictionary.get(pair[0]) == None:
            after_dictionary[pair[0]] = set()
        before_dictionary[pair[1]].add(pair[0])
        after_dictionary[pair[0]].add(pair[1])
    print("BEFORE_DICTIONARY")
    for index, (key, value) in enumerate(before_dictionary.items()):
        print(f"Index: {index}, Key: {key}, Value: {value}")
    print("AFTER_DICTIONARY")
    for index, (key, value) in enumerate(after_dictionary.items()):
        print(f"Index: {index}, Key: {key}, Value: {value}")


def _solve2(data: list[str]):
    data_copy = deepcopy(data)

################################################
#                                              #
#            Execution and File I/O            #
#                                              #
################################################


def _read_file(file_name):
    script_directory = os.path.dirname(__file__)
    file_path = os.path.join(script_directory, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        data.append(line.replace('\n', ''))
    return data


def main():
    sample_file_name = 'sample.txt'
    input_file_name = 'input.txt'
    sample_data = _read_file(sample_file_name)
    input_data = _read_file(input_file_name)

    print(sample_file_name)
    _solve1(sample_data)
    # _solve2(sample_data)

    print(input_file_name)
    # _solve1(input_data)
    # _solve2(input_data)


# Allows execution only from command line
# and not from import statements
if __name__ == '__main__':
    main()
