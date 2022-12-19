## Pandas package
  - ```py
    import pandas as pd
    ```
    
## Series class
  - numpy의 1차원 배열과 비슷
  - 각 data 의미를 표시하는 index를 붙일 수 있음
  - `series = value + index`

## Series 생성
  - ```py
    s = pd.Series([9904312, 3448737, 2890451, 2466052],
                  index=["서울", "부산", "인천", "대구"])
    s
    # 서울    9904312
    # 부산    3448737
    # 인천    2890451
    # 대구    2466052
    # dtype: int64
    
    # index 없이 만들면 0부터 시작하는 정수값으로 index 자동 지정
    pd.Series(range(10, 14))
    # 0    10
    # 1    11
    # 2    12
    # 3    13
    # dtype: int64
    
    # index 접근
    s.index # Index(['서울', '부산', '인천', '대구'], dtype='object')
    
    # 값(value 접근)
    s.values # array([9904312, 3448737, 2890451, 2466052])
    
    # name 속성으로 series와 index에 이름 붙일 수 있음
    s.name = "인구"
    s.index.name = "도시"
    s
    # 도시
    # 서울    9904312
    # 부산    3448737
    # 인천    2890451
    # 대구    2466052
    # Name: 인구, dtype: int64
    
## Series 연산
  - 벡터화 연산 가능 (index에는 ㄴㄴ)
  - ```py
    s / 1000000
    # 도시
    # 서울    9.904312
    # 부산    3.448737
    # 인천    2.890451
    # 대구    2.466052
    # Name: 인구, dtype: float64
    
## Series indexing
  - indexing / slicing 가능
    - indexing
      - ```py
        s[3], s["대구"] # (2466052, 2466052)
        s[1], s["부산"] # (3448737, 3448737)
        
    - 이런 것도 된다 (label이 영문 문자열인 경우만 됨)
      - ```py
        s0 = pd.Series(range(3), index=["a", "b", "c"])
        s0
        # a    0
        # b    1
        # c    2
        # dtype: int64
        s0.a # 0
        s0.b # 1
  - 배열 indexing -> 부분적인 값을 가지는 series 자료형 반환
    - ```py
      s[[0, 3, 1]] # s[["서울", "대구", "부산"]] 이거랑 같음
      # 도시
      # 서울    9904312
      # 대구    2466052
      # 부산    3448737
      # Name: 인구, dtype: int64

      s[(250e4 < s) & (s < 500e4)]  # 인구가 250만 초과, 500만 미만인 경우
      # 도시
      # 부산    3448737
      # 인천    2890451
      # Name: 인구, dtype: int64

  - slicing도 series 자료형 반환
    - index로 slicing 할 때랑 문자열 label로 slicing 할 때 다르니 주의!
      - ```py
        s[1:3]  # 두번째(1)부터 세번째(2)까지 (네번째(3) 미포함)
        # 도시
        # 부산    3448737
        # 인천    2890451
        # Name: 인구, dtype: int64
        
        s["부산":"대구"]  # 부산에서 대구까지 (대구도 포함)
        # 도시
        # 부산    3448737
        # 인천    2890451
        # 대구    2466052
        # Name: 인구, dtype: int64
        
## dictionary 자료형
  - series는 label로 indexing이 가능하므로 index label을 key로 가지는 dictionary 자료형과 같음
  - dictionary 자료형에서 제공하는 in 연산 / for loop 가능
    - ```py
      "서울" in s # True
      "대전" in s # False
      for k, v in s.items():
          print("%s = %d" % (k, v))
      # 서울 = 9904312
      # 부산 = 3448737
      # 인천 = 2890451
      # 대구 = 2466052
  - dictionary 객체에서 series를 만들 수도 있음
    - 순서를 가지지 않기 때문에 series 역시 순서 보장 ㄴㄴ
    - 순서 정하고 싶으면 index를 list로 지정해야 함
    - ```py
      s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158})
      s2
      # 서울    9631482
      # 부산    3393191
      # 인천    2632035
      # 대전    1490158
      # dtype: int64
      
      s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158},
               index=["부산", "서울", "인천", "대전"])
      s2
      # 부산    3393191
      # 서울    9631482
      # 인천    2632035
      # 대전    1490158
      # dtype: int64
      
## index 기반 연산
  - 두 series에 대해 연산을 하는 경우 index가 같은 data에 대해서만 계산
    - ```py
      ds = s - s2
      ds
      # 대구         NaN
      # 대전         NaN
      # 부산     55546.0
      # 서울    272830.0
      # 인천    258416.0
      # dtype: float64
      
      s.values - s2.values # array([ 6511121, -6182745,   258416,   975894])
      
      ds.notnull()
      # 대구    False
      # 대전    False
      # 부산     True
      # 서울     True
      # 인천     True
      # dtype: bool
      
      ds[ds.notnull()]
      # 부산     55546.0
      # 서울    272830.0
      # 인천    258416.0
      # dtype: float64
      
      rs = (s - s2) / s2 * 100  # 인구 증가율
      rs = rs[rs.notnull()]
      rs
      # 부산    1.636984
      # 서울    2.832690
      # 인천    9.818107
      # dtype: float64
      
## data 갱신 / 추가 / 삭제
  - indexing을 이용해서 dictionary처럼 data 갱신(update) / 추가(add) 가능
    - ```py
      rs["부산"] = 1.63
      rs
      # 부산    1.630000
      # 서울    2.832690
      # 인천    9.818107
      # dtype: float64
      
      rs["대구"] = 1.41
      rs
      # 부산    1.630000
      # 서울    2.832690
      # 인천    9.818107
      # 대구    1.410000
      # dtype: float64
      
      del rs["서울"]
      rs
      # 부산    1.630000
      # 인천    9.818107
      # 대구    1.410000
      # dtype: float64
