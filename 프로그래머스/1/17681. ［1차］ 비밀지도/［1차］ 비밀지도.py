def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        deconde_str = ""
        bin_arr1 = bin(arr1[i])[2:].zfill(n)
        bin_arr2 = bin(arr2[i])[2:].zfill(n)
        decode_str = ""
        for j in range(n):
            if bin_arr1[j] == "0" and bin_arr2[j] == "0":
                decode_str += " "
            else:
                decode_str += "#"
        answer.append(decode_str)
    return answer