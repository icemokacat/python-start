# while
# while <expr>:
#   <statement(s)>


# 예제1
n = 5
while n > 0:
    n = n - 1
    print(n)

# 예제2
a = ['foo','bar','baz']

print()
while a:
    print(a.pop())    
    
print()
# while else
n = 10
while n > 0:
    n -= 1
    print(n)
else:
    print('else out')