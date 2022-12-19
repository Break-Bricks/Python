## DataFrame advanced indexing
  - numpy처럼 쉼표를 사용한 2차원 indexing을 지원하기 위해 indexer 속성 제공
    - `loc` : label 값 기반의 2차원 indexing
    - `iloc` : 순서를 나타내는 정수 기반의 2차원 indexing

## `loc` indexer
  - `df.loc[행 indexing값]` or `df.loc[행 indexing값, 열 indexing값]`
    - ```py
      df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                    index=["a", "b", "c"],
                    columns=["A", "B", "C", "D"])
      df
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208376895-8ea06043-e214-43ee-8182-16d415ba3c2d.png)
  - index를 하나만 넣으면 행(row) 선택, Series로 출력
    - ```py
      df.loc["a"]
      # A    10
      # B    11
      # C    12
      # D    13
      # Name: a, dtype: int64      
    - slicing도 가능
      - ```py
        df.loc["b":"c"] # loc 안쓴거랑 같음 (df["b":"c"])
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208379364-3c634267-2c2f-4cc2-adb5-a488eb43caab.png)
    - index data의 list도 가능
      - ```py
        df.loc[["b", "c"]] # 요건 loc 안쓰면 error 남
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208379563-9302d3f8-b885-4870-af02-9bb95659277e.png)
    - indexing값으로 boolean도 됨
      - ```py
        df.A > 15
        # a    False
        # b    False
        # c     True
        # Name: A, dtype: bool
        df.loc[df.A > 15]
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208379990-dcffdd47-a094-4915-87ed-89758e03a520.png)
    - index 대신 index 값을 반환하는 함수로 indexing도 가능
      - ```py
        def select_rows(df):
        return df.A > 15
        df.loc[select_rows(df)]
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208380326-7d697f2b-a086-4fff-a7f8-c92885d570ea.png)
    - 행 index 값이 정수인 경우 slicing도 label slicing 방식 따름 (마지막 값 포함!!)
      - ```py
        df2 = pd.DataFrame(np.arange(10, 26).reshape(4, 4), columns=["A", "B", "C", "D"])
        df2
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208380628-2800696a-437c-4c30-bebb-d58b265ffd80.png)
      - ```py
        df2.loc[1:2]
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208380754-af7a7164-dad0-4499-ba90-6f56e0577725.png)
  - 행, 열 모두 indexing 값을 받는 경우
    - ```py
      df.loc["a", "A"] # 10
    - slicing 이나 list 가능
      - ```py
        df.loc["b":, "A"]
        # b    14
        # c    18
        # Name: A, dtype: int64
        df.loc["a", :]
        # A    10
        # B    11
        # C    12
        # D    13
        # Name: a, dtype: int64
        ```
      - ```py
        df.loc[["a", "b"], ["B", "D"]]
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208381727-3711b1b1-4501-4022-a949-ecad10a9aa55.png)
    - boolean of boolean 반환 함수 가능
      - ```py
        df.loc[df.A > 10, ["C", "D"]]
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208382007-bcc04c67-a97c-42d2-a52c-f10e41952626.png)

## `iloc` indexer
  - `loc`과 반대로 label이 아니라 순서를 나타내는 정수(integer) index만 받음
  - 다른건 `loc`과 같음
    - ```py
      df.iloc[0, 1] # 11
      ```
    - ```py
      df.iloc[:2, 2]
      # a    12
      # b    16
      # Name: C, dtype: int64
      ```
    - ```py
      df.iloc[0, -2:]
      # C    12
      # D    13
      # Name: a, dtype: int64
      ```
    - ```py
      df.iloc[2:3, 1:3]
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208383674-f9646333-7cb1-496b-a279-6d5651c06137.png)
    - ```py
      df.iloc[-1] # index가 하나 들어가면 행 선택
      # A    18
      # B    19
      # C    20
      # D    21
      # Name: c, dtype: int64
      ```
    - ```py
      df.iloc[-1] = df.iloc[-1] * 2
      df
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208384764-772a8622-8f56-4bf3-8f74-b9b94c8a07a6.png)
