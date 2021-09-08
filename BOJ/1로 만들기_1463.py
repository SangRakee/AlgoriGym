# DP 문제
# 3,2로 나눠지는걸 elif문이 아닌 각각의 조건에 if문을 해줘야 한다
# 또한, DP문제의 경우, 처음 리스트이 크기를 잘 지정해줘야한다(런타임에러)

import sys

N=int(sys.stdin.readline())

dp=[0]*(N+2)

dp[1]=0
dp[2]=1

for i in range(3,N+1):

    dp[i]=dp[i-1]+1
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0:
        dp[i] = min(dp[i],dp[i//2]+1)


print(dp[N])