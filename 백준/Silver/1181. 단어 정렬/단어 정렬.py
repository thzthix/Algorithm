import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
words = list(set(input().rstrip() for _ in range(N)))
words.sort(key=lambda x:(len(x), x))
for n in words:
    output(n+"\n")