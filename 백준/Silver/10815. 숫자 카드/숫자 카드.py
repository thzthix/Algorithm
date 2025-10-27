import sys
input = sys.stdin.readline
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
answers = [1 if n in cards else 0 for n in numbers]
print(" ".join(map(str, answers)))