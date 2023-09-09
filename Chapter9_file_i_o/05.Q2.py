# Replace the a word in a given file.

with open('donkey.txt', 'r') as f:
    content = f.read()

content = content.replace("Donkey", "*&^%$#@!~")

with open('donkey.txt', 'w') as f:
    f.write(content)

