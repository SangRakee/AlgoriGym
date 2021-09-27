# 최대공약수, 최소공배수 구하기
# 유클리드 호제법


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(arr):
    answer = 0

    a = arr[0]
    for i in arr[1:]:
        b = i
        gcd_num = gcd(a, b)
        a = (a * b) // gcd_num

    return a