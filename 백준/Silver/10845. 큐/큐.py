from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
N = int(input())

while(N>0):
    try:
        command = input().split()
        match command[0]:
            case "push":
                queue.append(command[1])
            case "front":
                if not queue:
                    print(-1)
                else:
                    print(queue[0])
            case "size":
                print(len(queue))
            case "pop":
                if not queue:
                    print(-1)
                else:
                    print(queue.popleft())
            case "back":
                if not queue:
                    print(-1)
                else:
                    print(queue[-1])
            case "empty":
                if queue:
                    print(0)
                else:
                    print(1)
       
    except EOFError:
        break
    N-=1
