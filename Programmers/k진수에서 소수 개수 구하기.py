# 구현
# n진수로 변환, 소수 확인 함수

def isnumChange(n, k):
    result = ""

    while n > 0:
        a = n // k
        b = n % k
        result = str(b) + result
        n = a

    return result


def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** (1 / 2)) + 1):
        if a % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    # 진수 변환
    num = isnumChange(n, k)
    print(num)

    # 0으로 분할
    num_split = num.split("0")
    print(num_split)

    # 소수 판단
    for i in num_split:
        if i:
            if isPrime(int(i)):
                answer += 1

    return answer

# print(solution(437674,3))