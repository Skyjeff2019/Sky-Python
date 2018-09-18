def myfun():
    print("I am from Bellarmine")
    print("My favorite subject is Python")

myfun()

def myfun2():
    grade = input ( "what grade are you in school? -")
    yearsinschool= (int(grade) + 6)
    print(yearsinschool)

myfun2()


def myfun3():
    city= input ("what city are you from?")
    grade2= input (" what grade in school are you")
    print( "you are from " + city)
    print( " you are in this grade " + grade2)

myfun3()

from random import *

def myfun4():
    x= input( "enter one number -")
    y= input( "enter another numnber-")
    myNumber= randint(int(x), int(y))
    print(str(myNumber) + " this is your random number")

def myfun5():
    length= input( "what is the length of a box")
    width= input( "what is the width of a box")
    area= int(length) * int(width)
    print("the area is" + area)
    return(area)


myfun5()


