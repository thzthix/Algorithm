def solution(arr):
    #arr을 돌면서
    #stack에 없으면 넣는다.
    stack = []
    for n in arr:
        if not stack or stack[-1] != n:
            stack.append(n)
    return stack