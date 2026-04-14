import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    left= []
    right= []
    inputs = input().strip()
    for c in inputs:
        if c == '<':
            if left:
                right.append(left.pop())
        elif c == '>':
            if right:
                left.append(right.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)
    print ("".join(left)+ "".join(reversed(right)))