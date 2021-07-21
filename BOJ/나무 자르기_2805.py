# Parametric Search
# 파이썬 특성상 시간 초과나는 문제 pypy3로 하면 통과

import sys

N,M = map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))

start=0
end=max(tree)
mid=(0+end)//2

while True:
    temp=0
    for i in tree:
        if i-mid>0:
            temp+=(i-mid)

    if temp==M:
        break
    elif temp>M:
        start=mid+1
        temp=mid
        mid=(start+end)//2
    elif temp<M:
        end=mid-1
        mid=(start+end)//2
    if start>end:
        break
    # print(start,mid,end)
    # print(temp)

print(mid)
