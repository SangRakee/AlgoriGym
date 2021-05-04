def solution(progresses, speeds):
    answer = []

    while progresses:
        cnt = 0  # 배포할 변수
        for i in range(len(progresses)):
            if progresses[i] >= 100:  # 완성됐을때
                if i == 0:  # 젤 앞에 작업이 완성 됐을떄 if문

                    # 젤 앞에 작업이 완성 됐을때 그 뒤에 완성된 것이 있는지 확인하는 반복문
                    for j in range(len(progresses)):
                        if progresses[j] >= 100:
                            cnt += 1
                        else:
                            break
            else:  # 완성하지 못하였을때
                progresses[i] += speeds[i]

        # 완성된 작업들을 리스트들에서 제거하는 반복문
        for i in range(cnt):
            progresses.pop(0)
            speeds.pop(0)

        if cnt > 0:
            answer.append(cnt)

    return answer