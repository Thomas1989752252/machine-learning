# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#%%---------------------------

class Person:
    
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def SayName(self):
        print("Hi, my name is", self.name)
        
        
#p1 = Person(23, "Bela")
#p1.SayName()


class Employee(Person):
    
    def __init__(self, age, name, company):
        super().__init__( age, name )
        self.company = company
        pass
        
    def SayName(self):
        super().SayName()
        print("I work at", self.company)
        

class Boss(Employee):
    
    def __init__(self, age, name, company, title):
        super().__init__(age, name, company)
        self.title = title
        
    def SayName(self):
        super().SayName()
        print("I am a big boss of level", self.title)
        
p3 = Boss(40, "Clay", "Amazon", "Department Executive")
p3.SayName()
    

#%%---------------------------

class MyClass:
    name = "rrr"
    age = 0
    
    def changeName(self, newName):
        self.name = newName
        return self
        
    def changeAge(self, newAge):
        self.age = newAge
        return self
        
        
x = MyClass().changeName("New_Name").changeAge(99).changeName("ddd").changeAge(44)
print(x.name, x.age)


def adding(A : str):
    print(A)
    A = A.replace("PYTHON", "CPLUSPLUS")
    return A

def negativ(B : str):
    print(B)
    B = B.split()
    return B

x = negativ( adding( "   I love Python    ".upper().strip() ) )

print (x)
    


#%%---------------------------
class MyCompany:
        
    # methods
    def __init__(self, compname, revenue, employeesize):
        self.name = compname
        self.revenue = revenue
        self.no_of_employees = employeesize
        self.number1 = 1
        self.number2 = 2
        self.x = 9
        self.z = 8
        self.x = self.z = self.y = 10
        self.value1 = 8

    def productivity(self, x):
        if x > 20:
            return 99 + 9
        else:
            return "valami_strings"
    
    def adding(self):
        return self.productivity(7)
    

temp1 = MyCompany('XYZ Bank', 1000,100)
print(temp1.adding())

print(temp1)
#%%---------------------------
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:31:43 2023

@author: User
"""

class triangle:

	def __init__(self, lenght, width):
		self.lenght = lenght
		self.width = width

	def Perimeter(self, lenght, width):
        self.Perimeter = (self.lenght**2 + self.width**2)^(0.5)
        print(self.Perimeter)
        
    def area(self, lenght, width):  
        self.area = (self.lenght*self.width)/2
        print(self.area)
		
        
mytriangle = triangle(3, 5)
print(mytriangle.Perimeter)
print(mytriangle.area)



#%%---------------------------
#   https://www.my-courses.net/2020/02/exercises-with-solutions-on-oop-object-oriented-programming-in-python.html
#   Exercise 43. Bank Account class


class Person:
    def __init__(self, name , age):
		self.name = name
		self.age = age  

    class Person:
        def __init__(self, name , age):
            self.name = name
            self.age = age  

#subclassokat hogyan lehet létrehozni


#%%---------------------------

class Vehicle:
    minimumrate = 50
    def __init__(self,driver,wheels,seats,kms,bill):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats
        self.running = kms
        self.bill = bill
    
    def rateperkm(self):
        return self.bill/self.running

class Cab(Vehicle):
    minimumrate = 75    
    def __init__(self,driver,wheels,seats,kms,bill,cabtype):
        Vehicle.__init__(self,driver,wheels,seats,kms,bill)         #mit jelent ez a sor
        self.category = cabtype
        
        
        

#%%---------------------------

import os
os.chdir(C:\Users\Tamás\Downloads)
import Mymodule




#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------















