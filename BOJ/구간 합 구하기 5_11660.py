# dp를 활용한 누적합2
# 정말 구현적인 측면에서 머리 아프게 했던 문제
# 리스트가 (0,0)부터 시작하기 때문에 indexError에 대한 예외처리를 해줘야함
# 밑에 코드는 리스트가 (1,1)부터 시작하게 구현

import sys

N,M=map(int,sys.stdin.readline().split())

num=[]
for i in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    num.append(x)

# print(num)
dp=[i[:] for i in num] # 깊은 복사

# 누적합 구하기
for i in range(len(num)):
    for j in range(len(num)):
        if i==0 and j==0:
            continue
        elif i==0:
            dp[i][j]+=dp[i][j-1]
        elif j==0:
            dp[i][j]+=dp[i-1][j]
        else:
            dp[i][j]+=dp[i-1][j]+sum(num[i][:j])

# print(dp)

# 범위에 따른 누적합 뽑기
for i in range(M):
    # x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    x1, y1, x2, y2 = map(lambda x: x - 1, map(int, sys.stdin.readline().split()))
    # print(x1,y1,x2,y2)

    # ans=dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

    # 첫 행, 첫 열
    if y1 == 0 and x1 == 0:
        ans = dp[x2][y2]
    # 첫 행
    elif x1 == 0:
        ans = dp[x2][y2] - dp[x2][y1 - 1]
    # 첫 열
    elif y1 == 0:
        ans = dp[x2][y2] - dp[x1 - 1][y2]
    # 나머지 경우
    else:
        ans = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(ans)
    
    
    
# 다른 코드
# N,M = map(int,sys.stdin.readline().split())
# num_list = []
# dp = [[0]*(N+1) for _ in range(N+1)]
# 
# 
# for _ in range(N):
#     c = list(map(int,sys.stdin.readline().split()))
#     num_list.append(c)
# print(num_list)
# 
# for i in range(N):
#     for j in range(N):
#         dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + num_list[i][j] - dp[i][j]
# 
# for _ in range(M):
#     x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
#     print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])