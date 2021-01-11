def solution(x):
    sum=0

    x=str(x)
    for i in range(len(x)):
        sum+=int(x[i])
    x=int(x)
    
    if x%sum==0:
        return True
    else:
        return False