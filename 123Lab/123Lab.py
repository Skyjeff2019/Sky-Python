def main() :

    gradeYear = input('What year are you in school - ')
    strGrade = getgrade(gradeYear)
    print (strGrade)
    avgGrade = [92.5,95.6,96.6,98.9]
    theAvggrade = avggpa(avgGrade,len(avgGrade))
    strPercent = lettergrade(theAvggrade)
    print(strPercent)
    if strPercent == 'You have an A' or strPercent == 'You have a B' or strPercent == 'You have a C':
        print('You are passing')
    else:
        print('You are failing')



def getgrade(gradeYear):
        if gradeYear == '9':
            return('You are a freshman')
        elif gradeYear == '10':
            return('You are a sophmore')
        elif gradeYear == '11':
            return('You are a junior')
        elif gradeYear == '12':
            return('You are a senior')
        else:

            return('You are not in highschool')


def avggpa(mylist,num) :

        x = mylist[0] + mylist[1] + mylist[2] + mylist[3]
        y = x / 4
        return y

def lettergrade(percentgrade):
        if percentgrade >= 92.5:
            return('You have an A')
        elif percentgrade >= 88:
            return('You have a B')
        elif percentgrade >= 78:
            return('You have a C')
        elif percentgrade >= 72:
            return ('You have a D')
        elif percentgrade >= 65:
            return ('You have a F')
        else:
            return('where were you all this time?')


main()
