# 완전탐색 문제
# 조합 라이브러리 이용

import sys
from itertools import combinations

answer=int(1e9)

N=int(sys.stdin.readline())
arr=[i for i in range(1,N+1)]

S=[]
for _ in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    S.append(x)

comb=list(combinations(arr,N//2))
# print(comb)


for i in comb:
    a=[]
    b=[]
    teamA,teamB=0,0
    for j in arr:
        if j in i:
            a.append(j)
        else:
            b.append(j)
    a_comb=list(combinations(a,2))
    b_comb = list(combinations(b, 2))
    # print(a_comb,b_comb)
    for i in range(len(a_comb)):
        # print(a_comb[i][0]-1,a_comb[i][1]-1)
        teamA+=(S[a_comb[i][0]-1][a_comb[i][1]-1] + S[a_comb[i][1]-1][a_comb[i][0]-1])
        teamB += (S[b_comb[i][0]-1][b_comb[i][1]-1] + S[b_comb[i][1]-1][b_comb[i][0]-1])

    # print(teamA,teamB)
    answer=min(answer,(abs(teamA-teamB)))

print(answer)