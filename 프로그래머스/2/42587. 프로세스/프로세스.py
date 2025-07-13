
from collections import deque
import math
def solution(priorities, location):
    q = deque()
    for i in range(0,len(priorities)):
        q.append({"location":i, "value": priorities[i]})
    count = 0
    while priorities:
        c = q.popleft()
        max_p = max(priorities)
        if(c["value"] == max_p):
            priorities.remove(max_p)
            count+=1
            if(c["location"] == location):
                return count
        else:
            q.append(c)
 
