import sys
input = sys.stdin.readline
N = int(input())
cards = set(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))
answers = []
for n in numbers:
    if n in cards:
        answers.append(1)
    else:
        answers.append(0)
print(" ".join(map(str, answers)))