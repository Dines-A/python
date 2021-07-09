N=int(input())
if N > 0 :
    print("Positive") 
elif N < 0:
    print("Negative") 
else:
    print("Neither Positive nor Negative")

    
m=int(input("Enter your mark :"))
if (m<=100 and m>=90):
          print("Your grade is : S")
elif (m>=80 and m<90):
          print("Your grade is :A")
elif(m<=70 and m>80):
          print("Your grade is :B")
elif (m>=60 and m<70):
          print("Your grade is :A")
elif(m<=50 and m>60):
          print("Your grade is :B")
elif(m==50 and m>=0):
          print("Your grade is :U")
else:
          print("You entered value is grader than 100 or less than 0")
