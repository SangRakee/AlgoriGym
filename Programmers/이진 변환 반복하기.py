# 구현 문제
# 10진수를 2진수로 변환하기

def binary(n):
    result = ""

    if n == 1:
        return "1"

    while n >= 2:
        p = n // 2
        r = n % 2
        result = str(r) + result
        n = p
    result = str(p) + result

    return result


def solution(s):
    answer = []
    zero_cnt = 0
    cnt = 0
    while s != "1":
        bit = ""

        # 1.0제거
        for i in s:
            if i == "1":
                bit += i
            else:
                zero_cnt += 1

        # 2.c구하기
        c = len(bit)

        # 3.c를 이진수로 변경
        num = binary(c)
        s = num
        cnt += 1

    return [cnt, zero_cnt]

print(solution("110010101001"))