grade = int(input("Enter a grade from 0 to 100: "))

#NOT WORKING
while 0 > grade > 100:
    print("Invalid Number")
    grade = int(input("Enter a grade from 0 to 100: "))

if grade >= 90:
    print("Your grade is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
    print("Your grade is D")
elif grade <= 59:
    print("Your grade is F")
