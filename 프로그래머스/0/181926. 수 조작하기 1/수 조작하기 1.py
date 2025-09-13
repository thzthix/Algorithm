def solution(n, control):
    commands = {'w':1, 's':-1, 'd':10, 'a':-10}
    for c in control:
        n+= commands[c]
    
    return n