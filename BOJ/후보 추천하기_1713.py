#구현 문제
#딕셔너리 사용
#밑에 주석처리 반복문은 처음 조건이 딕셔너리가 해당 크기이상일때 먼저 판단하는 것

import sys

N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

picture={}

for i in range(len(arr)):
    if arr[i] in picture:
        picture[arr[i]][0]+=1
    else:
        if len(picture) < N:
            picture[arr[i]] = [1, i]
        else:
            del_picture=sorted(picture.items(),key=lambda x:x[1][0])
            # print(del_picture)
            del_key=del_picture[0][0]
            picture.pop(del_key)
            picture[arr[i]] = [1, i]

result=sorted(picture.keys())
for i in result:
    print(i, end=" ")

# for i in range(len(arr)):
#     if len(picture)<N:
#         if arr[i] not in picture:
#             picture[arr[i]]=[1,i]
#         else:
#             picture[arr[i]][0]+=1
#     else:
#         if arr[i] not in picture:
#             del_picture=sorted(picture.items(),key=lambda x:x[1][1])
#             del_key=del_picture[0][0]
#             picture.pop(del_key)
#             picture[arr[i]]=[1,i]
#         else:
#             picture[arr[i]][0]+=1