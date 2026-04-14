N = int(input())
inputs = input().rstrip()
numbers = [int(input()) for _ in range(N)]
stack = []
for c in inputs:
    if c.isalpha():
        idx = ord(c)- ord('A')
        stack.append(numbers[idx])
    else:
        if stack:
            right = stack.pop()
            left = stack.pop()
        if c == "*":
            stack.append(left*right)
        elif c == "/":
            stack.append(left / right)
        elif c == "+":
            stack.append(left + right)
        elif c == "-":
            stack.append(left - right)
print(f"{stack.pop():.2f}")