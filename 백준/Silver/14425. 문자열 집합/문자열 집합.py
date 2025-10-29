import sys
input = sys.stdin.readline
N,M = map(int, input().split())
count = 0
wordset = set([])
for i in range(N):
    wordset.add(input())
for i in range(M):
    word = input()
    if word in wordset:
        count+=1
print(count)