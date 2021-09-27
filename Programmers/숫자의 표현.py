# 단순 구현 문제

def solution(n):
    answer = 0

    arr = [i for i in range(n + 1)]

    for i in range(1, len(arr)):
        sum_num = 0
        num = i
        while True:
            if sum_num == n:
                answer += 1
                break
            if sum_num > n:
                break
            sum_num += num
            num += 1

    return answer