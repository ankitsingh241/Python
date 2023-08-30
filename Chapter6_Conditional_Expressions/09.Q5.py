# Write a program which finds out whether a given name is present in a list or not.

list = ["Aman", "Shashi", "Aditya", "Anku", "Ankit"]
name = input("Enter a name: ")
if (name in list):
    print(name + " is present in the list.")
else:
    print(name + " is not present in the list.")
