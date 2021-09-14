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

T=int(sys.stdin.readline())

for t in range(1,T+1):
    print('Scenario %d:' %(t))
    n=int(sys.stdin.readline())
    parent=[]
    for i in range(n+1):
        parent.append(i)

    k=int(sys.stdin.readline())
    for i in range(k):
        a,b=map(int,sys.stdin.readline().split())
        union(a,b)

    m=int(sys.stdin.readline())
    for i in range(m):
        u,v=map(int,sys.stdin.readline().split())

        if find(u)==find(v):
            print(1)
        else:
            print(0)

    print()


