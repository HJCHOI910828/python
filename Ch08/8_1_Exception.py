"""
날짜 : 2021/07/26
이름 : 임진슬
내용 : 파이썬 예외처리 실습하기 교재 p212
"""

# try ~ except
num1, num2 = 1, 0

r1 = num1 + num2
r2 = num1 - num2
r3 = num1 * num2
r4 = 0
try: # 예외(에러)가 발생할 코드로직 작성
    r4 = num1 / num2
except: # 예외가 발생했을 때 처리로직 작성
    print('예외발생...')

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)

# try ~ except ~ finally
people = ['김유신', '김춘추', '장보고']

try:
    # 예외가 발생할 가능성이 있는 코드로직
    for i in range(4):
        print(people[i])

except:
    # 예외가 발생했을 때 처리로직
    print('유효하지 않는 인덱스 참조...')
finally:
    # 예외 발생 여부에 관계없이 마지막에 실행되는 코드로직
    print('예외처리 완료...')

# try ~ except ~ else

animal = ['사자', '호랑이', '코끼리', '기린']
result = ''

while True:

    try:
        # 예외가 발생할 가능성이 있는 코드로직
        print('동물을 선택하세요.')
        print('1:사자, 2:호랑이, 3:코끼리, 4:기린, 0:종료')

        answer = int(input('선택 :'))

        if answer == 0:
            break

        result = animal[answer-1]

    except:
        # 예외가 발생했을 때 처리로직
        print('0 ~ 4 사이의 숫자를 입력하세요.')
    else:
        # 예외가 발생 안했을 때 코드로직
        print('선택한 animal :', result)



print('프로그램 종료...')