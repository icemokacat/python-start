# =====================================================================
# Chapter 04 복습 연습문제 (2)
#   자료형 / 형변환 / 숫자 함수 / 리스트 / 튜플 / 셋 / 딕셔너리
# ---------------------------------------------------------------------
# 제약: chapter04 까지 아직 안 배운 for / while 은 사용하지 말 것.
#       (반복이 필요하면 print 를 여러 번 호출하거나 슬라이싱/내장함수로 해결)
# 정답 확인:  python chapter04/practice2.py
#            (풀이 예시: chapter04/practice2_answers.py)
# =====================================================================


# ---------------------------------------------------------------------
# 문제 1. 자료형 확인 - type()
# ---------------------------------------------------------------------
# 아래 6개 값의 자료형을 예측해서 주석에 적고, print(type(...)) 로 확인하라.
#
# 참고: https://docs.python.org/ko/3/library/functions.html#type
# 참고: https://docs.python.org/ko/3/library/stdtypes.html
s1 = (10, 20)
s2 = [10, 20]
s3 = {10, 20}
s4 = {"a": 1}
s5 = 3 + 4j
s6 = (10 == 10)
# TODO: print 6번  (예측도 주석으로)
#
# 기대 출력:
# <class 'tuple'>
# <class 'list'>
# <class 'set'>
# <class 'dict'>
# <class 'complex'>
# <class 'bool'>


# ---------------------------------------------------------------------
# 문제 2. divmod() / abs() / 형 변환
# ---------------------------------------------------------------------
# (1) 문자열 금액 amount 를 int 로 바꿔 people 명이 똑같이 나눠 가질 때
#     "1인당 금액" 과 "남는 금액" 을 divmod 로 구해 한 줄에 출력하라.
# (2) low, high 두 정수의 차이를 abs 로 출력하라. (순서와 무관하게 양수)
#
# 참고: https://docs.python.org/ko/3/library/functions.html#divmod
# 참고: https://docs.python.org/ko/3/library/functions.html#abs
amount = "1000000"
amount = int(amount)
people = 7
moc, remain = divmod(amount,people)
print(f'{moc} {remain}')
low, high = 5, -3

import math
temp = abs(low-high)
print(temp)

# TODO:
#
# 기대 출력:
# 142857 1
# 8


# ---------------------------------------------------------------------
# 문제 3. 중첩 리스트 인덱싱 + 슬라이싱
# ---------------------------------------------------------------------
# data 로부터 아래 3가지를 인덱싱/슬라이싱만으로 만들어 출력하라.
#  (1) 마지막 요소(리스트) 안에서 인덱스 1~2 (Base, Captain)
#  (2) data 전체를 거꾸로
#  (3) data 의 앞 2개
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#common-sequence-operations
# 참고: https://docs.python.org/ko/3/reference/expressions.html#slicings
data = [100, 200, ["Ace", "Base", "Captain", "Delta"]]
# TODO: print 3번
print(data[-1][1:3])
print(list(reversed(data)))
print(data[:2])
#
# 기대 출력:
# ['Base', 'Captain']
# [['Ace', 'Base', 'Captain', 'Delta'], 200, 100]
# [100, 200]


# ---------------------------------------------------------------------
# 문제 4. 리스트 연산 (+, *) 과 str() 형 변환
# ---------------------------------------------------------------------
#  (1) nums 뒤에 40 을 붙인 새 리스트를 출력하라. ( + 연산 )
#  (2) tags 를 3번 반복한 리스트를 출력하라. ( * 연산 )
#  (3) "num=" 뒤에 nums[0] 을 이어 붙여 출력하라. (숫자는 str 로 형변환 필요)
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#common-sequence-operations
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#str
nums = [10, 20, 30]
new1 = [40]
print(nums+new1)
tags = ["a", "b"]
print(tags * 3)
print("num="+str(nums[0]))
# TODO: print 3번
#
# 기대 출력:
# [10, 20, 30, 40]
# ['a', 'b', 'a', 'b', 'a', 'b']
# num=10


# ---------------------------------------------------------------------
# 문제 5. 리스트 메서드 조합 (반복문 금지)
# ---------------------------------------------------------------------
# box 에서 시작해 아래 순서대로 조작하라.
#  (1) 오름차순 정렬
#  (2) 값 2 가 몇 개인지 count 로 출력
#  (3) 인덱스 0 위치에 99 를 삽입(insert)
#  (4) 마지막 요소를 pop 해서 그 값을 출력
#  (5) 값 2 를 하나 제거(remove)한 뒤 리스트를 출력
#
# 참고: https://docs.python.org/ko/3/tutorial/datastructures.html#more-on-lists
box = [5, 2, 8, 1, 2]
box.sort()
box.count(2)
box.insert(0,99)
print(box.pop())
box.remove(2)
print(box)
# TODO:
#
# 기대 출력:
# 2
# 8
# [99, 1, 2, 5]


# ---------------------------------------------------------------------
# 문제 6. 참조(alias) vs 복사(copy) 와 id()
# ---------------------------------------------------------------------
# (a) 아래 두 print 의 결과를 예측해서 주석으로 적어라.
# (b) clone 은 origin 을 건드리지 않고 99 만 추가되도록 그 줄을 고쳐라.
#
# 참고: https://docs.python.org/ko/3/library/copy.html
# 참고: https://docs.python.org/ko/3/library/functions.html#id
origin = [1, 2, 3]
alias = origin
alias.append(4)
# print(origin)                   # 예측: ?
# print(id(origin) == id(alias))  # 예측: ?

clone = origin            # <-- 이 줄을 고쳐야 함
clone.append(99)
# print(origin)   # 기대: [1, 2, 3, 4]   (99 가 들어가면 안 됨)


# ---------------------------------------------------------------------
# 문제 7. 튜플 패킹 / 언패킹 / swap
# ---------------------------------------------------------------------
#  (1) 임시 변수 없이 x, y 를 서로 바꿔라.
#  (2) 괄호 없이 10, 20, 30 을 packed 에 패킹하고 type 을 출력하라.
#  (3) packed 를 a, b, c 로 언패킹하라.
#  (4) 확장 언패킹으로 first=첫 값, last=마지막 값, middle=나머지(리스트).
#
# 참고: https://docs.python.org/ko/3/tutorial/datastructures.html#tuples-and-sequences
# 참고: https://peps.python.org/pep-3132/
x, y = 1, 2
y, x = x, y
packed = 10, 20, 30
print(type(packed))
seq = (1, 2, 3, 4, 5)
# TODO:
#
# 기대 출력:
# 2 1
# <class 'tuple'>
# 10 20 30
# 1 [2, 3, 4] 5


# ---------------------------------------------------------------------
# 문제 8. 튜플의 불변성 + index()
# ---------------------------------------------------------------------
# (1) 값 3 의 인덱스를 index() 로 출력하라.
# (2) t + (9,) 결과를 출력하라. (원본 t 는 그대로다)
# (3) 아래 세 줄 중 "에러가 나는" 것에 주석으로 표시하고 이유를 적어라.
#       t[0] = 100
#       t = t + (9,)
#       t.append(9)
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#tuple
t = (5, 2, 3, 1, 4)
print(t.index(3))
print(t + (9,))
# TODO: print 2번 + 주석
#
# 기대 출력:
# 2
# (5, 2, 3, 1, 4, 9)


# ---------------------------------------------------------------------
# 문제 9. 딕셔너리 - get 기본값 / 추가 / in
# ---------------------------------------------------------------------
# (1) 'stock' 키가 없으면 0 을 반환하도록 get 을 써서 출력하라.
# (2) 'stock' 키를 10 으로 추가하라.
# (3) 'stock' in item 결과를 출력하라.
# (4) 다시 item.get('stock', 0) 을 출력하라.
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#dict
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#dict.get
item = {"name": "mouse", "price": 15000}
item['stock'] = 10
print(item.get('stock', 0))
# TODO:
#
# 기대 출력:
# 0
# True
# 10


# ---------------------------------------------------------------------
# 문제 10. 딕셔너리 - keys / values / pop / update
# ---------------------------------------------------------------------
# (1) 키들을 리스트로 만들어 출력하라.
# (2) 값들을 리스트로 만들어 출력하라.
# (3) d.pop('b') 의 반환값을 출력하고, 그 뒤 d 를 출력하라.
# (4) d.update(a=100, z=9) 후 d 를 출력하라.
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#dict
d = {"a": 1, "b": 2, "c": 3}
# TODO:
print(list(d.keys()))
print(list(d.values()))
print(d.pop('b'))
d.update(a=100, z=9)
print(d)
#
# 기대 출력:
# ['a', 'b', 'c']
# [1, 2, 3]
# 2
# {'a': 1, 'c': 3}
# {'a': 100, 'c': 3, 'z': 9}


# ---------------------------------------------------------------------
# 문제 11. 셋(set) - 중복 제거 / add / 집합 연산
# ---------------------------------------------------------------------
# (1) raw 의 중복을 제거한 원소 개수를 출력하라.
# (2) 3 과 4 를 add 한 뒤 정렬된 리스트로 출력하라. (sorted 사용)
# (3) {1,2,3,4} 와 {3,4,5} 의 교집합을 정렬된 리스트로 출력하라.
# (4) {1,2,3,4} 에서 {3,4,5} 를 뺀 차집합을 정렬된 리스트로 출력하라.
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#set-types-set-frozenset
raw = [1, 1, 2, 2, 3]
raw2 = set(raw)
print(len(raw2))

# TODO: print 4번
#
# 기대 출력:
# 3
# [1, 2, 3, 4]
# [3, 4]
# [1, 2]
