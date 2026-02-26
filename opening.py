
import levels
import random
from time import sleep #https://docs.python.org/3/library/time.html We use function .sleep(). This function can help us to suspend execution of the figures in our window for certain seconds before the next cycle of movement. We need to import this function here so that we can use it later in our function opening() and level().
from graphics import *

WIDTH = 1300
HEIGHT = 700
win = GraphWin("Game Page", WIDTH, HEIGHT)


def moveStart(button, message, win):
    """
    This function lets the start buttom and the text to move up and down until we click on it.
    :param button:(graphics.Oval) The oval shape that acts as the button.
    :param message:(graphics.Text) The text "start" displayed on the button.
    :param win: (graphics.GraphWin) The window where the button is drawn and clicked.
    :return: The point where the user clicked, or None if no click.
    """
    click = win.checkMouse()
    while click is None:
        button.move(0, -2)
        message.move(0, -2)
        time.sleep(0.1) # .sleep() here can help to pause the figure for 0.1 seconds to make the movement visible.

        click = win.checkMouse()
        if click: break # https://www.geeksforgeeks.org/python-break-statement/ If a click is detected, break the loop and stop the animation.

        button.move(0, 2)
        message.move(0, 2)
        time.sleep(0.1)

        click = win.checkMouse()
    return click

def opening():
    """
    This function draws the opening page of our game.
    """
    background = Image(Point(WIDTH/2, HEIGHT/2),"flower arrangement.gif")
    background.draw(win)

    button = Oval(Point(WIDTH/3,HEIGHT*3/5),Point(WIDTH*2/3,HEIGHT*4/5))
    button.setFill(color_rgb(239,139,169))
    button.setOutline(color_rgb(206,99,130))
    button.setWidth(5)
    button.draw(win)


    message = Text(Point(WIDTH*1/2,HEIGHT*7/10),"START")
    message.setSize(36)
    message.setFace("courier")
    message.setFill(color_rgb(39,68,50))
    message.draw(win)

    clicktoexit = Text(Point(WIDTH*1/2,HEIGHT*5/6),"Click anywhere else to exit.")
    clicktoexit.setSize(15)
    clicktoexit.setFace("courier")
    clicktoexit.setFill(color_rgb(39, 68, 50))
    clicktoexit.draw(win)

    click = moveStart(button, message, win)
    if click.getX()>WIDTH/3 and click.getX()<WIDTH*2/3 and click.getY()>HEIGHT*3/5 and click.getY()<HEIGHT*4/5:
        button.undraw()
        background.undraw()
        message.undraw()
        levels.level()
    else:
        win.close()
    

