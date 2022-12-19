## Data 입출력
  - Pandas는 data file을 읽어 DataFrame을 만들 수 있음
    - CSV : comma-separated value
    - Excel
    - HTML
    - JSON
    - HDF5
    - SAS
    - STATA
    - SQL

## %%writefile 명령
  - `%%writefile` 명령으로 CSV file 만들기
  - ```py
    %%writefile sample1.csv
    c1, c2, c3
    1, 1.11, one
    2, 2.22, two
    3, 3.33, three
    # Writing sample1.csv
    
## CSV file 입력
  - ```py
    pd.read_csv('sample1.csv') # CSV file로부터 data 읽어서 DataFrame 만들어 줌
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208356658-5443561b-ea58-426f-ab3e-e86341744df5.png)
  - 행 index 정보가 없어서 0부터 시작하는 정수 index가 자동으로 추가
    - 특정 열을 행 index로 쓰고 싶으면 `index_col` 인수를 사용
    - ```py
      pd.read_csv('sample1.csv', index_col='c1')
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208358778-18f5de9c-c0e4-4ebb-8d80-671099bc16dc.png)
  - 확장자가 comma가 아니면 (CSV가 아니면) `sep` 인수를 써서 구분자를 지정
    - 길이가 정해지지 않은 공백이 구분자인 경우 `\s+` 정규식(regular expression) 문자열 사용
    - ```py
      %%writefile sample3.txt
      c1        c2        c3        c4
      0.179181 -1.538472  1.347553  0.43381
      1.024209  0.087307 -1.281997  0.49265
      0.417899 -2.002308  0.255245 -1.10515
      # Writing sample3.txt
      
      pd.read_table('sample3.txt', sep='\s+')
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208360831-ca059a41-3ba8-46ff-bbd6-212aa0aaca01.png)
  - 자료에서 건너 뛰어야 할 행이 있으면 `skiprows` 사용
    - ```py
      %%writefile sample4.txt
      파일 제목: sample4.txt
      데이터 포맷의 설명:
      c1, c2, c3
      1, 1.11, one
      2, 2.22, two
      3, 3.33, three
      # Writing sample4.txt
      
      pd.read_csv('sample4.txt', skiprows=[0, 1]) # 0~1행 skip
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208363011-16570d3b-efd0-4848-aa29-90a701571a4f.png)
  - 특정 값을 NaN으로 취급하고 싶으면 -> `na_values` 인수에 NaN으로 취급할 값을 입력
    - ```py
      %%writefile sample5.csv
      c1, c2, c3
      1, 1.11, one
      2, , two
      누락, 3.33, three
      # Writing sample5.csv
      
      df = pd.read_csv('sample5.csv', na_values=['누락'])
      df
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208363868-f24952c7-e4da-4b72-8dc8-8f2d57e6d969.png)

## CSV file 출력
  - `to_csv` method 사용
  - ```py
    df.to_csv('sample6.csv')
    !type sample6.csv # 리눅스에서는 !cat sample6.csv -> file 내용 확인
    # ,c1, c2, c3
    # 0,1.0, 1.11, one
    # 1,2.0, , two
    # 2,, 3.33, three
    
    df.to_csv('sample7.txt', sep='|')
    !type sample7.csv
    # |c1| c2| c3
    # 0|1.0| 1.11| one
    # 1|2.0| | two
    # 2|| 3.33| three
    
    df.to_csv('sample8.csv', na_rep='누락')
    !type sample8.csv
    # ,c1, c2, c3
    # 0,1.0, 1.11, one
    # 1,2.0, , two
    # 2,누락, 3.33, three
    
    df.index = ["a", "b", "c"]
    df
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208368706-9b43f688-67e0-4375-a734-7afe4ae64ffe.png)
  - ```py
    df.to_csv('sample9.csv', index=False, header=False)
    !type sample9.csv
    # 1.0, 1.11, one
    # 2.0, , two
    # , 3.33, three
    
##  인터넷 상의 CSV file 입력
  - `read_csv` 명령 사용 시 file path 대신 URL을 지정
    - ```py
      df = pd.read_csv("https://raw.githubusercontent.com/datascienceschool/docker_rpython/master/data/titanic.csv")

      pd.set_option("display.max_rows", 20)  # 앞뒤로 모두 20행만 보여줌
      df
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208372361-9d73b533-6ef8-49a9-84ab-9b90bac39950.png)

  - 앞이나 뒤의 특정 갯수만 보고 싶으면 `head` `tail` method 사용
    - ```py
      df.head()
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208372566-5edc38c6-64ae-48b8-8e2f-30946f719b95.png)
    - ```py
      df.tail(2)
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208372643-d3bdc4a7-e43e-4b57-ac13-e1161734c631.png)
