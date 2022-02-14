# 구현 문제
# index, count 함수를 사용하면 코드가 더 줄어들수 있음

def solution(id_list, report, k):
    answer = []

    result = {}
    for i in id_list:
        result[i] = 0
    print(result)

    # 신고한 사람 딕셔너리 만들기
    people = {}

    # 신고 당한 횟수 딕셔너리
    rep_dic = {}

    # 반복문 - report
    for rep in report:
        x, y = rep.split(" ")

        # people[x] 있는 경우
        if x in people:
            if [y] not in people[x]:
                people[x].append([y])
                if y in rep_dic:
                    rep_dic[y] += 1
                else:
                    rep_dic[y] = 1

        # people[x] 없는 경우
        else:
            people[x] = [[y]]
            if y in rep_dic:
                rep_dic[y] += 1
            else:
                rep_dic[y] = 1

        # if y in rep_dic:
        #     rep_dic[y] +=1
        # else:
        #     rep_dic[y]=1

    # print(people)
    # print(rep_dic)

    # rep_dic에서 k 넘는 사람 뽑기
    stop = []
    for key in rep_dic:
        if rep_dic[key] >= k:
            stop.append([key])

    # print(stop)
    # people에서 stop 명단이 있는 사람 파악
    for key in people:
        cnt = 0
        for value in people[key]:
            if value in stop:
                cnt += 1
        result[key] = cnt

    # print(result)
    for i in result.values():
        answer.append(i)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))