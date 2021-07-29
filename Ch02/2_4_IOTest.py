"""
날짜 : 2021/07/13
이름 : 임진슬
내용 : 파이썬 입출력 실습하기 교재 p42
"""

# 파이썬 표준 입력장치
num = input('숫자입력 :')

# 파이썬 표준 출력장치
print('입력한 숫자 :', num)
print('num type :', type(num)) # Run 에 숫자입력하고 엔터

# 문자열을 숫자로 변환(캐스팅)
var = int(num)
result = var + 1
print('result :', result)

# 서식문자 출력
print('%d년 %d월 %d일 %s요일' % (2021, 7, 13, '화')) # d = decimal s = string

# 출력문 옵션
print('helllo', end='~')
print('python~')

print('010', '1234', '5678', sep='-')

# 포맷문자 출력문
print('이름:{}\n나이:{}\n주소:{}'.format('김유신', 23, '김해시'))
