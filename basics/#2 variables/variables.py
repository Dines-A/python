#basic of variable
x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#casting the variable 
#we can convert the int variable to float variable 
# int ->float/str
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#geting type of the variable 
x = 5
y = "John"
print(type(x))
print(type(y))

# single Quotes vs double quots both are same 
x = "John"
y = 'John'
print(x,"==",y)

"""
Case-Sensitive
Variable names are case-sensitive.

Example
This will create two variables:
"""
a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)