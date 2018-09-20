def myfun():
    print("I am from Bellarmine")
    print("My favorite subject is Python")

myfun()

def myfun2():
    grade = input ("what grade are you in school? -")
    yearsinschool= int(grade)
    print("you have benn to school for this many years " +str(yearsinschool))

myfun2()


def myfun3():
    city= input ("what city are you from?")
    grade2= input ("what grade in school are you")
    print( "you are from " + city)
    print( " you are in this grade " + grade2)

myfun3()

from random import *

def myfun4():
    x= input("enter one number -")
    y= input("enter another numnber-")
    myNumber= randint(int(x), int(y))
    print(str(myNumber) + "-this is your random number between-")
    print(str(x) + " and " +str(y))

myfun4()

def myfun5(num1, num2):
    area = int(num1) *  int(num2)
    return(area)

length=input( "enter a length for your box-")
width= input( " enter a width for your box-")
area= myfun5(length, width)
print("the area is " + str(area))


def myfun6(num1, num2):
    perimeter= int(num1) *2 + int(num2) *2
    return(perimeter)

perimeter = myfun6(length, width)
print( "the perimeter of your box is " + str(perimeter))

