
import sys
from pathlib import Path

print(sys.path)
# Python이 모듈을 import할 때 검색하는 경로 목록

print('-' * 20)

print(type(sys.path))
# 영구적으로 등록되는 것이 아님
sys.path.append(str(Path(__file__).parent.parent / "extra"))

print(sys.path)

# Pylance는 동적으로 추가된 sys.path 경로를 인식하지 못할 수 있지만, 실제 Python 실행 시에는 정상적으로 import됨
# import test_module

# 
import test_module

print(test_module.add(10, 20))