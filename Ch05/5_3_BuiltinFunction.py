"""
날짜 : 2021/07/20
이름 : 임진슬
내용 : 파이썬 내장함수 실습하기 교재 p115
"""

import time as time
import math
import random

# time
t1 = time.time() # unix time
print('t1 :', t1)

t2 = time.ctime() # 변환된 unix time
print('t2 :', t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)

print('%s년, %s월, %s일' % (year, month, date))
print('{}시, {}분, {}초'.format(hour, min, sec))

# abs = 절대값
r1 = abs(-5)
print('r1 :', r1)

# ceil = 올림값(정수)
r2 = math.ceil(1.2)
r3 = math.ceil(1.8)

print('r2 :', r2)
print('r3 :', r3)

# floor = 내림값(정수)
r4 = math.floor(1.2)
r5 = math.floor(1.8)

print('r4 :', r4)
print('r5 :', r5)

# round = 반올림
r6 = round(1.2)
r7 = round(1.8)

print('r6 :', r6)
print('r7 :', r7)

# random
num1 = random.random()
print('num1 :', num1) # 0~1 사이 임의의 실수

num2 = num1 * 10
print('num2 :', num2) # 0~10 사이 임의의 실수

num3 = math.ceil(num2)
print('num3 :', num3) # 0~10 사이 임의의 정수

result = math.ceil(random.random() * 45)
print('result :', result)