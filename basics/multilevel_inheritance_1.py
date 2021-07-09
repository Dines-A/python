class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self,a,b):
        A.__init__(self,a)
        self.b = b


class C(B):
    def __init__(self,a,b,c):
        B.__init__(self,a,b)
        self.c = c
obj=C(10,20,30)
print(f"A : {obj.a}\nB : {obj.b}\nC : {obj.c}")