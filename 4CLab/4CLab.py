def main():
    draw7()

def draw7():
    for x in range (0, 7):
        myList = ""
        for x in range (0, 7):
            myList += "*"
        print(myList)



main()


def starsandstripes():
    for x in range(0, 3):
        starstring=""
        dashstring=""

    for z in range(0, 7):
        starstring += '*'
        dashstring += '-'

    print(starstring)
    print(dashstring)


starsandstripes()
