# =====================================================================
# Chapter 02 복습 연습문제 (2)  - print / 문자열 포매팅 / 변수 / type / id
# ---------------------------------------------------------------------
# 제약: chapter02 에서 아직 안 배운 for / while 은 사용하지 말 것.
#       (반복이 필요하면 print 를 여러 번 호출해서 해결)
# 정답 확인:  python chapter02/practice2.py
# =====================================================================


# ---------------------------------------------------------------------
# 문제 1. sep 와 end 를 함께 쓰기
# ---------------------------------------------------------------------
# print 를 "두 번" 호출해서 아래 한 줄을 만들어라.
#  - 첫 번째 print: "2026", "09", "01" 세 조각을 sep="/" 로 이어 붙이고,
#                   줄바꿈이 안 되도록 end 옵션을 준다.
#  - 두 번째 print: "  (금)" 만 출력.
#
# 참고: https://docs.python.org/ko/3/library/functions.html#print
# TODO:
print('2026','09','01',sep='/',end='')
print(' (금)')
# print(...)
# print(...)
#
# 기대 출력:
# 2026/09/01  (금)


# ---------------------------------------------------------------------
# 문제 2. 같은 결과를 세 가지 방식으로
# ---------------------------------------------------------------------
# 아래 값으로 "Kim : 92점" 을 각각
#  (1) % 연산자   (2) str.format()   (3) f-string
# 방식으로 만들어 "3줄" 출력하라.
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#printf-style-string-formatting
# 참고: https://docs.python.org/ko/3/library/string.html#formatstrings
# 참고: https://docs.python.org/ko/3/reference/lexical_analysis.html#f-strings
name, score = "Kim", 92
# TODO: print 3번
print('%s : %d점' % (name,score))
print('{} : {}점'.format(name,score))
print(f'{name} : {score}점')
#
# 기대 출력:
# Kim : 92점
# Kim : 92점
# Kim : 92점


# ---------------------------------------------------------------------
# 문제 3. % 포매팅 - 진행률 리포트
# ---------------------------------------------------------------------
# done / total 의 백분율을 소수 1자리로, 전체 5칸을 확보해 출력하라.
# 끝에는 리터럴 '%' 기호가 붙어야 한다. (힌트: %% 는 % 한 글자를 뜻함)
#
# 참고: https://docs.python.org/ko/3/library/stdtypes.html#printf-style-string-formatting
done, total = 3, 7
# TODO:
d1 = done/total * 100
print('{:5.1f}%'.format(d1))
# print("진행률: %5.1f%%" % (...))
#
# 기대 출력:
# 진행률:  42.9%


# ---------------------------------------------------------------------
# 문제 4. str.format() - 인덱스 재정렬 + 같은 인덱스 재사용
# ---------------------------------------------------------------------
# d, m, y 를 str.format() "하나"로 아래처럼 출력하라.
#  - 순서를 y.m.d 로 바꾸고,
#  - 월/일은 두 자리(0 채움),
#  - 연도({y})는 끝에서 한 번 더 사용한다.
#
# 참고: https://docs.python.org/ko/3/library/string.html#format-string-syntax
d, m, y = 9, 1, 2026
# TODO:
print('{2}.{1:02}.{0:02}'.format(d,m,y))
# print("...".format(d, m, y))
#
# 기대 출력:
# 2026.01.09 (2026)


# ---------------------------------------------------------------------
# 문제 5. 채우기 + 가운데 정렬로 배너 만들기
# ---------------------------------------------------------------------
# 문자열 label 을 전체 20칸 가운데 정렬하고 남는 칸은 '-' 로 채워 출력하라.
# (반복문으로 '-' 를 이어붙이지 말 것. 포맷 스펙 하나로 해결)
#
# 참고: https://docs.python.org/ko/3/library/string.html#format-specification-mini-language
label = " MENU "
# TODO:
print("{:-^20}".format(label))
# print("{:-^20}".format(label))
#
# 기대 출력:
# ------- MENU -------


# ---------------------------------------------------------------------
# 문제 6. 정렬된 표 (print 3번, 반복문 금지)
# ---------------------------------------------------------------------
# 세 행을 각각 str.format() 으로 출력하라.
#  - 1열: 왼쪽 정렬 6칸
#  - 2열: 왼쪽 정렬 8칸
#  - 3열: 오른쪽 정렬 4칸
#
# 참고: https://docs.python.org/ko/3/library/string.html#format-examples
r1 = ("ID", "NAME", "AGE")
r2 = ("1", "Ann", "30")
r3 = ("2", "Bob", "5")
# TODO: print 3번  (예: "{:<6}{:<8}{:>4}".format(r1[0], r1[1], r1[2]))
form = '{:<6}{:<8}{:>4}'
print(form.format(r1[0],r1[1],r1[2]))
print(form.format(r2[0],r2[1],r2[2]))
print(form.format(r3[0],r3[1],r3[2]))
#
# 기대 출력:
# ID    NAME     AGE
# 1     Ann       30
# 2     Bob        5


# ---------------------------------------------------------------------
# 문제 7. 문자열 절삭 (precision 을 문자열에 적용)
# ---------------------------------------------------------------------
# word 의 앞 4글자만 남겨서 출력하라. % 방식과 .format() 방식 둘 다.
# 추가로 f-string 으로 앞 4글자 + "..." 를 붙여 출력하라.
#
# 참고: https://docs.python.org/ko/3/library/string.html#format-specification-mini-language
word = "documentation"
# TODO:
print('%.4s' % word)
print('{:.4}'.format(word))
print(f'{word:.4}...')
# print("%.4s" % word)
# print("{:.4}".format(word))
# print(f"{word:.4}...")
#
# 기대 출력:
# docu
# docu
# docu...


# ---------------------------------------------------------------------
# 문제 8. type() 과 id() - 동적 타이핑 & 참조
# ---------------------------------------------------------------------
# 아래를 "예측"해서 주석에 적고 실행으로 확인하라.
#  (1) 같은 변수에 다른 타입을 다시 대입하면 type() 결과가 바뀌는가?
#  (2) p 를 q 에 대입한 직후 id 가 같은가? q 에 새 값을 넣으면?
#
# 참고: https://docs.python.org/ko/3/library/functions.html#type
# 참고: https://docs.python.org/ko/3/library/functions.html#id
v = 10
# print(type(v))          # 예측: ?
v = "ten"
# print(type(v))          # 예측: ?

p = 300
q = p
print(id(p) == id(q))
# print(id(p) == id(q))   # 예측: ?
q = 400
print(id(p) == id(q))
# print(id(p) == id(q))   # 예측: ?
# 이유:
