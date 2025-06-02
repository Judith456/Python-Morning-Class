class Bird:
    def fly(self):
        print("Birds fly in the sky")
        
class Eagle(Bird):
    def fly(self):
        print("Eagles flies at higher altitude")
        
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies at lower altitdes")
        
#how polymrphism is used?
def flight_test(bird):
    bird.fly()
    
#create object
eagle1 = Eagle()
sparrow1 = Sparrow()

#call the flight test method with different objects
flight_test(eagle1)
flight_test(sparrow1)
