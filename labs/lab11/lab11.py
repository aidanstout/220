"""
Aidan Stout
lab11.py
Problem: create a game that lets user win if they pick the correct door
I certify that this is entirely my work
"""

from lab10.button import Button
from lab10.door import Door
from graphics import *
from random import randint


def main():
    win = GraphWin("Test", 650, 500)
    rect_button = Rectangle(Point(450, 30), Point(600, 100))
    button = Button(rect_button, "Exit")
    button.draw(win)
    rect_door_1 = Rectangle(Point(50, 150), Point(200, 450))
    door_1 = Door(rect_door_1, "Door 1")
    door_1.color_door('brown')
    door_1.draw(win)
    rect_door_2 = Rectangle(Point(250, 150), Point(400, 450))
    door_2 = Door(rect_door_2, "Door 2")
    door_2.color_door('brown')
    door_2.draw(win)
    rect_door_3 = Rectangle(Point(450, 150), Point(600, 450))
    door_3 = Door(rect_door_3, "Door 3")
    door_3.color_door('brown')
    door_3.draw(win)
    counter = Rectangle(Point(50, 30), Point(200, 100))
    counter.draw(win)
    line = Line(Point(125, 30), Point(125, 100))
    line.draw(win)
    win_text = Text(Point(87, 20), "Wins")
    win_text.draw(win)
    loss_text = Text(Point(162, 20), "Losses")
    loss_text.draw(win)
    win_count = 0
    wins = Text(Point(87, 65), str(win_count))
    wins.draw(win)
    loss_count = 0
    losses = Text(Point(162, 65), str(loss_count))
    losses.draw(win)
    top_text = Text(Point(325, 100), "I have a secret door")
    top_text.draw(win)
    bottom_text = Text(Point(325, 475), "Click to guess which is the secret door!")
    bottom_text.draw(win)
    click = win.getMouse()
    doors = [door_1, door_2, door_3]
    while not button.is_clicked(click):
        rand_door = doors[randint(0, 2)]
        rand_door.set_secret(True)
        if door_1.is_clicked(click):
            if door_1.is_secret():
                door_1.open('green', 'Door 1')
                win_count += 1
                wins.setText(str(win_count))
                top_text.setText('You win!')
                bottom_text.setText("Click anywhere to play again!")
            else:
                door_1.open('red', 'Door 1')
                loss_count += 1
                losses.setText(str(loss_count))
                top_text.setText("Sorry, incorrect")
                bottom_text.setText("Click anywhere to play again!")
        elif door_2.is_clicked(click):
            if door_2.is_secret():
                door_2.open('green', 'Door 2')
                win_count += 1
                wins.setText(str(win_count))
                top_text.setText('You win!')
                bottom_text.setText("Click anywhere to play again!")
            else:
                door_2.open('red', 'Door 2')
                loss_count += 1
                losses.setText(str(loss_count))
                top_text.setText("Sorry, incorrect")
                bottom_text.setText("Click anywhere to play again!")
        elif door_3.is_clicked(click):
            if door_3.is_secret():
                door_3.open('green', 'Door 3')
                win_count += 1
                wins.setText(str(win_count))
                top_text.setText('You win!')
                bottom_text.setText("Click anywhere to play again!")
            else:
                door_3.open('red', 'Door 3')
                loss_count += 1
                losses.setText(str(loss_count))
                top_text.setText("Sorry, incorrect")
                bottom_text.setText("Click anywhere to play again!")
        click = win.getMouse()
        if button.is_clicked(click):
            win.close()
        else:
            door_1.close('brown', "Door 1")
            door_2.close('brown', 'Door 2')
            door_3.close('brown', 'Door 3')
            rand_door.set_secret(False)
            top_text.setText("I have a secret door")
            bottom_text.setText("Click to guess which is the secret door!")
            click = win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
