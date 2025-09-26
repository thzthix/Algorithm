import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
min_val = float("inf")
N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
teamA = []
def back(index, teamA):
   
    global min_val
    if len(teamA) ==N//2: 
        teamA_set = set(teamA)
        teamB = [i for i in range(N) if i not in teamA_set]
        sumA = 0
        for i in teamA:
            for j in teamA:
                if i != j:
                    sumA += graph[i][j]
        
        sumB = 0
        for i in teamB:
            for j in teamB:
                if i != j:
                    sumB += graph[i][j]
        
        min_val = min(min_val, abs(sumA - sumB))
        return
    for i in range(index,N):
            teamA.append(i)
            back(i+1, teamA)
            teamA.pop()
back(0,teamA)
print(min_val)