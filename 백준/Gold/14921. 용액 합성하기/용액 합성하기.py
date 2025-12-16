import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

min_diff = float("inf")
min_property = 0
left= 0
right = N-1

while (left<right):
    curr_prorpety = liquids[left] + liquids [right]
    diff_from_zero = abs(curr_prorpety - 0)
    min_diff = min(min_diff, diff_from_zero) 
    if min_diff == diff_from_zero:
        min_property = curr_prorpety
    if curr_prorpety < 0:
        left +=1
    elif curr_prorpety > 0:
        right -=1       
    else:
        break
print(min_property)