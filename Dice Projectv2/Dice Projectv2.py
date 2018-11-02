import random
ROLLNUM = 2

def main():
    setOfDice=[0] * 6 # create a list to store 6 different dice
    setOfDice = defineDice()
    printDiceSideBySide(setOfDice) # print all six dice
    play = 'y'
    game = 0
# prime with y for yes and keep playing until n for no
    while play == 'y':
        for i in range(0, 22):
            print('_', end ='') # print a line between each new roll
    print()
    game += 1
    print(' game - ' + str(game))
    play = input('play again - y or n - ') # keep playing or stop
print('you played ' + str(game) + ' times')
# defines 6 different dice counts and returns the characters
# needed to print the dice to the console

def defineDice():
    dice=[0] * 6
    topBot  = ' -------- '
    blank   = '|       |'
    oneDotL = '| *     |'
    oneDotM = '|   *   |'
    oneDotR = '|     * |'
    twoDot  = '|  * *  |'
    for num in range(0, 6):
        if num == 0:
            dice[num] = [topBot,blank,oneDotM, blank,topBot]
        elif num == 1:
            dice[num] = [topBot,blank,twoDot,blank,topBot]
        elif num == 2:
            dice[num] = [topBot,oneDotL,oneDotM,oneDotR,topBot]
        elif num == 3:
            dice[num] = [topBot,twoDot,blank,twoDot,topBot]
        elif num == 4:
            dice[num] = [topBot,twoDot,oneDotM,twoDot,topBot]
        else:
            dice[num] = [topBot,twoDot,twoDot,twoDot,topBot]
    return dice
# generate a random number between 1 and 6 to represent random roll of dice

def rollDice():
    print('roll dice')
# receives a list of the dice


def printDiceSideBySide(diceSet):
    print('print dice')
main()
