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


def name_reverse():
    name = input("enter a name (first last):")
    space = name.find(' ')
    first_name = name[:space]
    last_name = name[space:]
    print(last_name.strip() + ", " + first_name.rstrip())



def company_name():
    domain = input('enter a domain')
    company_start = domain.find('.')
    company_end = domain.rfind('.')
    company = domain[company_start + 1:company_end]
    print(company)


def initials():
    students = eval(input("how many students are in the class?"))
    for i in range(1, students + 1):
        name = input("what is the name of student " + str(i) + "?")
        first_initial = name[0]
        space = name.find(" ")
        last_initial = name[space + 1]
        print(first_initial + last_initial)



def names():
    input_names = input("enter a list of names")
    name_list = input_names.split(", ")
    print(name_list)
    for i in name_list:
        space = i.find(" ")
        initial = i[0] + i[space + 1]
        print(initial, end=" ")


def thirds():
    input_number = eval(input("enter the number of sentences:"))
    for i in range(1, input_number + 1):
        sentence = input("enter sentence " + str(i) + ":")
        third_letter = sentence[::3]
        print(third_letter)


def word_average():
    sentence = input("enter a sentence:")
    word_sum = 0
    words = sentence.split()
    for i in words:
        letters = len(i)
        word_sum = word_sum + letters
    average = word_sum / (len(words))
    print(average)


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin:")
    words = sentence.split()
    for i in words:
        last_letters = str(i[1]).upper() + str(i[2:])
        latin = last_letters, str(i[0:1]).lower(), "ay"
        i = ''.join(latin)
        print(i, end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
