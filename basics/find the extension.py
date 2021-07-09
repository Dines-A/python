"""Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java"""
file=input("Enter the file name :")
file_1=file.split(".")
print("the file extension is :",file_1[-1])
