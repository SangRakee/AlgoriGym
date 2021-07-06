def solution(rows, columns, queries):
    answer = []

    # 리스트 만들기
    matrix = [[0] * (columns+1) for i in range(rows+1)]
    x = 0
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            x += 1
            matrix[i][j] = x

    #우하좌상
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]


    # queries마다 들어있는 값들 넣기
    for query in queries:
        tempArr=[]
        nowX,nowY=query[0],query[1] #시작 좌표
        for k in range(4):
            nextX=nowX+dx[k]
            nextY=nowY+dy[k]
            tempValue=-1
            while True:
                if query[0]<=nextX<query[2] or query[1]<=nextY<query[3]:
                    break
                else:
                    #옮기는 코드
                    
                    nowX,nowY=nextX,nextY
                    tempArr.append(matrix[nowX][nowY])


        # 최소값
        answer.append(min(tempArr))
 

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))