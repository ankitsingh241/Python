# Create an empty set.

a = set()
print(type(a))

# Adding values to an empty set.
a.add(2)
a.add(5)
a.add(5)
a.add(5) # It will add 5 only one time.

# Anything that is unhashable (which changes) can not be added in set.

# a.add([6,7,8]) # We can not add list to a set.

a.add((6,7,8)) # We can add tuple to a set.

# a.add({4:5}) # We can not add dictionay to a set.

print(a)

# Print the length of set.
print(len(a))

# Removal of an Item
a.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(a)

