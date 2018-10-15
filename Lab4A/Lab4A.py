def main():
    mystring = input('Input your string here - ')
    print(deVowel(mystring))
    print(mathstuff(myList))

def deVowel(mystring):
    noVowel = ''

    for x in mystring:

        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':

            y = 'p'

        else:
            noVowel = noVowel + x

    return (noVowel)




def mathstuff(myList):
    for num in myList:
        print('the number is ' + str(num*2))

myList= [1, 2, 3, 4, 5]

main()
