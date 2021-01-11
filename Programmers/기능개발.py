def solution(progresses, speeds):
    answer = []
    result=[]
    day=0

    for i in range(len(progresses)):
        while progresses[i]<100:
            progresses[i]+=speeds[i]
            day+=1
        answer.append(day)
        day=0
    print(answer)


    for i,d in enumerate(answer):
        if i==0:
            max=d
            result.append(1)
            continue

        if d<=max:
            result[-1]+=1
        else:
            max=d
            result.append(1)

    return result