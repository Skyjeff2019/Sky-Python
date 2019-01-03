#textcodes={'tyl':'text you later', 'lol': 'laugh out loud', 'wyd':'what you doing'}

#define the dictionary and call the functions that allow you to change, delete,
def dictionary():

    textCodes = {"lol" : "laugh out loud", "wyd" : "what you doing", "ttyl" : "talk to you later"}

    print (textCodes)

    yesNo = input("Find a text code? -y -n")

    while (yesNo == "y"):

        print(textCodes)

        defCode = input("What code would you like defined?")

        if (defCode in textCodes):

            print (textCodes[defCode])

        if (defCode not in textCodes):

            add(textCodes, defCode)

        changeDeletetextcodese(textCodes)

        yesNo = input("Would you like to keep going? -y -n")

#this is where code can be added and then defined or given a new meaning. need to use an if statement in order to allow something to be added or changed

def add(textCodes, defCode):

    add = input("Would you like to add this to the dictionary? -y -n")

    if (add == "y"):

        newCode = defCode

        newMeaning = input("Enter the code's meaning(this is found after the abreviation).")

        textCodes[newCode] = newMeaning

        print (textCodes)

#this is to change or delete codes. need to use inputs and fit them into if statements

def changeDeletetextcodese(textCodes):

    userEdit = input("Would you like to change or delete code(s)? -c -d -n")
    if (userEdit == "c"):

        whichCode = input("What code would you like to change or modify?")

        print(whichCode)

        newmeaning = input("Enter the code's new meaning or modification.")

        if (whichCode in textCodes):

            textCodes[whichCode] = newmeaning
        else:
            add(textCodes, whichCode)
        print (textCodes)

    if (userEdit == "d"):
        deleteCode = input("Which code do you want to delete or remove?")

        if (deleteCode in textCodes):
            areYouSure = input("Are you sure you want to delete this- " + deleteCode + " from the dictionary? -y -n")

            if (areYouSure == "y"):
                del textCodes[deleteCode]
        print (textCodes)

dictionary()


