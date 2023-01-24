word = input("Enter a string: ")
char_list = list(word)
temp = " "

for i in range(0, len(char_list)):
    if (char_list[i]).islower():
        temp = temp + (char_list[i])


for i in range(0, len(char_list)):
    if (char_list[i]).isupper():
        temp = temp + (char_list[i])

word = temp

print(word)
