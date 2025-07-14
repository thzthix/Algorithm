def solution(x):
    return x % sum([int(digit) for digit in str(x)]) == 0
    