"""
Aidan Stout
lab6.py
Problem: create program to encode a message
I certify that this is entirely my work
"""

from graphics import *


def vigenere():
    win = GraphWin("Vigenere", 500, 300)
    message_text = Text(Point(100, 40), "Message to code")
    keyword_text = Text(Point(120, 80), "Enter Keyword")
    message_text.draw(win)
    keyword_text.draw(win)
    message = Entry(Point(330, 40), 30)
    keyword = Entry(Point(285, 80), 20)
    message.draw(win)
    keyword.draw(win)
    # button
    box = Rectangle(Point(210, 180), Point(290, 120))
    box.draw(win)
    button = Text(Point(250, 150), "Encode")
    button.draw(win)

    win.getMouse()
    text = message.getText()
    text = text.replace(" ", '')
    text = text.upper()
    key = keyword.getText()
    key = key.replace(" ", '')
    key = key.upper()

    output = ""
    for i in range(len(text)):
        character = ord(text[i]) - 65
        key_character = ord(key[i % len(key)]) - 65
        encode = character + key_character
        encode = encode % 26
        encode = encode + 65
        output = output + chr(encode)

    button.undraw()
    box.undraw()
    result_message = Text(Point(250, 200), "Resulting Message")
    result_message.draw(win)
    result = Text(Point(250, 225), output)
    result.draw(win)
    close_message = Text(Point(250, 280), "Click Anywhere to Close Window")
    close_message.draw(win)
    win.getMouse()
    win.close()
