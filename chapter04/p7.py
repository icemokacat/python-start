# Chapter03-6
# 집합(Set)
# 순서 x, 중복 x, 추가수정 O

# 선언
a = set()
print(a)
print(type(a))
b = set([1,2,3,4,5])
print(b)
c = set([1,4,5,6])
d = set([1,2,3,'Pen','Cap','Plate'])
e = {'foo','bar','baz','foo','qux'}
print(type(e))
f = {42,'foo',(1,2,3),3.141592}
print(2 in a)

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
# 교집합
print(s1 & s2)
a2 = s1 & s2
print(a2)
print(s1.intersection(s2))

# 합집합
print('s1 | s2 :', s1 | s2)
print('s1 | s2 :', s1.union(s2))

# 차집합
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))
# => 중복있으면 False (반대로 나옴)

# 부분 집합 확인
print(s1.issubset(s2))

s3 = {1,2,3,4}
s4 = {1,2}
#print(s4.issubset(s3)) 
# => true
print(s3.issuperset(s4))
# => 부분집합의 반대 (s3 가 s4 요소를 모두 가지고 있는지 판단)