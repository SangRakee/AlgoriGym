import sys

def binarySearch(card,sang):
    start=0
    finish=len(sang)-1

    while start<=finish:
        mid=(start+finish)//2

        if sang[mid]==card:
            return 1
        elif sang[mid]<card:
            start=mid+1
        else:
            finish=mid-1
    return 0

N=int(sys.stdin.readline())
sang=list(map(int,sys.stdin.readline().split()))

M=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().split()))

sang.sort()

result=[]
for card in cards:
    num=binarySearch(card,sang)
    result.append(num)

print(*result)