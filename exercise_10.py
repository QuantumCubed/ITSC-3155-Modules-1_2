word = input("Enter a string: ")
char_list = list(word)
inner_lists = []
n = 0

for i in range(0, (int((len(word))/3) + 1)):
    variable_list = []
    for k in range(0, 3):
        variable_list.append(char_list[k])
        n = n + 1

    inner_lists.append(variable_list)


print(variable_list)
print(inner_lists)
