class demo:
          #we can just print the function without creating the objcet for the
          #class
          print(" im demo function")
          f=15
          #we use whatever instead of self keyword
          def fun(self,x,y):
                    c=x+y
                    print(c)
                   #if you want to use a variable from outside of the function
                   #you shot use like (self.f)
                    zz=self.f+x
                    #print(zz)
                    return zz
          #if you ferget to return the value the output will be "none"
obj=demo()
#obj.fun(10,20)
zz=obj.fun(10,20)
print(zz)
