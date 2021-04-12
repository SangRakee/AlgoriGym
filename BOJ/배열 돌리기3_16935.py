n,m,r=map(int,input().split())
arr=[]
swap_arr=[]


for i in range(n):
    x=list(map(int,input().split()))
    arr.append(x)
o_arr=list(map(int,input().split()))

def func(o,arr):
    if o==1:
        for i in range(len(arr)//2):
            arr=arr[::-1]
    elif o==2:
        for i in range(len(arr)):
            arr[i]=arr[i][::-1]
    elif o==3:
        change_arr=[list(row)[::-1] for row in zip(*arr)]
        arr=change_arr
    elif o==4:
        change_arr=[list(row) for row in list(zip(*arr))[::-1]]
        arr = change_arr
    elif o==5:
        change_arr = [[0] * m for i in range(n)]
        for i in range(n//2):
            for j in range(m//2):
                change_arr[i][m//2+j]=arr[i][j]
        for i in range(n//2):
            for j in range(m//2,m):
                change_arr[n//2+i][j]=arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2,m):
                change_arr[i][j-m//2]=arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2):
                change_arr[i-n//2][j]=arr[i][j]
        arr = change_arr
    elif o==6:
        change_arr = [[0] * m for i in range(n)]
        for i in range(n//2):
            for j in range(m//2):
                change_arr[n//2+i][j]=arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2):
                change_arr[i][j+m//2]=arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2,m):
                change_arr[i-n//2][j]=arr[i][j]
        for i in range(n//2):
            for j in range(m//2,m):
                change_arr[i][j-m//2]=arr[i][j]
        arr = change_arr

for op in o_arr:
    func(op,arr)

for e in arr:
    print(*e)


