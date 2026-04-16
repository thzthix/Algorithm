# 정렬해서
#투포인터로 짝을 탐색 (i는 작은 박스. j는 큰 박스)

import sys
input = sys.stdin.readline

N = int(input())
boxes = sorted([int(input()) for _ in range(N)])

i = 0
half = N//2
j = half
pairs = 0

while i < half and j < N:
    if boxes[i] * 2 <=  boxes[j]:
        pairs +=1
        i +=1
        j +=1
    else:
        j+=1

print(N-pairs)
