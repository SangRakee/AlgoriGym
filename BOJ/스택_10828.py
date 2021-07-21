# Stack 문제
# 단순 스택 구현

import sys

N=int(sys.stdin.readline())
stack=[]

def push(stack,x):
    stack.append(x)
    return stack

def pop(stack):
    if stack:
        index=stack.pop()
        return index
    else:
        return -1

def size(stack):
    leng=len(stack)
    return leng

def empty(stack):
    if not stack:
        return 1
    else:
        return 0

def top(stack):
    if stack:
        return stack[-1]
    else:
        return -1

for i in range(N):
    x=list(map(str,sys.stdin.readline().split()))

    if x[0]=="push":
        push(stack,x[1])
    elif x[0]=="pop":
        print(pop(stack))
    elif x[0]=="size":
        print(size(stack))
    elif x[0]=="empty":
        print(empty(stack))
    elif x[0]=="top":
        print(top(stack))
