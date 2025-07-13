from functools import reduce
def solution(n):
    return sum(int(digit) for digit in str(n))
