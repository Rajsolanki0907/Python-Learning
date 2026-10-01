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
