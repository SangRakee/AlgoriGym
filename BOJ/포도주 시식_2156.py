# DP 문제
# 계단 오르기랑 비슷한 문제
# 1: 1
# 2: 12
# 3: 12, 23, 13
# 4: 124, 134
# 5: 1245, 235

import sys

N=int(sys.stdin.readline())
arr=[0]*10001
dp=[0]*10001

for i in range(1,N+1):
    arr[i]=int(sys.stdin.readline())

dp[1]=arr[1]
dp[2]=arr[1]+arr[2]
dp[3]=max(dp[2],arr[2]+arr[3],arr[1]+arr[3])

for i in range(4,N+1):
    dp[i]=max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i],dp[i-1])

print(dp[N])

