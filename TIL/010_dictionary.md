## 자료의 개수
  - ```py
    x = {"a": 10, "b": 20}
    len(a) # 2
    
## 자료의 갱신 / 추가 / 삭제
  - 갱신 : 걍 대입해서 쓰면 됨
    - ```py
      x["a"] = 30
      x # {'a': 30, 'b': 20}
  - 추가 : 새로운 키(기존에 존재하지 않아야 함)와 이에 대응하는 값 대입해서 추가
    - ```py
      x["c"] = 40
      x # {'a': 30, 'b': 20, 'c': 40}
  - 삭제 : `del` 명령어 사용
    - ```py
      del x["b"]
      x # {'a': 30, 'c': 40}

## 키 확인
  - dictionary 자료에 특정한 키가 있는지 없는지 알기 위해서는 `in` 명령어 사용
  - 해당 키가 존재하면 True, 존재하지 않으면 False 반환
    - ```py
      "a" in x # True
      "d" in x # False
      
## dictionary 자료형의 반복
  - dictionary 자료형에 있는 data도 for loop에 넣을 수 있지만
  - dictionary 자료형은 내부적으로 자료의 순서를 보장하지 않음
    - ```py
      for k in x:
          print(k)
      # a
      # c
  - 키 반복
    - ```py
      x.keys() # dictionary 자료의 키 목록을 list로 반환 -> dict_keys(['a', 'c'])
      for k in x.keys():
          print(k)
      # a
      # c
  - 값 반복
    - ```py
      x.values() # dictionary 자료의 값 목록을 list로 반환 -> dict_values([30, 40])
      for v in x.values():
          print(v)
      # 30
      # 40
  - 키와 값 쌍을 반복
    - `items` method 사용
    - for 다음의 카운터 변수를 두 개 지정 (첫번째 키, 두번째 값)
    - ```py
      for k, v in x.items():
          print("key [%s] => value [%d]" % (k, v))
      # key [a] => value [30]
      # key [c] => value [40]
