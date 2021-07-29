"""
날짜 : 2021/07/20
이름 : 임진슬
내용 : 파이썬 클래스 실습하기 교재 p148
"""

from Ch06.sub1.Car import Car
from Ch06.sub1.Account import Account

# 객체 생성
bmw = Car('BMW 520d', '남색', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

benz = Car('Benz', '검정색', 5000)
benz.speedUp()
benz.speedDown()
benz.show()


# 은행 객체 생성
kb = Account('국민은행', '125-52-52345', '김유신', 10000)
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

wr = Account('우리은행', '456-561-4653', '김춘추', 30000)
wr.deposit(40000)
wr.withdraw(25000)
wr.show()
