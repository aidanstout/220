"""
Aidan Stout
lab4.py
Problem: create a greeting card for Valentine's day
I certify that this lab is entirely my work
"""

from graphics import *

def greeting_card():
    val = GraphWin('Greeting Card', 700, 600)
    val.setBackground('purple')
    arrow = Line(Point(500, 450), Point(650, 500))
    arrow.setWidth(4)
    arrow.setFill('black')
    arrow.setArrow("first")
    arrow.draw(val)
    left_heart = Polygon(Point(350, 270), Point(300, 220), Point(250, 200), Point(200, 250), Point(350, 500))
    left_heart.setFill('red')
    left_heart.setOutline('red')
    left_heart.draw(val)
    right_heart = Polygon(Point(350, 270), Point(400, 220), Point(450, 200), Point(500, 250), Point(350, 500))
    right_heart.setFill('red')
    right_heart.setOutline('red')
    right_heart.draw(val)
    greeting = Text(Point(350, 100), "Happy Valentine's Day")
    greeting.setFill('pink')
    greeting.setSize(30)
    greeting.setFace('courier')
    greeting.setStyle('bold')
    greeting.draw(val)
    for i in range(10):
        arrow.move(-50, -16)
        time.sleep(.5)
    message = Text(Point(350, 550), "click to close")
    message.draw(val)
    val.getMouse()
    val.close()
