# 구현
# 삼성 기출

import sys
from itertools import permutations


def check(x,y,op):
    num=0

    if op=="*":
        num=x*y
    elif op=="/":
        if x<0 and y<0:
            x=abs(x)
            y=abs(y)
            num=x//y
        elif x<0:
            x=abs(x)
            num=x//y
            num=(-num)
        else:
            num=x//y
    elif op=="+":
        num=x+y
    elif op=="-":
        num=x-y

    return num



N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

a,b,c,d=map(int,sys.stdin.readline().split())

oper=[]
for i in range(a):
    oper.append("+")
for i in range(b):
    oper.append("-")
for i in range(c):
    oper.append("*")
for i in range(d):
    oper.append("/")

# print(oper)
leng=len(oper)
perm_list=list(permutations(oper,leng))

answer=[]
stack=[]
for perm in perm_list:
    num=0
    for i in range(len(A)-1):
        if i==0:
            num=check(A[i],A[i+1],perm[i])
        else:
            num=check(num,A[i+1],perm[i])
    answer.append(num)

print(max(answer))
print(min(answer))


