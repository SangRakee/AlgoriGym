# DP 문제

# 1: p1
# 2: dp[1]+p1, p0p2
# 3: dp[2]+p1, p1p2, p0p3
# 4: P1P1P1P1, P2P2, P1P3, P0P4

import sys

N=int(sys.stdin.readline())
P=[0]+list(map(int,sys.stdin.readline().split()))
dp=[0]*(N+1)

dp[1]=P[1]

for i in range(2,N+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i-j]+P[j],dp[i])

print(dp[N])


