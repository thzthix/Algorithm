N,S = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0
end = 0
curr_sum = 0

for start in range(N):
    while end < N and curr_sum < S:
        curr_sum += numbers[end]
        end +=1
    if curr_sum == S:
        count +=1
    curr_sum -= numbers[start]
print(count)