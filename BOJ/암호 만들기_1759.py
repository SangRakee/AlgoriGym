#백트래킹

import sys

def dfs(start):

    # 목적지인가
    if len(result)==L:
        vo=0
        co=0
        for i in result:
            if i in ["a","e","i","o","u"]:
                vo+=1
            else:
                co+=1
        if vo>=1 and co>=2:
            temp="".join(result)
            print(temp)
        return

    # 갈 수 있는 곳 순회
    for i in range(start,M):
        # 갈 수 있는가
        if visited[i]==0:
            # 체크인
            result.append(C[i])
            visited[i] = 1
            # 간다
            dfs(i+1,visited,result)
            # 체크아웃
            visited[i]=0
            result.pop()

L,M=map(int,sys.stdin.readline().split())
C=list(sys.stdin.readline().split())
C.sort()
answer=[]


result = []
visited = [0] * (len(C))
dfs(0)



