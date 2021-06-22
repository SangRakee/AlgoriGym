def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        arr = []
        for j in range(1, i + 1):
            if i / j == int(i / j):
                arr.append(j)
        if len(arr) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer