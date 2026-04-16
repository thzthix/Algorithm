N,L = map(int, input().split())
holes = sorted(map(int, input().split()))
answer = 0
covered_length = 0
for hole in holes:
    if covered_length < hole:
        answer += 1 
        covered_length = hole + L -1
print(answer)    