import sys
input = sys.stdin.readline
N = int(input())
left = 0
count = 0
current_sum = 0
for right in range(0,N+1):
    current_sum += right
    while current_sum > N:
        current_sum -= left
        left +=1
    if current_sum == N:
        count +=1
print(count)

