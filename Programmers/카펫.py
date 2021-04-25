brown=24
yellow=24

def solution(brown, yellow):
    answer = []
    weight=brown+yellow

    for i in range(brown,2,-1):
        for j in range(brown,2,-1):
            if yellow == (i-2)*(j-2):
                if weight==i*j:
                    answer.append(i)
                    answer.append(j)
                    return answer


    return answer

print(solution(brown,yellow))