"""Write a Python program which accepts a sequence of comma-separated numbers
          from user and generate a list and a tuple with those numbers. 

          Sample data : 3, 5, 7, 23
          Output :
          List : ['3', ' 5', ' 7', ' 23']
          Tuple : ('3', ' 5', ' 7', ' 23')      """

value=str(input("Enter the value :"))
print(f"The List is : {list(value)}\nThe tuple is : {tuple(value)}")

