import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

numbers = sorted(map(int, input().split()))
left = 0
right = N-1
count = 0

while left < right:
    curr_sum = numbers[left] + numbers[right]
    if curr_sum == M:
        count +=1
        right -=1
    elif curr_sum < M:
        left +=1
    else:
        right -=1
print(count)



