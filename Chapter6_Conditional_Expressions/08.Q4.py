# Write a program to find wheather a given username is less than 10 characters or not.

name = input("Ener your name: ")
length = len(name)
if (length <= 10):
    if(length == 10):
        print(name + " is equal to 10 character.")
    else:
        print(name + " is less than 10 character.")
else:
    print(name + " is more than 10 character.")

