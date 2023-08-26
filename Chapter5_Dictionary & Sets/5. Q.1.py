# Write a programme in which it will give you options from a 
# dictionay so you can print the meaning of it.

myDict = {
    "Pnakha": "Fan",
    "Dabba": "Box",
    "Saman": "Item"
}

print("Options are ", myDict.keys())

a = input("Enter the Hindi word \n")

print("The meanung of the word is: ", myDict.get(a))

