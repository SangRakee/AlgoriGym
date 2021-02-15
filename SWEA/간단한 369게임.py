N = int(input())
arr = [str(i) for i in range(1, N+1)]

for num in arr:
    cnt = 0
    if '3' in num:
        cnt += num.count('3')
    if '6' in num:
        cnt += num.count('6')
    if '9' in num:
        cnt += num.count('9')
    if cnt > 0:
        print('-'*cnt, end=' ')
    else:
        print(num, end=' ')
