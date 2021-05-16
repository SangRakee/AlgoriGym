def solution(s):
    answer = 0
    stack = []

    for i in range(len(s)):
        try:
            if i > 0:
                if stack[-1] != s[i]:
                    stack.append(s[i])
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        except IndexError:
            stack.append(s[i])

    if len(stack) == 0:
        answer = 1

    return answer