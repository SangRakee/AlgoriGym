arr=list(input())
answer=0
stack=[]
prev=None

for i in range(len(arr)):
    if arr[i]=='(':
        stack.append('(')
    else:
        if prev=='(':
            stack.pop()
            answer+=len(stack)
        else:
            stack.pop()
            answer+=1
    prev=arr[i]
print(answer)