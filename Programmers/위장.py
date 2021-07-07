#약수 개수 구하는 방식 사용

def solution1(clothes):
    answer = 1
    dict={}
    
    for i in clothes:
        if i[1] in dict:
            dict[i[1]]+=1
        else:
            dict[i[1]]=1
    
    for i in dict.values():
        answer*=(i+1)
    
    return answer-1


def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))