# 40% overall to and 33% in each subject to pass the exam, write a program ?

sub1 = int(input("Enter the number of subject 1 : "))
sub2 = int(input("Enter the number of subject 2 : "))
sub3 = int(input("Enter the number of subject 3 : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You have failed the eaxm because you got less than 33 in one subject.")
elif((sub1+sub2+sub3)/3 < 40):
    print("You have failed the exam because your overall marks is leass than 40%.")
else:
    print("Congratulations, you have passed the examination !")

