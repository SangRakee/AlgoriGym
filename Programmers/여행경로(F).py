from _collections import deque

tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


def bfs(start,ticekets,visited,answer):

    for i in tickets:
        if i[0]=="ICN":
            queue = deque([i[1]])
            visited[tickets.index(i)]=1
            answer.append(i[0])
            answer.append(i[1])
            break

    while queue:
        start=queue.popleft()
        for i in tickets:
            if not visited[tickets.index(i)]:
                if i[0]==start:
                    queue.append(i[1])
                    visited[tickets.index(i)]=1
                    answer.append(i[1])
                    break
                    print(queue,visited)




def solution(tickets):
    answer = []
    tickets.sort()
    visited=[0]*(len(tickets))
    bfs("ICN",tickets,visited,answer)



    return answer



print(solution(tickets))