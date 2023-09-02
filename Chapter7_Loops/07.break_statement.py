# It instructs the program to exit the loop.
# so the else statement wont be print.

for i in range(10):
    print(i)
    if i==5:
        break
else:
    print("This is inside else of for")
