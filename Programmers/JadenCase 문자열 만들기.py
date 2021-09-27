# 구현문제
# split(" ")와 split()의 차이

def solution(s):
    answer = []
    s = s.split(" ")
    for i in s:
        if i != "":
            temp = i[0].upper() + i[1:].lower()
            answer.append(temp)
        else:
            answer.append("")

    answer = " ".join(answer)

    return answer

print(solution(s))
