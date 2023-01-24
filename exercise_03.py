num = int(input("Enter an integer greater than 1: "))

while num <= 1:
    num = int(input("Enter A Valid Number: "))

for i in range(0, num + 1):
    print("The cube of {} is {}".format(i, i ** 3))
