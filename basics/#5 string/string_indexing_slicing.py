# string slicing
str="python"
print(str)
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
#we can access the string from the reverse
print(str[-1])
print(str[-2])
print(str[-3])
print(str[-4])
print(str[-5])
#we cant change the string value bcz string is immutable.
str="python"
#str[0]="hack"
# it will throw an error
print(str)
str="python"
print(str[0:6])
#if u want slice the string using minus the first value must be less than next index
print("hi",str[-5:-1])
print(str[:6])
print(len(str))

str1="imlearingpython"
print(str1[4:-1])
