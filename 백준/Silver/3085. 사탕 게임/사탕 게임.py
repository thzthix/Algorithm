N = int(input())
board = [list(input()) for _ in range(N)]
answer = 1
def check_row(R):
    global answer
    cnt = 1
    for j in range (1, N):
        if board[R][j-1] == board[R][j]:
            cnt+=1
            answer = max(answer, cnt)
        else:
            cnt = 1
def check_column(C):
    global answer
    cnt = 1
    for i in range(1, N):
        if board[i-1][C] == board[i][C]:
            cnt +=1
            answer = max(answer, cnt)
        else:
            cnt = 1
    
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check_row(i)
            check_column(j)
            check_column(j+1)
            board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
        if i+1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check_column(j)
            check_row(i)
            check_row(i+1)
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
            
print(answer)