num = input("Enter a number or QUIT to quit: ")
all_nums = []
even_nums = []

while num != "QUIT":
    all_nums.append(num)
    num = input("Enter a number or QUIT to quit: ")

for i in range(0, len(all_nums)):
    if int(all_nums[i]) % 2 == 0:
        even_nums.append(all_nums[i])

print("All Nums: {}".format(all_nums))
print("Even Nums: {}".format(even_nums))
