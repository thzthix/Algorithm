import math
#[3,3,3,1,1]
def solution(citations):
    #배열을 sort해서
    #가장 큰 값부터 찾는다.
    #그 값 이상인게 h이상, 아닌게 h이하라면 h-index
    citations.sort(reverse = True)
    length = len(citations)
    for i in range(length):
        if citations[i] <= i:
            return i
        
    return length
        
        
        
    