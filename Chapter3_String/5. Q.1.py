
letter = '''Dear <|NAME|>,
Greetings from CIVO. I am happy to tell you about your interview.
You are selected!
Have a great day ahead!
Thanks and regards,
Saiyam Pathak.
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

