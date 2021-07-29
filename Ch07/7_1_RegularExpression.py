"""
날짜 : 2021/07/21
이름 : 임진슬
내용 : 파이썬 정규표현식 실습하기 교재 p192

정규표현식(Regular Expression)
 - 문자열에서 특정한 규칙을 적용해서 특정패턴의 문자열을 찾는 문법
 - 일반적으로 특정문자 검색, 매칭여부 확인에 많이 사용

"""

import re
from re import findall, match

str1 = '1234 abc홍길동 ABC_555_6 부산광역시'

# 숫자검색
print(findall('1234', str1))
print(findall('[0-9]', str1))
print(findall('[0-9]{3}', str1))
print(findall('[0-9]{3,}', str1))

# 문자열 검색
print(findall('[가-힣]{3,}', str1))
print(findall('[a-z]{3,}', str1))
print(findall('[a-z|A-Z]{3,}', str1))

str2 = 'test1abcABC 123mbc 45test'
print(findall('test', str2))
print(findall('^test', str2)) # ^ = start
print(findall('st$', str2)) # $ = end

str3 = 'test^홍길동 abc 대한*민국 123$tbc'
print(findall('\\w{3,}', str3)) # 3자리 이상 단어

# 응용
str4 = '123456-1234567'
result = match('[0-9]{6}-[1-2][0-9]{6}', str4)


if result:
    print('숫자가 매칭 됩니다.')
else:
    print('숫자가 매칭 안됩니다.')
