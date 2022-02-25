# 파이썬 자주 사용하는 유용한 코드

- n진수 -> 10진수

  ```python
  # int(string,진법)
  
  print(int('101',2))   # 5
  print(int('202',3))   # 20
  print(int('303',4))   # 51
  print(int('404',5))   # 104
  print(int('505',6))   # 185
  print(int('ACF',16))  # 2767
  ```

  



- 슬라이싱

  ```python
  list = [1,2,3,4,5,6,7]
  
  # 1번째 인덱스 부터
  list[1:] # 출력값 : 2,3,4,5,6,7
  
  # 5번째 인덱스 전까지(4번째 인덱스 까지)
  list[:5] # 출력값 : 1,2,3,4
  ```



- 문자열 변경

  ```python
  # 문자열.replace("찾을값","바꿀값",[바꿀 횟수],[바꿀 시작 위치])    
  # 바꿀시작위치(기본값: 좌측, -1:우측)
  
  text='123,456,789,999'
  
  text.replace(",","")     # 123456789999
  text.replace(",", "",1)  # 123456,789,999
  text.replace(",", "",2)  # 123456789,999
  text.replace(",", "",3)  # 123456789999
  ```




- 문자열 공백 및 특무 문자 제거

  ```python
  # strip("문자열")
  
  a=" python "
  
  # 공백 제거
  a.strip()  # "python"
  a.lstrip() # "python " 
  a.rstrip() # " python"
  ```

  



- 문자열 대소문자

  ```python
  a="python"
  A="PYTHON"
  
  # 1.대소문자 변환
  a.upper() # PYTHON
  A.lower() # python
  
  # 2.대소문자 판단
  print(a.isupper()) # False
  print(a.islower()) # True
  ```



- 문자열 찾기

  ```python
  # find("찾을 문자열")
  'apple pineapple'.find('pl') # 2
  
  # index("찾을 문자열")
  'apple pineapple'.index('pl') # 2
  
  # find, index 함수는 왼쪽부터 찾음(단, rfind(),rindex()를 통해 오른쪽부터 찾기 가능)
  # index는 찾을 문자열이 존재하지 않으면 에러 발생(find는 -1 반환)
  ```

  

- 문자열 개수 세기

  ```python
  # count("셀 문자열")
  'apple pineapple'.count('pl') # 2
  ```

  




- 리스트 출력시 대괄호 제거

  ```python
  result=[1,2,3]
  
  print(result)
  # [1,2,3]
  
  for i in range(len(result)):
      print(result[i], end=" ")
  # 1 2 3 
  # 단, 마지막 인덱스 출력 후에 공백 생성
  
  print(*result)
  # 1 2 3
  ```



- 깊은 복사

  ```python
  # 1차 행렬
  list1 = [a,b,c]
  list2 = list1[:]
  
  # 2차 행렬
  list1 = [[a,b],[c,d]]
  list2 = [i[:] for i in list1]
  
  
  import copy
  
  list2=copy.deepcopy(list1)
  ```




- 2차원 리스트 회전

  ```python
  # 반시계 90도 방향
  a = [i for i in list(zip(*a))[::-1]]
  
  # 시계 90도 방향
  a = [list(i)[::-1] for i in zip(*a)]
  ```
  




- 정렬

  ```python
  list=[[1,2],[2,3],[2,1]]
  
  list.sort(key=lambda x:x[1]) # i[1]번째 인덱스로 정렬
  
  list.sort(key=len) # 리스트 길이로 정렬
  ```



- 딕셔너리 

  ```python
  #딕셔너리 생성
  dict1={}
  dict2=dict()
  
  # 딕셔너리 삭제
  dict.pop(x) # x를 삭제 동시에 반환
  del dict(x) # x를 삭제
  
  # 딕셔너리.get() - 찾고자 하는 value가 없을때
  years={"a":2020, "b":2021}
  c=years.get("c","Nothing") # 찾고자하는 key가 존재하지 않을때 Nothing이라는 변수를 저장
  
  
  # 딕셔너리 정렬 - items() 함수를 이용하여 딕셔너리를 튜플 형태로 변환하는 방식
  	# 1.key 값으로 정렬
  dict = {'A' :1,'D' :4,'C' :3,'B' :2}
  sort_dict= sorted(dict.items()) # 딕셔너리를 튜플로 바꾼다음에 정렬
  
  	# 2.value 값으로 정렬
  dict = {'A' :1,'D' :4,'C' :3,'B' :2}
  sort_dict= sorted(dict.items(), key=lambda x:x[1][0]) #람다로 해당 value 위치 결정
  ```
  
  



- 리스트을 문자열로 변환

  ```python
  list=['a', 'b', 'c', 'd', '1', '2', '3']
  
  result1 = "".join(a) # 출력 : abcd123
  ```

  



- 예외 처리

  ```python
  try:
      # 실행 코드
  except ZeroDivisionError:  # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
      print('숫자를 0으로 나눌 수 없습니다.')
  except IndexError:         # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
      print('잘못된 인덱스입니다.')
  ```





- 리스트 원소들의 갯수

  ```python
  from collections import Counter
  
  list1=["a","b","c","a","a","b"]
  
  counter=Counter(list1)    # 출력 : Counter({"a":3,"b":2,"c":1})
  
  # Counter 내장함수
  # most_common(n)
  Counter(list1).most_common(1) # 출력 : [("a":3)]
  
  ```



- bisect 라이브러리

  ```python
  from bisect import bisect_left, bisect_right
  
  a = [1, 2, 4, 4, 8]
  
  print(bisect_left(a, 4))  #2
  print(bisect_right(a, 4))  #4
  ```

  

- extend

  ```python
  x = ["lee", "kim"]
  y = ["park", "choi"]
  x.append(y) # ["lee", "kim", ["park", "choi"]]
  x.extend(y) # ["lee", "kim", "park", "choi"]
  ```

  

- defaultdit 라이브러리

  ```python
  from collections import defaultdict
  
  d_dict = defaultdict(int)
  d_dict["a"]  # 0
  
  d_dict = defaultdict(lambda: 'default value')
  d_dict["a"]  # 'default value'
  ```




- 순열, 조합, 중복순열, 중복조합

  ```python
  from itertools import permutations # 순열
  from itertools import combinations # 조합
  from itertools import product # 중복순열
  from itertools import combinations_with_replacement # 중복조합
  
  arr = ['A', 'B', 'C']
  
  res = list(product(arr, repeat = 2)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
  
  res = list(combinations_with_replacement(arr, 2)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
  ```

  
