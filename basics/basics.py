Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(hi)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(hi)
NameError: name 'hi' is not defined
>>> a=1
>>> b=2
>>> c=a+b
>>> print(c)
3
>>> d=3
>>> f=d+c
>>> print(f)
6
>>> print(_+d)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(_+d)
NameError: name '_' is not defined
>>> name ="YOUTUBE"
>>> name[1]
'O'
>>> name[6]
'E'
>>> name[7]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name[7]
IndexError: string index out of range
>>> name[-1]
'E'
>>> name[-7]
'Y'
>>> name[1:6]
'OUTUB'
>>> name[1:]
'OUTUBE'
>>> name[:4]
'YOUT'
>>> a={}
>>> type(a)
<class 'dict'>
>>> b=[]
>>> type(b)
<class 'list'>
>>> c=()
>>> type(c)
<class 'tuple'>
>>> a=1
>>> type(a)
<class 'int'>
>>> float(a)
1.0
>>> type(a)
<class 'int'>
>>> a=1
>>> b=1
>>> a==b
True
>>> a|=b
>>> 
>>> a!=b
False
>>> x=int("enter the number")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x=int("enter the number")
ValueError: invalid literal for int() with base 10: 'enter the number'
>>> x=int(input("entere the number")
      y=int(input("enter the second number"))
      
SyntaxError: invalid syntax
>>> x=int(input("entere the number")
      5
      
SyntaxError: invalid syntax
>>> a=eval(input("enter the value")
       1-4+6-3+44
       
SyntaxError: invalid syntax
>>> a=eval(input("enter the value")
       print(a)
       
SyntaxError: invalid syntax
>>> 