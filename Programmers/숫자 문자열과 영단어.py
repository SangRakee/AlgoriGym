# 구현 문제
# 딕셔너리에 key,value를 저장하여, 반분문을 통해 찾아서 변환하는 코드
# 다른 방법 : replace 함수를 이용하면 바꿀 문자를 쉽게 변경가능

def solution(s):
    answer = ""

    # 1.영단어별 딕셔너리 생성
    dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
            "eight": "8", "nine": "9"}

    temp = ""

    for i in s:
        # 2.s가 숫자일때 answer추가
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            answer += i
        # 3.s가 문자일때 temp 추가
        else:
            temp += i
            # 4.temp가 dict에 존재할시 value값 answerc추가
            if temp in dict:
                answer += dict[temp]
                temp = ""

    return int(answer)