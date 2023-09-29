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

4. Hierarchical Inheritance :- when one parent class and have multiple child class

        class A
            |
    class B   class C

5. Hybrid Inheritance :- it is combination of different inheritance

                 class A
                    |
            class B   Class C
                    |
                class D
'''

# Single - Level Inheritance
'''class Parent:
    def house(self):
        print("3 BHK House")

class Child(Parent):
    def car(self):
        print("Mercedez car")

c = Child()
c.car() 
c.house()'''

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
'''class Father:
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
c.car()'''

# Hierarchical Inheritance
class Parent:
    def parent(self):
        print("This is parent class")

class Child1(Parent):
    def child1(self):
        print("This is child1")

class Child2(Parent):
    def child2(self):
        print("This is child2")

#object creation
c1 = Child1()
c2 = Child2()

c1.parent()
c1.child1()
c2.parent()
c2.child2()


'''class Grandfather:
    def land(self):
        print("20 acres of land")

class Father(Grandfather):
    def shops(self):
        print("5 shops")

class Uncle(Grandfather):
    def car(self):
        print("BMW car")

class Son(Father,Uncle):
    def factory(self):
        print("Iron casting Factory")

s1 = Son()
s1.land()
s1.shops()
s1.car()
s1.factory()'''