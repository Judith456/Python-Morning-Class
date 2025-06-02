"""
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

#x = Person("John", "Doe")
#x.printname()

#child class
class Student(Person):
 x = Student("Mike", "Ross")
 x.printname()
"""
 
 
class Animal:
   def speak(self):
     print("Animals can make sound")
     
class Cat(Animal):
  def sound(self):
    print("Cat meows")
    
cat1 = Cat()
cat1.speak()


    
class Dog(Animal):
  def sound(self):
    print("Dog barks")
    

dog1 = Dog()
dog1.speak()
    