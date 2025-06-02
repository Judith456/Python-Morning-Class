"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass   # this method has no implementation
    
#child class implementing abstract method

class Car(Vehicle):
    def start(self):
        print("The car engine starts")
        
#another derived class
class Bike(Vehicle):
    def start(self):
        print("the bike is starting")
        
#NOTE
#we cannot create objects of an abstract class
#vehicle1 = Vehicle()   This would create an error

car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()
"""
