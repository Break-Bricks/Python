## 기술 통계 (descriptive statistics)
  - data 집합에 대해 간단한 통계를 계산하는 함수들 제공
    - ```py
      x = np.array([18, 5, 10, 23, 19, -8, 10,   0,  0,  5,  2,  15,   8,
                     2, 5,  4, 15, -1,  4, -7, -24,  7,  9, -6,  23, -13])
    - data 개수
      - ```py
        len(x) # 26
    - 표본 평균
      - ```py
        np.mean(x) # 4.8076923076923075
    - 표본 분산
      - ```py
        np.var(x) # 115.23224852071006
        np.var(x, ddof=1) # 비편향 분산
    - 표본 표준편차
      - ```py
        np.std(x) # 10.734628476137871
    - 최댓값 / 최솟값
      - ```py
        np.max(x) # 23
        np.min(x) # -24
    - 중앙값
      - ```py
        np.median(x) # 5.0
    - 사분위수(quartile) / 백분위수(percentile)
      - ```py
        np.percentile(x, 0) # -24.0 (최솟값)
        np.percentile(x, 25) # 0.0 (1사분위 수)
        np.percentile(x, 50) # 5.0 (2사분위 수)
        np.percentile(x, 100) # 23.0 (4사분위 수)
