# DP 문제
# 계단오르는 점화식(연속3칸 이동x)
# 1 : 1(10)
# 2 : 12(30)
# 3 : 13(30), 23(35)
# 4 : 134(50), 124(55)
# 5 : 1245(65), 135(35)

import sys

N=int(sys.stdin.readline())
arr=[0]*301
for i in range(N):
    x=int(sys.stdin.readline())
    arr[i+1]=x

dp=[0]*301

dp[1]=arr[1]
dp[2]=arr[1]+arr[2]
dp[3]=max(arr[1]+arr[3],arr[2]+arr[3])

for i in range(4,N+1):
    dp[i]=max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])

print(dp[N])

