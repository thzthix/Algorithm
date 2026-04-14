from itertools import combinations
numbers = [int(input()) for i in range(9)]
for i in combinations(numbers,7):
    if sum(i) == 100:
        for n in i:
            print(n)
        break