row = int(input("Enter a row num from 1 to 5: "))
column = int(input("Enter a col num from 1 to 5: "))

for i in range(0, 5):
    for k in range(0, 4):
        if row == i + 1 and column == k + 1:
            print(1, end=" ")
        else:
            print(0, end=" ")

    print(0)
