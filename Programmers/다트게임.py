def solution(dartResult):
    answer = []
    result=0

    arr=[]
    x=""
    for i in dartResult:
        if i in ["S","D","T","*","#"]:
            if x!="":
                arr.append(x)
                x=""
            arr.append(i)
        else:
            x+=i
    temp=0
    print(arr)
    for i in arr:
        if i in ["0","1","2","3","4","5","6","7","8","9","10"]:
            if temp!=0:
                answer.append(temp)
                temp=0
            temp+=int(i)
        elif i in ["S","D","T"]:
            if i == "S":
                temp=temp**1
            elif i == "D":
                temp=temp**2
            elif i == "T":
                temp=temp**3
        elif i in ["*","#"]:
            if i == "*":
                temp=temp*2
                if answer:
                    answer[-1]=answer[-1]*2
            elif i == "#":
                temp=temp*(-1)
    else:
        if temp != 0:
            answer.append(temp)
    for i in answer:
        result+=i

    return result

print(solution("1S*2T*3S"))



