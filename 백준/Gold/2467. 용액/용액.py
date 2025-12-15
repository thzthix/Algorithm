import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
answer = float("inf")
left = 0
right = N-1
answers = []
while (left<right):
    property_value = liquids[left] + liquids[right]
    diff_zero = abs(property_value-0)
    answer = min(answer, diff_zero )
    if answer == diff_zero:
        answers = [str(liquids[left]), str(liquids[right])]
    if property_value < 0:
            left +=1
    elif  property_value > 0:
            right -=1
    else:
        break
print(" ".join(answers))