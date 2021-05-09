def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = day * 55
    pattern = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    answer = day[sum(pattern[:a]) + b - 1]
    return answer