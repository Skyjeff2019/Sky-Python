def main () :
    print("Bellarmine Student grade point average")
    yearinschool()
    print ()
    grades()



def yearinschool () :
    numGrade = int(input ("What grade are you in? - "))
    if numGrade == 9:
        print ("You are a freshman")
    elif numGrade == 10:
        print ("You are a sophmore")
    elif numGrade == 11:
        print ("You are a junior")
    elif numGrade == 12:
        print ("Your a senior")
    else:
        print ("You skipped highschool!")


def grades () :
    num1 = float(input ("Put in your first grade number - "))
    num2 = float(input ("Put in your second grade number - "))
    num3 = float(input ("Put in your third grade number - "))
    num4 = float(input ("Put in your fourth grade number - "))

    List1 = [0] * 4
    List1 [0] = num1
    List1 [1] = num2
    List1 [2] = num3
    List1 [3] = num4

    ListL = len (List1)
    ListA = List1.pop (0) + List1.pop (0) + List1.pop (0) + List1.pop (0)

    Gpa = ListA / ListL
    print ()
    print ("Your percentage avergae is - " + str(Gpa) )

    if int(Gpa) > 90:
        print ("Your letter grade is - A")
        Letter = str("A")

    elif int(Gpa) > 80:
        print ("Your letter grade is - B")
        Letter = str("B")

    elif int(Gpa) > 70:
        print ("Your letter grade is - C")
        Letter = str("C")

    elif int(Gpa) > 60:
        print ("Your letter grade is - D")
        Letter = str("D")

    else:
        print ("Your letter grade is - F")
        Letter = str("F")

    if (Letter == "A") or (Letter == "B") or (Letter == "C"):
        print ("You are passing.")

    else:
        print ("You are failing.")



main()
