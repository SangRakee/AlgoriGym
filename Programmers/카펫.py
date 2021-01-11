def solution(numbers, target):
    cnt = 0

    def operator(numbers, idx):
        if idx < len(numbers):
            numbers[idx] *= 1
            operator(numbers, idx + 1)
            numbers[idx] *= -1
            operator(numbers, idx + 1)
        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1

    operator(numbers, 0)

    return cnt