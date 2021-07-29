"""
날짜 : 2021/07/13
이름 : 임진슬
내용 : 파이썬 반복문 for 실습하기 교재 p70
"""

# for
for i in range(5):
    print('{}회 반복'.format(i))

for i in range(10, 20):
    print('반복변수 i :', i)

for k in range(10, 0, -1):
    print('반복변수 k :', k)

# 1부터 10까지 합
sum1 = 0

for i in range(11):
    sum1 += i

print('1부터 10까지 합 :', sum1)

# 1부터 10까지 짝수합

sum2 = 0

for k in range(11):

    if k % 2 == 0:
        sum2 += k

print('1부터 10까지 짝수합 :', sum2)

# 중첩 for문
for a in range(3):
    print('a :', a)
    for b in range(5):
        print('b :', b)

# 구구단
for x in range(2,10):
    print(x, '단')
    for y in range(1, 10):
        z = x * y
        print('%d x %d = %d' % (x, y, z))

# 별삼각형
for a in range(10, 1, -1):

    for b in range(a):

        print('☆', end= '')

    print('')

# 별삼각형
for i in range(10):
    print('★' * i)
