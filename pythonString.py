str1 = "raj"
str2 = "solanki"


# Concatenation of two strings
print(str1 +" "+ str2)

#length of String
print(len(str1))
print(len(str2))

print(str1.upper()) #convert string into uppercase
print(str2.lower()) #convert string into lowercase


# Slicing concept in python
slice1 = str1[0:3]    # 0 indx to 3 without including the 3 index
slice2 = str2[2:5]
slice3 = str1[-4:-3]
print(slice1)
print(slice2)

sliceEx = str1[:2]
sliceExa = str2[3:]
print(sliceExa)
print(sliceEx) 

# slicing with step
sliceStep = str1[0:3:2]
print(sliceStep)

#endswith  startswith
name  = "raj solanki"
print(name.endswith("ki"))
print(name.endswith("ar"))
print(name.startswith("raj"))
print(name.startswith("Raj"))

print(name.capitalize()) #string with capital letter 
print(name.count("a")) # count the occurance of character
print(name.lower()) #convert the string in lowercase
print(name.upper()) #convert the string in uppercase
print(name.find("a")) #it returns the first occcurance of character from string
print(name.replace("raj","RAJ")) #replace the word entire string

#escaps character
str = "Raj solanki is software developer and \n currently \t learning \"python\"" #\t for tab space
print(str)

# loop on string
for x in "Banana":
 print(x)

# check string - in
txt = "the best things in life are free!"
print("free" in  txt)

# only if 
if "free" in txt:
    print("find")

# not in - check string
txt = "the best things in life are free!"
print("expensive" not in  txt)

# only if 
if "expensive" not in txt:
    print(" not find")

# Remove WhiteSpaces
str = "      hello world  "
print(str)
print(str.strip())

#Replace of String
Org = "python Developer"
print(Org.replace("py","Hy"))
print(Org.replace("python" , "mython"))

#split in python
splitStr = "Hello World of python"
print(splitStr.split(" "))

# Python formate String  - formate() methd
''' F-String - F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.'''
age = 24
num = 2
txt = f"my name is raj . I am {age} , I have {num} siblings"
print(txt) 

#Placeholders and Modifiers 
#A placeholder can contain variables, operations, functions, and modifiers to format the value.
price = 56
txt = f"The price is {price:.2f} rupees"
print(txt)
#placeholder can contain python code
txt1 = f"The price is {20*40} rupees"
print(txt1)

#casefold() - convert string into lower case
s = "HeLlo"
print(s.casefold())

