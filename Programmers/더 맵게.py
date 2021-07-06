#heap 문제
#heapsort를 직접 구현할 수도 있고 heapify 내장 함수로 쉽게 만들 수도 있다.

import heapq

def heapsort(scoville):
    h=[]
    result=[]
    for i in scoville:
        heapq.heappush(h,i)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def solution(scoville, K):
    answer = 0
    # heapq.heapify(scoville)
    heapsort(scoville)
    
    while scoville[0]<K:
        if len(scoville)<=1:
            return -1
        new=heapq.heappop(scoville)+(heapq.heappop(scoville))*2
        heapq.heappush(scoville,new)
        answer+=1
        
    return answer