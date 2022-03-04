"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import encryption


def number_words(in_file_name, out_file_name):
    with open(in_file_name, "r") as inputs:
        with open(out_file_name, "w") as outputs:
            lines = inputs.readlines()
            for line_var in lines:
                words = line_var.split()
                for i in range()



def hourly_wages(in_file_name, out_file_name):
    my_file = open(in_file_name, "r")
    file_inputs = my_file.readlines()
    for i in file_inputs:
        file_list = i.split()
        first_name = file_list[0]
        last_name = file_list[1]
        wage = eval(file_list[2])
        hours = eval(file_list[3])
        pay = wage * hours
        my_output = open(out_file_name, "w")
        print("{} {}'s pay is: ${:0>2}".format(first_name, last_name, pay), file=my_output)
        print(" ", file=my_output)


def calc_check_sum(isbn):
    isbn = isbn.replace('-', '')
    isbn = isbn.split()
    length = len(isbn)
    isbn = list(map(int, isbn))
    output = 0
    for n in isbn:
        value = isbn[n] * (length - n)
        output = output + value
    return output


def send_message(file_name, friend_name):
    friend_file = friend_name + ".txt"
    my_file = open(file_name, "r")
    file_input = my_file.readlines()
    for i in file_input:
        friend_file = open(friend_file, "w")
        print(i, file=friend_file)
        print(" ", file=friend_file)


def send_safe_message(file_name, friend_name, key):
    friend_file = friend_name + ".txt"
    my_file = open(file_name, "r")
    file_input = my_file.readlines()
    for message in file_input:
        encode()
        friend_file = open(friend_file, "w")
        print(message, file=friend_file)
        print(" ", file=friend_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    friend_file = friend_name + ".txt"
    my_file = open(file_name, "r")
    file_input = my_file.readlines()
    for message in file_input:
        encode_better()
        friend_file = open(friend_file, "w")
        print(message, file=friend_file)
        print(" ", file=friend_file)


if __name__ == '__main__':
    pass
