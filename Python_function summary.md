# 파이썬 자주 사용하는 유용한 코드

- 슬라이싱

  ```python
  list = [1,2,3,4,5,6,7]
  
  # 1번째 인덱스 부터
  list[1:] # 출력값 : 2,3,4,5,6,7
  
  # 5번째 인덱스 전까지(4번째 인덱스 까지)
  list[:5] # 출력값 : 1,2,3,4
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

  