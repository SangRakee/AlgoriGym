n=6
times=[7, 10]


def solution(n, times):
    ## 최악의 경우: 가장 비효율적인 심사관에게 다 받는 경우의 시간.
    left =0
    right = max(times) * n
    answer = 0
    while left <= right:
        # 한 심사관에게 주어진 시간
        mid = (left + right) // 2
        people = 0
        for i in times:
          # 각 심사관마다, 주어진 시간 동안 몇 명의 사람을 심사할 수 있는지
            people += mid // i
            # 모든 사람을 심사할 수 있으면 시간을 줄여본다
            if people >= n:
                answer = mid
                right = mid - 1
                break
        # 모든 사람을 심사할 수 없는 경우
        # 한 심사관에게 주어진 시간을 늘려본다.
        if people < n :
            left = mid + 1
    return answer


print(solution(n,times))


