def solution(N, stages):
    answer = []
    result = []

    for i in range(1, N + 1):  # 스테이지 단계 for문
        rate = 0  # 각 스테이지 별 실패율 계산 변수
        count = 0  # 각 스테이지 별 실패한 사용자 갯수 변수
        delete_list = []
        length = len(stages)
        for j in range(len(stages)):  # 스테이지 별 실패한 사용자 확인 반복문
            if i >= stages[j]:
                count += 1
                delete_list.append(j)

        delete_list.reverse()
        for j in delete_list:
            del stages[j]

        if count == 0:  # 도달한 유저가 없을 시 실패율 0
            rate = 0
        else:
            rate = float(count) / float(length)

        result.append([i, rate])

    # 딕셔너리 형태의 value 값이 작은 순으로 정렬
    result.sort(reverse=True, key=lambda x: x[1])

    # 정렬된 딕셔너리 key 값 보여주기
    for i in result:
        answer.append(i[0])

    return answer

print(solution(	5, [2, 1, 2, 6, 2, 4, 3, 3]))