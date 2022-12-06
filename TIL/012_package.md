## package import
  - package 설치 후
  - 사용하려면 import 해야 함
    - ```py
      import 패키지이름
      import 패키지이름 as 패키지별명
      import sklearn as sk
  - 일부 하위 패키지는 자동으로 import 되지 않아서 수동으로 해줘야 함
    - ```py
      import sklearn.preprocessing
  - 특정 명령어들만 선택적으로 import 가능
    - ```py
      from 패키지이름 import 명령어
      from 패키지이름 import 명령어1, 명령어2, 명령어3
      from numpy import arange
      arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  - 패키지 안의 모든 명령을 선택적 import할 때는 명령어 이름 대신 * 기호 사용
    - wild import
    - 기존의 변수나 함수를 덮어쓸 수 있어서 사용에 주의
    - ```py
      from scipy.stats import *
    
## package 내용 보기
  - dir(패키지이름 or 패키지별명)
  - ```py
    dir(sk)
    # ['_ASSUME_FINITE',
    #  '__SKLEARN_SETUP__',
    #  '__all__',
    #  '__builtins__',
    #  '__cached__',
    #  '__check_build',
    #  '__doc__',
    #  '__file__',
    #  '__loader__',
    #  '__name__',
    #  '__package__',
    #  '__path__',
    #  '__spec__',
    #  '__version__',
    #  '_contextmanager',
    #  'base',
    #  'clone',
    #  'config_context',
    #  'exceptions',
    #  'externals',
    #  'get_config',
    #  'logger',
    #  'logging',
    #  'os',
    #  're',
    #  'set_config',
    #  'setup_module',
    #  'sys',
    #  'utils',
    # 'warnings']
