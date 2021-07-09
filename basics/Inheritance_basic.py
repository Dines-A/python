"""class std:
          def __init__(self,name,age,dob):
                    self.name=name
                    self.age=age
                    self.dob=dob
                    print(f"Name : {self.name}\nAge : {self.age}\nfine : {self.fine}")
class lib(std):
          fine=500
obj=lib("dinesh",21,25032002)"""

#private variable
#syntax:
#__a
class student:
          def __init__(self,name,age,dob):
                    self.name=name
                    self.age=age
                    self.dob=dob
                    self.__fees=27000
          def getfees(self):
                    return self.__fees
                    #print(self.__fees)
class library(student):
          def __init__(self,name,age,dob,fine):
                    student.__init__(self,name,age,dob)
                    self.fine=fine
                    #print(f"Name : {self.name}\nAge : {self.age}\nDOB : {self.dob}\nFine : {self.fine}")
obj=library("Dinesh",21,25032002,500)
#why i  cant print it out side
#this is not working
#print(f"Name : {self.name}\nAge : {self.age}\nDOB : {self.dob}\nFine : {self.fine}")
print(f"Name : {obj.name}\nAge : {obj.age}\nDOB : {obj.dob}\nFine : {obj.fine}\nFees : {obj.getfees()}")
#print(obj.getfees())
