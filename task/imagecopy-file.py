f=open("155595860_12bb9b28d322b070ecb89c3dea10d22e.jpg",'rb')
fc=open("gukan.jpg","wb")
for i in f:
    fc.write(i)
# it is working succes fully