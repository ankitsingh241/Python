# Write a pyhton function to print multiplication table.

def table():
    n=int(input("Enter a no : "))
    for i in range (1,11):
        a=(f"{n} X {i} = {n*i}")
        print(a)
    return


print(table())

