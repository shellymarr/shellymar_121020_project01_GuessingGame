from graphics import *
from random import*
def roll():

    w = GraphWin()
    s1 = Rectangle(Point(80,80), Point(20,20))
    s1.setFill("Blue")
    s1.draw(w)

    s2 = Rectangle(Point(140, 140), Point (80,80))
    s2.setFill("Blue")
    s2.draw(w)

    
    m = Text(Point(80,10), ("Click to roll: "))
    m.draw(w)
    
    center = Point(60,60)
    sd1 = Circle(center, 5)
    sd1.setFill("White")

    center = Point(45,60)
    sd2 = Circle(center, 5)
    sd2.setFill("White")

    center3 = Point(30,60)
    sd3 = Circle(center3, 5)
    sd3.setFill("Red")

    center4 = Point(30,30)
    sd4 = Circle(center4, 5)
    sd4.setFill("White")

    center5 = Point(45,30)
    sd5 = Circle(center5, 5)
    sd5.setFill("White")

    center6 = Point(60,30)
    sd6 = Circle(center6, 5)
    sd6.setFill("White")

    center7 = Point(130,130)
    sd7 = Circle(center7, 5)
    sd7.setFill("White")

    center8 = Point(130,115)
    sd8 = Circle(center8, 5)
    sd8.setFill("White")

    center9 = Point(130,100)
    sd9 = Circle(center9, 5)
    sd9.setFill("White")

    center10 = Point(100,100)
    sd10 = Circle(center10, 5)
    sd10.setFill("White")

    center11 = Point(100,115)
    sd11 = Circle(center11, 5)
    sd11.setFill("White")

    center12 = Point(100,130)
    sd12 = Circle(center12, 5)
    sd12.setFill("White")


    w.getMouse()
    Random_number_1 = randint(1,6)
    if Random_number_1 == 1:
        w.getMouse()
        sd1.draw(w)
    elif Random_number_1 == 2:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
    elif Random_number_1 == 3:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
        sd3.draw(w)
    elif Random_number_1 == 4:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
        sd3.draw(w)
        sd4.draw(w)
    elif Random_number_1 == 5:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
        sd3.draw(w)
        sd4.draw(w)
        sd5.draw(w)
    elif Random_number_1 == 6:
        w.getMouse()
        sd1.draw(w)
        sd2.draw(w)
        sd3.draw(w)
        sd4.draw(w)
        sd5.draw(w)
        sd6.draw(w)

    w.getMouse()
    Random_number_2 = randint(1,6)
    if Random_number_2 == 1:
        w.getMouse()
        sd7.draw(w)
    elif Random_number_2 == 2:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
    elif Random_number_2 == 3:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
        sd9.draw(w)
    elif Random_number_2 == 4:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
        sd9.draw(w)
        sd10.draw(w)
    elif Random_number_2 == 5:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
        sd9.draw(w)
        sd10.draw(w)
        sd11.draw(w)
    elif Random_number_2 == 6:
        w.getMouse()
        sd7.draw(w)
        sd8.draw(w)
        sd9.draw(w)
        sd10.draw(w)
        sd11.draw(w)
        sd12.draw(w)

    
    m.undraw()
    m2 = Text(Point(80,10), ("Click to close program: "))
    m2.draw(w)

    w.getMouse()
    w.close()
    return [Random_number_1, Random_number_2]
guess = [0,0]
while True:
    print("Guess Number on 1st Die roll: (1-6)")
    guess[0] = int(input())
    if guess[0]<6 or guess[0]>1:
        break

while True:
    print("Guess Number on 2nd Die roll: (1-6)")
    guess[1] = int(input())
    if guess[1]<6 or guess[1]>1:
        break
    guess.sort()
actual_appearance = roll()
actual_appearance.sort()

if actual_appearance[0] == guess[0] and actual_appearance[1] == guess[1]:
    print("You Won!")
else:
    print("Try Again!")


