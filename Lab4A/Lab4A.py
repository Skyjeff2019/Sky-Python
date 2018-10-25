def main ():
    deVowel()
    g = [0] * 4
    g [0] = float(input("Enter a number - "))
    g [1] = float(input("Enter a number - "))
    g [2] = float(input("Enter a number - "))
    g [3] = float(input("Enter a number - "))
    m = float(input("What do you want to multiply by? - "))

    print ( "using a for loop equals " + mathStuff(g , m))
    print ()

def deVowel():
    mystring= (input("type a string"))
    mystring2 = mystring
    mystringA=""
    for x in mystring2:
        if (x=="a" or x=="e" or x=="i" or x== "o" or x== "u"):
            y=69
        else :
            mystringA= mystringA + x
    print(mystringA)
    return (mystringA)



def mathStuff (g , m) :
    Listf = [] * 4
    for x in g :
        Listf.append(float(x) * float(m))
    return (str(Listf))


main()
