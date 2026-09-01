# print

# 기본 출력
print('python start!')
print("python start!")
# ''' """ 둘다 가능

# Separator 옵션
print('P','Y','T',sep=',');
# P,Y,T 로 출력
print('P','Y','T');
# 주지 않을 경우 공백으로
# P Y T

# end 옵션
print('Welcome to', end='')
print('IT News', end='')
# 이렇게 끝 부분을 지정하지 않으면 `자동 줄바꿈` 이 되지 않는다
# 아무것도 없으면 엔터 처리
print() 
print('Hello',end=' ')
print('World')
# => Hello World (줄바꿈 없이)

# D S F
# S => 어떤 것을 대체할 수 있다 (문자열)
print('%s %s' % ('one','two'))
# => one two
print('{} {}'.format('one','two'))
print()
# => one two
print('{1} {0}'.format('one','two'))
# 1번째 인덱스의 값이 들어간다 (여기서는 two)
# 0번째 인덱스의 값이 들어간다 (여기서는 one)

# %s
print('%10s' % ('nice'))
# => 기본적으로 LPAD 같이 공백으로 채우고 나머지를 nice 로 채움 (6자리 공백)
print('{:>10}'.format('nice'))
# => 결과값 같음 (      nice)
print()

print('%-10s' % ('nice'))
# RPAD => nice 를 먼저 넣고 남은 갯수만큼 공백 채움
print('{:10}'.format('nice'))
# 결과 같음
print()

# 언더바를 넣고 하면?
print('{:_>10}'.format('nice'))
# => ______nice (공백대신 언더바)

# 중앙정렬
print('{:^10}'.format('nice'))

# . 을 붙이면 절삭한다
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
# => pytho
# . 없이 만약 공간보다 큰 글자가 들어오면
print('%5s' % ('pythonstudy'))
# => pythonstudy 그냥 출력한다

print()
# 10개의 공간을 확보하되 5개만 나와라
print('{:10.5}'.format('pythonstudy'))
# => pytho

# %d (정수 출력)
print('%d %d' % (0,1))
print('{} {}'.format(0,1))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f 
print('%f' % (3.1444))
print('{:f}'.format(3.141414))

# 총자리수 6자리, 소수부는 2째자리 (나머지는 0으로 채움, "." 도 자리 차지)
print('%06.2f' % (3.141592653592))
print('{:06.2f}'.format(3.143432543567))
# => 결과 같음

# 3가지 format practice
x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1 
ex1 = 'n = %s, s = %s, sum=%d' % (n,text,(x+y))
print(ex1)
# => n = Lee, s = 308276567, sum=150

# 출력2
ex2 = 'n = {n}, s is = {s}, sumis={sum}'.format(n=n,s=text,sum=x+y)
print(ex2)

# 출력3
ex = f'n = {n}, s= {text}, sum is ={x + y}'
print(ex)

# 구분기호
m = 100000000
print(f'm : {m:,}')
# => 1000 단위로 쉼표가 찍힘

# 정렬
print()
# ^ : 가운데 정렬
# < : 왼쪽 정렬
# > : 오른쪽 정렬

t = 20
# 10 자리를 확보
print(f"t = {t:10}")
print(f"t cener: {t:-^10}")
print(f"t cener: {t:-<10}")
print(f"t cener: {t:->10}")