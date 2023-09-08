# Writing files --> It will create a new file and will paste the text in that file.

# f = open("another.txt", "w")
f = open("another.txt", "a") # to append any text.
# f.write("Please write this in above mentioned file.")
f.write(input("Enter the text:"))
f.close()

