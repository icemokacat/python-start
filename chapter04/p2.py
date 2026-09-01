# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a))
print(type(b))
print(type(c))
print(type(d))
"""
<class 'float'>
<class 'int'>
<class 'float'>
<class 'float'>
"""

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True))
# => true:1 false:0 출력됨

print()
# 수치 연산 함수
x, y = divmod(100,8)
print(x,y)
# => 나눈 몫(x)과 나머지(y) 를 할당함

# 외부 모듈
import math

print(math.pi)