# List - list are used to store multiple items in a single variable
myList = ["apple","banana","mango","cherry"]
print(myList)
#list items are ordered , changeable , and allow duplicate
print(len(myList))

list1 = ["abc",1,True,40,"maje"] # we can create a list of different datatypes
print(list1)
print(type(list1))

#create a list by using list() constructor
thislist = list(("apple","banana","mango"))
#access list items
print(thislist[1])
print(thislist[2])
print(thislist[-1])
print(thislist[1:2])
print(thislist)
print("apple" in thislist)

if "apple" in thislist:
    print("yess")

# add item in list
thislist[1] = "cherry"
thislist[0:2] = ["grapes" , "lichhi"]
print(thislist)
thislist.insert(2,"watermelon") # on specific index
print(thislist)
thislist.append("orange") # at the last of the list
print(thislist)
thatlist = ["Apple","banana"]

# append element from another list to the current list
thislist.extend(thatlist) 
print(thislist)
# extend does not have to append lists, you can add any iterable obj (tuple, set , dictionaries etc..)
thistuple = ("Kiwi","papaya")
thislist.extend(thistuple)
print(thislist)

# remove item from the list
thislist.remove("banana") # remove specific item if one item have more than one value then remove() , removes the first occurance.
print(thislist)
thislist.pop(2) # remove specified index
print(thislist)
thislist.pop() # not specifies index than it remove the last index
print(thislist)
del thislist[0] # delete specified index
print(thislist)
# del thatlist  # delete the list completely
# print(thatlist)
# thislist.clear()  # empties the list []
# print(thislist)

# Loop Lists
for x in thislist:
    print(x)

print("loop using index by range and len function")
for i in range(len(thislist)):
    print(thislist[i])

#while loop on list
print("loop using while loop")
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# looping using list comprehension
print("looping using list comprehension")
[print(x) for x in thislist]

#Sort List
thislist.sort() # ascending order
print(thislist)
thislist.sort(reverse = True) # descending order
print(thislist)
numList = [100,20,50,62,287]
numList.sort()
print(numList)
numList.sort(reverse =  True)
print(numList)

# key = function - 
def myfun(n):
    return abs(n - 50)

numList.sort(key = myfun)
print(numList)

print(thislist)
thislist.sort(key  =  str.lower) # ignore case insentivity
print(thislist)
thislist.reverse()
print(thislist)

# copy list 
mylist =  thislist.copy()
print(mylist)
mylist2 = list(thislist) # copy by using list()
print(mylist2)
mylist3 = thislist[:] #copy by using the slice operator
print(mylist3)

#concatenation of list
newList = thislist + list1
print(newList)
 
for x in thislist:
    list1.append(x)

print(list1)
  