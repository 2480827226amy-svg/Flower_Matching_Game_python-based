import opening
import level1
import level2
import level3
from graphics import *
import random
from time import sleep #https://docs.python.org/3/library/time.html We use function .sleep(). This function can help us to suspend execution of the figures in our window for certain seconds before the next cycle of movement. We need to import this function here so that we can use it later in our function opening() and level().


def moveClick(levels, win):
    """ This function moves levels to make cute animations. 
    :param levels: the list of levels stored as objects
    :param win: the window where the game is
    :return: The point where the user clicked, or None if no click.
    """
    click = win.checkMouse() 
    while click is None:
       
        levels[0].move(0, -3)
        levels[1].move(0, 3)
        levels[2].move(0, -3)
        time.sleep(0.1)# .sleep() here can help to pause the figure for 0.1 seconds to make the movement visible.
        levels[0].move(0, 3)
        levels[1].move(0, -3)
        levels[2].move(0, 3)
        time.sleep(0.1)# .sleep() here can help to pause the figure for 0.1 seconds to make the movement visible.
        click = win.checkMouse()
        if click is not None:
            return click  # check for a mouse click during the movement
    return click

def level():
    """ The function draws levels onto the window and gets click from users to move onto the next page.
    """
    background = Image(Point(opening.WIDTH/2, opening.HEIGHT/2),"flower levels background.gif")
    background.draw(opening.win)

    LV1 = Image(Point(opening.WIDTH*2.5/9, opening.HEIGHT*0.6),"number_1.gif")
    LV1.draw(opening.win)

    LV2 = Image(Point(opening.WIDTH*4.5/9, opening.HEIGHT*0.6),"number_2.gif")
    LV2.draw(opening.win)

    LV3 = Image(Point(opening.WIDTH*6.5/9, opening.HEIGHT*0.6),"number_3.gif")
    LV3.draw(opening.win)
    clickLevel = moveClick([LV1, LV2, LV3], opening.win)

    
    if clickLevel.getX()>opening.WIDTH*2/9 and clickLevel.getX() <opening.WIDTH*3/9 and clickLevel.getY()>opening.HEIGHT*1/2 and clickLevel.getY()<opening.HEIGHT*3.5/5:
        LV1.undraw()
        LV2.undraw()
        LV3.undraw()
        background.undraw()
        level1.level1()
        # import function level 1
    elif clickLevel.getX()>opening.WIDTH*4/9 and clickLevel.getX()< opening.WIDTH*5/9 and clickLevel.getY()>opening.HEIGHT*1/2 and clickLevel.getY()<opening.HEIGHT*3.5/5:
        LV1.undraw()
        LV2.undraw()
        LV3.undraw()
        background.undraw()
        level2.level2()
        # import function level 2
    elif clickLevel.getX()>opening.WIDTH*6/9 and clickLevel.getX()< opening.WIDTH*7/9 and clickLevel.getY()>opening.HEIGHT*1/2 and clickLevel.getY()<opening.HEIGHT*3.5/5:
        LV1.undraw()
        LV2.undraw()
        LV3.undraw()
        background.undraw()
        level3.level3()
        # import function level 3