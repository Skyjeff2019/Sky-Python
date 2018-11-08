import random

ROLLNUM = 2

def dice():
    loop = "y"

    #setOfDice = createDice()
    #printDiceSideBySide(setOfDice)
    times = 0
    while loop== "y":
        diceList = [0]*ROLLNUM
        #for i in range(ROLLNUM):
        (roll, roll2) = randnum()
        print(roll, roll2)
        diceList = createDice(roll, roll2)

        printDiceSideBySide(diceList)
            #printDiceSideBySide(diceSet)
        times += 1

        print ('you rolled this- ' + str(roll) + " and a " +str(roll2))

        loop = input('would you like to play again (y/n)')

        print('you have played ' + str(times) + " times")



def randnum():
    x = random.randint(1,5)
    y = random.randint(1,5)
    return(x,y)

def createDice(roll, roll2):
   topBot = ' ------- '
   blank1  = '|       |'
   blankL  = '| *     |'
   blankR  = '|     * |'
   blankM  = '|   *   |'
   blank2  = '|  * *  |'


   onedice = [topBot, blank1, blankM, blank1, topBot]

   twodice = [topBot, blank1, blank2, blank1, topBot]

   threedice = [topBot, blankL, blankM, blankR, topBot]

   fourdice = [topBot, blank2, blank1, blank2, topBot]

   fivedice = [topBot, blank2, blankM, blank2, topBot]

   sixdice = [topBot, blank2, blank2, blank2, topBot]

   if roll == 1:
       roll = onedice

   elif roll == 2:
       roll = twodice

   elif roll == 3:
       roll = threedice

   elif roll == 4:
       roll = fourdice

   elif roll == 5:
       roll = fivedice

   elif roll == 6:
       roll = sixdice

   if roll2 == 1:
       roll2 = onedice

   elif roll2 == 2:
       roll2 = twodice

   elif roll2 == 3:
       roll2 = threedice

   elif roll2 == 4:
       roll2 = fourdice

   elif roll2 == 5:
       roll2 = fivedice

   elif roll2 == 6:
       roll2 = sixdice

   else:
       print('error')

   Dice1 = roll
   Dice2 = roll2



   allDice = [Dice1, Dice2]


   return allDice

def printDiceSideBySide(allDice):
     for row in range(0,len(allDice[0])):
         for col in range(0,len(allDice)):
             print(allDice[col][row], end = '\t')
         print()


dice()
