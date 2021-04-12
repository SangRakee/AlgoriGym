N=list(map(int,input().split(" ")))

def solution(N):
    N_min = min(N)


    while 1:
        cnt = 0
        for i in range(len(N)):
            if N_min%N[i]==0:
                cnt+=1
            if cnt >= 3:
                return N_min

        N_min+=1

print(solution(N))