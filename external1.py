# 외장 함수

# 예제1
import sys
# 파이썬 실행시 전달된 인자를 출력
print('---------- SYS -----------')
print(sys.argv)

# 예제2 (강제 종류)
# sys.exit()

# 예제3 (파이썬 패키지 위치)
print('---------- SYS PATH -----------')
print(sys.path)

# 예제4 (객체 파일 쓰기)
print('---------- PICKLE -----------')
import pickle

# wb : write binary
f = open('test.obj', 'wb')

obj = {1: 'test', 2: 'test2'}
# dump : 객체를 파일에 쓰기
pickle.dump(obj, f)
f.close()

# 예제5 (객체 파일 읽기)
# rb : read binary
f = open('test.obj', 'rb')
# load : 파일에서 객체 읽기
obj = pickle.load(f)
print(obj)
f.close()

import os
#print(os.environ)
print('---------- OS -----------')
print(os.path.exists('test.obj'))
print(os.path.isfile('test.obj'))
print(os.path.isdir('test.obj'))
# 현재 경로
print(os.getcwd())

print()

# time : 시간 관련 함수
import time
print('---------- TIME -----------')
print(time.time())      # 1970년 1월 1일 00:00:00 부터 현재까지의 초 단위 시간
print("local time:", time.localtime(time.time()))
# 간단 표현
print(time.ctime())
# 형식 표현
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 시간 간격 발생
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random : 난수 관련 함수
import random
print('---------- RANDOM -----------')
print(random.random()) # 0.0 ~ 1.0 사이의 임의의 값 생성
print(random.randint(1, 100)) # 1 ~ 100 사이의 임의의 정수 생성
print(random.randrange(1, 100)) # 1 ~ 100 사이의 임의의 정수 생성

# 섞기
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# 랜덤 선택
print(random.choice(d))

# webbrowser : 웹 브라우저 관련 함수
import webbrowser
print('---------- WEBBROWSER -----------')
# webbrowser.open('https://www.google.com')
# webbrowser.open_new('https://www.google.com')
# webbrowser.open_new_tab('https://www.google.com')