#use encabsulation(setter and getter) without darect axes
class Student :
    num_of_student = 0
    def __init__(self, name, age=0, courses ='none'):
        self.__name =  name
        self.__age = age
        self.__courses = courses
        Student.num_of_student += 1 
        
    def get_name(self):
            return self.__name

    def set_name(self, new_name):
            self.__name = new_name
    
    def descripe(self):
        print("my name is {} and my age is {}".format(self.__name, self.__age))

    def is_old(self, num):
        if self.__age <= num:
            print("the student is not old")
        else:
            print("the student is old")

student1 = Student("salman", 18)
student2 = Student("sofia", 33)

 

student1.set_name("mohamed")
student1.set_name(50)
print(student1.__name)
student1.descripe() #Оно будет скрыто от пользователей (это отображаться как ошибка)