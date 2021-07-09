#25.03.2021
def  desplay(day,month,year):
      print("Day : ",day)
      print("Month :",month)
      print("Year :",year)
day=int(input("Enter the day : "))
month=int(input("Enter the month : "))
year=int(input("Enter the year : "))
desplay(day,month,year)
#over write the default value
def  desplay(day,month,year=2021):
      print("Day : ",day)
      print("Month :",month)
      print("Year :",year)
day=25
month=3
year=2002
desplay(day,month,year)
#output is 25.03.2002
#but the actual output is 25.03.2021 source from mother tongue.
#keyword arguments
def  desplay(day,month,year):
      print("Day : ",day)
      print("Month :",month)
      print("Year :",year)
#one type
#desplay(25,3,2021)
#other type
#desplay(day=25,month=3,year=2021)
#desplay(month=3,year=2021,day=25)
#Arbitrary arguments
def  desplay(*data):
      print(data)
desplay(25,3,2021,'alan')

def  desplay(*data):
      for i in data:
            print(data)
desplay(25,3,2021,'alan')

#Applicaion
#sum of n numbers
def  desplay(*data):
      ans=0
      for i in data:
            ans+=i
            print(ans)
desplay(25,3,2021)



























