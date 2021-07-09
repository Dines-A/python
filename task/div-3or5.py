nu=int(input("enter the ending point of the number : "))
for i in range(1,nu+1):
    if i%3==1 or i%5==1:
        continue
    print(i)