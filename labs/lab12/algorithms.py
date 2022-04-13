"""
Aidan Stout
lab12.py
Problem: solve a series of problems to help further my knowledge of while loops and lists
I certify that this is entirely my work
"""


def read_data(filename):
    num_list = []
    file = open(filename, 'r')
    line = file.readline()
    while line:
        line = line.split()
        index = 0
        while index < len(line):
            num = eval(line[index])
            num_list.append(num)
            index += 1
        line = file.readline()
    file.close()
    return num_list


def is_in_linear(search_val, values):
    index = 0
    while index < len(values):
        if values[index] != search_val:
            index += 1
            return False
        else:
            return True


