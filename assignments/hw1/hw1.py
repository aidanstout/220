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


def calc_rec_area():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area = length * width
    print("Area = ", area)


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("Volume = ", volume)


def shooting_percentage():
    shots = eval(input("Enter the player's total shots:"))
    made = eval(input("Enter how many shots the player made:"))
    percent = made / shots * 100
    print("Shooting percentage:", percent, "%")


def coffee():
    pounds = eval(input("How many pounds of coffee would you like?"))
    total = pounds * 11.36 + 1.50
    total = round(total, 2)
    print("Your total is:", total)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers / 1.61
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
