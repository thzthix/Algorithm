import math
#[3,3,3,1,1]
def solution(citations):
    #배열을 sort해서
    #가장 큰 값부터 찾는다.
    #그 값 이상인게 h이상, 아닌게 h이하라면 h-index
    citations.sort(reverse = True)
    max_value = 0
    current_value  = citations[0] 
    last_value = 0
    while(current_value > 0):
        high_array = [c for c in citations if c >= current_value]
        if len(high_array) >= current_value and current_value != last_value:
            return current_value
        last_value = current_value
        current_value -=1
        
    return 0
        
        
        
    