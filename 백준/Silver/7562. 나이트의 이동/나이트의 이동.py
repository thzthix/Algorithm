# 이동할 수 있는 좌표 지정

# 입력을 받습니다 (테스트 케이스의 개수) 
# 테스트 케이스 마다 
# 보드 배열, 덱, 방문 배열 선언
# 처음 좌표를 덱에 넣는다 (방문했다고 표시)

# 덱에서 꺼내면 (y, x, l)
# 가야할 곳의 좌표를 계산 



from collections import deque
direction_y = [-1,-2, -2, -1, 1, 2, 2, 1 ]
direction_x = [-2, -1 , 1 , 2 , 2 , 1 , -1 , -2]
l = 0

def is_valid_place(y,x):
    return 0<=y<l and 0<=x<l

N = int(input())

for _ in range(N):
    l = int(input())
    visited = [[False] * l for _ in range(l)]
    knight_deque = deque()
    start_x, start_y = map(int,input().split())
    finish_x, finish_y = map(int,input().split())
    knight_deque.append((start_y,start_x ,0))
    visited[start_y][start_x] = True
    
    while knight_deque:
        y,x,distance = knight_deque.popleft()
        # 이동한 곳이 목적지라면 멈추고, 이동한 거리를 표시
        if y == finish_y and x == finish_x:
            print(distance)
            break
        # 덱에 넣어주면서 이동
        for k in range(8):
            next_y = y + direction_y[k]
            next_x = x + direction_x[k]
            next_distance = distance + 1
            if is_valid_place(next_y ,next_x) and not visited[next_y][next_x]:
                visited[next_y][next_x] = True
                knight_deque.append((next_y, next_x, next_distance))
    
    