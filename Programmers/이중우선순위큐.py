import heapq

def solution(operations):
    answer = []
    heap = []

    for i in operations:
        # 삽입하는 조건문
        if i[0] == "I":
            heapq.heappush(heap, int(i[2:]))
        elif i[0] == "D":
            # 최댓값 삭제 조건문
            if i[2] == "-":
                if heap:
                    heapq.heappop(heap)
            # 최소값 삭제 조건문
            else:
                if heap:
                    heap.pop()
        # print("heap :",heap)
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
        return answer
    else:
        return [0,0]


print(solution(["I 7","I 5","I -5","D -1"]))