# 1.dfs
#
result=[]
def dfs(begin, tickets, visited, path):
    if len(path) == len(tickets) + 1:
        print(path)
        result.append(path[:])
        return

    for ticket in range(len(tickets)):
        if visited[ticket] == 0 and tickets[ticket][0] == begin:
            visited[ticket] = 1
            begin = tickets[ticket][1]
            path.append(begin)
            dfs(begin, tickets, visited, path)
            begin=tickets[ticket][0]
            path.pop()
            visited[ticket] = 0


def solution(tickets):
    # answer = []
    visited = [0] * len(tickets)

    path = ["ICN"]
    begin = "ICN"
    dfs(begin, tickets, visited, path)
    print("result :",result)
    result.sort()

    return result[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))