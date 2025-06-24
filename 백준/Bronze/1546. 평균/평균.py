import math
N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
avg_score = sum(scores) / len(scores)
print(avg_score/max_score*100)