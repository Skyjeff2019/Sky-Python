class Petclass():
    petType= "cage free pet"

    def __init__(self, pType, pName, pBreed):
        """Initial attributes to describe a pet"""
        self.type = pType
        self.name = pName
        self.breed = pBreed

    def getName(self):
        return(str(self.name))

    def getBreed(self):
        return(str(self.breed))

    def whatItIs(self):
        print(self.type, self.name, self.breed)


class Cageclass():
    petType= " caged pet"
    def __init__(self, pType, pDanger):
        self.type = pType
        self.danger = pDanger

    def whatDanger(self):
      if self.danger == "T":
            return("You have a dangerous " + self.type + ".")
      if self.danger == "F":
            return ("You have a safe " + self.type + ".")


#----------------------------------------------------------------------------------------------------------------------



myPet1 = Petclass("Dog","Skipper","Golden Retriever")
print("The pet's name is " + myPet1.name + " and it is a  " + myPet1.type)


myPet2 = Petclass("Cat", "Wiskers", "Siberian" )
print("This pet's name is " + myPet2.name + " and it is a " + myPet2.type)

myCage1 = Cageclass("Snake", "T" )
print("This is a " + myCage1.type)
print("This is a" + myCage1.petType)
print(myCage1.whatDanger())

myCage2 = Cageclass("Rat", "F" )
print( "This is a " + myCage2.type)
print("This is a" + myCage2. petType)
print(myCage2. whatDanger())









#print(whatItIs(myPet1))


