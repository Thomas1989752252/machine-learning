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
# SyntaxError

# initialize the amount variable
amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if (amount > 2999)
print("You are eligible to purchase Dsa Self Paced")

#%%---------------------------

# TypeError

s = "alma" #str
f = 3.14 #float
i = 10 #int
b = True #bool

print(type(s), type(f), type(i), type(b))

x = s + s
y = i + i

'''
int operator+(int a, int b)
{
  return a*b;
}

int operator+(str a, str b)
{
  return a*b;
}

# operátor v függvénytúlterhelés (overloading)

'''




#%%---------------------------

# NameError
print(yyy)

#%%---------------------------

# IndexError

l = [1, 2, 3]
x = l[5]

#%%---------------------------

# KeyError

d = {}
d["A"] = 123
d["E"] = 124
d["F"] = 125
#print(d["B"])

for key, value in d.items():
    print(key, value)
    

#%%---------------------------

# maximum selection

a, b = 1, 2

l = [12, -3, 8, 8, 99, 1, 2, 3]

max_value = l[0]

for i in l:
    if i > max_value:
        max_value = i
        
        
        
print(max_value)
    


#%%---------------------------

# maximum selection

a, b = 1, 2

myList = [12, -3, 8, 8, 99, 1, 2, 3]

s = 0

for i in myList:
    s += i
            
print(s)


print(type(myList))
n = sum(myList)
print(n)
 


s = "ssdfsdf"
print(type(A))

#%%---------------------------

# FUNCTIONAL PROGRAMMING

myList = [1, 2, 3, 8, 9]

myList2 = []

for i in myList:
    myList2.append(i+1)
    
print(myList2)

fun1 = (lambda x : x+1) #lambda function 

def fun2(x):
    return x+1

def fun3(x):
    return x+2

def fun4(x):
    return fun2(fun3(x))

myList3 = list ( map(fun3, list( map( fun2, myList) ) ) )


print(myList3)

x = [i for i in range(100) if i%5==0] #list generator / list comprehension
print(x)

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------

#%%---------------------------















