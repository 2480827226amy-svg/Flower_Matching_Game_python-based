import opening
import levels
from graphics import *
import random


def level3():
    """
    This function helps to draw the page of level three, also, people can play level three and see whether they win the game or not.
    """
    background_level = Image(Point(opening.WIDTH/2, opening.HEIGHT/2),"levels.gif")
    background_level.draw(opening.win)

    instruction = Text(Point(opening.WIDTH/2,opening.HEIGHT/12),"You're allowed to switch the position between two flowers at a time. Please click the two flowers you want to move!")
    instruction.setSize(15)
    instruction.setFace("courier")
    instruction.setFill(color_rgb(39, 68, 50))
    instruction.draw(opening.win)

    step = Rectangle(Point(150, opening.HEIGHT - 600), Point(50, opening.HEIGHT-500))
    step.setOutline(color_rgb(206,99,130))
    step.setWidth(5)
    step.draw(opening.win)


    steps = Text(Point(100,opening.HEIGHT - 480),"Steps Left")
    steps.setSize(20)
    steps.setFace("courier")
    steps.setFill(color_rgb(39, 68, 50))
    steps.draw(opening.win)

    star1 = Image(Point(1100, 200), "star1_green.gif")
    star2 = Image(Point(200, 600), "star1_green.gif")
    star3 = Image(Point(1180, 500), "star2_green.gif")
    star4 = Image(Point(600, 120), "star2_green.gif")
    star5 = Image(Point(100, 350), "star2_green.gif")

    star1.draw(opening.win)
    star2.draw(opening.win)
    star3.draw(opening.win)
    star4.draw(opening.win)
    star5.draw(opening.win)

    pot_1 = Image(Point(opening.WIDTH*2.5/9, opening.HEIGHT*0.8),"flower_pot2.gif")
    pot_1.draw(opening.win)

    pot_2 = Image(Point(opening.WIDTH*4.5/9, opening.HEIGHT*0.8),"flower_pot2.gif")
    pot_2.draw(opening.win)

    pot_3 = Image(Point(opening.WIDTH*6.5/9, opening.HEIGHT*0.8),"flower_pot2.gif")
    pot_3.draw(opening.win)

    pot_4 = Image(Point(opening.WIDTH*2.5/9, opening.HEIGHT*0.4),"flower_pot2.gif")
    pot_4.draw(opening.win)

    pot_5 = Image(Point(opening.WIDTH*4.5/9, opening.HEIGHT*0.4),"flower_pot2.gif")
    pot_5.draw(opening.win)

    pot_6 = Image(Point(opening.WIDTH*6.5/9, opening.HEIGHT*0.4),"flower_pot2.gif")
    pot_6.draw(opening.win)

    


    position=[(312.1 , 185),(361.1, 125),(410.1, 185),(601,  185),(650, 125),(699,  185),(889.9, 185),(938.9, 125),(987.9, 185),\
              (312.1 , 465),(361.1, 405),(410.1, 465),(601,  465),(650, 405),(699,  465),(889.9, 465),(938.9, 405),(987.9, 465)]
    flowerPosition=[]
    flowerColor=[]
    flowerObject = []
    for i in range (6):
        a=random.choice(position)

        flower = Image(Point(a[0],a[1]),"blue1.gif")
        flower.draw(opening.win)
        flowerPosition.append(a)
        flowerColor.append("b"+str(i+1))
        position.remove(a)
        flowerObject.append(flower)


    for i in range (6):
        a=random.choice(position)

        flower = Image(Point(a[0],a[1]),"pink1.gif")
        flower.draw(opening.win)
        flowerPosition.append(a)
        flowerColor.append("p"+str(i+1))
        position.remove(a)
        flowerObject.append(flower)

    for i in range (6):
        a=random.choice(position)

        flower = Image(Point(a[0],a[1]),"purple1.gif")
        flower.draw(opening.win)
        flowerPosition.append(a)
        position.remove(a)
        flowerColor.append("v"+str(i+1))
        flowerObject.append(flower)

    

    sorted_pairs = sorted(zip(flowerPosition, flowerColor), key=lambda pair: pair[0][0]) #https://docs.python.org/3/reference/expressions.html#expression-lists lambda here can help us to extract the x-coordinate (pair[0][0]) from each (position, color) pair. In this way, the flowers in the dictionary will be placed from right to left in sequence. Thus, we can easily locate the three flowers in each group that we need to check no matter how they exchange.
    flowerDic = {pos: color for pos, color in sorted_pairs}
    print(flowerDic)

    if checkSuccess3(flowerDic):
        print("You Win!")
        opening.win.getMouse()  
        opening.win.close()    

    for i in range (6):
        number=Text(Point(100,opening.HEIGHT-550),str(6-i))
        number.setSize(30)
        number.setFace("courier")
        number.setFill(color_rgb(206,99,130))
        number.draw(opening.win)


        click1 = opening.win.getMouse()
        x=getFlowerIndex3(click1,flowerPosition)

        click2=opening.win.getMouse()
        y=getFlowerIndex3(click2,flowerPosition)

        if x !=None and y != None: 
            flowerObject[x].undraw()
            flowerObject[y].undraw()


        
        pos_x = flowerPosition[x]
        pos_y = flowerPosition[y]

   
        flowerObject[x].move(pos_y[0] - flowerObject[x].getAnchor().getX(),pos_y[1] - flowerObject[x].getAnchor().getY())

        flowerObject[y].move(pos_x[0] - flowerObject[y].getAnchor().getX(),pos_x[1] - flowerObject[y].getAnchor().getY())


        flowerObject[x].draw(opening.win)
        flowerObject[y].draw(opening.win)


        flowerColor[x], flowerColor[y] = flowerColor[y], flowerColor[x] #https://docs.python.org/3/reference/simple_stmts.html#assignment-statements Section7.2  a,b=b,a can help us swap the colors of the two flowers we click on at positions x and y. We need to use this swap to contnuously update the list after two flowers have exchanged places, so that it can keep the color data in the list accurate.
        flowerPosition[x], flowerPosition[y] = flowerPosition[y], flowerPosition[x] #https://docs.python.org/3/reference/simple_stmts.html#assignment-statements Section7.2  a,b=b,a can help us swap the coordinates of the two flowers we click on at positions x and y. We need to use this swap to contnuously update the list after two flowers have exchanged places, so that it can keep the position data in the list accurate.



        flowerDic[flowerPosition[x]], flowerDic[flowerPosition[y]] = (flowerDic[flowerPosition[y]],flowerDic[flowerPosition[x]]) #https://docs.python.org/3/reference/simple_stmts.html#assignment-statements Section7.2 a,b=b,a here can help us to swap the color values associated with the updated flower positions in the dictionary. This helps us to ensure that after swapping the flowers' positions, each position still connects to the right flower color.

        print("Updated Dict:", flowerDic)

        number.undraw()

        if checkSuccess3(flowerDic):
            print("You Win!")
            
            clickExit = opening.win.getMouse()
            if clickExit.getX()>opening.WIDTH/5 and clickExit.getX() <opening.WIDTH*2/5 and clickExit.getY()>550 and clickExit.getY()<650:
                levels.level()
            if clickExit.getX()>opening.WIDTH*3/5 and clickExit.getX() <opening.WIDTH*4/5 and clickExit.getY()>550 and clickExit.getY()<650:
                opening.win.close()

    else:
        box = Rectangle(Point(opening.WIDTH/2 - 200, opening.HEIGHT/2 - 80),Point(opening.WIDTH/2 + 200, opening.HEIGHT/2 + 80))
        box.setOutline(color_rgb(115,145,76)) 
        box.setWidth(10)
        box.draw(opening.win)


        winText = Text(Point(opening.WIDTH/2, opening.HEIGHT/2), "YOU FAIL!")
        winText.setSize(36)
        winText.setStyle("bold")
        winText.setFace("courier")
        winText.setFill(color_rgb(115,145,76)) 
        winText.draw(opening.win)

        print("You Fail!")
        choice1 = Rectangle(Point(opening.WIDTH/5, 550),Point(opening.WIDTH*2/5 , 650))
        choice1.setOutline(color_rgb(115,145,76)) 
        choice1.setWidth(10)
        choice1.draw(opening.win)

        Text1 = Text(Point(opening.WIDTH*3/10, 600), "Go back to levels.")
        Text1.setSize(20)
        Text1.setStyle("bold")
        Text1.setFace("courier")
        Text1.setFill(color_rgb(115,145,76)) 
        Text1.draw(opening.win)



        choice2 = Rectangle(Point(opening.WIDTH*3/5, 550),Point(opening.WIDTH*4/5 , 650))
        choice2.setOutline(color_rgb(115,145,76)) 
        choice2.setWidth(10)
        choice2.draw(opening.win)

        Text2 = Text(Point(opening.WIDTH*7/10, 600), "Exit:(")
        Text2.setSize(20)
        Text2.setStyle("bold")
        Text2.setFace("courier")
        Text2.setFill(color_rgb(115,145,76)) 
        Text2.draw(opening.win)

        clickExit = opening.win.getMouse()

        if clickExit.getX()> opening.WIDTH/5 and clickExit.getX() < opening.WIDTH*2/5 and clickExit.getY()>550 and clickExit.getY()<650:
            winText.undraw()
            box.undraw()
            for flowers in flowerObject:
                flowers.undraw()
            pot_1.undraw()
            pot_2.undraw()
            pot_3.undraw()
            pot_4.undraw()
            pot_5.undraw()
            pot_6.undraw()
            instruction.undraw()
            star1.undraw()
            star2.undraw()
            star3.undraw()
            star4.undraw()
            star5.undraw()
            step.undraw()
            steps.undraw()
            Text1.undraw()
            Text1.undraw()
            levels.level()
        if clickExit.getX()> opening.WIDTH*3/5 and clickExit.getX() < opening.WIDTH*4/5 and clickExit.getY()>550 and clickExit.getY()<650:
            opening.win.close()

 


def getFlowerIndex3(click, flowerPosition): 
    """
    This function helps to get the index of the flower we click on.
    :param click:(graphics.Point) The Point where the mouse was clicked.
    :param flowerPosition: (list[tuple[int, int]])A list of (x, y) coordinate tuples representing flower centers that we have in the level1() function
    :return: The index of the flower clicked on, or None if no flower is clicked.
    """
    i=0
    for position in flowerPosition:
        x,y=position #https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-expression_list x, y = position devides the position(x, y)  into two separate variables. This makes it easier for us to directly compare the x and y coordinates with the mouse click position.
        if abs(click.getX()-x)<= 34 and abs(click.getY()-y) <=34:
            return i
        i+=1
    return None

def checkSuccess3(flowerDic):
    """
    This function helps to check whether the flowers are arranged successfully.
    :param flowerDic: (dict[tuple[int, int], str]) A dictionary where keys are (x, y) positions and values are color strings. The color string ends with a number or character distinguishing different flowers.
    :return: True if all three groups of flowers are correctly arranged by color, otherwise None.
    """
    top = []
    bottom = []

    for pos, color in flowerDic.items(): #
        if pos[1] < 300:
            top.append((pos, color))
        else:
            bottom.append((pos, color))

    def check_row(row):  
        """ The function checks if the flowers in each rows are of the same color.
        :param row: the rows of flowers
        """
        row.sort(key=lambda x: x[0][0]) #https://docs.python.org/3/reference/expressions.html#expression-lists lambda here can help us to extract the x-coordinate (pair[0][0]) from each (position, color) pair. In this way, the flowers in the dictionary will be placed from right to left in sequence in both two rows. Thus, we can easily locate the three flowers in each group that we need to check no matter how they exchange.
        for i in range(0, 9, 3):
            group = row[i:i+3]
            same_color = group[0][1][:-1]
            if not all(g[1][:-1] == same_color for g in group): #https://docs.python.org/3/library/functions.html#all The all() function here can help us to check if all flowers in the current group share the same color at the same time.
                return False
        return True

    if check_row(top) and check_row(bottom):
        # success UI
        box = Rectangle(Point(opening.WIDTH/2 - 200, opening.HEIGHT/2 - 80),Point(opening.WIDTH/2 + 200, opening.HEIGHT/2 + 80))
        box.setOutline(color_rgb(206,99,130)) 
        box.setWidth(10)
        box.draw(opening.win)


        winText = Text(Point(opening.WIDTH/2, opening.HEIGHT/2), "YOU WIN!")
        winText.setSize(36)
        winText.setStyle("bold")
        winText.setFace("courier")
        winText.setFill(color_rgb(206,99,130)) 
        winText.draw(opening.win)

        choice1 = Rectangle(Point(opening.WIDTH/5, 550),Point(opening.WIDTH*2/5 , 650))
        choice1.setOutline(color_rgb(206,99,130)) 
        choice1.setWidth(10)
        choice1.draw(opening.win)

        Text1 = Text(Point(opening.WIDTH*3/10, 600), "Go back to levels.")
        Text1.setSize(20)
        Text1.setStyle("bold")
        Text1.setFace("courier")
        Text1.setFill(color_rgb(206,99,130)) 
        Text1.draw(opening.win)



        choice2 = Rectangle(Point(opening.WIDTH*3/5, 550),Point(opening.WIDTH*4/5 , 650))
        choice2.setOutline(color_rgb(206,99,130)) 
        choice2.setWidth(10)
        choice2.draw(opening.win)

        Text1 = Text(Point(opening.WIDTH*7/10, 600), "Exit:)")
        Text1.setSize(20)
        Text1.setStyle("bold")
        Text1.setFace("courier")
        Text1.setFill(color_rgb(206,99,130)) 
        Text1.draw(opening.win)

        return True
    return False
