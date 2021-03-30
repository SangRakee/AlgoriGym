def solution(answers):
    answer = []
    result = []
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(len(student)):
        cnt = 0
        for j in range(len(answers)):
            if student[i][j % len(student[i])] == answers[j]:
                cnt += 1
        answer.append(cnt)

    num = max(answer)
    for i in range(len(answer)):
        if num == answer[i]:
            result.append(i + 1)

    return result