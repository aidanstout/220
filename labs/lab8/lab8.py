"""
Aidan Stout
lab8.py
Problem:
I certify that this program is entirely my work
"""

from random import randint
from time import sleep

from graphics import *


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball, ball_2):
    center_one = ball.getCenter()
    center_two = ball_2.getCenter()
    center_one_x = center_one.getX()
    center_two_x = center_two.getX()
    center_one_y = center_one.getY()
    center_two_y = center_two.getY()
    x_dist = (center_two_x - center_one_x) ** 2
    y_dist = (center_two_y - center_one_y) ** 2
    distance = (x_dist + y_dist) ** (1 / 2)
    if distance <= (ball.getRadius() + ball_2.getRadius()):
        return True
    return False


def hit_vertical(ball, win):
    window_height = win.getHeight()
    ball_point_top = ball.getCenter().getY() + ball.getRadius()
    ball_point_bottom = ball.getCenter().getY() - ball.getRadius()
    if ball_point_top >= window_height or ball_point_bottom <= 0:
        return True
    return False


def hit_horizontal(ball, win):
    window_width = win.getWidth()
    ball_point_right = ball.getCenter().getX() + ball.getRadius()
    ball_point_left = ball.getCenter().getX() - ball.getRadius()
    if ball_point_right >= window_width or ball_point_left <= 0:
        return True
    return False


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return color_rgb(r, g, b)


def bumper():
    win = GraphWin('bumper cars', 500, 500)
    random_point = Point(randint(50, 450), randint(50, 450))
    ball = Circle(random_point, 50)
    random_point_2 = Point(randint(50, 450), randint(50, 450))
    ball_2 = Circle(random_point_2, 50)
    ball.draw(win)
    ball_2.draw(win)
    ball.setFill(get_random_color())
    ball_2.setFill(get_random_color())
    dx = get_random(10)
    dy = get_random(10)
    dx_2 = get_random(10)
    dy_2 = get_random(10)
    while not win.checkMouse():
        ball.move(dx, dy)
        ball_2.move(dx_2, dy_2)
        sleep(.2)
        if did_collide(ball, ball_2):
            dx = dx * -1
            dy = dy * -1
            dx_2 = dx_2 * -1
            dy_2 = dy_2 * -1
        if hit_vertical(ball, win):
            dy = dy * -1
        if hit_vertical(ball_2, win):
            dy_2 = dy_2 * -1
        if hit_horizontal(ball, win):
            dx = dx * -1
        if hit_horizontal(ball_2, win):
            dx_2 = dx_2 * -1
    win.close()
