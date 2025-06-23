import math
N = input()
numbers = input().split()
numbers_list = list(map(int, numbers))
print(" ".join([str(min(numbers_list)),str(max(numbers_list))]))
