N = int(input())
for i in range(N):
    r, s = input().split()
    r = int(r)
    print("".join(c * r for c in s))