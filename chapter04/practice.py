# =====================================================================
# Chapter 04 복습 연습문제
#   (자료형 / 형변환 / 숫자 함수 / 리스트 / 튜플 / 셋 / 딕셔너리)
# ---------------------------------------------------------------------
# - 각 문제의 TODO 부분을 직접 채워서 "기대 출력"과 같아지도록 만든다.
# - 정답 확인:  python chapter04/practice.py
# =====================================================================


# ---------------------------------------------------------------------
# 문제 1. 형 변환 - 문자열 가격 목록의 합계
# ---------------------------------------------------------------------
# 문자열로 들어온 가격들을 int 로 바꿔 총합을 구하고,
# 평균은 float 로 소수 1자리까지 출력하라. (합계/개수)
#
# 참고: https://docs.python.org/ko/3/library/functions.html#int
# 참고: https://docs.python.org/ko/3/library/functions.html#float
prices = ["1200", "3400", "5000", "800"]
# TODO:
total = int(prices[0]) + int(prices[1]) + int(prices[2]) + int(prices[3])
print(total)
avg = ( total / len(prices) )
print('{:.1f}'.format(avg))
# total = ...
# avg = ...
# print(total, f"{avg:.1f}")
#
# 기대 출력:
# 10400 2600.0


# ---------------------------------------------------------------------
# 문제 2. divmod() - 초를 시/분/초로 변환
# ---------------------------------------------------------------------
# 총 seconds 를 "H시 M분 S초" 형태로 출력하라. (divmod 2번 사용)
#
# 참고: https://docs.python.org/ko/3/library/functions.html#divmod
seconds = 3661
# TODO:
# 61분
m,s = divmod(seconds,60)
h,m = divmod(m,60)
print(f'{h}시 {m}분 {s}초')
# ...
# print(f"{h}시 {m}분 {s}초")
#
# 기대 출력:
# 1시 1분 1초


# ---------------------------------------------------------------------
# 문제 3. 리스트 슬라이싱
# ---------------------------------------------------------------------
# nums 로부터 아래 4가지를 슬라이싱만으로 만들어 출력하라.
#  (1) 앞의 3개
#  (2) 뒤의 2개
#  (3) 전체를 거꾸로
#  (4) 짝수 인덱스(0,2,4...)의 값들
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#common-sequence-operations
# 참고: https://docs.python.org/ko/3/reference/expressions.html#slicings
nums = [10, 20, 30, 40, 50, 60, 70]
# TODO: print 4번
print(nums[:3])
print(nums[-2:])
print(list(reversed(nums)))
#
# 기대 출력:
# [10, 20, 30]
# [60, 70]
# [70, 60, 50, 40, 30, 20, 10]
# [10, 30, 50, 70]


# ---------------------------------------------------------------------
# 문제 4. 리스트 메서드 - 목표 리스트 만들기
# ---------------------------------------------------------------------
# data 에서 시작해 아래 순서대로 조작하여 최종 리스트를 만들어라.
#  (1) 오름차순 정렬
#  (2) 값 100 을 인덱스 0 위치에 삽입
#  (3) 마지막 요소를 꺼낸다(pop) - 꺼낸 값도 출력
#  (4) 값 3 을 제거(remove)
#
# 참고: https://docs.python.org/ko/3/tutorial/datastructures.html#more-on-lists
data = [5, 2, 8, 3, 1]
# TODO:
data.sort()
data.insert(0,100)
print(data.pop())
data.remove(3)
print(data)
# ...
# print("popped:", popped)
# print(data)
#
# 기대 출력:
# popped: 8
# [100, 1, 2, 5]


# ---------------------------------------------------------------------
# 문제 5. 얕은 복사 vs 참조
# ---------------------------------------------------------------------
# (a) 아래 print 의 결과를 예측해서 주석으로 적어라.
# (b) origin 을 건드리지 않고 clone 에만 99 를 추가하도록 코드를 고쳐라.
#
# 참고: https://docs.python.org/ko/3/library/copy.html
# 참고: https://docs.python.org/ko/3/tutorial/datastructures.html#more-on-lists  (list.copy)
origin = [1, 2, 3]
alias = origin
alias.append(4)
# print(origin)   # 예측: ?

clone = origin            # <-- 이 줄을 고쳐야 함
clone.append(99)
# print(origin)   # 기대: [1, 2, 3, 4]  (99 가 들어가면 안 됨)


# ---------------------------------------------------------------------
# 문제 6. 셋(set) - 중복 제거와 집합 연산
# ---------------------------------------------------------------------
# 두 리스트에 대해 아래를 구해 출력하라.
#  (1) a 의 중복을 제거한 원소 개수
#  (2) 공통으로 들어있는 값 (교집합), 정렬된 리스트로
#  (3) a 에만 있고 b 에는 없는 값 (차집합), 정렬된 리스트로
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#set-types-set-frozenset
a = [1, 2, 2, 3, 3, 3, 4]
b = [3, 4, 5, 6]
setA = set(a)
n = []

# TODO: print 3번
#
# 기대 출력:
# 4
# [3, 4]
# [1, 2]


# ---------------------------------------------------------------------
# 문제 7. 튜플 패킹 / 언패킹
# ---------------------------------------------------------------------
# (1) 임시 변수 없이 x, y 값을 서로 바꿔라(swap).
# (2) 확장 언패킹으로 first 에 첫 값, last 에 마지막 값,
#     middle 에 나머지(리스트)를 담아라.
#
# 참고: https://docs.python.org/ko/3/tutorial/datastructures.html#tuples-and-sequences
# 참고: https://peps.python.org/pep-3132/   (확장 언패킹  first, *rest = ...)
x, y = 10, 20
# TODO: swap
y, x = x, y
# print(x, y)   # 기대: 20 10

scores = (90, 80, 70, 60, 50)
# TODO: first, *middle, last = ...
# print(first, middle, last)   # 기대: 90 [80, 70, 60] 50


# ---------------------------------------------------------------------
# 문제 8. 딕셔너리 - get 기본값과 순회
# ---------------------------------------------------------------------
# (1) 'stock' 키가 없으면 0 을 반환하도록 get 을 사용해 출력하라.
# (2) items() 로 순회하며 "key=value" 형태를 한 줄씩 출력하라.
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#dict
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#dict.get
item = {"name": "keyboard", "price": 27000}
# TODO:

# print(item.get(...))
# for k, v in ...:
#     print(f"{k}={v}")
#
# 기대 출력:
# 0
# name=keyboard
# price=27000
