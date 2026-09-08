# There are three numeric types in Python:
# 1.int
# 2.float
# 3.complex
# Variables of numeric types are created when you assign a value to them:
# we can verify there type by using type() function

#INT
x = 12
x1 = 232352356315135
x2 = -24252352355
print(type(x))
print(type(x1))
print(type(x2))


# FLOAT
y = 1.10
y1 = 1.0
y2 = -35.59

print(type(y))
print(type(y1))
print(type(y2))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
z = 35e3
z1 = 12E4
z2 = -87.7e100
print(type(z))
print(type(z1))
print(type(z2))


#COMPLEX - Complex numbers are written with a "j" as the imaginary part:
c = 3+5j
c1 = 5j
c2 = -5j

print(type(c))
print(type(c1))
print(type(c2))

# if we want we can crate a type of varible what we want 
x = int(3)
print(type(x))
y = float(3.4)
print(type(y))
z  = complex(3+4j)
print(type(z))


# Type Conversion - you can convert one type to another with the mtds
x = 1
y = 2.3
z = 1j # we cannot convert complex number into another number type


a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1,10))