max = 0
index = 0;
for i in range(1,10):
    current_number = int(input())
    if(max<current_number):
        max = current_number
        index = i
print(f"{max}\n{index}")
