import sys
input = sys.stdin.readline
n = int(input())
numbers = sorted(map(int, input().split()))
target = int(input())
left = 0
right = n -1
count = 0
while left<right:
    curr_sum  = numbers[left] + numbers[right]
    if curr_sum < target:
        left +=1
    elif curr_sum == target:
        count +=1
        right -=1
    else:
        right -=1
print(count)