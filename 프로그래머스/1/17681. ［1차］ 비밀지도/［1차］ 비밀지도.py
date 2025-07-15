def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        bin_result = bin(i | j)[2:].zfill(n)
        bin_result  = bin_result.replace("0", " ")
        bin_result  = bin_result.replace("1", "#")
        answer.append(bin_result)
    return answer