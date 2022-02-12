"""
Name: <Aidan Stout>
hw4.py

Problem: <Brief, one or two sentence description of the problem that this program solves,
in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 100), Point(100, 50))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)


    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of square
        shape = shape.clone()
        shape.draw(win)

        # move amount is distance from center of square to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

    message = Text(Point(200, 200), "Click again to close")
    message.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Rectangles", width, height)

    instruction = Text(Point(200, 50), "Click twice to draw rectangle")
    instruction.draw(win)

    click_1 = win.getMouse()
    p1 = Point(click_1.getX(), click_1.getY())
    click_2 = win.getMouse()
    p2 = Point(click_2.getX(), click_2.getY())

    length = click_2.getX() - click_1.getX()
    width = click_2.getY() - click_1.getY()
    perimeter = abs((2 * length) + (2 * width))
    area = abs(length * width)
    perimeter = str(perimeter)
    area = str(area)
    perim_result = Text(Point(200, 370), "Perimeter: " + perimeter)
    area_result = Text(Point(200, 385), "Area: " + area)
    perim_result.draw(win)
    area_result.draw(win)

    shape = Rectangle(p1, p2)
    shape.setFill("green")
    shape.draw(win)
    message = Text(Point(200, 200), "Click again to close")
    message.draw(win)
    win.getMouse()
    win.close()


def circle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    click_1 = win.getMouse()
    p1 = Point(click_1.getX(), click_1.getY())
    click_2 = win.getMouse()
    radius = ((click_2.getX() - click_1.getX()) ** 2) + ((click_2.getY() - click_1.getY()) ** 2)
    radius = radius ** (1/2)

    shape = Circle(p1, radius)
    shape.setFill("light blue")
    shape.draw(win)

    radius = str(radius)
    result = Text(Point(200, 370), "Radius\n" + radius)
    result.draw(win)

    message = Text(Point(200, 200), "Click again to close")
    message.draw(win)
    win.getMouse()
    win.close()

import math

def pi2():
    terms = eval(input("enter the number of terms to sum:"))
    for i in range(terms):
        pi_approximation = 4 * (1 / (i + (i + 1)))
    print("pi approximation:", pi_approximation)
    print("accuracy:", math.pi - pi_approximation)


if __name__ == '__main__':
    pass
