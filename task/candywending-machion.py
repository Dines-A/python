av=80
i=1
n=int(input("Enter your candy count : "))
x="Oops :) we have only {}"
y="but,you have enterd {} candies"
"""else:
        print(x.format(av))
break"""
while i<=n:
    if i>av:
        print(x.format(av),"\n",y.format(n))
        break
    print(i ,"candy")
    i+=1
print("welcome again:)")
