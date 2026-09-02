# Raw string
# 역슬러시 자체를 신경안씀
raw_s1 = r'D:\python\test'
print(raw_s1)
# => 문자열 그대로 표기

# 멀티라인 입력
multi_str = \
'''
문자열
멀티 라인 입력
'''
# => 역슬러시가 있으면 다음라인에 뭔가 있음을 표시

print(multi_str)

# 문자열 형 변환
print(str(66),type(str(66)))

# 문자열 함수
str_01 = 'python'
# 첫문자만 대문자로
print(str_01.capitalize())
# 마지막이 대입한 문자로 끝나는지
str_02 = "Apple"
print("end with?:",str_02.endswith("e"))
# 교체 java 와 다르게 replace 가 replace all 역할
print('replace : ',str_01.replace('Nice','Good'))
print('replace : ',str_01.replace('thon','Good'))
# 정렬 (쪼개서 리스트화 시켜서 정렬시킴)
print(sorted(str_01))

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)
    
# 아스키 코드
a = 'Z'
print(ord('a')) # 97
print(ord('A')) # 65
print(chr(65)) # => A