LIMIT = 45
t = [n*(n+1)//2 for n in range(LIMIT)]
N = int(input())

def is_expressed(K):
    for i in range(1, LIMIT):
        for j in range (i,LIMIT):
            for k in range (j, LIMIT):
                if t[i] + t[j] + t[k] == K:
                    return 1
                    
    return 0
for _ in range(N):
    print(is_expressed(int(input())))