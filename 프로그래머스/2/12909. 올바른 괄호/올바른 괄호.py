def solution(s):
    s = list(s)
    stack = []
    for b in s:
        if b == "(":
            stack.append(b)
        else:
            if not stack:
                return False
            stack.pop()
    return True if len(stack) == 0 else False