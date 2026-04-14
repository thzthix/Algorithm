N = int(input())
board = [list(input()) for _ in range(N)]
answer = 1
def search():
    global answer
    for i in range(N):
        cnt = 1
        for j in range (1, N):
            if board[i][j-1] == board[i][j]:
                cnt+=1
                answer = max(answer, cnt)
            else:
                cnt = 1
    
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i-1][j] == board[i][j]:
                cnt +=1
                answer = max(answer, cnt)
            else:
                cnt = 1
    
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            search()
            board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
        if i+1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            search()
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
            
print(answer)