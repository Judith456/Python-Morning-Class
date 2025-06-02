"""
def add(datatype, *args): 
  
    # if datatype is int initialize answer as 0 
    if datatype =='int': 
        answer = 0
          
    # if datatype is str initialize answer as '' 
    if datatype =='str': 
        answer ='' 
  
    for x in args: 
  
        answer = answer + x 
  
    print(answer) 
  
# Integer 
add('int', 5, 6) 
  
# String 
add('str', 'Hi ', 'Geeks')

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3)) 
print(calc.add(2, 3, 4))  
"""

class Shipping:
    @singledispatchmethod
    def calculate(self, arg):
        print("Unsupported type")

    @calculate.register
    def _(self, weight: int):
        print(f"Standard shipping for {weight}kg: ${weight * 5}")

    @calculate.register
    def _(self, weight: float):
        print(f"Heavy item shipping for {weight}kg: ${weight * 6}")

# Usage
s = Shipping()
s.calculate(10)      # int → standard
s.calculate(10.5) 