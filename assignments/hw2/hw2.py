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


def sum_of_threes():
    upper_bound = eval(input('Enter your upper bound:'))
    threes_sum = 0
    for i in range(0, upper_bound + 1, 3):
        threes_sum = threes_sum + i
    print("sum of threes is", threes_sum)



def multiplication_table():
    for i in range(1, 11):
        for table in range(1, 11):
            print(i * table, end='\t')
        print('\n')




def triangle_area():
    side_a = eval(input('Enter side a length:'))
    side_b = eval(input('Enter side b length:'))
    side_c = eval(input("Enter side c length:"))
    side = side_a + side_b + side_c
    side = side / 2
    area = (side - side_a) * (side - side_b) * (side - side_c)
    area = (area * side) ** (1/2)
    print('area is', area)


def sum_squares():
    lower_range = eval(input('Enter lower range:'))
    upper_range = eval(input('Enter upper range:'))
    squares_sum = 0
    for i in range(lower_range, upper_range + 1):
        squares_sum = squares_sum + i ** 2
    print(squares_sum)


def power():
    base_number = eval(input("Enter base:"))
    exponent_number = eval(input("Enter exponent:"))
    result = 1
    for i in range(exponent_number):
        result = result * base_number
    print(base_number, "^", exponent_number, '=', result)


if __name__ == '__main__':
    pass
