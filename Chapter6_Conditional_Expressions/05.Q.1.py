# Write a program to find greatest of four numbers ?

num1 = input("Enter number 1 : ")
num2 = input("Enter number 2 : ")
num3 = input("Enter number 3 : ")
num4 = input("Enter number 4 : ")

if(num1>num2):
    f1 = num1
else:
    f1 = num2

if(num3>num4):
    f2 = num3
else:
    f2 = num4

if(f1>f2):
    print(f1 + " is the greatest number.")
else:
    print(f2 + " is the greatest number.")
