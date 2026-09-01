# =====================================================================
# Chapter 02 복습 연습문제  (print / 문자열 포매팅 / 변수 / type / id)
# ---------------------------------------------------------------------
# - 각 문제의 TODO 부분을 직접 채워서 "기대 출력"과 같아지도록 만든다.
# - 정답 확인:  python chapter02/practice.py
# =====================================================================


# ---------------------------------------------------------------------
# 문제 1. print() 의 sep 옵션 + 자리수 채우기
# ---------------------------------------------------------------------
# year, month, day 를 "한 번의" print() 호출로 아래처럼 출력하라.
# 단, 월/일이 한 자리면 앞에 0을 붙여 두 자리로 맞춘다. (sep 옵션 사용)
#
# 참고: https://docs.python.org/ko/3/library/functions.html#print
# 참고: https://docs.python.org/ko/3/library/string.html#format-specification-mini-language
year, month, day = 2026, 9, 1
# TODO:
#print(year,month,day,sep='')
print('{:4}-{:0>2}-{:0>2}'.format(year,month,day))
# print(...)
#
# 기대 출력:
# 2026/09/01


# ---------------------------------------------------------------------
# 문제 2. % 포매팅 - 표 형태 정렬
# ---------------------------------------------------------------------
# 아래 상품들을 한 줄에 하나씩,
# 이름은 왼쪽 정렬 10칸, 가격은 오른쪽 정렬 8칸 + 소수 2자리로 출력하라.
# (% 연산자만 사용. .format / f-string 금지)
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#printf-style-string-formatting
# TODO: for 문으로 출력
products = [("Apple", 1500.0), ("Milk", 2450.5), ("Coffee", 12000.9)]
print('%-10s %8.2f' % (products[0][0],products[0][1]))
print('%-10s %8.2f' % (products[1][0],products[1][1]))
print('%-10s %8.2f' % (products[2][0],products[2][1]))
#
# 기대 출력:
# Apple        1500.00
# Milk         2450.50
# Coffee      12000.90


# ---------------------------------------------------------------------
# 문제 3. str.format() - 인덱스 재정렬 + 이름 있는 필드
# ---------------------------------------------------------------------
# 아래 값을 str.format() "하나"로 조합해서 출력하라.
#  - 위치 인자의 순서를 바꿔 쓰고(성 먼저, 이름 나중),
#  - 나이는 이름 있는 필드({age})로 받는다.
#
# 참고: https://docs.python.org/ko/3/library/string.html#formatstrings
first, last, age = "Minsu", "Lee", 30
# TODO:
print('{1} {0} (age: {2})'.format(first,last,age))
# text = "...".format(...)
# print(text)
#
# 기대 출력:
# Lee Minsu (age: 30)


# ---------------------------------------------------------------------
# 문제 4. f-string - 천 단위 구분 기호 + 정렬
# ---------------------------------------------------------------------
# 아래 항목들을 영수증 한 줄처럼 출력하라.
#  - 품목명: 왼쪽 정렬 8칸
#  - 금액  : 오른쪽 정렬 12칸, 1000단위 콤마
#
# 참고: https://docs.python.org/ko/3/reference/lexical_analysis.html#f-strings
# 참고: https://docs.python.org/ko/3/library/string.html#format-examples
# (참고: 포맷 폭은 '문자 개수' 기준이라, 한글은 터미널에서 살짝 어긋나 보일 수 있다)
cart = [("노트북", 1350000), ("마우스", 29000), ("USB", 8900)]
# TODO: for 문으로 f"{name:<8}{price:>12,}" 형태로 출력
print(f'{cart[0][0]:<8}{cart[0][1]:>12,}')
print(f'{cart[1][0]:<8}{cart[1][1]:>12,}')
print(f'{cart[2][0]:<8}{cart[2][1]:>12,}')
#
# 기대 출력:
# 노트북             1,350,000
# 마우스                29,000
# USB                    8,900


# ---------------------------------------------------------------------
# 문제 5. 문자열 절삭 + 채우기 조합
# ---------------------------------------------------------------------
# 문자열 title 을 아래 규칙으로 출력하라.
#  - 전체 20칸 확보, 가운데 정렬, 남는 칸은 '=' 로 채움
#  - 단, 원본이 길어도 앞에서 8글자까지만 사용(절삭)
#
# 참고: https://docs.python.org/ko/3/library/string.html#format-specification-mini-language
title = "python-programming"
# TODO:
print(f'{title:=^20}')
# print(f"...")
#
# 기대 출력:
# ======python-p======


# ---------------------------------------------------------------------
# 문제 6. type() 로 자료형 이름 얻기
# ---------------------------------------------------------------------
# 값을 받아 자료형 이름 문자열('int', 'str' ...)을 돌려주는 함수를 완성하라.
# (힌트: type(x).__name__)
#
# 참고: https://docs.python.org/ko/3/library/functions.html#type
print(type(2))
def type_name(x):
    clname = type(x).__name__
    return clname
    # TODO: return ...
    pass
print(type_name(10))

# 확인용
# print(type_name(10))        # -> int
# print(type_name(3.14))      # -> float
# print(type_name("hi"))      # -> str
# print(type_name([1, 2]))    # -> list
# print(type_name((1,)))      # -> tuple
# print(type_name({1: 2}))    # -> dict


# ---------------------------------------------------------------------
# 문제 7. id() 와 is - 같은 객체 판별
# ---------------------------------------------------------------------
# 아래 코드의 결과를 먼저 "예측"해서 주석으로 적고, 실행해 확인하라.
# 왜 그런 결과가 나오는지도 한 줄로 적어본다.
#
# 참고: https://docs.python.org/ko/3/library/functions.html#id
# 참고: https://docs.python.org/ko/3/reference/expressions.html#is
a = [1, 2, 3]
b = a
c = a.copy()
# print(a is b, id(a) == id(b))   # 예측:  true
# print(a is c, id(a) == id(c))   # 예측:  false
# 이유:
