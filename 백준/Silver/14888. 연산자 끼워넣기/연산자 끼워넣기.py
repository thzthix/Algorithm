import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
operator_num = list(map(int, input().split()))
max_val = float('-inf')
min_val = float('inf')
def back(index, result):
    global max_val
    global min_val
    if index == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    current_num = numbers[index]
    if (operator_num[0]>0):
        operator_num[0] -=1
        back(index+1, result + current_num )
        operator_num[0] +=1
    if (operator_num[1]>0):
        operator_num[1] -=1
        back(index+1, result - current_num )
        operator_num[1] +=1
    if (operator_num[2]>0):
        operator_num[2] -=1
        back(index+1, result * current_num )
        operator_num[2] +=1
    if (operator_num[3]>0):
        operator_num[3] -=1
        if result<0:
            back(index+1, -(-result // current_num) )
        else:
            back(index+1, result // current_num )
        
        operator_num[3] +=1

        


back(1,numbers[0])
print(max_val)
print(min_val)