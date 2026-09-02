# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError : 구문 오류
# NameError : 이름 오류
# TypeError : 타입 오류
# ValueError : 값 오류
# IndexError : 인덱스 오류
# KeyError : 키 오류
# AttributeError : 속성 오류
# PermissionError : 권한 오류
# ... 
# 모든 예외는 Exception 클래스를 상속받는다.
# 예외 처리는 try, except, finally 문으로 처리한다.
# try:
#     code
# except Exception as e:
#     print(e)
# finally:
#     code

# NameError 예외
a = 10
b = 20
# print(c)
# => NameError: name 'c' is not defined

# AttributeError 예외
a = 10
b = 20
# print(a.add(b))
# => AttributeError: 'int' object has no attribute 'add'

# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print(f"name[{x}] = {z}")
except ValueError:
    print("Occured! ValueError!")
except Exception as e:
    print("Occured! Exception!", e)
else:
    print("OK!")
finally:
    print("try except finally!")

# 예제2
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print(f"name[{x}] = {z}")
    a = 1/0
except Exception as e:
    print("Occured! Exception!", e)
else:
    # 에러가 발생하지 않은 경우
    print("OK!")
finally:
    print("try except finally!")

# 예제3
# 일부러 발생
print('-' * 20)
try:
    a = 'Park'
    if (a == 'Kim'):
        print('OK! pass!')
    else:
        raise ValueError
except Exception as e:
    print("Occured! Exception!", e)
else:
    print("OK! else")