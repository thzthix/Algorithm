import sys
sys.setrecursionlimit(10**6)
N,M = map(int, input().split())
ans = []
def back():
    if len(ans) == M:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,N+1):
        if len(ans) == 0 or i >= ans[-1]:
            ans.append(i)
            back()
            ans.pop()

back()