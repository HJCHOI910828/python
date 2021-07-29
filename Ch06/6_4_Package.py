"""
날짜 : 2021/07/21
이름 : 임진슬
내용 : 파이썬 패키지 묘듈 실습하기 교재 p175
"""

import Ch06.sub2.calc
import Ch06.sub2.calc as c
from Ch06.sub2.calc import multi
from Ch06.sub2.calc import *

r1 = Ch06.sub2.calc.plus(1, 2)
r2 = c.minus(3, 5)
r3 = multi(4, 6)
r4 = div(8, 4)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)

