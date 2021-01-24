x=input()
N=int(input())
arr=[]

cnt=0

for i in range(N):
    arr.append(2*input())

for i in arr:
    if x in i:
        cnt+=1

print(cnt)