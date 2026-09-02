# =====================================================================
# chap_function 복습 연습문제
#   함수 정의(def) / return / 다중 반환 / *args / **kwargs / lambda /
#   함수를 인자로 넘기기(고차 함수)
# ---------------------------------------------------------------------
# 제약: chap_function(f1.py) 까지 배운 문법만 사용한다.
#   사용 가능:
#     - def, return, 다중 반환(return a, b), 위치 인자 / 키워드 인자 호출
#     - *args, **kwargs, (위치, *args, **kwargs) 혼합 매개변수
#     - lambda, 함수를 다른 함수의 인자로 전달
#     - 이전 챕터 전부: if / elif / else, for ~ in, range(), while,
#       break, for-else, 슬라이싱, f-string / .format() / %,
#       리스트 / 튜플 / 셋 / 딕셔너리 메서드, len(), sum(), sorted(),
#       reversed(), enumerate()
#   사용 금지 (아직 안 배움):
#     - class (다음 챕터)
#     - 매개변수 기본값  def f(x, y=10)
#     - 리스트 / 딕셔너리 컴프리헨션
#     - map / filter / zip
#     - 예외처리 try / except
#     - 중첩 함수 / 클로저 / global / 데코레이터 / 재귀 호출
# 실행:  python chap_function/practice.py
#        (풀이 예시: chap_function/practice_answers.py)
# =====================================================================


# ---------------------------------------------------------------------
# 문제 1. 기본 함수 정의 + 호출 (반환값 없음)
# ---------------------------------------------------------------------
# 이름 name 을 받아  "안녕하세요, {name}님!"  을 출력하는 함수 greet 를 정의하고
# "Kim", "Park" 두 번 호출하라. (return 없이 print 만)
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#defining-functions
# TODO: def greet(name): ...
#
# 기대 출력:
# 안녕하세요, Kim님!
# 안녕하세요, Park님!


# ---------------------------------------------------------------------
# 문제 2. return 이 있는 함수
# ---------------------------------------------------------------------
# 두 수 a, b 를 받아 합을 "돌려주는"(return) 함수 add 를 정의하라.
# add(7, 5) 결과를 변수에 담아 출력하고, add(100, 200) 은 바로 출력하라.
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#defining-functions
# TODO:
#
# 기대 출력:
# 12
# 300


# ---------------------------------------------------------------------
# 문제 3. 다중 반환 + 언패킹
# ---------------------------------------------------------------------
# 리스트 numbers 를 받아 (최솟값, 최댓값) 을 return 하는 함수 min_max 를 정의하라.
# (min / max 내장 함수를 쓰지 말고 for 로 직접 비교할 것)
# lo, hi 로 언패킹해서 출력하고, 반환값 자체도 그대로 출력하라. (튜플로 찍힘)
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#defining-functions
numbers = [3, 9, 1, 7, 5]
# TODO:
#
# 기대 출력:
# 1 9
# (1, 9)


# ---------------------------------------------------------------------
# 문제 4. *args - 넘어온 모든 값의 합
# ---------------------------------------------------------------------
# 인자를 몇 개든 받아서 전부 더한 값을 return 하는 함수 total 을 정의하라.
# 인자가 하나도 없으면 0 을 반환해야 한다.
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#arbitrary-argument-lists
# TODO:
# print(total(1, 2, 3))
# print(total(10, 20, 30, 40))
# print(total())
#
# 기대 출력:
# 6
# 100
# 0


# ---------------------------------------------------------------------
# 문제 5. *args - 평균 (빈 인자 방어)
# ---------------------------------------------------------------------
# 인자를 몇 개든 받아 평균(합 / 개수)을 return 하는 함수 average 를 정의하라.
# 인자가 없으면 0 을 반환한다. (힌트: if not args)
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#arbitrary-argument-lists
# TODO:
# print(average(10, 20, 30))
# print(average(4, 5))
# print(average())
#
# 기대 출력:
# 20.0
# 4.5
# 0


# ---------------------------------------------------------------------
# 문제 6. **kwargs - 키=값 한 줄씩 출력
# ---------------------------------------------------------------------
# 키워드 인자를 몇 개든 받아  "키 = 값"  형태로 한 줄씩 출력하는
# 함수 show_profile 을 정의하고  name="Lee", age=20  으로 호출하라.
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#keyword-arguments
# TODO:
#
# 기대 출력:
# name = Lee
# age = 20


# ---------------------------------------------------------------------
# 문제 7. **kwargs - 값들의 합
# ---------------------------------------------------------------------
# 과목명=점수 형태의 키워드 인자를 받아 점수의 총합을 return 하는
# 함수 sum_scores 를 정의하라.
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#keyword-arguments
# TODO:
# print(sum_scores(kor=90, eng=80, math=100))
#
# 기대 출력:
# 270


# ---------------------------------------------------------------------
# 문제 8. 위치 인자 + *args + **kwargs 혼합
# ---------------------------------------------------------------------
# 첫 번째 인자는 title 로 받고, 나머지 위치 인자는 *items, 키워드 인자는 **options
# 로 받아 아래처럼 출력하는 함수 describe 를 정의하라.
#
#   describe("cart", "apple", "milk", coupon=True, point=500)
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#arbitrary-argument-lists
# TODO:
def describe(title, *items, **options):
    print('title: {}'.format(title))
    print('items: {}'.format(items))
    print('options: {}'.format(options))
describe("cart", "apple", "milk", coupon=True, point=500)    
#
# 기대 출력:
# title: cart
# items: ('apple', 'milk')
# options: {'coupon': True, 'point': 500}


# ---------------------------------------------------------------------
# 문제 9. lambda 기본
# ---------------------------------------------------------------------
# (1) 한 수를 받아 제곱을 돌려주는 lambda 를 square 라는 이름에 담아 square(5) 출력
# (2) 두 수를 받아 합을 돌려주는 lambda 를 add2 라는 이름에 담아 add2(3, 4) 출력
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#lambda-expressions
# TODO:
square = lambda x: x * x
add2 = lambda x,y: x + y
print(square(5))
print(add2(3,4))
#
# 기대 출력:
# 25
# 7


# ---------------------------------------------------------------------
# 문제 10. 함수를 인자로 받는 함수 (고차 함수)
# ---------------------------------------------------------------------
# calc(a, b, func) 는 func(a, b) 의 결과를 return 한다. 이 함수를 정의하고
#  (1) 곱셈 함수 mul 을 따로 def 로 정의해서 calc(6, 7, mul) 출력
#  (2) 덧셈 lambda 를 바로 넘겨서 calc(6, 7, lambda a, b: a + b) 출력
#
# 참고: f1.py 의 func_final 예제
# TODO:
def calc(a, b, func):
    return func(a,b)

mul = lambda x,y: x * y
print(calc(6,7,mul))

def add3(a,b):
    return a+b

print(calc(6,7,add3))

#
# 기대 출력:
# 42
# 13


# ---------------------------------------------------------------------
# 문제 11. lambda + 고차 함수 조합 (f1.py func_final 스타일)
# ---------------------------------------------------------------------
# run(x, y, func) 는  x * y * func(2, 3)  을 계산해서 출력한다.
# 이 함수를 정의하고  run(10, 10, lambda a, b: a + b)  로 호출하라.
#  ( 10 * 10 * (2 + 3) = 500 )
#
# TODO:
#
# 기대 출력:
# 500


# ---------------------------------------------------------------------
# 문제 12. 함수 안에서 for + if + 다중 반환, 그리고 f-string 으로 조립
# ---------------------------------------------------------------------
# 리스트 numbers 를 받아 (짝수 개수, 홀수 개수) 를 return 하는
# 함수 count_even_odd 를 정의하라.
# 반환값을 e, o 로 언패킹해서  "짝수 3개, 홀수 4개"  형태로 출력하라.
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#defining-functions
# TODO:
def count_even_odd(nums):
    c1 = 0
    c2 = 0
    for i in nums:
        if(i%2 == 0):
            c1 += 1
        else:
            c2 += 1
    return c1, c2

a2 = [1,2,3,4,5,6,7,8,9,10,11]
e,o = count_even_odd(a2)
print('짝수 {}개, 홀수 {}개'.format(e,o))
#
# 기대 출력:
# 짝수 3개, 홀수 4개
