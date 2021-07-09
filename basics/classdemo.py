#basic of class:
"""class demo:
          print("dinesh")
          # normal a print function kul kodukupata value nai objcet create panamala
          #call pana mudiumm.
          print("10")
          #but,here just we assign the value to "B" so if you want to call the b value without
          #the creating object we cant call "B" 
          b=12
obj=demo()
print(obj.b)"""
#self keyword use
#if u pass the argument without self
#TypeError: fun() takes 2 positional arguments but 3 were given
class self:
          a=10
          #we can use what ever instead of self:
          def fun(self,b,c):
                    z=b+c
                    print(z)
                   """  "a" is not present in fun function if we just call "x=a+b" it will throw error so
we use x=self.a+b"""
                    x=self.a+b
                    return x
          """the return statment will return the value of "x" to "q" """
obj=self()
q=obj.fun(20,30)
print(q)
"""print(f"name : {self.name}\nAge : {self.age}\nDOB : {self.DOB}")"""






























