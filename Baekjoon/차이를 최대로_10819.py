from itertools import permutations
N = int(input())

nums = permutations(list(map(int, input().split())))

ans = []

for i in nums:
    sum = 0
    for j in range(N-1):
        sum += abs(i[j] - i[j+1])

    ans.append(sum)
print(max(ans))