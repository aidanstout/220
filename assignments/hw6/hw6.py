"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves,
in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math


def cash_converter():
    integer = eval(input("enter and integer:"))
    print("that is ${:.2f}".format(integer))


def encode():
    message = input("enter a message:")
    key = eval(input("enter a key:"))
    output = ""
    for letter in message:
        number = ord(letter)
        code = chr(number + key)
        output = output + code
    print(output)


def sphere_area(radius):
    float(radius)
    area = radius ** 2
    area = area * 4 * math.pi
    return area


def sphere_volume(radius):
    float(radius)
    volume = radius ** 3
    volume = volume * math.pi * (4/3)
    return volume


def sum_n(number):
    result = 0
    for i in range(1, number + 1):
        result = result + i
    return result


def sum_n_cubes(number):
    result = 0
    for i in range(1, number + 1):
        result = result + i ** 3
    return result


def encode_better():
    text = input("enter a message:")
    key = input("enter a key")
    output = ""
    for i in range(len(text)):
        character = ord(text[i]) - 65
        key_character = ord(key[i % len(key)]) - 65
        code = character + key_character
        code = code % 58
        code = code + 65
        output = output + chr(code)
    print(output)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
