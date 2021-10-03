# 구현
# n진법 변환 문제

def change(n, num):
    result = ""

    if num == 0:
        return str(num)

    while num > 0:
        p = num // n
        r = num % n

        if r == 10:
            r = "A"
        elif r == 11:
            r = "B"
        elif r == 12:
            r = "C"
        elif r == 13:
            r = "D"
        elif r == 14:
            r = "E"
        elif r == 15:
            r = "F"

        result = str(r) + result
        num = p

    return result


def solution(n, t, m, p):
    result = ""
    answer = ''

    num = 0
    while len(answer) <= (t * m):
        bit = change(n, num)

        for i in bit:
            answer += i
        num += 1

    print(answer)
    for i in range(p - 1, t * m, m):
        result += answer[i]

    return result


print(solution(2,4,2,1))