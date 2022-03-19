"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    result = 0
    for i in range(len(nums)):
        result = result + nums[i]
    return result


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    for i in range(len(nums)):
        inner_list = nums[i].split()
        for num in inner_list:
            to_numbers(num)
            square_each(num)
            sum_list(num)


def starter(weight, wins):
    low_weight = 150 <= weight < 160
    high_weight = weight > 199
    if low_weight and wins >= 5:
        return True
    if high_weight or wins > 20:
        return True
    return False


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt(
        (center_2.getX() - circumference_point_2.getX()) ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    circle_overlap()
    center_one = circle_one.getCenter()
    center_two = circle_two.getCenter()
    center_one_x = center_one.getX()
    center_two_x = center_two.getX()
    center_one_y = center_one.getY()
    center_two_y = center_two.getY()
    x_dist = (center_two_x - center_one_x) ** 2
    y_dist = (center_two_y - center_one_y) ** 2
    distance = (x_dist + y_dist) ** (1 / 2)
    message_true = Text(Point(350, 500), "The circles overlap")
    message_false = Text(Point(350, 500), "The circles do not overlap")
    if distance <= (circle_one.getRadius() + circle_two.getRadius()):
        message_true.draw(win)
    else:
        message_false.draw(win)
    close_message = Text(Point(350, 550), "Click again to close")
    close_message.draw(win)


if __name__ == '__main__':
    pass
