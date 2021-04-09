# sort(key=lamda x:x[n])

# 테스트케이스
# strings=["abce", "abcd", "cdx"]
# n=2

def solution(strings, n):
    answer = []
    strings.sort()
    strings.sort(key=lambda x:x[n])

    return strings

print(solution(strings,n))