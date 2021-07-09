Name="Dinesh"
Age=20
Salary=90000
#type 1
print("type1")
print("Name : ",Name,"Age :", Age,"Salary : ", Salary)
print("Name : ",Name,"\nAge :", Age,"\nSalary : ", Salary)

#type 2
print("type2")
print("Name : "+Name,"Age :"+ str(Age),"Salary : "+str(Salary))
print("Name : "+Name,"\nAge :"+ str(Age),"\nSalary : "+str(Salary))
#type 3
#1using format()
print("type3")
print("Name : {} Age : {} Salary : {}".format(Name,Age,Salary))
print("Name : {} \nAge : {}\n Salary : {}".format(Name,Age,Salary))
#2using format()
print("type4")
print("Name : {0}Age : {1} Salary : {2}".format(Name,Age,Salary))
print("Name : {0}\nAge : {1}\nSalary : {2}".format(Name,Age,Salary))
#2using format()
print("type5")
print("Name : {n} Age : {a} Salary : {s}".format(n=Name,a=Age,s=Salary))
print("Name : {n} \nAge : {a} \nSalary : {s}".format(n=Name,a=Age,s=Salary))
#type 4
print("type6")
print(f"Name : {Name}Age :{Age}Salary : {Salary}")
print(f"Name : {Name}\nAge :{Age}\nSalary : {Salary}")



