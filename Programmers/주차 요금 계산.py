# 구현 문제
# 해싱형태로 변환 후 계산하는 구현 문제

import math

def calculate(start, end):
    result = 0
    s_h, s_m = start.split(":")
    e_h, e_m = end.split(":")

    s_h, s_m = int(s_h), int(s_m)
    e_h, e_m = int(e_h), int(e_m)

    # 시간이 같은 경우
    if s_h == e_h:
        result = e_m - s_m

    # 다른 경우
    else:
        # 시작 분이 더 작을 경우
        if s_m <= e_m:
            result = e_m - s_m
            result = result + (60 * (e_h - s_h))

        # 클 경우
        else:
            result = 60 + e_m - s_m
            result = result + (60 * (e_h - s_h - 1))

    return result


def solution(fees, records):
    answer = []

    # 해싱 형태로 전환
    parking = {}
    fee = {}

    # 입출내역을 적는 해싱1
    for record in records:
        time, num, io = record.split()

        # dic에 num이 있는 경우
        if num in parking:
            # 시간 계산
            start = parking[num]
            end = time
            total = calculate(start, end)
            del parking[num]

            # 요금 해싱 저장
            if num in fee:
                fee[num] += total
            else:
                fee[num] = total

        # 없는 경우
        else:
            parking[num] = time

    # 출차 안된 차가 있는지 확인
    for key in parking.keys():
        start = parking[key]
        total = calculate(start, "23:59")

        # 요금 해싱 저장
        if key in fee:
            fee[key] += total
        else:
            fee[key] = total

    # 해싱2를 통해 요금 계산
    print(fee)
    sort_dict=sorted(fee.items())
    print(sort_dict)

    for num,time in sort_dict:
        print(num,time)
        if time<=fees[0]:
            answer.append(int(fees[1]))
        else:
            more=math.ceil((time-fees[0])/fees[2])*fees[3]
            answer.append(int(fees[1]+more))

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))