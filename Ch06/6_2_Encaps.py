"""
날짜 : 2021/07/21
이름 : 임진슬
내용 : 파이썬 캡슐화(정보은닉) 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account

kb = Account('국민은행', '101-11-4645', '김유신', 10000)

kb.deposit(40000)
kb.withdraw(5000)

# 캡슐화(정보은닉)를 통한 취약코드 예방
# kb.__money += 1

kb.show()
