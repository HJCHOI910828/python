"""
날짜 : 2021/07/19
이름 : 임진슬
내용 : 파이썬 함수 실습하기 교재 p114
"""

# 함수: 일련의 로직을 재활용하기 위해 모듈화한 로직 단위
def f(x):
    y = 2 * x + 3
    return y

# 함수실행(호출)
y1 = f(1)
y2 = f(2)
y3 = f(3)

print('y1 :', y1)
print('y2 :', y2)
print('y3 :', y3)

# 함수유형1 : parameter O, return O
def type1(x, y):
    z = x + y
    return z

r1 = type1(1, 2)
r2 = type1(2, 3)
print('r1 :', r1)
print('r2 :', r2)

# 함수유형2 : parameter O, return X
def type2(items):
    sum = 0

    for item in items:
        sum += item

    print('items 합 :', sum)

type2([1, 2, 3, 4, 5])
type2((6, 7, 8, 9, 10))

# 함수유형3 : parameter X, return O
def type3():

    total = 0

    for i in range(11):
        total += i

    return total

result = type3()
print('result :', result)

# 함수유형4 : parameter X, return X
def type4():
    print('type4 result :', type3())

type4()

# 확인문제
def gugudan(num):
    print('%d단' % num)
    for i in range(1, 10):
        print('%d x %d = %d' % (num, i, num *i))

gugudan(2)
gugudan(3)
gugudan(4)