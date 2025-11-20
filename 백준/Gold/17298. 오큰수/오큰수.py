n = int(input())
arr = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n-1, -1, -1):
    # 현재 수보다 작거나 같은거 다 뺌
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    
    # 스택에 남은 게 있으면 그게 오큰수
    if stack:
        answer[i] = stack[-1]
    
    # 현재 값을 스택에 추가
    stack.append(arr[i])

print(' '.join(map(str, answer)))