def solution(n):
    numbers_to_sort = [digit for digit in str(n)]
    numbers_to_sort.sort(reverse=True)
    return int("".join(n for n in numbers_to_sort))