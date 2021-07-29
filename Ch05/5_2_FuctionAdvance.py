"""
날짜 : 2021/07/19
이름 : 임진슬
내용 : 파이썬 특수함수 실습하기 교재 p129
"""

# 디폴트 매개변수
def hello(name='홍길동', age=21):
    print('이름 :', name)
    print('나이 :', age)

hello()
hello('김유신')
hello('김춘추', 25)

# 가변 매개변수
def total(*scores):
    sum = 0

    for score in scores:
        sum += score

    return sum

r1 = total(1)
r2 = total(1, 2, 3)
r3 = total(1, 2, 3, 4, 5)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

# 하나 이상의 리턴 값
def sum_and_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2

    return y1, y2

rs1, rs2 = sum_and_multi(1, 2)
rs3, rs4 = sum_and_multi(2, 3)

print('rs1 : %d, rs2 : %d' % (rs1, rs2))
print('rs3 : {}, rs4 : {}' .format(rs3, rs4))

# 변수에 저장하는 함수
def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

var1 = plus
var2 = minus

res1 = var1(1, 2)
res2 = var2(2, 3)

print('res1 :', res1)
print('res2 :', res2)

# 함수리스트
funcs = [plus, minus]
res3 = funcs[0](2, 3)
res4 = funcs[1](4, 6)

print('res3 :', res3)
print('res4 :', res4)

# 람다함수(익명함수)
lambPlus = lambda x, y: x + y
lambMinus = lambda x, y: x - y

print('lambPlus(1, 2) :', lambPlus(1, 2))
print('lambMinus(2, 5) :', lambMinus(2, 5))