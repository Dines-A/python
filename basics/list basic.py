#List is a collection which is ordered and changeable. Allows duplicate members.
list=[10,20,30,40,50]
print(list)
#you can create listusing all data type
list1=["dinesh",10,5.00,True]
print(list1)
#print the item which is existed in list using for loop:
for i in list1:
    print(i)
#check item exists
list2=[10,20,30,40,50,60,70,80,90]
# it throw's an error
# for 10 in list2:
x=10
for i in list2:
    if i==x:
        print("yes")
        break
    else:
        print('no')
# this is the alternative of above program
list2=[10,20,30,40,50,60,70,80,90]
if 10 in list2:
    print("yes")
else:
    print("no")

#task by mother tong
numbers = [10, 20, 30,40,50]
sum=0
for i in numbers:
    sum=sum+i
print(sum)

#list indexing 
l1=[10,20,30,40,50]
print(l1[0])
print(l1[1])
#reverse indexiing
l1=[10,20,30,40,50]
#print(l1[-1])
#loop the indexing
for i in range(len(l1)):
    print(l1[i])


























