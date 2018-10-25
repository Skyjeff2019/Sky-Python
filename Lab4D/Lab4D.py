def main():
    shoppingCart = [['tooth past', 'q-tips', 'milks'],['milk', 'candy', 'apples'],['paper', 'pencils', 'q-tips']]
    print (shoppingCart)
    input("big pause")
    print (allinOne(shoppingCart))
    print( 'q-tips appear', countQtips(shoppingCart), 'times')

def allinOne(bag):#put the seperate lists into one big list
    newList= []
    for list in bag:
        for item in list:
            if item not in newList:
                newList.append(item)
    return newList

def countQtips(bag):# count the q-tips and return it
    newList2=[]
    count=0
    for list in bag:
        for item in list:
            if item not in bag:
                newList2.append(item)
    for i in range(len(newList2)):
        if newList2[i]== 'q-tips':
             count += 1
    return count


main()
