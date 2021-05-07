# from functools import cmp_to_key


# def comp(x, y):
#     if int(x + y) < int(y + x):
#         return True
#     elif int(x + y) == int(y + x):
#         return False
#     else:
#         return -1


# def solution(numbers):
#     answer = ""
#     num = []
#     for i in range(len(numbers)):
#         num.append(str(numbers[i]))

#     sorted_num = sorted(num, key=cmp_to_key(comp))

#     for i in range(len(sorted_num)):
#         answer += sorted_num[i]

#     answer = str(int(answer))
#     return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
