"""
Aidan Stout
lab10.py
Problem: create a program that has two working buttons using classes
I certify that this is entirely my work
"""

from graphics import *


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        if p1.getX() <= point.getX() <= p2.getX() and p1.getY() <= point.getY() <= p2.getY():
            return True
        return False

    def open(self, color, label):
        self.text.setText(label)
        self.color_door(color)

    def close(self, color, label):
        self.text.setText(label)
        self.color_door(color)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        return False

    def set_secret(self, secret):
        self.secret = secret
