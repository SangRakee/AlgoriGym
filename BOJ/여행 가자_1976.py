# 유니온파인 문제

import sys


def find(a):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    # a랑 b를 하나로 합집합 하겠다
    pa=find(a)
    pb=find(b)
    parent[pb]=pa

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

parent=[]
for i in range(N+1):
    parent.append(i)

for i in range(1,N+1):
    x=list(map(int,sys.stdin.readline().split()))
    for j in range(len(x)):
        if x[j]==1:
            union(i,j+1)

answer=list(map(int,sys.stdin.read().split()))
flag=False
for i in range(1,len(answer)):
    if find(parent[answer[i-1]])==find(parent[answer[i]]):
        continue
    else:
        print("NO")
        exit(0)

print("YES")