import array
arr=array.array('i',[ ])
size=int(input("Enter the array size :"))
for i in range(size):
    vals=int(input("Enter the values : "))
    arr.append(vals)
print(arr)

# find the index value of the value using mind
val1=int(input("Enter the value to find the index : "))
txt="{} is the index of {}"
k=0
for vv in arr:
    if vv==val1:
        print(txt.format(k,vv))
        break
    k+=1
else:
    print("re-enter the value : ")
# find the index value of the value using function
# if you give out of range value it throw error
print(arr.index(val1))