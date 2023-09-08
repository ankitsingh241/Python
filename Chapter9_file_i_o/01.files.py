# Files : 1. Text files(.txt, .c etc)
#         2. Binary files(.jpg, .dat etc)

# Opening a file

# Parameters : filename and mode
#       open("filename", "mode") --> Open is a built in function.

# Mode : r --> reading mode
#      : w --> writing mode
#      : a --> appending mode
#      : + --> updating mode

# 'rb' will open and read in binary mode.
# 'rt' will open and read in text mode.


f = open("sample.txt", "r") # If you do not mention any mode it will take "r" by default.
data = f.read()
# data = f.read(5) # reads first 5 characters from the file.
print(data)
f.close()

