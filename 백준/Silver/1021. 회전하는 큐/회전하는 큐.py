from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
deque = deque([i for i in range(1,N+1)])
numbers = map(int, input().split())

answer = 0
for num in numbers:
    #왼쪽이 가까운지 오른쪽이 가까운지 계산
    idx = deque.index(num)
    left_count = idx - 0
    right_count = len(deque) - idx

    #가장 가까운 방향 끝에 올때까지 이동
    if(left_count < right_count):
        deque.rotate(-left_count)
        answer += left_count
    else:
        deque.rotate(right_count)
        answer+=right_count
    deque.popleft()
    #덱에서 뽑아줌

print(answer)



