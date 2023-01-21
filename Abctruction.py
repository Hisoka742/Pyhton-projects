from abc import ABC , abstractmethod
from re import A

class shape(ABC):
    @abstractmethod
    def area(self):
        pass           #writ a method without writing what's heppned inside

    @abstractmethod
    def perimiter():
        pass

class sqaure(shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimiter(self):
        return self.__side * 4

class Rest(shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        return (self.__width + self.__length) *2
    
    def perimiter(self):
        return self.__length * self.__width

Sqaure = sqaure(10)
print(f"sqaure area is {Sqaure.area()} and sqaure perimiter is {Sqaure.perimiter()}")
rest = Rest(4, 5)
print(f"rest area is {rest.area()} and rest perimiter is {rest.perimiter()}")

    
        