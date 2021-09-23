# 구현 문제
# 재귀함수를 이용하는 알고리즘
# sys.stdin.readline()으로 인풋을 받을때 공백까지 입력될수 있어서 input()을 사용하거나 strip()함수를 이용하여 공백문자 제거 해줄 것

import sys

def oddcheck(N,cnt):
    for i in N:
        if int(i) % 2 == 1:
            cnt += 1

    return cnt


def solution(cnt,N):
    global answer

    if len(N)==1:
        answer.append(cnt)
        return
    elif len(N)==2:
        tmp=str(int(N[0])+int(N[1]))
        add_cnt=oddcheck(tmp,cnt)
        solution(add_cnt,tmp)

    elif len(N)>=3:
        for a in range(1,len(N)):
            for b in range(a+1,len(N)):
                # print(N[:a],N[a:b],N[b:])
                tmp = str(int(N[:a]) + int(N[a:b]) + int(N[b:]))
                add_cnt=oddcheck(tmp,cnt)
                solution(add_cnt,tmp)

N=str(sys.stdin.readline().strip())
answer=[]
cnt=oddcheck(N,0)
solution(cnt,N)
# print(answer)
print(min(answer),max(answer))
