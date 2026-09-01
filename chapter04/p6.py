# 딕셔너리 (튜플 집합)
# 순서 x, 키 중복 x, 수정 O, 삭제 O

bb = 'age'
a = {
    'name':'Kim',
    bb:20,
    'phone':'01012341234',
    'birth':'990101'
}
b = {0:'Hello Python'}
c = {'arr': [1,2,3,4]}
# e = dict([
#     ('name':'Niceman'),
#     ('City':'Seoul'),
#     ('Age':33)
# ])
f = dict(
    name = 'Niceman',
    City = 'Seoul',
    Age = 33
)
print()
# 출력
print(a['name'])
print(a.get('name'))
#print(a['name1'])       # => 오류
print(a.get('name1'))   # => None 출력

print(b[0])

print()
# 딕셔너리 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1,2,3]
print(a)

print()
# dict_keys, dict_values, dict_items : 반복문(__iter__) 에서 사용 가능
print(a.keys())
print(list(a.keys()))
print()
print(a.values())
print(list(a.values()))

# 
print()
print(a.items())
print(list(a.items()))

#
print()
print(a.pop('name'))
print(a)

# pop item
print()
print(a.popitem())
print(a)
print(a.popitem())
print(a)

# in
print('a -','birth' in a)
print('f -','City' in f)
print('f -','city' in f)

# 수정
a['test'] = 'test_dict' # 추가
print(a)
a['phone'] = 'ddd'
print(a)

a.update(phone='1234')
print(a)

temp = {'address':'Busan'}
a.update(temp)
print(a)