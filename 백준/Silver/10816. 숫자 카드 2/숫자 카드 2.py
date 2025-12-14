import sys
from collections import  Counter
input = sys.stdin.readline

N = int(input())
count_dict = Counter(map(int, input().split()))
numbers_to_find = int(input())
numbers = map(int, input().split())
result = []
for num in numbers:
    result.append(str(count_dict.get(num, 0)))
print(" ".join(result))