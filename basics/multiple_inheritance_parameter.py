class A():
    def __init__(self,a):
        self.a=a
class B():
    def __init__(self,b):
        self.b=b
class C(A,B):
    def __init__(self,a,b,c):
        A.__init__(self,a)
        B.__init__(self,b)
        self.c=c
obj=C(10,20,30)
print(f"A : {obj.a}\nB : {obj.b}\nC : {obj.c}")