begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque

def bfs(begin, target, words,visit):
    queue = deque([begin])
    index = words.index(target)
    print(queue)
    while queue:
        text = queue.popleft()
        if text == target:
            return visit[index]

        for i in range(1, len(words)):
            sum_of_word = 0
            for a, b in zip(text, words[i]):
                if not visit[i]:
                    if a == b:
                        sum_of_word += 1

                if sum_of_word == len(text) - 1:
                    visit[i] = visit[words.index(text)] + 1
                    queue.append(words[i])
                    print(visit,text,queue)





def solution(begin, target, words):
    answer = 0
    visit = [0] * (len(words)+1)

    # target이 words안에 존재하지 않으면
    if target not in words:
        return 0

    words.insert(0,begin)
    answer = bfs(begin, target, words,visit)
    return answer

print(solution(begin,target,words))