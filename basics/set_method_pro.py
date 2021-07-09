#set union is used for add a set 
a={1,2,3,4,5}
b={6,7,8,9,0}
c=a.union(b)
#print(c)

#set intersection
a={1,2,3,4,5}
b={1,2,3,4,5,6,7}
c=a.intersection(b)
#print(c)

#subset
a={1,2,3,4}
b={1,2,3,4,5,6,7,8,9}
print(a.issubset(b))
print(b.issubset(a))


#superset
a={1,2,3,4}
b={1,2,3,4,5,6,7,8,9}
print(a.issuperset(b))
print(b.issuperset(a))
