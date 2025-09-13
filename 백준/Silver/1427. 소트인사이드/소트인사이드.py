import sys
input =sys.stdin.readline
numbers = list(map(int,input().strip()))
numbers.sort(reverse=True)
print("".join(map(str, numbers)))