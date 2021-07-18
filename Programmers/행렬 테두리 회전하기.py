#배열 위치 옮기기
#기존 문제 방향대로 옮기면 겹치는 문제가 발생하여 반시계방향으로 시작해서 옮김

def solution(rows, columns, queries):
    answer = []

    matrix=[[0]*columns for i in range(rows)]

    idx=1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j]=idx
            idx+=1

    #하우상좌
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    for querie in queries:
        temp=[]
        x1,y1,x2,y2=map(lambda x:x-1,querie)  #matrix 인덱스가 (0,0)인 시작점을 맞추기 위해
        first=matrix[x1][y1]
        temp.append(first)
        nowX=x1
        nowY=y1
        # print(first)


        for k in range(4):
            while True:
                nextX = nowX + dx[k]
                nextY = nowY + dy[k]
                if nextX<x1 or nextX>x2 or nextY<y1 or nextY>y2:
                    break
                else:
                    matrix[nowX][nowY]=matrix[nextX][nextY]
                    nowX,nowY=nextX,nextY
                    temp.append(matrix[nextX][nextY])
        matrix[x1][y1+1]=first
        temp.append(first)
        print(temp)
        answer.append(min(temp))


    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))