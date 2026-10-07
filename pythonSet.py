#Sets are used to store multiple items in a single variable.
#unordered, unchangeable*,Not allow duplicate  and unindexed.
# Note: Set items are unchangeable, but you can remove items and add new items.
#
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#duplicate
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

print(len(thisset))#lenght of set


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

#A set can contain different data types:
setIn = {"apple", 22, True,365,"Gram"}

print(setIn)
print(type(setIn))
print(type(set1))
print(type(set2))
print(type(set3))

#It is also possible to use the set() constructor to make a set.
thissetnew = set(("apple", "banana", "cherry","mango","kiwi"))
print(thissetnew)

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in thissetnew:
    print(x)

print("cherry" in thissetnew)
print("cherry"not in thissetnew)
 
# Once a set is created, you cannot change its items, but you can add new items. 

# Add new item - To add one item to a set use the add() method.
thissetnew.add("orange")
print(thissetnew)

# Update()-- To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}
thissetnew.update(tropical)
print(thissetnew)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
mylist = ["grass", "chiku"]
thissetnew.update(mylist)
print(thissetnew)


