# 그래프 문제(서로소 집합)
# 유니온파인 구현

import sys

n,m = map(int,sys.stdin.readline().split())

parent=[0]


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


for i in range(1,n+1):
    parent.append(i)



for _ in range(m):
    type,a,b = map(int,sys.stdin.readline().split())
    if type==1: # 같은 집합인지 확인하는 경우 - find
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")
    elif type==0: # 합집합인 경우 - Union
        union(a,b)
    # print(parent)
