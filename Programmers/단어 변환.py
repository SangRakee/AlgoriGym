from collections import deque

def bfs(begin, target, words):
    queue = deque([begin])
    visit = [0] * len(words)
    index = words.index(target)
    while queue:
        text = queue.popleft()
        if text == target:
            return visit[index]

        for i in range(1, len(words)):
            sum_of_word = 0
            if not visit[i]:
                for a, b in zip(text, words[i]):
                    if a == b:
                        sum_of_word += 1

                if sum_of_word == len(text) - 1:
                    visit[i] = visit[words.index(text)] + 1
                    queue.append(words[i])

    return 0



def solution(begin, target, words):
    answer = 0

    # target이 words안에 존재하지 않으면
    if target not in words:
        return 0

    words.insert(0,begin)
    answer = bfs(begin, target, words)
    return answer

