## datetime package
  - ```py
    import datetime as dt
    ```
  - 날짜와 시간을 함께 저장하는 datetime class
    - dateitme class
      - package 이름과 class 이름이 datetime으로 같기 때문에 사용에 주의
      - 다른 class와 달리 class name이 대문자로 시작하지 않음
      - 객체를 생성하지 않고도 바로 class에서 사용할 수 있는 class method 제공
        - now: 현재 시각 반환
        - weekday: 요일 반환 (0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
        - strftime: 문자열 반환
          - %Y: 앞의 빈자리를 0으로 채우는 4자리 연도 숫자
          - %m: 앞의 빈자리를 0으로 채우는 2자리 월 숫자
          - %d: 앞의 빈자리를 0으로 채우는 2자리 일 숫자
          - %H: 앞의 빈자리를 0으로 채우는 24시간 형식 2자리 시간 숫자
          - %M: 앞의 빈자리를 0으로 채우는 2자리 분 숫자
          - %S: 앞의 빈자리를 0으로 채우는 2자리 초 숫자
          - %A: 영어로 된 요일 문자열
          - %B: 영어로 된 월 문자열
          - 그 외: https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes
        - date: 날짜 정보만 가지는 date 클래스 객체 반환
        - time: 시간 정보만 가지는 time 클래스 객체 반환
        - ```py
          x = dt.datetime.now()
          x # datetime.datetime(2022, 12, 8, 10, 50, 4, 517207)
          x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond # (2020, 10, 2, 15, 27, 4, 517207)
          x.weekday() # 4
          x.strftime("%A %d. %B %Y") # 'Friday 02. October 2020'
          print(x.strftime("%H시 %M분 %S초")) # 15시 27분 04초
          dt.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M") # datetime.datetime(2017, 1, 2, 14, 44)
        ```
  - 날짜만 저장하는 date class
  - 시간만 저장하는 time class
  - 시간 구간 정보를 저장하는 timedelta clase

## dateutil package
  - `parse` 함수를 쓰면 형식 문자열을 넣지 않아도 자동으로 찾아서 datetime class를 만들어 줌
  - ```py
    from dateutil.parser import parse
    parse('2016-04-16') # datetime.datetime(2016, 4, 16, 0, 0)
    parse("Apr 16, 2016 04:05:32 PM") # datetime.datetime(2016, 4, 16, 16, 5, 32)
    parse('6/7/2016') # datetime.datetime(2016, 6, 7, 0, 0)
    # 월과 일이 모두 12보다 작은 숫자면 먼저 나오는 숫자를 월로 판단
    
## 날짜/시간 연산
  - 날짜나 시간 사이의 간격을 구할 때는 두 개의 datetime class 객체의 차이를 구함
  - 이 결과는 timedelta class 객체로 반환됨
  - datetime class 객체에 timedelta class 객체를 더해서 새로운 시간을 구할 수도 있음
  - timedelta의 단점은 날짜를 초 단위로만 연산할 수 있다는 점, 이를 보완하기 위해 relativedelta class 제공
    - 속성
      - days: 일수
      - seconds: 초 (0 ~ 86399)
      - microseconds: 마이크로초 (0 and 999999)
    - method
      - total_seconds: 모든 속성을 초단위로 모아서 변환
    - ```py
      dt1 = datetime.datetime(2016, 2, 19, 14)
      dt2 = datetime.datetime(2016, 1, 2, 13)
      td = dt1 - dt2
      td # datetime.timedelta(days=48, seconds=3600)
      td.days, td.seconds, td.microseconds # (48, 3600, 0)
      td.total_seconds() # 4150800.0
      
      t0 = datetime.datetime(2018, 9, 1, 13)
      d = datetime.timedelta(days=90, seconds=3600)
      t0 + d # datetime.datetime(2018, 11, 30, 14, 0)
      
      from dateutil.relativedelta import relativedelta
      t0 + relativedelta(months=2) # datetime.datetime(2018, 11, 1, 13, 0)
      
## time package
  - time package는 실행을 잠시 멈추는 `sleep` 함수를 제공
  - ```py
    import time
    print(1) # 1 출력하고
    time.sleep(5) # 5초 쉬고
    print(2) # 2를 출력
