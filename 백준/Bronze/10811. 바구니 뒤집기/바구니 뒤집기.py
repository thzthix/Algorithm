N,M = map(int, input().split())
baskets = [i+1 for i in range(0,N)]
for m in range(M):
  i,j = map(int, input().split())
  baskets = baskets[:i-1] + list(reversed(baskets[i-1:j])) + baskets[j:N]
print(" ".join(map(str, baskets)))