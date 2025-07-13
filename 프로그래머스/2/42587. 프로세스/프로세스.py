
from collections import deque
def solution(priorities, location):
    q = deque()
    for i in range(0,len(priorities)):
        q.append({"location":i, "value": priorities[i]})
    count = 0
    while q:
        c = q.popleft()
        if any(process["value"] > c["value"] for process in q):
            q.append(c)
        else:
            count+=1
            if(c["location"] == location):
                return count
        
            
 
