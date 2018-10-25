def main():
    whatGrade = input('What grade are you in?')
    schoolYear = gradeName(whatGrade)
    print(schoolYear)
    gradeList = []
    grades = input('How many grades?')
    print(grades)
    for x in range (0, int(grades)):
        myGrades = float(input('Give a number grade.'))
        gradeList.insert(x, myGrades)
    print (gradeList)
    average = avgGrade(gradeList)
    print('Your average grade is a ' +str(average) + ' percent.')
    gradeLetter = letterGrade(average)
    print(gradeLetter)


def gradeName(yearGrade):
    if yearGrade == str(9):
        return 'You are a freshman.'
    elif yearGrade == str(10):
        return 'You are a sophmore.'
    elif yearGrade == str(11):
        return 'You are a junior.'
    elif yearGrade == str(12):
        return 'You are a senior'
    else:
        return 'You must not be in highschool.'

def avgGrade(list):
    sum = 0.0
    for grades in list:
        sum = sum +grades
    print(sum)
    average = sum/len(list)
    return average



def letterGrade(x):
    if float(x) >= 93:
        return'You have an A'
    elif float(x) >= 82:
        return 'You have a B'
    elif float(x) >= 72:
        return 'You have a C'
    elif float(x) >= 62:
        return 'You have a D'
    else:
        return 'You are failing'


main()

