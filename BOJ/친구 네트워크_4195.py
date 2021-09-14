# 유니온파인 문제
# 기본적인 parent형태가 정수형이 아닌 문자형으로 딕셔너리 형태로 구현

import sys

def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    pa=find(a)
    pb=find(b)
    parent[pb]=pa
    number[pa]+=number[pb]

T=int(sys.stdin.readline())
for i in range(T):
    parent = {}
    number = {}
    F = int(sys.stdin.readline())
    for j in range(F):
        a,b=map(str,sys.stdin.readline().split())
        if a not in parent:
            parent[a]=a
            number[a]=1
        if b not in parent:
            parent[b]=b
            number[b]=1
        if find(a)!=find(b):
            union(a,b)
        print(number[find(a)])
# print(parent)
# print(number)
