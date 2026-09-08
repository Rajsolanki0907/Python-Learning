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

if(count := len(numbers)) > 3:
    print(f"List has {count} elements")


