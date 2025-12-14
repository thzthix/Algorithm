import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

curr_sum = sum(temperatures[0:K])
answer = curr_sum


for right in range(K, N):
        curr_sum += temperatures[right]
        curr_sum -= temperatures[right - K]
        answer = max(answer, curr_sum)
print(answer)