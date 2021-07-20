# 2pointer 문제
# 두 배열에서의 포인트 문제
# 각 각의 배열에서 모든 경우의 부분합을 구한다음에 그 구한 부분합에서 투 포인트를 사용하는 문제

import sys

answer=0

T=int(sys.stdin.readline())

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
A=[]

m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
B=[]

left=0
right=0

for i in range(n):
    temp=a[i]
    A.append(temp)
    for j in range(i+1,n):
        temp+=a[j]
        A.append(temp)

for i in range(m):
    temp=0
    for j in range(i,m):
        temp+=b[j]
        B.append(temp)
A.sort()
B.sort(reverse=True)


PointA=0
PointB=0
sumValue=A[PointA]+B[PointB]
A_cnt=1
B_cnt=1

while PointA<len(A) and PointB<len(B):

    currentA=A[PointA]
    target=T-currentA

    if B[PointB]>target:
        PointB+=1
    elif B[PointB]<target:
        PointA+=1
    else:
        checkA=0
        checkB=0
        while PointA<len(A) and A[PointA]==currentA:
            PointA+=1
            checkA+=1
        while PointB<len(B) and B[PointB]==target:
            PointB+=1
            checkB+=1
        answer+=checkA*checkB

print(answer)