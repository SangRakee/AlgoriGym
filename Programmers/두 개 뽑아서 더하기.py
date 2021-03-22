#기본적인 문제이지만 itertools 라이브러리에 적응 할 수 있는 문제
#sort() 정렬 같은 경우 반환값이 None이기 때문에
#sort(선언 리스트) 입력 후 print(선언리스트)로 작성해야함
#print(sort(선언 리스트)) 하면 None으로 출력됨

from itertools import combinations

numbers=[2,1,3,4,1]

def solution(numbers):
    answer = []
    a=list(combinations(numbers,2))
    for i in a:
        answer.append(i[0]+i[1])

    list(set(answer)).sort()
    return list(set(answer))

print(solution(numbers))