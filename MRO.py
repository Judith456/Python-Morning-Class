# Python program showing
# how MRO works
"""
class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

r = B()
r.rk()


class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

class C(A):
    def rk(self):
        print("In class C")

# classes ordering
class D(B, C):
    pass

r = D()
r.rk()
"""

class A:
    def rk(self):
        print("In class A")

class B:
    def rk(self):
        print("In class B")

# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")

r = C()

# it prints the lookup order 
print(C.__mro__)
print(C.mro())