import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
names = []
for _ in range(N):
    names.append(input())
counts = Counter(names)
ans = sorted(counts.items(), key = lambda x: (-x[1], x[0]))
print(ans[0][0])