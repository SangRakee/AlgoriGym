#테스트케이스 p="()))((()"

#uv로 나누는 함수
def uvDivide(p):
    u,v='',''
    lcnt,rcnt=0,0 #균형 잡힌 문자열인지 판단하는 변수

    #uv 균형잡힌 문자로 반환
    for i in range(len(p)): # u분리 for문
        if p[i]=='(':
            u+=p[i]
            lcnt+=1
        elif p[i]==')':
            u+=p[i]
            rcnt+=1
        if lcnt==rcnt:
            cnt=i+1
            break
    for i in range(cnt, len(p)): # v분리 for문
        v += p[i]

    return u,v


    #u가 올바른 관호 문자열이라면 다시 재귀

#올바른 괄호 문자열 판단 함수
def isRight(p):
    result=[]

    for i in range(len(p)):
        if i==0:  #첫번째
            if p[i]==')':
                return 0
            else:
                result.append(p[i])
        else:  #두번째부터
            if p[i]=='(':
                result.append(p[i])
            else:
                if result[-1]=='(':  # ()이 성립했을때
                    result.pop()
                else:
                    result.append(p[i])

    if len(result) == 0:
        return 1
    else:
        return 0

def reverse(u):
    u=list(u)
    u.pop(0)
    u.pop()
    tmp=[]
    for i in u:
        if i=='(':
            tmp.append(")")
        else:
            tmp.append('(')
    return ''.join(tmp)


def solution(p):
    # 빈 문자일 경우 빈문자열로 반환
    if len(p) == 0:
        return ''

    u,v=uvDivide(p)
    print('u',u)
    print('v',v)

    tmpV,tmpU='',''

    if isRight(u)==1:
        v=solution(v)
        u=u+v

    else:
        tmp='('
        v=solution(v)
        tmp+=v+')'
        u=tmp+reverse(u)

    return u

print(solution(p))