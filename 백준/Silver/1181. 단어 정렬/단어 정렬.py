import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
words = []
for i in range(N):
    n = input().rstrip()
    if n not in words:
        words.append(n)
words.sort(key=lambda x:(len(x), x))
for n in words:
    output(n+"\n")