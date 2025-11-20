n = int(input())
arr = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):
    # arr[i] 오큰수로 가질 애들 
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()  
        answer[idx] = arr[i]  
    
    stack.append(i)  

print(' '.join(map(str, answer)))
