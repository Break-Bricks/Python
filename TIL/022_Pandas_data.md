## data count
  - `count` method 사용 (NaN은 빼고 count)
    - ```py
      s = pd.Series(range(10))
      s[3] = np.nan
      s
      # 0    0.0
      # 1    1.0
      # 2    2.0
      # 3    NaN
      # 4    4.0
      # 5    5.0
      # 6    6.0
      # 7    7.0
      # 8    8.0
      # 9    9.0
      # dtype: float64

      s.count() # 9
    
  - DataFrame에서는 각 열마다 별도로 data count
    - ```py
      np.random.seed(2)
      df = pd.DataFrame(np.random.randint(5, size=(4, 4)), dtype=float)
      df.iloc[2, 3] = np.nan
      df
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208386653-04b8400c-98e0-492f-ae19-ed6a0f0f916b.png)
    - ```py
      df.count()
      # 0    4
      # 1    4
      # 2    4
      # 3    3
      # dtype: int64 
    - ```py
      import seaborn as sns
      titanic = sns.load_dataset("titanic")
      titanic.head()
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208406451-ba27680c-9be5-4e3f-a328-2f3c1d5f025c.png)

## 카테고리 값 count
  - `value_counts` method 사용
    - ```py
      np.random.seed(1)
      s2 = pd.Series(np.random.randint(6, size=100))
      s2.tail()
      # 95    4
      # 96    5
      # 97    2
      # 98    4
      # 99    3
      # dtype: int64
    - ```py
      s2.value_counts()
      # 1    22
      # 0    18
      # 4    17
      # 5    16
      # 3    14
      # 2    13
      # dtype: int64
  - DataFrame에는 `value_counts` 없음 -> 각 열마다 별도로 사용
    - ```py
      df[0].value_counts()
      # 3.0    2
      # 4.0    1
      # 0.0    1
      # Name: 0, dtype: int64
      
## 정렬
  - `sort_index` `sort_values`
    - ```py
      s2.value_counts().sort_index()
      # 0    18
      # 1    22
      # 2    13
      # 3    14
      # 4    17
      # 5    16
      # dtype: int64
  - NaN 있으면 맨 뒤로
    - ```py
      s.sort_values()
      # 0    0.0
      # 1    1.0
      # 2    2.0
      # 4    4.0
      # 5    5.0
      # 6    6.0
      # 7    7.0
      # 8    8.0
      # 9    9.0
      # 3    NaN
      # dtype: float64
  - 큰 수에서 작은 수로 (반대 방향) : `ascending=False`
    - ```py
      s.sort_values(ascending=False)
      # 9    9.0
      # 8    8.0
      # 7    7.0
      # 6    6.0
      # 5    5.0
      # 4    4.0
      # 2    2.0
      # 1    1.0
      # 0    0.0
      # 3    NaN
      # dtype: float64
  - DataFrame에서 `sort_values` 사용하려면 `by` 인수로 정렬 기준 열을 지정
    - ```py
      df.sort_values(by=1)
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208408229-6c6728f4-f6aa-4d4e-ba1d-31417b13cc58.png)
    - ```py
      df.sort_values(by=[1, 2]) # list가 들어가면 첫번째 열을 기준으로 정렬 후 동일한 값이 나오면 그 다음 열로 순서 결정
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208408396-ed1cc417-f718-46c8-8e9b-b62109e3caf5.png)

## 행/열 합계
  - 행과 열의 합계는 `sum(axis)` method 사용
  - axis에는 합계로 인해 없어지는 방향축 (0=행, 1=열) 지정
    - 행방향 합계 sum(axis=1)
    - 열방향 합계 sum(axis=0) (인수 생략 가능, 0이 default)
    - ```py
      np.random.seed(1)
      df2 = pd.DataFrame(np.random.randint(10, size=(4, 8)))
      df2
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208409685-d935916f-ecc1-4cfa-8dc8-abf78b5729fd.png)
    - ```py
      df2.sum(axis=1)
      # 0    35
      # 1    34
      # 2    41
      # 3    42
      # dtype: int64
      ```
    - ```py
      df2["RowSum"] = df2.sum(axis=1)
      df2
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208409819-67735ad5-f8a9-4484-bfe1-37f5aab113df.png)
    - ```py
      df2.sum() # 인수 생략
      # 0          24
      # 1          33
      # 2          25
      # 3          24
      # 4          15
      # 5          10
      # 6           5
      # 7          16
      # RowSum    152
      # dtype: int64
      ```
    - ```py
      df2.loc["ColTotal", :] = df2.sum()
      df2
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208410083-03be9cd6-74c1-4918-8214-0a3177000e9e.png)

## `apply` 변환
  - 행이나 열 단위로 더 복잡한 처리를 하고 싶을 때 사용
  - 인수로 행(또는 열)을 받는 함수를 `apply` method 인수로 넣으면 각 열(또는 행)을 반복해서 그 함수에 적용
  - ```py
    df3 = pd.DataFrame({
    'A': [1, 3, 4, 3, 4],
    'B': [2, 3, 1, 2, 3],
    'C': [1, 5, 2, 4, 4]
    })
    df3
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208411928-f62e0b7f-d417-4b66-b17f-993a19e5726f.png)
    - 각 열의 max - min을 구하고 싶으면
      - ```py
        df3.apply(lambda x: x.max() - x.min())
        # A    3
        # B    2
        # C    4
        # dtype: int64
        ```
    - 행에 대해 적용하고 싶으면 `axis=1`
      - ```py
        df3.apply(lambda x: x.max() - x.min(), axis=1)
        # 0    1
        # 1    2
        # 2    3
        # 3    2
        # 4    1
        # dtype: int64
    - 각 열에 대해 어떤 값이 얼마나 사용되었는지 알고 싶으면
      - ```py
        df3.apply(pd.value_counts)
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208412423-720d19f7-56bf-4aa2-83a5-ecefef2e501a.png)
    - 타이타닉호 승객 중 나이 20살을 기준으로 성인과 미성년자를 구별하는 label 열 만들기
      - ```py
        titanic["adult/child"] = titanic.apply(lambda r: "adult" if r.age >= 20 else "child", axis=1)
        titanic.tail()
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208412925-a9a3b12c-6446-44d7-a9dd-1652f243bdc5.png)

## `fillna` method
  - NaN 값을 원하는 값으로 변경 가능
    - ```py
      df3.apply(pd.value_counts).fillna(0.0)
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208413152-7c62a462-d39c-4d09-bda1-d99fca515a86.png)

## `astype` method
  - 전체 data의 자료형을 변경
    - ```py
      df3.apply(pd.value_counts).fillna(0).astype(int)
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208413283-f0adb744-ec48-45c5-a831-06ac9ade8b81.png)

## 실수 값을 카테고리 값으로 변환
  - `cut` : 실수 값의 경계선을 지정
  - `qcut` : 갯수가 똑같은 구간으로 나눔
  - ```py
    ages = [0, 2, 10, 21, 23, 37, 31, 61, 20, 41, 32, 101]
    
    bins = [1, 20, 30, 50, 70, 100] # 카테고리를 나누는 기준값, 영역 넘으면 NaN
    labels = ["미성년자", "청년", "중년", "장년", "노년"]
    cats = pd.cut(ages, bins, labels=labels)
    cats
    # [NaN, 미성년자, 미성년자, 청년, 청년, ..., 장년, 미성년자, 중년, 중년, NaN]
    # Length: 12
    # Categories (5, object): [미성년자 < 청년 < 중년 < 장년 < 노년]
    
    # Categorical class 객체 반환
    type(cats) # pandas.core.arrays.categorical.Categorical
    
    # categories : label 문자열
    cats.categories # Index(['미성년자', '청년', '중년', '장년', '노년'], dtype='object')
    
    # codes : 정수로 incoding한 카테고리 값
    cats.codes # array([-1,  0,  0,  1,  1,  2,  2,  3,  0,  2,  2, -1], dtype=int8)
    ```
  - ```py
    df4 = pd.DataFrame(ages, columns=["ages"])
    df4["age_cat"] = pd.cut(df4.ages, bins, labels=labels)
    df4 # 여기서 age_cat 열 값은 문자열이 아님
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208415134-c8c41efa-46c2-40c0-92d8-8d028278a8bc.png)
    ```py
    # 문자열로 바꾸고 싶으면 astype 사용
    df4.age_cat.astype(str) + ' ' + df4.ages.astype(str)
    # 0       nan 0
    # 1      미성년자 2
    # 2     미성년자 10
    # 3       청년 21
    # 4       청년 23
    # 5       중년 37
    # 6       중년 31
    # 7       장년 61
    # 8     미성년자 20
    # 9       중년 41
    # 10      중년 32
    # 11    nan 101
    # dtype: object
  - ```py
    data = np.random.randn(1000)
    cats = pd.qcut(data, 4, labels=["Q1", "Q2", "Q3", "Q4"])
    cats
    # [Q2, Q1, Q2, Q3, Q1, ..., Q1, Q1, Q4, Q4, Q2]
    # Length: 1000
    # Categories (4, object): [Q1 < Q2 < Q3 < Q4]
    
    pd.value_counts(cats)
    # Q4    250
    # Q3    250
    # Q2    250
    # Q1    250
    # dtype: int64
