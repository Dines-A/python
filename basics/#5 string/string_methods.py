#string length
str="im_name_is_dinesh"
print(len(str))

#replacing string
str="im_name_is_dinesh"
print(str.replace("is","was"))
#removing whitespace from string

name="im dinesh    "
print(name)
#no diffrence between this two
print(name.strip())

#upper case
str="im_name_is_dinesh"
print(str.upper())

#lower case
str="im_name_is_dinesh"
print(str.lower())

#split the string
str="im_name_is_dinesh"
print(str.split("_"))

"""Check String
Check if "free" is present in the following text:"""

txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
#Use it in an if statement:

#Example
#print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

