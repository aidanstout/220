"""
Aidan Stout
lab10.py
Problem: create a program that has two working buttons using classes
I certify that this is entirely my work
"""

from button import Button
from door import Door
from graphics import *


def main():
    win = GraphWin("Test", 500, 600)
    rect_button = Rectangle(Point(150, 50), Point(350, 200))
    button = Button(rect_button, "Exit")
    button.draw(win)
    rect_door = Rectangle(Point(150, 250), Point(350, 550))
    door = Door(rect_door, "Closed")
    door.color_door('red')
    door.draw(win)
    click = win.getMouse()
    while not button.is_clicked(click):
        if door.is_clicked(click) and door.get_label() is "Closed":
            door.open('white', 'Open')
        elif door.is_clicked(click) and door.get_label() is "Open":
            door.close('red', 'Closed')
        click = win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
