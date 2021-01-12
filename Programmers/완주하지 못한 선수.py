# 처음에는 그냔 for안에 if문으로 in을 사용하여 전부 확인하는 방식으로 했지만 시간초과가 발생하였음
# 각 리스트를 정렬하여 인덱스가 다른 곳을 return하는 방식

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p,c in zip(participant, completion):
        print(p,c)
        if p != c:
            return p

    return participant.pop()