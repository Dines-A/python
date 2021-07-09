#read the file 
f=open("D:\Report's\selfintroduction.txt","r")
print(f.read())
f.close()

# read()
f=open("if.py","r")
print(f.read(2))
f.close()


#read the file line using readline

f=open("D:\Report's\selfintroduction.txt","r")
print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline(),end="")
f.close()
#if you dont use end="" the output has two space line between text
#if you write one readline function it will exicute one line for file
#first two readline comments exicutiog nice 
#last readline exicute another whole file i dont know why
#the fifty is mention the letter in the file



#read the file line using readline
#this is similer to read()
#i cant understand this
f=open("if.py","r")
print(f.readline(50))
f.close()
