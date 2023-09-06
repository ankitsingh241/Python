# Print the star pattern.

n = 5

for i in range(5):
    print("*" * (i+1))
    
# Triangle pattern.

m = 5

for i in range(5):
    print(" " * (m-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (m-i-1))


