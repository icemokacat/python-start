# 예제1

def first_func(w1):
    print("Hello,", w1)

word = "Goodboy"
first_func(word)

# 예제 2
def return_function(w1):
    value = "Hello," + str(w1) 
    return value

result = return_function(word)
print(result)

# 예제3 다중반환
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1,y2,y3

dd = func_mul(3)
print(type(dd))
print(dd)
# => <class 'tuple'>

def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1,y2,y3)

dd2 = func_mul(3)
print(type(dd2))
print(dd2)

# 중요
# *args, **kwargs

# *args(언팩킹)
print('====== *args ======')
def args_func(*argsss):
    for i,v in enumerate(argsss):
        print('Result {}'.format(i),v)
    print('---------')

args_func(1,2,'Top',[1,'TPO'])
args_func('Lee', 'Park')

# **kwargs (언팩킹)
# 키밸류로 여러개 넣을 수 있다
def kwargs_func(**myargs):
    for k in myargs.keys():
        print("{}".format(k), myargs[k])
    print('-------------')
    
kwargs_func(name1='Lee')    
kwargs_func(name1='Lee', name2='Park')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1,args_2, args, kwargs)

example(10,20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)
print('--------------')

# 람다식 예제
# 공식에서는 메모리 절약, 가독성 향상, 코드 간결
# 하지만 다양한 전문가들은 부정적인 의견이 있음

#def mul_func(x,y):
#    return x * y

#a = lambda x,y: x*y

def mul_func(x,y):
    return x * y

q = mul_func(10,50)
print(q)

lambda_mul_func = lambda x,y: x*y
print(lambda_mul_func(10,50))

# 활용
def func_final(x, y, func):
    print(x * y * func(100,100))

func_final(10, 20, lambda x,y: x*y)
