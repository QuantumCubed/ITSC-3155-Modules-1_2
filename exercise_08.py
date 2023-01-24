py_list = []
only_once = []
i = 0

for i in range(0, 10):
    py_list.append(int(input("Enter number {}: ".format(i + 1))))

for i in range(0, len(py_list)):
    if py_list.count(i) == 1:
        only_once.append(py_list[i])

print("Original List: {}".format(py_list))
print("Nums that appear only once: {}".format(only_once))
