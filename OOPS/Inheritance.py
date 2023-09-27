'''
Inheritance :- When one class inherutes from another class is called Inheritance.

Parent class :- Base class :- Super class
Child class :- Derived class :- sub class

--> Parent class properties will inherit to child class.

Types of Inheritance:-

1. Single-level Inheritance:

    class A
       |
       |
    class B

2. Multi-level Inheritance:

    class A
       |
       |
    class B
       |
       |
    class C

3. Multiple Inheritance:

    class A    Class B
            |
        Class C


'''

# Single - Level Inheritance
class Parent:
    def house(self):
        print("3 BHK House")

class Child(Parent):
    def car(self):
        print("Mercedez car")

c = Child()
c.car() 
c.house()

# Multi-level Inheritance
'''class Grandfather:
    def land(self):
        print("100 Acres of Land")

class Father(Grandfather):
    def house(self):
        print("5 BHk house")

class Son (Father):
    def car(self):
        print("Audi car")

c = Son()
c.land()
c.house()
c.car()'''

# Multiple Inheritance
class Father:
    def house(self):
        print("5 BHk house")

class Uncle:
    def land(self):
        print("5 Acres of Land")
class Son (Father,Uncle):
    def car(self):
        print("Audi car")

c = Son()
c.land()
c.house()
c.car()