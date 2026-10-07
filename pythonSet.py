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

# To remove an item in a set, use the remove(), or the discard() method.
thissetnew.remove('cherry')
print(thissetnew)

# Note: If the item to remove does not exist, remove() will raise an error.
thissetnew.discard('cherry')
print(thissetnew)

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
# you can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

# The clear() method empties the set
set3.clear()
print(set3)

# The del keyword will delete the set completely
del thisset
# print(thisset)

# Join Sets
# The union() and update() methods joins all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)#set1|set2

print(set3)
set = set1.union(set2, set3)
myset = set1 | set2 | set3
# The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.


# Intersection
# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)#set1&set2
print(set3)

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)#set3 = set1 - set2
print(set3)

# The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1.difference_update(set2)

print(set1)

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set3 = set1.symmetric_difference(set2)#set3 = set1 ^ set2

print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1.symmetric_difference_update(set2)

print(set1)
