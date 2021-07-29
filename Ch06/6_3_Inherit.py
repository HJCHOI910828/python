"""
날짜 : 2021/07/21
이름 : 임진슬
내용 : 파이썬 클래스 상속 실습하기 교재 p163
"""

from Ch06.sub2.StockAccount import StockAccount
from Ch06.sub2.SmartPhone import SmartPhone


kb = StockAccount('KB증권', '01254-1-235', '김유신', 100000, '삼성전자', 1, 80000)
kb.deposit(100000)
kb.buy(2, 70000)
kb.show()

iphone = SmartPhone('A10', '1GB', '256GB', 'iphone12', '010-4123-4562')
iphone.calc()
iphone.call()
iphone.info()

