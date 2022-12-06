## python 자료형
  - 자주 사용하는 자료형 종류
    - NoneType
    - bool
    - int
    - float
    - complex
    - str
    - tuple
    - list
    - dict
    - function
  - 변수 메모리 크기
    - ```py
      from sys import getsizeof
      a = 1
      getsizeof(a) # 28
      b = "1"
      getsizeof(b) # 50
  - 변수나 값의 자료형을 알아보려면 `type` 명령 사용
    - ```py
      type(None) # NoneType
      type(True) # bool
      type(1) # int
      type(3.14) # float
      type(2 + 3j) # complex
      type("abc") # str
      type([1, 2, 3]) # list
      type({"A": 10, "B": 20, "C": 30}) # dict
      def f():
          return 1
      type(f) # function
      
## 자료형 변환
  - 자료형을 바꾸기 위해서는 자료형 클래스 생성자를 이용
  - 정수를 문자열로 바꿀 때는 `str`, 문자열을 정수로 바꿀때는 `int`
  - ```py
    str(20221206) # '20221206'
    int("20221206") # 20221206

## 불변형 (immutable) 자료형 / 변형 (mutable) 자료형
  - 불변형 자료형은 data 값을 바꿀 때 메모리에 저장된 data 전체를 모두 없애고 새로 ㄱㄱ
    - int, float, str, tuple
  - 변형 자료형은 할당된 메모리를 그냥 놔두고 메모리에 씌여있는 내용(값)만 갱신
    - list, dictionary
  - ```py
    x = 1
    id(x) # 140709685770016
    x = 2
    id(x) # 140709685770048 메모리 주소도 바뀐다!
    
    x = [1]
    id(x) # 3034340425472
    id(x[0]) # 140709685770016
    x[0] = 2
    id(x) # 3034340425472 얘는 안바뀌고
    x[0] # 140709685770048 얘만 바뀜!
    # tuple은 불변형이라 list처럼 안되고 다 바뀜
