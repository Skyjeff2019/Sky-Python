def main():
    draw7()
    starsandstripes()
    toseven()

def draw7():
    for x in range (0, 7):
        myList = ""
        for x in range (0, 7):
            myList += "*"
        print(myList)



def starsandstripes():
    for x in range(0, 6):
        if (x%2 ==0) :
            print("*"*6)
        else:
            print("-"*6)
        dashstring=""


def toseven() :
    for x in range(1,8) :
        print (str(x) * x)

main()
