## NumPy array
  - 대량의 숫자 data를 하나의 변수에 넣고 관리할 때 list는 속도가 느리고 memory를 많이 차지하는 단점
  - 배열(array)을 사용하면 적은 memory로 많은 data를 빠르게 처리 가능
  - array는 list와 비슷하지만 다음과 같은 점에서 차이
    - 모든 원소가 같은 자료형이어야 함
    - 원소의 갯수를 바꿀 수 없음
  - python은 자체적으로 array 자료형을 제공하지 않아서, array를 구현한 다른 package를 import 해야 함
    - python에서 array를 사용하기 위한 standard package는 넘파이(NumPy)
  - NumPy는 수치해석용 python package
    - 다차원의 array 자료구조 class인 `ndarray` class를 지원하며 vector와 행렬을 사용하는 선형대수 계산에 주로 사용
    - NumPy의 array 연산은 C로 구현된 내부 반복문을 사용하기 때문에 python 반복문에 비해 속도가 빠름
    - vectorized operation을 이용하여 간단하게 복잡한 선형 대수 연산 수행 가능
    - array indexing을 사용한 query 기능으로 쉽게 복잡한 수식 계산 가능

## NumPy package import
  - ```py
    import numpy as np
    ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ar # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    type(ar) # numpy.ndarray
    
## 벡터화 연산 (vectorized operation)
  - array의 각 원소에 대한 반복 연산을 하나의 명령어로 처리하는 vectorized operation을 지원
  - ```py
    # 이 코드를
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = []
    for di in data:
        answer.append(2 * di)
    answer # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    
    # 이렇게 바꿀 수 있다
    x = np.array(data)
    2 * x # array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
    
    # 참고로 list 객체에 정수를 곱하면 객체의 크기가 정수배 만큼 증가
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(2 * L) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    ## 벡터화 연산은 이런 것도 다 됨
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])
    2 * a + b           # array([12, 24, 36])
    a == 2              # array([False,  True, False])
    b > 10              # array([False,  True,  True])
    (a == 2) & (b > 10) # array([False,  True, False])
    
## 2-dimensional array
  - `ndarray`는 N-dimensional Array의 약자
  - 2차원, 3차원 배열 등 다차원 배열 자료 구조 지원
  - 2차원 배열은 행렬(matrix)이라고 하고, 가로줄을 행(row), 세로줄을 열(column)이라 부름
  - list of list를 이옹하면 2차원 배열 생성 가능
    - 안쪽 list의 길이는 행렬의 열의 수 (가로 크기)
    - 바깥쪽 list의 길이는 행렬의 행의 수 (세로 크기)
    - ```py
      c = np.array([[0, 1, 2], [3, 4, 5]])  # 2 x 3 array
      c
      # array([[0, 1, 2],
      #        [3, 4, 5]])
      len(c)    # 2 (행의 갯수)
      len(c[0]) # 3 (열의 갯수)

## 배열의 차원과 크기
  - ```py
    print(a.ndim)  # 1
    print(a.shape) # (3,)
    
    print(c.ndim)  # 2
    print(c.shape) # (2, 3)
    
    d = np.array([[[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]],
                  [[11, 12, 13, 14],
                   [15, 16, 17, 18],
                   [19, 20, 21, 22]]])
    print(d.ndim)  # 3
    print(d.shape) # (2, 3, 4)
    
## indexing
  - ```py
    a = np.array([0, 1, 2, 3, 4])
    a[2] # 2
    a[-1] # 4
    a = np.array([[0, 1, 2], [3, 4, 5]])
    a[0, 0]   # 0 (첫번째 행의 첫번째 열)
    a[0, 1]   # 1 (첫번째 행의 두번째 열)
    a[-1, -1] # 5 (마지막 행의 마지막 열)
    
## array slicing
  - ```py
    a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    a
    # array([[0, 1, 2, 3],
    #        [4, 5, 6, 7]])
    
    a[0, :]  # array([0, 1, 2, 3]) (첫번째 행 전체)
    a[:, 1]  # array([1, 5]) (두번째 열 전체)
    a[1, 1:] # array([5, 6, 7]) (두번째 행의 두번째 열부터 끝열까지)
    a[:2, :2]
    # array([[0, 1],
    #        [4, 5]])
    
## array indexing (fancy indexing, Qeury)
  - ```py
    a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    idx = np.array([True, False, True, False, True,
                   False, True, False, True, False])
    a[idx]        # array([0, 2, 4, 6, 8])
    a % 2         # array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], dtype=int32)
    a % 2 == 0    # array([ True, False, True, False, True, False, True, False, True, False])
    a[a % 2 == 0] # array([0, 2, 4, 6, 8])
