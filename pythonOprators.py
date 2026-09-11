#Operators are used to perform operations on variables and values.
# Arithmetic operators
# + operator used to add two values and two variables
print(10+3)
print(10-3)
print(10*3)
print(10/2)
print(10%3)
print(10**3)
print(10//2)


#Assignment Operators
x = 5
print(x)
x += 5
print(x)
x -= 5
print(x)
x *= 5
print(x)
x /= 5
print(x)
x = 5 
x%=3
print(x)
x = 5
x **= 3
print(x)


#Walrus Operator - ( := )
#It assigns values to variables as part of a larger expression.
numbers =[1,2,3,4,5]
print(type(numbers))

if(count := len(numbers)) > 3:
    print(f"List has {count} elements")


#Ternary Operators
num = 6
x ="WEEKEND" if num > 5 else "Workday"
print(x)

num = 5
x = "Sunday" if num > 4 else "monday"
print(x)

num = 2

x = "Sun" if num == 1 else "Tue" if num==2 else "Wed"
print(x)

#Comparison Operator
x = 10
y = 12
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
 
 #chaining comparison operators
x = 5
print(1 < x < 10)


# Logical Operators
print("Logical operators")
print(x < 5 and x > 1)
print(x < 5 or x > 1)
print(not(x < 5 and x > 1))


#Identity Operators
 # is  and is not
x = ["apple" , "banana"]
y = ["apple", "banana"]
z = x
print("Identity operators")
print(x is y)
print(x == y)
print(x is z)
print(y is z)

p = 5
q = 5
print(p == q)
print(p is q)

#Python Membership Operators - are used to test if a sequence is presented  in an object
# in , not in
print(" membership operators")
fruits = ["apple","banana","mango","grapes"]
print("banana" in fruits)
print("cherry" in fruits)
print("cherry" not in fruits)

#Bitwise Operators
print("Bitwise Operators")
x = 4
y = 6
print(x & y) # and
print(x | y) # or
print(x ^ y) # xor
print(~x) #not
print(x << 2) #left shift
print(y >> 2) #right shift

#Operator Precedence
print("Operatoe Precedence")
print((6+4) - (6 + 3))
print(100+5*3)
