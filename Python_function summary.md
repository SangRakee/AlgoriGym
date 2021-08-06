# 파이썬 자주 사용하는 유용한 코드

- 슬라이싱

  ```python
  list = [1,2,3,4,5,6,7]
  
  # 1번째 인덱스 부터
  list[1:] # 출력값 : 2,3,4,5,6,7
  
  # 5번째 인덱스 전까지(4번째 인덱스 까지)
  list[:5] # 출력값 : 1,2,3,4
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



- 문자열 변경

  ```python
  # 문자열.replace("찾을값","바꿀값",[바꿀 횟수],[바꿀 시작 위치])    # 바꿀시작위치(기본값: 좌측, -1:우측)
  
  text='123,456,789,999'
  
  replaceAll= text.replace(",","")
  replace_t1 = text.replace(",", "",1)
  replace_t2 = text.replace(",", "",2)
  replace_t3 = text.replace(",", "",3)
  print("결과 :")
  print(replaceAll)
  print(replace_t1)
  print(replace_t2)
  print(replace_t3)
  
  '''
  결과 : 
  123456789999
  123456,789,999
  123456789,999
  123456789999
  '''
  ```

  



- 깊은 복사

  ```python
  # 1차 행렬
  list1 = [a,b,c]
  list2 = list1[:]
  
  # 2차 행렬
  list1 = [[a,b],[c,d]]
  list2 = [i[:] for i in list1]
  ```

  

- 정렬

  ```python
  list=[[1,2],[2,3],[2,1]]
  
  list.sort(key=lambda x:x[1]) # i[1]번째 인덱스로 정렬
  ```



- 딕셔너리 정렬

  ```python
  dict={}
  
  change1_dict=sorted(dict.item()) # 리스트로 변환 후 정렬
  change2_dict=sorted(dict.item(), key=lambda x:x[n]) # 리스트로 변환 후 n번째 인덱스 순으로 정렬
  
  #딕셔너리 삭제
  dict.pop(x) # x를 삭제 동시에 반환
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

  

- 딕셔너리 정렬

  ```python
  # item 함수를 이용하여 딕셔너리를 튜플 형태로 변환하는 방식
  
  # key 값으로 정렬
  dict = {'A' :1,'D' :4,'C' :3,'B' :2}
  sort_dict= sorted(dict.items()) # 딕셔너리를 튜플로 바꾼다음에 정렬
  
  # value 값으로 정렬
  dict = {'A' :1,'D' :4,'C' :3,'B' :2}
  sort_dict= sorted(dict.items(), key=lambda x:x[1][0]) #람다로 해당 value 위치 결정
  
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



