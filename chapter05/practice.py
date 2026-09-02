# =====================================================================
# Chapter 05 복습 연습문제
#   조건문(if / elif / else) / 반복문(for / range) / while / break / for-else
# ---------------------------------------------------------------------
# 제약: chapter05 까지 배운 문법만 사용한다.
#       사용 가능: if / elif / else, 비교/논리 연산, for ~ in, range(),
#                  중첩 for, break, for-else, while, while-else,
#                  len(), sum(), sorted(), reversed(), list(), tuple(),
#                  그리고 chapter04 까지 배운 모든 것(슬라이싱, f-string,
#                  딕셔너리/리스트/튜플/셋 메서드, %, // 등)
#       사용 금지: continue, enumerate, zip, map, filter,
#                  리스트/딕셔너리 컴프리헨션, 함수 정의(def), 예외처리
# 실행:  python chapter05/practice.py
#        (풀이 예시: chapter05/practice_answers.py)
# =====================================================================


# ---------------------------------------------------------------------
# 문제 1. if / elif / else - 점수로 등급 판정
# ---------------------------------------------------------------------
# score 값에 따라 등급을 한 줄 출력하라.
#   90 이상            -> "A"
#   80 이상 90 미만    -> "B"
#   70 이상 80 미만    -> "C"
#   그 외              -> "F"
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#if-statements
score = 83
# TODO: if / elif / else 로 등급 한 줄 출력
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
#
# 기대 출력:
# B


# ---------------------------------------------------------------------
# 문제 2. 참/거짓 판정 (truthiness)
# ---------------------------------------------------------------------
# 아래 4개의 값에 대해 각각 if 문을 써서
#   값이 참이면 그 값을 출력하고,
#   값이 거짓이면 "empty" 를 출력하라.
# (반복문 없이 if 문 4번)
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#truth-value-testing
val1 = "hello"
val2 = ""
val3 = 0
val4 = [1, 2]
# TODO: if 문 4번
if val1:
    print(val1)
else:
    print('empty')
# 기대 출력:
# hello
# empty
# empty
# [1, 2]


# ---------------------------------------------------------------------
# 문제 3. for + range - 누적 합
# ---------------------------------------------------------------------
# (1) 1 부터 50 까지의 합을 for 로 직접 더해서 출력하라.
# (2) 1 부터 50 까지의 수 중 짝수만 더해서 출력하라. (조건: 2 로 나눈 나머지)
#
# 참고: https://docs.python.org/ko/3/library/functions.html#func-range
# TODO: print 2번
sum = 0
for i in range(51):
    sum += i
print(sum)
print()
sum = 0 
for i in range(51):
    if(i%2 == 0):
        sum += i
print(sum)        
#
# 기대 출력:
# 1275
# 650


# ---------------------------------------------------------------------
# 문제 4. range(start, stop, step)
# ---------------------------------------------------------------------
# 3 부터 30 까지 3 의 배수를 공백으로 구분해 "한 줄"로 출력하라.
# (예: print(x, end=' ') 를 반복한 뒤 마지막에 print() 로 줄바꿈)
#
# 참고: https://docs.python.org/ko/3/library/functions.html#func-range
# TODO:
#
# 기대 출력:
# 3 6 9 12 15 18 21 24 27 30
for i in range(3,31,3):
    print(i, end= ' ')
else:
    print()

# ---------------------------------------------------------------------
# 문제 5. 중첩 for - 구구단 일부
# ---------------------------------------------------------------------
# 2단, 3단, 4단을 아래 형식으로 출력하라.
#   2 x 1 = 2
#   2 x 2 = 4
#   ...
#   4 x 9 = 36
# 각 단이 끝나면 빈 줄을 한 번 출력한다.
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#for-statements
# TODO: 바깥 for(단) 안에 안쪽 for(1~9)
for i in range(1,10):
    for v in range(1,10):
        print('{} x {} = {}'.format(i,v,(i*v)))
    else:
        print()
# 기대 출력(앞부분):
# 2 x 1 = 2
# 2 x 2 = 4
# ...


# ---------------------------------------------------------------------
# 문제 6. 리스트 순회 + 조건 카운트
# ---------------------------------------------------------------------
# nums 를 for 로 돌면서
#  (1) 10 이상인 값의 개수를 세어 출력하라.
#  (2) 홀수의 합을 구해 출력하라.
#
# 참고: https://docs.python.org/ko/3/tutorial/datastructures.html
nums = [3, 12, 7, 20, 5, 18, 9, 10]
# TODO: print 2번
cnt = 0
sum = 0
for i in nums:
    if(i >= 10):
        cnt += 1
    if(i%2 == 1):
        sum += i
print(cnt,sum) 
#
# 기대 출력:
# 4
# 24


# ---------------------------------------------------------------------
# 문제 7. range(len(...)) 로 인덱스와 값 함께 쓰기
# ---------------------------------------------------------------------
# names 를 순회하며 "1. Kim" 처럼 (순번). (이름) 형식으로 출력하라.
# 순번은 1 부터 시작한다.
#
# 참고: https://docs.python.org/ko/3/library/functions.html#len
names = ["Kim", "Park", "Lee", "Choi"]
# TODO: for i in range(len(names)) ...
for i in range(len(names)):
    print('{}. {}'.format(i+1,names[i]))
#
# 기대 출력:
# 1. Kim
# 2. Park
# 3. Lee
# 4. Choi


# ---------------------------------------------------------------------
# 문제 8. 딕셔너리 순회 - 합계와 최고점
# ---------------------------------------------------------------------
# scores 를 for 로 돌면서
#  (1) "이름: 점수" 형태로 한 줄씩 출력하라. (.items() 사용 가능)
#  (2) 점수의 합계를 출력하라.
#  (3) 가장 높은 점수를 가진 사람의 이름을 출력하라.
#      (max 함수 대신 for 로 직접 비교해서 찾을 것)
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#dict
scores = {"Kim": 85, "Park": 92, "Lee": 78, "Choi": 90}
# TODO:
for m in scores.keys():
    value = scores[m]
    print('{}: {}'.format(m,value))
#
# 기대 출력:
# Kim: 85
# Park: 92
# Lee: 78
# Choi: 90
# 345
# Park


# ---------------------------------------------------------------------
# 문제 9. break - 첫 번째 조건 만족 값 찾기
# ---------------------------------------------------------------------
# data 를 앞에서부터 순회하다가 "7 로 나누어떨어지는" 첫 값을 만나면
# 그 값을 출력하고 반복을 멈춰라(break).
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
data = [4, 9, 15, 22, 28, 35, 40]
for i in data:
    if(i%7 == 0):
        print(i)
        break
# TODO:
#
# 기대 출력:
# 28


# ---------------------------------------------------------------------
# 문제 10. for - else - 검색 실패 처리
# ---------------------------------------------------------------------
# words 안에 target 이 있으면 "found" 를 출력하고 반복을 멈춰라.
# 끝까지 없으면 (break 없이 for 가 끝나면) else 에서 "not found" 를 출력하라.
#
# 참고: https://docs.python.org/ko/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
words = ["apple", "banana", "cherry"]
target = "melon"
for w in words:
    if(target == w):
        print("found")
        break
else:
    print("not found")
# TODO: for ~ else
#
# 기대 출력:
# not found


# ---------------------------------------------------------------------
# 문제 11. while - 카운트다운
# ---------------------------------------------------------------------
# n 을 5 부터 1 까지 한 줄씩 출력하고, 마지막에 "start!" 를 출력하라.
#
# 참고: https://docs.python.org/ko/3/reference/compound_stmts.html#while
n = 5
# TODO:
while n > 0:
    print(n)
    n = n - 1
else:
    print("start!")
#
# 기대 출력:
# 5
# 4
# 3
# 2
# 1
# start!


# ---------------------------------------------------------------------
# 문제 12. while - 자릿수 다루기
# ---------------------------------------------------------------------
# 정수 num 의 각 자리 숫자의 합을 while 로 구해 출력하라.
# (규칙: num % 10 은 1의 자리 값, num // 10 은 그 자리를 뗀 나머지 수)
#
# 참고: https://docs.python.org/ko/3/reference/expressions.html#binary-arithmetic-operations
num = 4739
# TODO: while num > 0 ...
sum = 0
divider = 1000
while num > 0:
    x,y = divmod(num,divider)
    sum += x
    num = y
    if(num < 1):
        break
    divider = divider / 10
print(sum)
#
# 기대 출력:
# 23


# ---------------------------------------------------------------------
# 문제 13. while + 리스트 - 스택 비우기
# ---------------------------------------------------------------------
# stack 이 비어있지 않은 동안 pop() 으로 하나씩 꺼내 출력하라.
# 다 꺼낸 뒤 stack 을 출력하면 빈 리스트여야 한다.
#
# 참고: https://docs.python.org/ko/3/tutorial/datastructures.html#using-lists-as-stacks
stack = ["a", "b", "c", "d"]
# TODO: while stack ...
while stack:
    print(stack.pop())
#
# 기대 출력:
# d
# c
# b
# a
# []
