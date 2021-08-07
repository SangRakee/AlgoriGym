import sys

N=int(sys.stdin.readline())
tower=list(map(int,sys.stdin.readline().split()))

result=[]
stack=[]

for i in range(len(tower)):
    # 스택이 비어있을때
    if not stack:
        result.append(0)
        stack.append((tower[i],i+1))

    # 스택이 비어있지 않을때
    else:
        #top과 i 비교
        if stack[-1][0]>=tower[i]:
        # top이 클시
            result.append(stack[-1][1])
            # result에 top 인덱스 위치
            stack.append((tower[i],i+1))
            # i를 push


        # i가 클때
        elif stack[-1][0]<tower[i]:
            while True:
                stack.pop()
                if not stack:
                    result.append(0)
                    stack.append((tower[i],i+1))
                    break
                if stack[-1][0]>=tower[i]:
                    result.append(stack[-1][1])
                    stack.append((tower[i], i + 1))
                    break


print(*result)

