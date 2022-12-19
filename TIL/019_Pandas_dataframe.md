# DataFrame class
  - Series가 1차원 vector data에 행방향(row) index를 붙인거라면
  - DataFrame class는 2차원 행렬 data에 index를 붙인거랑 비슷 (대신 DataFrame은 자료형이 각 열마다 다를 수 있음)
  - 2차원이니 row index 뿐 아니라 column index도 붙일 수 있음

# DataFrame 생성
  - ```py
    data = {
        "2015": [9904312, 3448737, 2890451, 2466052],
        "2010": [9631482, 3393191, 2632035, 2431774],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        "지역": ["수도권", "경상권", "수도권", "경상권"],
        "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
    }
    columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
    index = ["서울", "부산", "인천", "대구"]
    df = pd.DataFrame(data, index=index, columns=columns)
    df
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208339843-739c3985-d1ac-4bba-b6bd-bbcf33c49a67.png)

  - ```py
    df.values
    # array([['수도권', 9904312, 9631482, 9762546, 9853972, 0.0283],
    #        ['경상권', 3448737, 3393191, 3512547, 3655437, 0.0163],
    #        ['수도권', 2890451, 2632035, 2517680, 2466338, 0.0982],
    #        ['경상권', 2466052, 2431774, 2456016, 2473990, 0.0141]], dtype=object)
    
    df.columns # Index(['지역', '2015', '2010', '2005', '2000', '2010-2015 증가율'], dtype='object')
    
    df.index # Index(['서울', '부산', '인천', '대구'], dtype='object')
    
  - Series처럼 각 방향 index에 이름 붙이는 것도 가능
    - ```py
      df.index.name = "도시"
      df.columns.name = "특성"
      df
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208340307-7c318814-8b90-4475-bfb4-3563cc551f44.png)

  - DataFrame은 transpose를 포함, numpy 2차원 배열이 가지는 대부분의 속성과 method를 지원
    - ```py
      df.T
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208340427-05bd275e-47c8-4f6d-a81c-e7a7565d09c1.png)

# 열 data 갱신 / 추가 / 삭제
  - ```py
    # "2010-2015 증가율"이라는 이름의 열 추가
    df["2010-2015 증가율"] = df["2010-2015 증가율"] * 100
    df
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208341010-60ebe510-1805-4ece-82c5-84681acdba07.png)

    ```py
    # "2005-2010 증가율"이라는 이름의 열 추가
    df["2005-2010 증가율"] = ((df["2010"] - df["2005"]) / df["2005"] * 100).round(2)
    df
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208341206-883b6178-bdcf-48b5-89f5-1d94ec5cf07c.png)

    ```py
    # "2010-2015 증가율"이라는 이름의 열 삭제
    del df["2010-2015 증가율"]
    df
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208341239-e8c237fe-a980-41ed-ac15-322e5659c6d3.png)

# 열 indexing
  - 하나의 열만 indexing 하면 Series 반환
    - ```py
      df["지역"]
      # 도시
      # 서울    수도권
      # 부산    경상권
      # 인천    수도권
      # 대구    경상권
      # Name: 지역, dtype: object
  - 여러개 열을 indexing 하면 부분적인 DataFrame 반환
    - ```py
      df[["2010", "2015"]]
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208348283-687570b6-2837-4ea4-bd4c-2281414dcb52.png)
  - 하나의 열만 indexing 하면서 DataFrame 자료형을 유지하고 싶다?
    - list 써서 indexing ㄱㄱ
      - ```py
        df[["2010"]]
        ```
        ![image](https://user-images.githubusercontent.com/85230269/208348637-7ae477c3-1639-40e5-b50a-f8f05702e134.png)
  - 열 indexing 할 때, 문자열 label을 가진 경우는 불가 (행 indexing에서 가능)
    - ```py
      df2 = pd.DataFrame(np.arange(12).reshape(3, 4)) # 이건 가능 (index가 정수형인 경우)
      df2
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208349430-e2370585-3cb9-4bbe-a83f-56a07add7aa3.png)
      ```py
      df2[2]
      # 0     2
      # 1     6
      # 2    10
      # Name: 2, dtype: int64
      
      df2[[1, 2]]
      ```
      ![image](https://user-images.githubusercontent.com/85230269/208349528-508c171b-7f86-484a-ac82-fe1ae4af2a30.png)

# 행 indexing
  - 행 단위로 indexing -> slicing 사용
  - index의 값이 문자열 label인 경우 label slicing도 가능
  - ```py
    df[:1]
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208349705-7ab1112f-a7e6-473c-9212-f5a79b91fe52.png)

    ```py
    df[1:2]
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208349761-1a0faf1e-7408-4b9e-ae89-70a159db4ee9.png)

    ```py
    df[1:3]
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208349803-4c85a3e5-f18b-44a2-bbea-c750b3445d12.png)

    ```py
    df["서울":"부산"]
    ```
    ![image](https://user-images.githubusercontent.com/85230269/208349834-5f171291-e00c-4031-baa6-aaeac7ef5321.png)

# 개별 data indexing
  - DataFrame에서 열 label로 Series를 indexing하면 Series가 됨 -> 이 Series를 다시 행 label로 indexing하면 개별 data 반환
  - ```py
    df["2015"]["서울"] # 9904312
