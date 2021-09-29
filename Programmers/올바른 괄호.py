# 스택 문제

def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        if i == 0:
            stack.append(s[i])
        else:
            if s[i] == ")":
                if stack:
                    if stack[-1] == "(":
                        stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

    if not stack:
        return True
    else:
        return False