from functools import reduce
def solution(n):
    number_list = list(str(n))
    return reduce( lambda acc, value: acc+int(value),number_list, 0)
