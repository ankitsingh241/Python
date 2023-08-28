# Logical Operators

# and = if both oprands are true then true else false.
# or = if at least one oprands is true then true else false.
# not = inverts true to false & false to true.

workage = int(input("Enter your age: "))
if (workage>30 and workage<60):
    print("You can work with us.")
else:
    print("You are not eligible.")

age = int(input("Enter your age: "))
if(age>34 or age<56):
    print("You can work with us.")

else:
    print("You cannot work with us.")

