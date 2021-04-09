def solution(nums):
    answer = 0

    if len(nums)//2 <len(set(nums)):
        answer=len(nums)//2
    else:
        answer=len(set(nums))

    return answer