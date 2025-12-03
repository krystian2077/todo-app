waiting_list = ['sen', 'ben', 'john']
waiting_list.sort()

for index, name in enumerate(waiting_list):
    row = f"{index + 1}.{name.capitalize()}"
    print(row)

for i, j in enumerate("abcd"):
    print(i + 1)