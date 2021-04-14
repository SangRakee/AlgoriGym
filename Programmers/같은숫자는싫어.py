#arr=[1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    num=0
    for i in range(len(arr)):
        if num!=arr[i]:
            answer.append(arr[i])
        num=arr[i]

    return answer

print(solution(arr))