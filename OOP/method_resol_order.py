class A:
    label = "A"

class B(A):
    label = "B"

class C(A):
    label = "C"

class D(B, C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)