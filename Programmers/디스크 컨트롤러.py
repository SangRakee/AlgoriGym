# 테스트 케이스 : jobs=[[0, 3], [1, 9], [2, 6]]

import heapq

def solution(jobs):
    count, last, answer = 0, -1, 0
    wait = []
    jobs.sort()
    print(jobs)
    # 시작시간 초기화
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(wait, (t, s))
                print(last, s, time, wait)
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(wait) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(wait)
            time += term
            answer += (time - start)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1
    return answer//len(jobs)
print(solution(jobs))