list_one = [None] * 5
list_two = [None] * 5
list_common = [None] * 5

for i in range(0, len(list_one)):
    list_one[i] = int(input("Enter a number for the first list: "))

for i in range(0, len(list_two)):
    element = list_two[i] = int(input("Enter a number for the second list: "))
    if list_one.__contains__(element):
        list_common[i] = list_two[i]

common_set = [*set(list_common)]
list_common = list(common_set)
temp_list = filter(lambda item: item is not None, list_common)
list_common = list(temp_list)

print("First List: {}".format(list_one))
print("Second List: {}".format(list_two))
print("Common List: {}".format(list_common))
