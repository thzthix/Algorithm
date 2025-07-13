#case 1
# 100-93/1 = 7일 후 배포
# 100-30/30 = 2.xx  = 3일 후 배포
# 100 - 55 / 5 = 9일 후 배포
#7일 째 2개, 9일 째 1개
# [9,3,7]  작은거 다 빼면 [2,1]


#case 2
#100-95 = 5/1 = 5
#100-90 = 10 / 1 = 10
#100-99 = 1 / 1 = 1
#100-99 = 1/ 1 = 1
#100-80 = 20/1 = 20
# 100 - 99 = 1/1 = 1
#5일 째 1개, 10일 째 3개 20일 쨰 2개

# 선입선출 -> 큐
#원소마다 며칠 째 완료되는지 계산
#큐에 다 넣는다
#  현재 보다 작으면 빼고 리스트에 넣는다.

#[1,20,1,1,10,5]
#[1, 3, 2]
from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    q = deque()
    for i in range(len(progresses)):
        q.append(math.ceil((100-progresses[i])/speeds[i]))
    while q:
        first_deploy_day = q.popleft()
        count = 1
        while q and q[0]<= first_deploy_day:
            q.popleft()
            count +=1
        answer.append(count)
    return answer
        
        