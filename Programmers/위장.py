#약수 개수 구하는 방식 사용

def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1


# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key = lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))