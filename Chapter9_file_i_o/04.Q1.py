# Write a program to read the text from a given file.

f = open('poem.txt')
t = f.read()
if 'woods' in t:
    print("Woods is present in the poem.")
else:
    print("Woods is not present in the poem.")
f.close()

