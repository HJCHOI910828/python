"""
날짜 : 2021/07/13
이름 : 임진슬
내용 : 파이썬 반복문 while 실습하기 교재 p64
"""

# While 기본
num = 1

while num < 5:
    print('%d회 반복' % num)
    num += 1

# 1부터 10까지 합
sum, k = 0, 1

while k <= 10:
    sum += k
    k += 1

print('1부터 10까지 합 :', sum)

# 1부터 10까지 짝수합
tot, j = 0, 1

while j <= 10:

    if j % 2 == 0:
        tot += j

    j += 1

print('1부터 10까지 짝수합 :', tot)

# break
i = 1

while True:

    if i % 5 == 0 and i % 7 == 0:
        # 반복문 종료
        break

    i += 1

print('5와 7의 최소공배수 :', i)

# continue
n, total = 1, 0

while n <= 10:

    n += 1

    if n % 2 == 1:
        # 반복문 상위로 이동
        continue

    total += n

print('1부터 10까지 짝수합 :', total)
