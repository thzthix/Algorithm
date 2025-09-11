def quick_sort(a):
    if len(a) <= 1:
        return a
    left = []
    right = []
    pivots = []
    piv = a[0]
    for i in a:
        if i < piv:
            left.append(i)
        elif i > piv:
            right.append(i)
        else:
            pivots.append(i)
    return quick_sort(left) + pivots + quick_sort(right)
def solution(citations):
    sorted_arr = list(reversed(quick_sort(citations)))
    for i in range(len(sorted_arr)):
        if sorted_arr[i] < i+1:
            return i
    return len(sorted_arr)
     #6 5 3 1 0
    