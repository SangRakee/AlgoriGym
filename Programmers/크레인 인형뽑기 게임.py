board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]


def solution(board, moves):
    answer = 0
    basket=[0]

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]==0:
                continue
            if basket[-1]==board[j][i-1]:
                answer+=1
                basket.pop()
            else:
                basket.append(board[j][i-1])
            board[j][i - 1]=0
            break

    return answer*2

print(solution(board,moves))