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


def selection_sort(values):
    for index in range(len(values)):
        min_index = index
        min_val = values[min_index]
        for i in range(index, len(values)):
            if values[i] < min_val:
                min_index = i
                min_val = values[i]
        swap_val = values[index]
        values[index] = min_val
        values[min_index] = swap_val
    return values


def calc_area(rect):
    y1 = rect.getP1.getY()
    y2 = rect.getP2.getY()
    x1 = rect.getP1.getX()
    x2 = rect.getP2.getX()
    side1 = abs(y1 - y2)
    side2 = abs(x1 - x2)
    return side1 * side2


def rect_sort(rectangles):
    for rect in range(len(rectangles)):
        min_index = rect
        min_area = calc_area(rectangles[rect])
        for i in range(rect, len(rectangles)):
            if calc_area(rectangles[i]) < min_area:
                min_index = i
                min_area = calc_area(rectangles[i])
        swap_rect = rectangles[rect]
        swap_val = rectangles[min_index]
        rectangles[rect] = swap_val
        rectangles[min_index] = swap_rect


if __name__ == '__main__':
    values = [7, 3, 4, 5, 1, 2, 6, 9, 8]
    selection_sort(values)
