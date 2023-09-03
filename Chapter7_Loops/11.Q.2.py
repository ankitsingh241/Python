# Write a program to greet all the names stored in a list which starts with S.

list = ["Ankit", "Sohan", "Shiojee", "Bikki"]
for name in list:
    if name.startswith("S"):
        print("Hello " + name)
