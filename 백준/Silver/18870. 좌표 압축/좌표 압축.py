import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
numbers = list(map(int, input().split()))
numbers_hash = list(set(numbers))
numbers_hash.sort()
numbers_dict = {value: i for i, value in enumerate(numbers_hash)}
result = []
for n in numbers:
    result.append(str(numbers_dict[n]))
output(" ".join(result))