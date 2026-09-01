# 파이썬 튜플
# 순서 O, 중복 O, 수정 X, 삭제 X
# 불변 
# java14+ 의 record

a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>>>>>>')
print('d - ',d[1])
print(d[0] + d[1] + d[1])

la = list(e[-1][1]) # 중첩 튜플의 두번째 요소를 리스트화
print(la)

# 수정x
# d[0] = 1500
# => 에러 발생
# 
a = (5,2,3,1,4)
print(a)
print(a.index(3))   # 숫자 3의 인덱스가 뭐냐

# 팩킹 & 언팩킹

# 패킹 (Packaging)
t = ('foo','bar','baz','qux')
# => 4개의 원소를 '묶었다'

# 언팩킹
(x1,x2,x3,x4) = t
print(type(x1),type(x2),type(x3),type(x4))
# => <class 'str'> <class 'str'> <class 'str'> <class 'str'>
print(x1,x2,x3,x4)
# 개별요소를 풀어서 할당
# 괄호가 없어도 되긴함 (튜플 특성상)
x1,x2,x3,x4 = t

t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4,5,6

print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)

