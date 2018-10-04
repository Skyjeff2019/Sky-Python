def main():

    mystring = input('Input your string here - ')

    print(deVowel(mystring))

def deVowel(mystring):

    noVowel = ''

    for x in mystring:

        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':

            y = 'p'

        else:
            noVowel = noVowel + x

    return (noVowel)

main()
