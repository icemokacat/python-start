# 리스트
# 선언
a = []
b = list()
c = [70, 75, 80, 85] #Len
d = [1000,10000, 'Ace', 'Base', 'Captine']
e = [1000,10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.141592]
print(len(c))
print(d)
print('d - ',type(d),d)
print(d[1])
# 음수는 역순
print(d[-1])

# 슬라이스
print('d - ',d[0:3])
# => 0번째 부터 '3' 개 
print('d[2:]')
# => 2번째 부터 '끝'까지
print(e[-1][1:3])
# 이중 배열일때 순서대로 e[첫번째 배열의 인덱스][중첩된 배열의 인덱스]
# [1000,10000, ['Ace', 'Base', 'Captine']]
# => 마지막 요소인 문자열 배열의 [1:3]
# => Base 부터 3개 출력 (그런데 3번째가 없으므로 무시되고 2개만 출력)

# 리스트 연산
print('c + d',c+d)
# => 리스트가 옆으로 붙어서 합쳐짐
# => c + d [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captine']
print('c * 3',c * 3)
# => 리스트가 똑같은게 3개 붙어서 하나의 리스트로(순서 유지)
# print("'Test' + c[0]", 'Test' + c[0])
# => 오류
print("'Test' + c[0]", 'Test' + str(c[0]))
# => 형변환 하면 됨

# 값 비교
print("===========")
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# c = [70, 75, 80, 85]
temp = c
print(temp,c)
print(id(temp),id(c))
# => 아이디가 같다
c.append(702)
print(temp)
del c[-1]
# => 똑같이 추가됨 (메모리 주소를 공유)
# 깊은 복사시 copy 메소드 사용
print("======")
temp2 = c.copy()
c.append(999)
print(temp2)
# => 999 없음
