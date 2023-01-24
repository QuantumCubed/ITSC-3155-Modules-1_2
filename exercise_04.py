n = int(input("Enter a number: "))
py_list = [None] * n

for i in range(0, n):
    py_list[i] = float(input("Enter number {}: ".format(i + 1)))

print("List: {}".format(py_list))
print("Average: {}".format((sum(py_list)/len(py_list))))
