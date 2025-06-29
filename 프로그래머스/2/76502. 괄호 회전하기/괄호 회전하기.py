def solution(s):
    return sum( 1 for rotation in range(len(s)) if is_valid(s, rotation))
def is_valid(s, start_pos):
    stack = []
    bracket_pairs = {")": "(","}":"{","]":"["}
    for i in range(len(s)):
        current_char = s[(i+start_pos)%len(s)]
        if current_char in "{[(":
            stack.append(current_char)
        else:
            if not stack or stack[-1] != bracket_pairs[current_char]:
                return False
            stack.pop()
    return len(stack) == 0