t=int(input())


for i in range(t):
    N, M = map(int, input().split())

    printList = list(map(int, input().split()))
    checkList = [0 for _ in range(N)]
    checkList[M] = 1

    count = 0
    while True:
        if printList[0] == max(printList):
            count += 1

            if checkList[0] != 1:
                del printList[0]
                del checkList[0]
            else:
                print(count)
                break
        else:
            printList.append(printList[0])
            checkList.append(checkList[0])
            del printList[0]
            del checkList[0]


