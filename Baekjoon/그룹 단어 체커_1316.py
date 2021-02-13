def check(word):
    chk=[]

    for i in range(len(word)):
        if word[i] in chk and word[i] != chk[-1]:
            return False
        else:
            chk.append(word[i])

    return True

n=int(input())
arr=[]
for i in range(n):
    x=input()
    arr.append(x)

answer=0

for i in range(n):
    if check(arr[i]) == True:
        answer+=1

print(answer)