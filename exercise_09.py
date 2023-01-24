words = []
one_string = " "

for i in range(0,5):
    words.append(input("Enter a word: "))

one_string = one_string.join(words)

print("Words: {}".format(words))
print("One String: {}".format(one_string))

