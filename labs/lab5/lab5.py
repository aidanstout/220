"""
Aidan Stout
Problem: create and edit various programs
I certify that this lab is entirely my work.
"""

from graphics import *


def triangle():
    width = 400
    height = 400
    win = GraphWin("Triangle", width, height)

    instruction = Text(Point(200, 50), "Click three times to draw a triangle")
    instruction.draw(win)

    click_1 = win.getMouse()
    p1 = Point(click_1.getX(), click_1.getY())
    click_2 = win.getMouse()
    p2 = Point(click_2.getX(), click_2.getY())
    click_3 = win.getMouse()
    p3 = Point(click_3.getX(), click_3.getY())
    shape = Polygon(p1, p2, p3)
    shape.draw(win)

    length_1 = (((click_2.getX() - click_1.getX()) ** 2) + ((click_2.getY() - click_1.getY()) ** 2)) ** (1/2)
    length_2 = (((click_3.getX() - click_2.getX()) ** 2) + ((click_3.getY() - click_2.getY()) ** 2)) ** (1/2)
    length_3 = (((click_1.getX() - click_3.getX()) ** 2) + ((click_1.getY() - click_3.getY()) ** 2)) ** (1/2)

    perimeter = round(length_1 + length_2 + length_3, 2)
    perimeter = str(perimeter)
    perim_text = Text(Point(200, 350), "Perimeter: " + perimeter)
    perim_text.draw(win)
    s = (length_1 + length_2 + length_3) / 2
    area = round((s * (s - length_1) * (s - length_2) * (s - length_3)) ** (1/2), 2)
    area = str(area)
    area_text = Text(Point(200, 365), "Area: " + area)
    area_text.draw(win)

    message = Text(Point(200, 380), "Click again to close")
    message.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_text.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_text.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_text.draw(win)

    for i in range(5):
        red_number = Entry(Point(250, 240), 10)
        red_number.draw(win)
        green_number = Entry(Point(250, 270), 10)
        green_number.draw(win)
        blue_number = Entry(Point(250, 300), 10)
        blue_number.draw(win)
        win.getMouse()
        red_color = eval(red_number.getText())
        green_color = eval(green_number.getText())
        blue_color = eval(blue_number.getText())
        shape.setFill(color_rgb(red_color, green_color, blue_color))

    # Wait for another click to exit
    message = Text(Point(200, 50), "Click again to close")
    message.draw(win)
    win.getMouse()
    win.close()

def process_string():
    user_string = input("enter a string:")
    first_letter = user_string[0]
    last_letter = user_string[-1]
    print(first_letter)
    print(last_letter)
    print(user_string[1:5])
    print(first_letter + last_letter)
    three_first = user_string[0:3]
    print(three_first * 10)
    for i in user_string:
        print(i)
    print(len(user_string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = (values[1]) * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4] + values[0:1]
    print(x)
    x = values[2:3] + values[0:1] + [eval(values[5])]
    print(x)
    x = values[2] + values[0] + eval(values[5])
    print(x)
    x = len(values)
    print(x)



def another_series():
    terms = eval(input("enter the number of terms in the pattern:"))
    pattern = [2, 4, 6]
    my_sum = 0
    for i in range(terms):
        print(pattern[i % 3], end="")
        my_sum = my_sum + pattern[i % 3]
    print()
    print(my_sum)


def target():
    width = 400
    height = 400
    win = GraphWin("Target", width, height)
    win.setBackground("light blue")
    radius = 200
    colors = ["white", "black", "blue", "red", "yellow"]
    for i in colors:
        shape = Circle(Point(width / 2, height / 2), radius)
        shape.setFill(i)
        shape.draw(win)
        radius = radius - 40
    message = Text(Point(50, 15), "Click to close")
    message.draw(win)
    win.getMouse()
    win.close()