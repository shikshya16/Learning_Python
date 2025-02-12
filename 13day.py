# Multiple Inheritance

class A:
    def method_a(self):
        print("Method A")
class B:
    def method_a(self):
        print("Method B")
class C(A,B):
    def method_c(self):
        print("Method C")
c = C()
c.method_a()

#Multilevel Inheritance
class A:
    def method_a(self):
        print("Method A")
class B(A):
    def method_b(self):
        print("Method B")
class C(B):
    def method_c(self):
        print("Method C")
c = C()
c.method_a()
c.method_b()
c.method_c()



#Abstraction
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, year):
        super().__init__()
        self.brand = brand
        self.year = year
    
    @abstractmethod
    def print_details(self):
        pass

class SUV(Car):
    def print_details(self):
        print(f"Brand: {self.brand} and Year: {self.year}")
    def brake(self):
        print("Brake...")

suv = SUV('SUV', 2025)
suv.print_details()
suv.brake()



#Operator Overloading

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"

v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1 + v2

print(v3.x, v3.y)
print(v1)

