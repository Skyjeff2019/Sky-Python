import random

def dice () :
    #this is were the magic happens
    #be sure to include the question to play again and to print the amout of times played
    loop = 'y'
    times = 0
    while loop =='y' :
        times = times + 1
        y = randNum ()
        print(whichDice(y))
        print ("You just rolled  - " + str(y))
        loop = input ("Would you like to play again? (y/n) - ")
        print ("You have played " + str(times) + " times.")


#------------------------------------------------------------------------


def randNum () :
    #this is where the dice values are defined and made
    #remember to return the values after defining them
    x = random.randint(1,6)
    return (x)

def whichDice (randnum) :
    a = ' ------- '

    if randnum==1 or randnum==2 :
        b = '|       |'
    elif randnum==3 :
        b = '|   *   |'
    elif randnum==4 or randnum==5 or randnum==6 :
        b = '| *  *  |'

    if randnum==1 or randnum==3 or randnum==5 :
        c = '|   *   |'
    elif randnum==4 :
        c = '|       |'
    elif randnum==2 or randnum==6 :
        c = '| *  *  |'

    if randnum==1 or randnum==2 :
        d = '|       |'
    elif randnum==3 :
        d = '|   *   |'
    elif randnum==4 or randnum==5 or randnum==6 :
        d = c = '| *  *  |'

    e = ' ------- '

    return(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e)


dice()
