def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        current = numLog[i]
        next = numLog[i+1]
        if current + 1 == next:
            answer += 'w'
        elif current - 1== next:
            answer += 's'
        elif current + 10 == next:
            answer += 'd'
        elif current - 10 == next:
            answer += 'a'
    return answer