def solution(n):
    answer = []
    answer.append(n)
    while(n!=1):
        n = n // 2 if n % 2 == 0 else 3*n+1
        answer.append(n)
    return answer