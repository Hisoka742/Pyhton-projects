class Math:
    @staticmethod
    def PI():
        return 3.14
    
class Pizza:
    def __init__(self, radius, prix ):
        self.prix = prix
        self.radius = radius
    
    def __str__(self) :
        return f"the prix of this pizza is : {self.prix}"

    def area(self):
        return Pizza.circle_area(self.radius) #circle_area : staticemethod
    
    
    @staticmethod
    def circle_area(r):
        return r ** 2 * Math.PI() #calculate the size of the circle (Pizza-_-)
    
    
P = Pizza(20, "mozarilla : 500")
print(P.area())
print(Pizza.circle_area(15))
print(Pizza.circle_area(10))

    

