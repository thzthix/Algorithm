r_list = list()
for i in range(10):
    r = int(input()) % 42
    if r not in r_list:
        r_list.append(r)
print(len(r_list))