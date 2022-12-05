## for 반복문
  - ```
    for 카운터 변수 in range(반복횟수):
        반복해서 실행할 명령
  - ```py
    for i in range(10):
        print("=" + str(i + 1) + "=")
    # =1=
    # =2=
    # =3=
    # =4=
    # =5=
    # =6=
    # =7=
    # =8=
    # =9=

## 중첩 for 반복문
  - ```py
    for i in range(4):
        for j in range(4):
            print(i + j, end=" ")
        print()
    # 0 1 2 3
    # 1 2 3 4
    # 2 3 4 5
    # 3 4 5 6
  - 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
    - ```py
      for i in range(6):
          n1 = i + 1
          for j in range(6):
              n2 = j + 1
              n = n1 + n2
              if n % 4 == 0:
                  print(n1, n2)
      # 1 3
      # 2 2
      # 2 6
      # 3 1
      # 3 5
      # 4 4
      # 5 3
      # 6 2
      # 6 6
      
## 카운터 변수가 변하는 경우
  - 안쪽 반복문의 반복 횟수가 바깥쪽 반복문의 카운터 변수에 따라 변하는 경우
  - ```py
    for j in range(10):
        sum = 0
        for i in range(j + 1):
            sum = sum + (i + 1)
        print(sum)
    # 1
    # 3
    # 6
    # 10
    # 15
    # 21
    # 28
    # 36
    # 45
    # 55
