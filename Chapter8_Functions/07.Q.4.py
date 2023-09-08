# Write a function which converts inches to cm.

def inch(cm):
    return (2.54*cm)

i = int(input("Enter any number: "))
c = inch(i)

print(f"The value of {i} inch is {c}cm")

