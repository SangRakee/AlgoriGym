# 구현 문제
# LRU 알고리즘


from collections import deque


def solution(cacheSize, cities):
    answer = 0
    queue = deque([])

    if cacheSize==0:
        answer=len(cities)*5
        return answer

    for city in cities:
        # 1.도시 이름 소문자로 변경
        city = city.lower()
        # 2.캐시 공간이 남아있을때
        if len(queue) < cacheSize:
            # 2-2. 기존에 있던 데이터인지
            if city in queue:
                answer += 1
                queue.remove(city)
                queue.append(city)

            # 2-3. 기존에 없던 데이터인지
            else:
                answer += 5
                queue.append(city)

        # 3.캐시 공간이 꽉찰때
        else:
            # 3-2. 기존에 있던 데이터인지
            if city in queue:
                answer+=1
                queue.remove(city)
                queue.append(city)

            # 3-3. 기존에 없던 데이터인지
            else:
                answer+=5
                queue.popleft()
                queue.append(city)

    return answer

print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	))