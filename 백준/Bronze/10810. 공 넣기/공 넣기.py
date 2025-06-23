N, M = map(int, input().split())
list =  [ 0 for i in range(N)]
for n in range(M):
    i,j,k = map(int, input().split())
    for z in range(i-1,j):
        list[z] = k
print(" ".join(map(str, list)))