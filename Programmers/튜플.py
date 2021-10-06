# 문자열
# 길이순으로 정렬 방식

def solution(s):
    answer = []

    arr = []
    temp = []
    num = ""
    for i in range(len(s)):
        if i == 0 or i == (len(s) - 1):
            continue
        else:
            if s[i] == "}":
                temp.append(num)
                arr.append(temp)
                num = ""
                temp = []
            elif s[i].isdigit():
                num += s[i]
            elif s[i] == ",":
                if len(num) != 0:
                    temp.append(num)
                    num = ""

    # print(arr)
    arr.sort(key=len)


    for i in range(1, len(arr) + 1):
        for j in arr:
            if len(j) == i:
                for z in range(len(j)):
                    if int(j[z]) not in answer:
                        answer.append(int(j[z]))

    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))