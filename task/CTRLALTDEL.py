import array as arr
T=int(input("time"))
N=int(input("numberof car"))
a=arr.array('I',[ ])
for i in range(N):
    v=int(input("velocity"))
    a.append(v)
print(a[T-1])

