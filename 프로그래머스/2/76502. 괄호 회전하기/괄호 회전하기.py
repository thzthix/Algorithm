def solution(s):
    #괄호 받아오기
    brackets = s
    #스택 초기화
    stack = []
    #count 초기화
    count = 0
    #입력 배열 개수만큼 반복
    for j in range(0, len(brackets)):
        for i in range (0,len(brackets)):
            #스택에 "{"나 "(" 이면
            current = brackets[i]
            is_success = True
            if current in ["{","(","["]:
                stack.append(current)
            #스택에 집어넣는다.
            else:
                if not stack:
                    is_success = False
                    break
                #스택에서 "}" 나 ")" 이면
                #만약 stack에 아무것도 없으면 skip
                head = stack[-1]
                #스택에서 "}" 일 때 "{"이고 스택에서 ")"일 때 ")"면
                if (current == "}" and head == "{") or (current == ")" and head == "(") or (current==']' and head == '['):
                #pop
                    
                    stack.pop()
                #아니면 skip
                #스택이 비었으면 count++
        if is_success and not stack:
            count+=1
        stack = []
    #인덱스 슬라이싱으로 회전
        brackets = change_brackets(brackets)
    return count
def change_brackets(brackets):
    return brackets[1:] + brackets[0]