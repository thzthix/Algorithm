import math
def solution(n):
    sqrt = math.sqrt(n)
    if(sqrt == int(sqrt) ):
        return math.pow(sqrt+1,2)
    else:
        return -1