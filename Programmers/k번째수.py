def solution(array, commands):
    answer = []
    result = []
    for x in range(len(commands)):
        i, j, k = commands[x][0] - 1, commands[x][1] - 1, commands[x][2] - 1
        for y in range(len(array)):
            if y >= i and y <= j:
                answer.append(array[y])
        answer.sort()
        result.append(answer[k])
        answer = []

    return result