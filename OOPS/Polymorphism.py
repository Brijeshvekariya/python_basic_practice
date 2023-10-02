'''
Polymorphism:- Polymorphism is derived from Greek word. Poly means many and morphism means forms. so polymorphism is many forms.

polymorphism is defined as a class which have different forms.

1. Method Overloading(Compile-time polymorphism) :- When we have same method name but different parameters

--> Python does not support method overloading

2. Method Overriding(Run-time polymorphism) : when parent class and child class have same method name is called method Overri

'''

class A:
    def display(self):
        print("A class")

class B(A):
    def display(self):
        print("B class")

obj = B()
obj.display()