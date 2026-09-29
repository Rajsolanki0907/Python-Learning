#Tuples are used to store multiple items in a single variable.
myTuple = ("apple","banana","cherry")

# A tuple is a collection which is ordered and unchangeable and allow duplicate values.
# Tuples are written with round brackets.
print(myTuple)
# tuple can also created without parantheses.
thisTuple = "apple","banana","cherry"
print(thisTuple)
print(len(thisTuple)) #lenght of tuple 

#to create a tuple with one item , you have to add a comma after the item otherwise python will not recognize it as a tuple
newTuple = ("apple",)
print(type(newTuple))
newTuple = ("apple")
print(type(newTuple))
emptyTuple = ()
print(emptyTuple)
tuple1 = ("apple","banana","cherry")
tuple2 = (1,2,4,5,3)
tuple3 = (True,False,True)

#tuple can contain any type of items 
tupleMix = ("app",404,True,500,"web")
print(type(tupleMix))
print(tupleMix)

thistuple = tuple(("apple","banana","cherry","orange","kiwi","melon","mango")) #note the double round brackets
print(thistuple)
print(thistuple[1]) #access indexed items
print(thistuple[-1])
print(thistuple[1:4]) # range access 

# if item exist in tuple
if "apple" in thistuple:
    print("yes")

# update tuple - but as specified tuple is unchangeble or immutable you cannot change , add , remove items 
# you can convert tuple into list and modify that list and again convert it into the tuple
thislist = list(thistuple)
thislist[1] = "gavava"
thistuple = tuple(thislist)
print(thistuple)

# we can add tuple with another tuple
y = ("grapes",)
thistuple += y
print(thistuple)

# delete -  del keyword used to delete the tuple completely
del tuple1
# print(tuple1) # error because it is not exist

# unpacking of tuple in python
fruits = ("apple","banana","cherry","mango")

(grren,yellow,red,orange) = fruits
print(grren)
print(yellow)
print(red)
print(orange)
# unpacking using Asterick

print("asterick at last")
(green,yellow,*red) =  fruits
print(green)
print(yellow)
print(red)

print("if asterick at mid items")
(green,*tropic,red) = fruits
print(green)
print(tropic)
print(red)

# loop through a tuple
print("loop using for")
for x in fruits:
    print(x)


print("loop using index")
#loop through range index
for i in range(len(fruits)):
    print(fruits[i])


print("loop using while")
#while loop 
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i +1
 
#Join two tuples
tuple1 = ("a" , "b" ,"c" , "d")
tuple4 = (1,2,1,3,4)

tupleMerge = tuple1 + tuple4
print(tupleMerge)

mytuple = fruits * 2
print(mytuple)

#count mtd
x = tuple4.count(1)
y = tuple4.index(1)
print(x)
print(y)

