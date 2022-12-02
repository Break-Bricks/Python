## 함수
  - `def`와 `return` 키워드를 사용
    - ```py
      def 함수이름(입력변수이름):
          출력변수를 만드는 명령
          return 출력변수이름
      ```
    - ```py
      def twotimes(x):
          y = 2 * x
          return y
    
      twotimes(2) # 4
      twotimes(10) # 20
      ```
      
  - 입력이 여러개인 함수
      - ```py
        def 함수이름(입력변수1, 입력변수2, 입력변수3):
            출력변수를 만드는 명령
            return 출력변수이름
        ```
      - ```py
        def sum(a, b, c):
            s = a + b + c
            return s
            
        sum(1, 2, 3) # 6
        
        ```
        
## 람다(lambda) 함수
  - 함수로 정의하면
    - ```py
      def f(x):
          return 2 * x
      ```
  - 람다 함수로 정의하면
    - ```py
      f = lambda x : 2 * x
      
      ```
