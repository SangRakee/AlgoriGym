# 구현
# 삼성 기출

import sys

def row_check(x):
    visited=[0]*N

    for i in range(N-1):
        if maps[x][i]==maps[x][i+1]:
            continue
        elif (maps[x][i]+1)==maps[x][i+1]:
            tmp=maps[x][i]
            # visited[i]=1
            for j in range(i,i-L,-1):
                if 0<=j<N:
                    if tmp!=maps[x][j]:
                        return False
                    if visited[j]==0:
                        visited[j]=1
                    else:
                        return False
                else:
                    return False

        elif maps[x][i] == (maps[x][i+1]+1):
            tmp = maps[x][i + 1]
            # visited[i]=1
            for j in range(i+1, i+L+1):
                if 0 <= j < N:
                    if tmp != maps[x][j]:
                        return False
                    if visited[j]==0:
                        visited[j]=1
                    else:
                        return False
                else:
                    return False

        else:
            return False

    return True

def col_check(x):
    visited=[0]*N

    for i in range(N-1):
        if maps[i][x]==maps[i+1][x]:
            continue
        elif (maps[i][x]+1)==maps[i+1][x]:
            tmp=maps[i][x]
            # visited[i]=1
            for j in range(i,i-L,-1):
                if 0<=j<N:
                    if tmp!=maps[j][x]:
                        return False
                    if visited[j]==0:
                        visited[j]=1
                    else:
                        return False
                else:
                    return False

        elif maps[i][x] == (maps[i+1][x]+1):
            tmp = maps[i+1][x]
            # visited[i]=1
            for j in range(i+1, i+L+1):
                if 0 <= j < N:
                    if tmp != maps[j][x]:
                        return False
                    if visited[j]==0:
                        visited[j]=1
                    else:
                        return False
                else:
                    return False

        else:
            return False

    return True


# 입력
N,L=map(int,sys.stdin.readline().split())

maps=[]
for i in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    maps.append(x)

answer=0
for i in range(N):
    if row_check(i):
        answer+=1
    if col_check(i):
        answer+=1



print(answer)