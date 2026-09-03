# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

with open('resource/test1.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) # 첫 번째 줄 스킵

    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader))

    for c in reader:
        #print(c)
        # 타입 확인
        #print(type(c))
        # 속성 확인
        #print(dir(c))
        # 반복문 확인
        #print(f'{c[0]} code is {c[1]}')
        print(':'.join(c))
print()

# 예제2
print('-' * 50)
with open('resource/test2.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)

# 예제3
print('-' * 50)
with open('resource/test1.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    next(reader)

    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        dd = dict(c)
        print(dd.get('Name'))

# 예제4
print('-' * 50)
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('resource/test3.csv','w',encoding='utf-8') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제5
print('-' * 50)
with open('resource/test3.csv','w',encoding='utf-8') as f:
    # 필드명
    fields = ['One','Two','Three']
    # DictWriter
    wt = csv.DictWriter(f, fieldnames=fields)
    # 헤더 작성
    wt.writeheader()
    # 데이터 작성
    for v in w:
        wt.writerow({'One':v[0], 'Two':v[1], 'Three':v[2]})