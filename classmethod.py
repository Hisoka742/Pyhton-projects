from datetime import date
class Student :
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def descripe(self):
        print("my name is {} and my age is {}".format(self.name, self.age))

    @classmethod
    def initFromBirthYear(cls, name, birthyear):
        return cls(name, date.today().year - birthyear )

student1 = Student("salman", 20)
student2 = Student.initFromBirthYear("hisoka", 2000)

class Pizza:
    def __init__(self, prix):
        self.prix = prix
    
    @classmethod
    def veg(cls):
        return cls(["big: 400", "small: 200"]) #prix in roble
    
    @classmethod
    def modzarilla(cls):
        return cls(["big: 300", "small: 150"])

    def __str__(self) :
        return"the prix of this pizza is : {}".format(self.prix)

Pizza1 = Pizza("bigbig: 900")
Pizza2 = Pizza.veg()
Pizza3 = Pizza.modzarilla()
print(Pizza1 )
print (Pizza2 )
print(Pizza3 )




