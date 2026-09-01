# 변수

n = 700
print(n)
print(type(n))
# => <class 'int'>

# 재선언
var = 75
var = "Change Value"
print(var)
print(type(var))
# => Change Value
# => <class 'str'>

# id(indentify) 확인 : 객체의 고유값
m = 800
n = 655
print(id(m))
print(id(n))
# 어떤 숫자가 나옴 -> 해당 값의 고유값