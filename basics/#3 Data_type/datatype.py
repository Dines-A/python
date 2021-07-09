"""
x = "Hello World"	                                     ->                      str	
x = 20	                                                 ->                      int	
x = 20.5	                                             ->                      float	
x = 1j	                                                 ->                      complex	
x = ["apple", "banana", "cherry"]	                     ->                      list	
x = ("apple", "banana", "cherry")	                     ->                      tuple	
x = range(6)	                                         ->                      range	
x = {"name" : "John", "age" : 36}	                     ->                      dict	
x = {"apple", "banana", "cherry"}	                     ->                      set	
x = frozenset({"apple", "banana", "cherry"})	         ->                      frozenset	
x = True	                                             ->                      bool	
x = b"Hello"	                                         ->                      bytes	
x = bytearray(5)	                                     ->                      bytearray	
x = memoryview(bytes(5))	                             ->                      memoryview
"""
# check the above existed code data type when you are free
import random
print(random.randrange(1, 10))

x = 35e3
y = 12E4
z = -87.7e100
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))