
myDict = {
    "fast": "In a Quick Manner",
    "Ankit": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Ankit': 'Player'},
    1: 2
}

# Dictionary Methods

print(list(myDict.keys())) # Prints the keys of the dictionary in a list.

print(myDict.values()) # Prints the keys of the dictionary 

print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 

print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Ankit": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

# The difference between .get and [] sytax in Dictionaries?

print(myDict.get("Ankit")) # Prints value associated with key "Ankit"
print(myDict["Ankit"]) # Prints value associated with key "Ankit"

print(myDict.get("Ankit2")) # Returns None as Ankit2 is not present in the dictionary
print(myDict["Ankit2"]) # throws an error as Ankit2 is not present in the dictionary


