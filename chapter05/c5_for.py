# For

for v1 in range(10):
    print('v1 is :',v1)

# range 의 마지막 순서는 제외한다    
for v2 in range(1,11): # 1~10
    print('v2 is :',v2)

print()
for v3 in range(1, 11, 2):
    print('v3 is :',v3)    
# => 1,3,5,7,9    

sum1 = 0
for v in range(1, 1001):
    sum1 += v
print(sum1)

print('1 ~ 1000 sum : ', sum(range(1,1001)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

print()
# 예제1
names = ['Kim','Park','Cho','Lee',"Choi",'Yoo']

for name in names:
    print('You are : ', name)
    
# 예제4
my_info = {
    'name'  : 'Lee',
    'Age'   : 33,
    'City'  : 'Seoul'
}    

print()
for key in my_info:
    print("key :",my_info[key])
print()    
for v in my_info.values():
    print('value:',v)
    
print()
# items 하면 튜플로 찍힘
for v in my_info.items():
    print(v)
    print(type(v))
    
# break
print("==== break ====")
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]
for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print("Not found :",num)
        
# for - else
print("=== FOR - ELSE ===")
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else:
    print("Not Found : 24")

print("==== for 모두 수행하고(break 제외) else 로 넘어감")    
for num in numbers:
    if num == 48:
        print("Found : 48")
        break
else:
    print("Not Found : 48")   

# 변환 예제
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('List',list(reversed(name2)))
print('Tuple', tuple(reversed(name2))) 