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
def solution(array, commands):
    answers = []
    for com in commands:
        sorted_arr = quick_sort(array[com[0]-1:com[1]])
        answers.append(sorted_arr[com[2]-1])
    return answers
        
    