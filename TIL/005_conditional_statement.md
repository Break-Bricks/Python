## if ~ else 명령
  - 조건이 2가지일 때 사용
  - ```py
    if 참 또는 거짓을 가지는 값:
        조건이 참일 때 실행되는 명령들
    else:
        조건이 거짓일 때 실행되는 명령들
    ```
  - ```py
    a = 1
    if a % 2 == 0:
        print("짝수")
    else:
        print("홀수")
    # 홀수

    b = 55
    if (b >= 10) & (b < 100) & (b % 2 == 0):
        print("2자리 수의 짝수이다.")
    else:
        print("2자리 수의 짝수가 아니다.")
    # 2자리 수의 짝수가 아니다.
    ```

## if ~ elif ~ else 명령
  - 조건이 3가지 이상일 때 사용
  - ```py
    if 조건1:
        조건1이 참일 때 실행되는 명령
    elif 조건2:
        조건1이 거짓이고 조건2가 참일 때 실행되는 명령
    elif 조건3:
        조건1과 조건2가 거짓이고 조건3이 참일 때 실행되는 명령
    elif 조건4:
        조건1과 조건2, 조건3이 거짓이고 조건4가 참일 때 실행되는 명령
    else:
        지금까지의 어떤 조건도 참이 아니면 실행되는 명령
    ```
  - ```py
    c = 6
    if c >= 8:
        print("A")
    elif c >= 5:
        print("B")
    else:
        print("C")
    ```
    
## 중첩(nesting) 조건문
  - 조건문 내부에 다시 조건문 중첩 가능
  - 단 들여쓰기 더 해줘야 함
  - ```py
    if 조건1:
        조건1이 참일 때 실행되는 명령
        if 조건2:
            조건1과 조건2가 모두 참일 때 실행되는 명령
        else:
            조건1은 참이고 조건2는 거짓일 때 실행되는 명령
    else:
        조건1이 거짓일 때 실행되는 명령
    ```
  - ```py
    sex = "boy"
    pushup = 8
    if sex == "boy":
        if pushup >= 10:
            grade = "Pass"
        else:
            grade = "Fail"
    else:
        if pushup >= 10:
            grade = "Pass"
        else:
            grade = "Fail"

    print(grade) # Fail
    ```
