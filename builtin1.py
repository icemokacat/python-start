# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수들
# 사용하다보면 자연스럽게 숙달해진다.

# all : iterable 요소 검사(참/거짓)
# all() : 인자 모두 참
# any() : 인자 하나라도 참
print(all([1, 2, 3]))
# => True
print(all([1, 2, 0]))
# => False
print(all([1, 2, 3, 0]))
# => False

# chr: 아스키 -> 문자, ord: 문자 -> 아스키
print(chr(65))
# => 'A'
print(ord('A'))
# => 65

# dict : 키-값 쌍의 집합
print(dict(a=1, b=2, c=3))
# => {'a': 1, 'b': 2, 'c': 3}

# enumerate : 인덱스와 값을 함께 반환
print(enumerate(['a', 'b', 'c']))
# => <enumerate object at 0x7f8b4c000000>
print(list(enumerate(['a', 'b', 'c'])))
# => [(0, 'a'), (1, 'b'), (2, 'c')]

# filter : 조건에 맞는 요소 필터링
def conv_pos(x):
    return abs(x) > 2

print('filter -----------')
print(filter(conv_pos, [1, -3, 2, 0, -5, 6]))
print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# filter 실무 형태
# - 조건이 짧으면 lambda
# - 조건이 길면 함수로 분리
# - 결과는 iterator라서 list()로 소비하는 경우가 많음
users = [
    {"name": "kim", "email": "kim@example.com", "is_active": True, "age": 29},
    {"name": "lee", "email": "lee@example.com", "is_active": False, "age": 34},
    {"name": "park", "email": "park@example.com", "is_active": True, "age": 17},
]

active_users = list(
    filter(lambda user: user["is_active"], users)
)
print(active_users)

def is_active_adult(user):
    return user["is_active"] and user["age"] >= 18

adult_users = list(filter(is_active_adult, users))
print(adult_users)

# 빈 값 / None 제거 (falsy 제거)
raw_emails = ["kim@example.com", "", None, "lee@example.com"]
valid_emails = list(filter(None, raw_emails))
print(valid_emails)

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print('map -----------')
print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))

# map 실무 형태
# - 타입 변환, 공백 제거, 필드 추출에 많이 씀
# - 함수가 이미 있으면 lambda 없이 함수 이름만 넘김
price_texts = ["12000", "9900", "1500"]
prices = list(map(int, price_texts))
print(prices)

names = ["  kim  ", "lee", "  park"]
cleaned_names = list(map(str.strip, names))
print(cleaned_names)

emails = list(map(lambda user: user["email"], users))
print(emails)

# filter + map 조합: 조건에 맞는 것만 변환
active_emails = list(
    map(
        lambda user: user["email"],
        filter(lambda user: user["is_active"], users),
    )
)
print(active_emails)

# zip : 여러 객체 동시 루프 하면서 tuple 형태로 반환
print('zip -----------')
print(zip([1, 2, 3], ['a', 'b', 'c']))
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))
# => [(1, 'a'), (2, 'b'), (3, 'c')]