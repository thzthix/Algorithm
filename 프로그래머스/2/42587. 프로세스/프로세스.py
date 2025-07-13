#처음 프로세스들 [1,2,3,4,5,6]
#[1,2,3,4,5,6] [1,1,9,1,1,1]
#[2,3,4,5,6,1] [1,9,1,1,1,1]
#[]
#[0,1,2,3] [2,1,3,2]
#[1,2,3,0] [1,3,2,2]
#[3,0,1] [2,2,1]
from collections import deque
import math
def solution(priorities, location):
    q = deque()
    priority_q = deque()
    for i in range(0,len(priorities)):
        q.append(i)
        priority_q.append(priorities[i])
    count = 0
    while priorities:
        c = q.popleft()
        p = priority_q.popleft()
        max_p = max(priorities)
        if(p == max_p):
            priorities.remove(max_p)
            count+=1
            if(c == location):
                return count
        else:
            q.append(c)
            priority_q.append(p)
 
