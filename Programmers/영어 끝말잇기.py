# 구현문제

def solution(n, words):
    answer = []

    for i in range(len(words)):
        order = i % n
        # print(order)
        if not answer:
            answer.append(words[i])
        else:
            if answer[-1][-1] == words[i][0]:
                if words[i] not in answer:
                    answer.append(words[i])
                else:
                    print(order)
                    break
            else:
                print(order)
                break

    print(answer)
    if len(words) == len(answer):
        return [0, 0]
    else:
        return [order + 1, len(answer) // n + 1]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))