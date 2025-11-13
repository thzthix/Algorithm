while True:
    line = list(map(int, input().split()))
    n = line[0]
    
    if n == 0:
        break
    
    heights = line[1:]
    stack = []  # (인덱스, 높이) 저장
    max_area = 0
    
    for i, h in enumerate(heights):
        start = i
        
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            width = i - idx
            area = height * width
            max_area = max(max_area, area)
            start = idx  
        
   
        stack.append((start, h))
    
 
    for idx, height in stack:
        width = n - idx
        area = height * width
        max_area = max(max_area, area)
    
    print(max_area)