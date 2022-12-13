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
    
    # 벡터화 연산은 이런 것도 다 됨
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])
    2 * a + b           # array([12, 24, 36])
    a == 2              # array([False,  True, False])
    b > 10              # array([False,  True,  True])
    (a == 2) & (b > 10) # array([False,  True, False])
    np.exp(a)           # array([1., 2.71828183, 7.3890561])
    10 ** a             # array([1, 10, 100])
    np.log(a + 1)       # array([0., 0.69314718, 1.09861229])
    
    # 배열의 모든 원소가 다 같은지 알고 싶으면 all 사용
    a = np.array([1, 2, 3, 4])
    b = np.array([4, 2, 2, 4])
    c = np.array([1, 2, 3, 4])
    np.all(a == b) # False
    np.all(a == c) # True
    
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

## array datatype
  - ```py
    x = np.array([1, 2, 3], dtype='f')
    x.dtype # dtype('float32')
    
    # datatype을 명시 안하면 주어진 data로 알아서 유추
    x = np.array([1, 2, 3])
    x.dtype # dtype('int64')
    x = np.array([1.0, 2.0, 3.0])
    x.dtype # dtype('float64')
    x = np.array([1, 2, 3.0])
    x.dtype # dtype('float64')
    
![image](https://user-images.githubusercontent.com/85230269/206985830-e4cb9eb2-eb6b-4449-aed8-04fa9b73ee81.png)

## Inf / NaN
  - 무한대를 표현하기 위한 np.inf (infinity)
  - 정의할 수 없는 숫자를 나타내는 np.nan (not a number)
  - ```py
    np.array([0, 1, -1, 0]) / np.array([1, 0, 0, 0]) # array([  0.,  inf, -inf,  nan])
    np.log(0) # -inf
    np.exp(-np.inf) # 0.0
    
## array 생성
  - NumPy에서 제공하는 배열 생성 명령
    - `zeros`, `ones`
    - `zeros_like`, `ones_like`
    - `empty`
    - `arange`
    - `linspace`, `logspace`
    - ```py
      a = np.zeros(5) # 크기 5에 모든 값이 0
      a # array([0., 0., 0., 0., 0.])
      
      b = np.zeros((2, 3)) # 크기 뜻하는 tuple 입력하면 다차원 배열도 생성 가능
      b
      # array([[0., 0., 0.],
      #        [0., 0., 0.]])
      
      c = np.zeros((5, 2), dtype="i")
      c
      # array([[0, 0],
      #        [0, 0],
      #        [0, 0],
      #        [0, 0],
      #        [0, 0]], dtype=int32)
      
      # 문자열 배열도 가능하지만 모든 원소의 문자열 크기가 같아야 함
      d = np.zeros(5, dtype="U4")
      d[0] = "abc"
      d[1] = "abcd"
      d[2] = "ABCDE"
      d #array(['abc', 'abcd', 'ABCD', '', ''], dtype='<U4')
      
      e = np.ones((2, 3, 4), dtype="i8") # 값을 1로 초기화
      e
      # array([[[1, 1, 1, 1],
      #         [1, 1, 1, 1],
      #         [1, 1, 1, 1]],
      #        [[1, 1, 1, 1],
      #         [1, 1, 1, 1],
      #         [1, 1, 1, 1]]])
      
      # 크기를 따로 명시하지 않고 다른 배열과 같은 크기의 배열을 생성 -> ones_like, zeros_like
      f = np.ones_like(b, dtype="f")
      f
      # array([[1., 1., 1.],
      #        [1., 1., 1.]], dtype=float32)
      
      # 배열이 커지면 초기화하는데도 시간이 걸려서, 시간을 단축하려면 empty 명령 사용
      # 기존에 메모리에 저장되어 있던 값이 있으므로 원소의 값을 미리 알 수 없음
      g = np.empty((4, 3))
      g
      # array([[6.94820328e-310, 4.67533915e-310, 5.28964691e+180],
      #        [6.01346953e-154, 4.81809028e+233, 7.86517465e+276],
      #        [6.01346953e-154, 2.58408173e+161, 2.46600381e-154],
      #        [2.47379808e-091, 4.47593816e-091, 6.01347002e-154]])
      
      # arange 명령은 NumPy 버전의 range 명령 (특정한 규칙에 따라 증가하는 수열)
      np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) (0 ... n-1)
      np.arange(3, 21, 2) # array([ 3,  5,  7,  9, 11, 13, 15, 17, 19]) (시작, 끝(포함x), 단계)
      
      # linspace 명령이나 logspace 명령은 선형 구간 혹은 로그 구간을 지정한 구간의 수만큼 분할
      np.linspace(0, 100, 5) # array([  0.,  25.,  50.,  75., 100.]) (시작, 끝(포함), 갯수)
      np.logspace(0.1, 1, 10)
      # array([ 1.25892541,  1.58489319,  1.99526231,  2.51188643,  3.16227766,
      #         3.98107171,  5.01187234,  6.30957344,  7.94328235, 10.        ])
      
## 전치(transpose) 연산
  - 2차원 배열의 전치 연산은 행과 열을 바꾸는 작업
  - 배열의 `T` 속성으로 구할 수 있음 (method가 아닌 속성이라는 점에 유의)
  - ```py
    A = np.array([[1, 2, 3], [4, 5, 6]])
    A.T
    # array([[1, 4],
    #        [2, 5],
    #        [3, 6]])
    
## array 크기 변경
  - 만들어진 배열의 내부 data는 보존한 채로 형태만 바꾸려면 `reshape` method 사용
    - ```py
      a = np.arange(12)
      a # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

      b = a.reshape(3, 4)
      b
      # array([[0, 1, 2, 3],
      #        [4, 5, 6, 7],
      #        [8, 9, 10, 11]])

      # 원소의 갯수가 정해져 있기 때문에 tuple의 원소 중 하나는 -1로 대체 가능 (다른 값으로부터 자동 계산됨)
      a.reshape(3, -1)
      # array([[0, 1, 2, 3],
      #        [4, 5, 6, 7],
      #        [8, 9, 10, 11]])

      a.reshape(2, 2, -1)
      # array([[[0, 1, 2],
      #         [3, 4, 5]],
      #        [[6, 7, 8],
      #         [9, 10, 11]]])
    
  - 다차원 배열을 무조건 1차원으로 만들려면 `flatten` 또는 `ravel` method 사용
    - ```py
      a.flatten() # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
      a.ravel() # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
      
  - 배열의 차원만 증가시키는 경우 `newaxis` method 사용
    - ```py
      x = np.arange(5)
      x # array([0, 1, 2, 3, 4])
      
      x.reshape(1, 5) # array([[0, 1, 2, 3, 4]])
      x[np.newaxis, :]  # array([[0, 1, 2, 3, 4]])

## array concatenate (배열 연결)
  - 행의 수나 열의 수가 같은 두 개 이상의 배열을 연결하여 더 큰 배열을 만들 수 있음
  - `hstack`
  - `vstack`
  - `dstack`
  - `stack`
  - `r_` : method 이지만 소괄호 대신 indexing처럼 대괄호[]를 사용 (indexer)
  - `c_` : 얘도 indexer
  - `tile`
  - ```py
    a1 = np.ones((2, 3))
    a2 = np.zeros((2, 2))
    np.hstack([a1, a2])
    # array([[1., 1., 1., 0., 0.],
    #        [1., 1., 1., 0., 0.]])
    
    b1 = np.ones((2, 3))
    b2 = np.zeros((3, 3))
    np.vstack([b1, b2])
    # array([[1., 1., 1.],
    #        [1., 1., 1.],
    #        [0., 0., 0.],
    #        [0., 0., 0.],
    #        [0., 0., 0.]])
    
    c1 = np.ones((3, 4))
    c2 = np.zeros((3, 4))
    np.dstack([c1, c2]) # (3 x 4 x 2)
    # array([[[1., 0.],
    #         [1., 0.],
    #         [1., 0.],
    #         [1., 0.]],
    #        [[1., 0.],
    #         [1., 0.],
    #         [1., 0.],
    #         [1., 0.]],
    #        [[1., 0.],
    #         [1., 0.],
    #         [1., 0.],
    #         [1., 0.]]])
    
    c = np.stack([c1, c2]) # axis default = 0 -> (2 x 3 x 4)
    c
    # array([[[1., 1., 1., 1.],
    #         [1., 1., 1., 1.],
    #         [1., 1., 1., 1.]],
    #        [[0., 0., 0., 0.],
    #         [0., 0., 0., 0.],
    #         [0., 0., 0., 0.]]])
    c = np.stack([c1, c2], axis=1) # (3 x 2 x 4)
    c
    # array([[[1., 1., 1., 1.],
    #         [0., 0., 0., 0.]],
    #        [[1., 1., 1., 1.],
    #         [0., 0., 0., 0.]],
    #        [[1., 1., 1., 1.],
    #         [0., 0., 0., 0.]]])
    
    np.r_[np.array([1, 2, 3]), np.array([4, 5, 6])] # array([1, 2, 3, 4, 5, 6])
    
    np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])]
    # array([[1, 4],
    #        [2, 5],
    #        [3, 6]])
    
    # tile은 동일한 배열을 반복하여 연결
    a = np.array([[0, 1, 2], [3, 4, 5]])
    np.tile(a, 2)
    # array([[0, 1, 2, 0, 1, 2],
    #        [3, 4, 5, 3, 4, 5]])
    np.tile(a, (3, 2))
    # array([[0, 1, 2, 0, 1, 2],
    #        [3, 4, 5, 3, 4, 5],
    #        [0, 1, 2, 0, 1, 2],
    #        [3, 4, 5, 3, 4, 5],
    #        [0, 1, 2, 0, 1, 2],
    #        [3, 4, 5, 3, 4, 5]])
    
## broadcasting
  - 벡터(또는 행렬)끼리 덧셈 혹은 뺄셈을 하려면 두 벡터의 크기가 같아야 함
  - numpy에서는 서로 다른 크기를 가진 두 배열의 사칙연산도 지원
  - 이 기능을 브로드캐스팅(broadcasting)이라고 함
  - 크기가 작은 배열을 자동으로 반복 확장하여 크기가 큰 배열에 맞추는 방법

![image](https://user-images.githubusercontent.com/85230269/207217941-964c3858-a56a-4bc6-883b-30cfe74bd459.png)![image](https://user-images.githubusercontent.com/85230269/207217959-78c0dc11-00a8-46de-b71d-43ea820c661c.png)

![image](https://user-images.githubusercontent.com/85230269/207218400-e5a68754-27f0-4717-ad1d-58d67f9370eb.png)

## 차원 축소 (dimension reduction) 연산
  - 최대/최소 : `min`, `max`, `argmin`, `argmax`
  - 통계 : `sum`, `mean`, `median`, `std`, `var`
  - boolean : `all`, `any`
  - ```py
    x = np.array([1, 2, 3, 4])
    x # array([1, 2, 3, 4])
    np.sum(x) # 10
    x.sum() # 10
    x.min() # 1
    x.max() # 4
    x.argmin() # 0 (최솟값의 위치)
    x.argmax() # 3 (최댓값의 위치)
    
    x = np.array([1, 2, 3, 1])
    x.mean() # 1.75
    np.median(x) # 1.5
    np.all([True, True, False]) # False
    np.any([True, True, False]) # True
    
    a = np.zeros((100, 100), dtype=np.int)
    np.any(a != 0) # False
    np.all(a == a) # True
    
    a = np.array([1, 2, 3, 2])
    b = np.array([2, 2, 3, 2])
    c = np.array([6, 4, 4, 5])
    ((a <= b) & (b <= c)).all() # True
    
    # 연산의 대상이 2차원 이상인 경우에는 어느 차원으로 계산할 지 axis 인수로 지시
    # axis = 0인 경우(default)는 열 연산, axis = 1인 경우는 행 연산
    x = np.array([[1, 1], [2, 2]])
    x.sum() # 6
    x.sum(axis=0) # array([3, 3]) (열 합계)
    x.sum(axis=1) # array([2, 4]) (행 합계)
    
## 정렬 (sorting)
  - `sort` 함수나 method로 배열 안의 원소를 크기에 따라 정렬하여 새로운 배열 생성
  - 2차원 이상인 경우에는 행이나 열을 각각 따로따로 정렬, axis 인수로 결정
  - 정렬 시 axis 인수의 default 값은 0이 아닌 -1 (가장 안쪽(나중)의 차원)
  - ```py
    a = np.array([[4,  3,  5,  7],
                  [1, 12, 11,  9],
                  [2, 15,  1, 14]])
    np.sort(a) # axis = -1 또는 axis = 1과 동일
    # array([[ 3,  4,  5,  7],
    #        [ 1,  9, 11, 12],
    #        [ 1,  2, 14, 15]])
    np.sort(a, axis=0)
    # array([[ 1,  3,  1,  7],
    #        [ 2, 12,  5,  9],
    #        [ 4, 15, 11, 14]])
    
    # sort method는 해당 객체의 자료 자체가 변화하는 자체변화(in-place) method이므로 사용에 주의
    a.sort(axis=1)
    a
    # array([[ 3,  4,  5,  7],
    #        [ 1,  9, 11, 12],
    #        [ 1,  2, 14, 15]])

    # 자료를 정렬하는 게 아니라 순서만 알고싶을 경우 argsort 사용
    a = np.array([42, 38, 12, 25])
    j = np.argsort(a)
    j # array([2, 3, 1, 0])
    a[j] # array([12, 25, 38, 42])
