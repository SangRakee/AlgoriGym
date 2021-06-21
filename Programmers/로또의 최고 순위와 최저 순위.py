lottos=[44, 1, 0, 0, 31, 25]
win_nums=[31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    answer = []
    cnt,zero_cnt=0,0
    for i in lottos:
        if i==0:
            zero_cnt+=1
        else:
            if i in win_nums:
                cnt+=1
    temp=[]
    max_cnt=cnt+zero_cnt
    min_cnt=cnt
    temp.append(max_cnt)
    temp.append(min_cnt)
    for i in temp:
        if i==6:
            answer.append(1)
        elif i==5:
            answer.append(2)
        elif i==4:
            answer.append(3)
        elif i==3:
            answer.append(4)
        elif i==2:
            answer.append(5)
        else:
            answer.append(6)

    return answer

print(solution(lottos,win_nums))