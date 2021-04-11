# 몫,나머지 = divmod(n,값)
# int(숫자,n진수로 바꿀 변수) 로 하면 변환됨

# 테스트케이스
n=45

def solution(n):
    answer = 0
    number=''

    while n>0:
        q=n//3
        r=n%3
        number=number+str(r)
        n=q


    return int(number,3)

print(solution(n))