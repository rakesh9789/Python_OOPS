#Inheritance::
class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"name: {self.name}, age:{self.age}")
        
class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
        
    def display_info_student(self):
        self.display_info()
        print(f"grade {self.grade}")
        
c = student("raki",20,"A")
c.display_info_student()

       

class shape():
    def draw(self):
        print("draw method in shape")
        
class circle(shape):
    def draw(self):
        print("circle in draw")
        

c = circle()
s.draw()


class vehicle():
    def start(Self):
        print("vehicle method start")
        
class car(vehicle):
    def start(self):
        super().start()
        print("car method start")
        
car = car()
car.start()


#polymorphism & abstraction

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass  

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class MobilePayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Mobile Payment")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in cash")

payments = [CreditCardPayment(), MobilePayment(), CashPayment()]

user_input = int(input("enter the amount:"))

for payment in payments:
    payment.pay(user_input) 


#Encapsulation::

class Employee:
    def __init__(self, name, age):
        self.__name = name  
        self.__age = age    

   
    def get_name(self):
        return self.__name

    
    def set_name(self, name):
        self.__name = name

    
    def get_age(self):
        return self.__age

    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")


Employee = Employee("Raki", 24)

print(Employee.get_name()) 
print(Employee.get_age())   

Employee.set_name("hari")    
Employee.set_age(30)        

print(Employee.get_name())  
print(Employee.get_age())   

Employee.set_age(-5)        

        
