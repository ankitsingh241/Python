# Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter a number: "))
for i in range(1, 11):
    # print(str(number) + "X" + str(i) + "=" + str(i*number))
    print(f"{number}X{i} = {number*i}")

