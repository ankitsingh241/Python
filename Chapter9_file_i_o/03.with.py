# While using WITH we dont need to close a file.

with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("Hello Guys!")

print(a)
