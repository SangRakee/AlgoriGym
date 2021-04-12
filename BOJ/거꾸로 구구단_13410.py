N,K = input().split()
arr=[]

for i in range(1,int(K)+1):
    cnt=str(int(N)*i)
    answer = cnt
    answer = list(answer)
    cnt = list(cnt)
    if len(cnt)>=2:
        for j in range(len(cnt)//2):
            answer[-1-j]=cnt[0+j]
            answer[0+j]=cnt[-1-j]
            print(j,"번째",cnt, answer)
    arr.append("".join(answer))
    arr=list(map(int,arr))
print(arr)
print(max(arr))