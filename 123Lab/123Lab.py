def main():
    print ("Bellarmine student current grade point average")
    numList1= [ 93.4, 86.8, 98.2, 89.9, 94.6]
    gradeIn= input("What year are you in school?- ")
    grade1= int(gradeIn)
    print("you are" + str(gradeIn))
    print (" your current average score is-" + str(getAverage(numList1)))
    print ("your current letter grade is-" + str(getLetterGrade(getAverage(numList1))))

def getYearInSchool(gradeIn):
    if gradeIn == 12:
        return (str("a senior"))
    elif gradeIn == 11:
        return (str("a junior"))
    elif gradeIn == 10:
        return (str("a sophmore"))
    elif gradeIn == 9:
        return (str("a freshmen"))
    else:
        return (str(" you're not in highschool yet"))


def getAverage():




def getLetterGrade(getAverage):
    if getAverage >= 90:
        lettergrade = (str("A"))
    elif getAverage >= 80:
        lettergrade = (str("B"))
    elif getAverage >= 70:
        lettergrade = (str("C"))
    elif getAverage >= 60:
        letterGrade = (str("D"))
    else:
        lettergrade = (str("F"))
    return(letterGrade)

main()
