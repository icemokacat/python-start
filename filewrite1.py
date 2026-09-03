# 파일 읽기 및 쓰기

# 읽기모드 : r , 쓰기모드 : w , 추가모드 : a, 텍스트 모드 : t, 바이너리 모드 : b

# 파일 읽기
# 기본적으로 파일 읽기 모드는 텍스트 모드이다.
f = open('resource/it_news.txt','rt',encoding='utf-8')
# 속성 확인
print(dir(f))    
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)

print("=" * 50)
cts = f.read()
print(cts)
print("=" * 50)
f.close()

# 예제2
with open('resource/it_news.txt','rt',encoding='utf-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    #print(list(c))
# => with 문을 사용하면 파일을 자동으로 닫아준다.
print()

# 예제3
print("=" * 50)
# read() : 전체 읽기, read(10) : 10Byte 읽기
with open('resource/it_news.txt','r',encoding='utf-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(40)
    print(c)
    #print(list(c))
    # 커서 이동 : seek(0,0) : 처음으로 이동
    f.seek(0,0)
    c = f.read(10)
    print(c)
print()

# 예제4
# readline() : 한 줄 읽기
print("*" * 50)
with open('resource/it_news.txt','r',encoding='utf-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
print()

# 예제5
# readlines() : 전체 읽기
# => 전체를 읽은 후 라인 단위 리스트로 저장
print("*" * 50)
with open('resource/it_news.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    print(len(lines))
print()

# 파일 쓰기
with open('resource/contents1.txt','w',encoding='utf-8') as f:
    f.write('I Love Python \n')
print()
with open('resource/contents1.txt','at',encoding='utf-8') as f:
    f.write('I Love Python2 \n')    
print()
# writelines : 리스트 -> 파일
with open('resource/contents2.txt','w',encoding='utf-8') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n']
    f.writelines(list)

# file 로 print
with open('resource/contents3.txt','w',encoding='utf-8') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n']
    print(list, file=f)
    print('TEST1', file=f)
print()