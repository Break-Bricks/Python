# set으로 바꾼 후 다시 list로 변환 (원래 순서가 유지 안될 수 있음)
duplicate_list = ['안','녕','하','세','요','세','요']
cleaned_list = list(set(duplicate_list))
# -> ['세','녕','안','하','요']

# dict.fromkeys()를 이용해서
# 1) 먼저 리스트의 값이 key가 되는 딕셔너리를 만든 후
# 2) 딕셔너리를 다시 리스트로 변환하면 순서가 유지되지 않는 위의 문제점을 해결하면서 중복된 값을 제거할 수 있다.
duplicate_list = ['안','녕','하','세','요','세','요']
tmp = dict.fromkeys(duplicate_list)
cleaned_list2 = list(tmp)
# -> ['안','녕','하','세','요']
