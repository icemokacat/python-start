import sys
from pathlib import Path

# 스크립트 실행 시 sys.path[0]은 이 파일이 있는 chap_class/ 이다.
# sub 패키지는 프로젝트 루트에 있으므로 루트를 검색 경로에 넣는다.
sys.path.append(str(Path(__file__).parent.parent))

# 길게 안쓰려면 (패키지 구조가 복잡할때)
from sub.sub1 import module1 as m2

print(m2)