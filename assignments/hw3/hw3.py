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


def average():
    number_of_inputs = eval(input("How many grades will you enter?"))
    grade_average = 0
    for i in range(number_of_inputs):
        grades = eval(input("Enter grade"))
        grade_average = grade_average + grades
    grade_average = grade_average / number_of_inputs
    print("average is", grade_average)


def tip_jar():
    total_tips = 0
    for i in range(5):
        tip_amount = eval(input("How much would you like to donate?"))
        total_tips = total_tips + tip_amount
    print('total tips:', total_tips)


def newton():
    number_to_sqrt = eval(input("What number do you want to square root?"))
    approx = 1
    amount_of_approx = eval(input("How many times should we improve the approximation?"))
    for i in range(amount_of_approx):
        approx = ((approx + (number_to_sqrt / approx)) / 2)
    print("The square root is approximately", approx)


def sequence():
    terms = eval(input('how many terms would you like?'))
    numbers = 1
    print("1", end='\t')
    for i in range(terms - 1):
        numbers = numbers + (i % 2) + (i % 2)
        print(numbers, end='\t')


def pi():
    terms = eval(input('how many terms in the series?'))
    numerator = 0
    denominator = 1
    results = 1
    for i in range(terms):
        numerator = numerator + (i - 1) % 2 + (i - 1) % 2
        denominator = denominator + (i % 2) + (i % 2)
        results = results * (numerator / denominator)
    results = results * 2
    print(results)



if __name__ == '__main__':
    pass
