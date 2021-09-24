# 위상정렬

import sys
from collections import deque



N=int(sys.stdin.readline())
names=sorted(list(map(str,sys.stdin.readline().split())))


M=int(sys.stdin.readline())

outdegree={}
indegree={}
answer={}
for name in names:
    outdegree[name]=[]
    indegree[name]=[]
    answer[name]=[]

for _ in range(M):
    x,y=map(str,sys.stdin.readline().split())
    outdegree[x].append(y)
    indegree[y].append(x)

K=0
K_list=[]
for i in outdegree:
    if len(outdegree[i])==0:
        K+=1
        K_list.append(i)

print(outdegree)
# print(indegree)

queue=deque([])
for o in outdegree:
    if len(outdegree[o])==0:
        queue.append(o)

# print()
while queue:
    now=queue.popleft()
    outdegree.pop(now)

    for j in indegree[now]:
        # if len(indegree[j])!=0:
        # answer[now].append(j)
        outdegree[j].remove(now)
        if len(outdegree[j]) == 0:
            answer[now].append(j)
            queue.append(j)
    # print(outdegree)

print(K)
print(*K_list)
# print(answer)
for i in answer:
    if len(answer[i])>0:
        print(i,len(answer[i]),*sorted(answer[i]))
    else:
        print(i,len(answer[i]))

