# 1.장르별로 total 구하기
# 2.각 장르별로 각 정렬된 리스트 만들기
# 3.각 리스트의 2번때 인덱스까지 출력
def solution(genres, plays):
    answer = []

    # 1.장르별로 total 구하기
    dict = {}
    # 장르별로 total 구하는 반복문
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
        else:
            dict[genres[i]] = plays[i]

    # 딕셔너리를 리스트 형태로 바꾼 후 정렬하는 코드
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    genre_count = len(dict)

    arr = []

    # 2.각 장르별로 각 정렬된 리스트 만들기
    for genre in dict:
        temp = []
        for i in range(len(genres)):
            # print(genres[i], genre[0])
            if genres[i] == genre[0]:
                temp.append([i, plays[i]])
        temp.sort(reverse=True, key=lambda x: x[1])
        arr.append(temp)
    print(arr)
    # print(len(arr))

    # 3.각 리스트의 2번때 인덱스까지 출력
    for i in arr:
        # print(i)
        for j in range(2):
            try:  # 장르가 두개 이상 없는 경우 예외처리문
                print(i[j])
                answer.append(i[j][0])
            except IndexError:
                break

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))