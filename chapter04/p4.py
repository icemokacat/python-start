# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
# 수정
a[3] = 10
# 추가
a.append(99)

# 정렬
a.sort()
print('a - ',a)
a.reverse()
print(a)
print()
# 중간에 삽입 (인덱스 위치에, 값)
a.insert(2,7)
print(a)

print("DEL")
# 삭제
del a[0]        # 0번째 요소삭제 (함수가 아닌 예약어임)
print(a)
a.remove(10)    # 값 99 라는 걸 삭제해라 (대신 없는걸 삭제하려 하면 오류남)
print(a)

# pop
print("POP")
print(a.pop())  # 마지막 요소를 출력하고 꺼내라
print(a)

# count
print("count")
print(a.count(4))   # 4가 몇개있니

# 반복문 활용
while a:
    data = a.pop()
    print(data)