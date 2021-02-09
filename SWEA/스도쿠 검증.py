sudoku=[]

for i in range(9):
    x=list(map(int,input().split()))
    sudoku.append(x)

def hori(sudoku):
    for i in range(9):
        if sum(sudoku[i])!=45:
            return False

    return True


def vert(sudoku):
    for i in range(9):
        for j in range(9):
            cnt=0
            for k in range(9):
                cnt += sudoku[k][j]
            if cnt != 45:
                return False

    return True

def bythree(sudoku):
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            cnt=0
            for i in range(3):
                for j in range(3):
                    cnt+=sudoku[i+x][j+y]
            if cnt!=45:
                return False
    return True


if hori(sudoku)==True and vert(sudoku)==True and bythree(sudoku)==True:
    print("#"+str(test_case),str(1))
else:
    print("#"+str(test_case),str(0))



