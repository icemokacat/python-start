
# 파이썬 지원 자료형
"""
int, float, bool, str, list(시퀀스)
complex : 복소수
tuple: 튜플 (시퀀스)
set : 집합 
dict : 사전
"""

# 사전 (json map?) (java 의 hashmap)
dict = {
    "name": "machine Learning",
    "version": 2.0
}
print(dict.get('name'))

# 튜플
tuple = (7,8,9)
# set
set = {7,8,9}

"""
튜플 : 순서 O, 중복허용, 불변 , 인덱싱(특정 순서 값 조회) 가능
셋 : 순서 X, 중복 불가능, 가변, 인덱싱 불가능 (순서가 없으므로)  
"""
t = (1, 2, 2, 3)
print(t)
print(t[0])

s = {1, 2, 2, 3}
print(s)
# => 자동으로 중복 제거
s.add(4)
s.add(2)
# => 가능

## 튜플의 java14+ 의 Record 와 비슷 "여러 값을 묶어 놓은 불변 객체"
## Set 은 java 의 hashset 

X = -70
### 숫자형 연산자
# 절대값
abs(X) 
## 