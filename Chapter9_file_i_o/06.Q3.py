# Write a program to copy text from a file.and

with open('poem.txt', 'r') as f:
    content = f.read()
with open('copy.txt', 'w') as f:
    f.copy(content)

