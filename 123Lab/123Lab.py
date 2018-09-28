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
        return "a senior"
    elif gradeIn == 11:
        return "a junior"
    elif gradeIn == 10:
        return "a sophmore"
    elif gradeIn == 9:
        return "a freshmen"
    else:
        return " you're not in highschool yet"


def getAverage(numList1):
    average = sum(numList1) / float(len(numList1))
    return(average)
    ## calculate average grade and return value to main







def getLetterGrade(getAverage):
    if getAverage >= 90:
        lettergrade = ("A")
    elif getAverage >= 80:
        lettergrade = ("B")
    elif getAverage >= 70:
        lettergrade = ("C")
    elif getAverage >= 60:
        letterGrade = ("D")
    else:
        lettergrade = ("F")
    return(letterGrade)

main()
