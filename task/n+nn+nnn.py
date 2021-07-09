"""Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Go to the editor
Sample value of n is 5
Expected Result : 615"""

n=int(input("Enter the number :"))
n1=str(n)
n2=str(n)+str(n)
n3=str(n)+str(n)+str(n)
print(f"The output is :",int(n1)+int(n2)+int(n3))

