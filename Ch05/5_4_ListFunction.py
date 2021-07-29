"""
날짜 : 2021/07/20
이름 : 임진슬
내용 : 파이썬 리스트함수 실습하기 교재 p88
"""

import time as time
import math
import random

dataset = [1, 4, 3]
print('1. dataset :', dataset)

# 원소 추가
dataset.append(2)
dataset.append(5)
print('2. dataset :', dataset)

# 원소 오름차순 정렬
dataset.sort()
print('3. dataset :', dataset)

# 원소 내림차순 정렬
dataset.sort(reverse=True)
print('4. dataset :', dataset)

# 원소 뒤집기
dataset.reverse()
print('5. dataset :', dataset)


# 원소 삽입 - 인덱스 번호, 삽입할 원소
dataset.insert(2, 6)
print('6. dataset :', dataset)

# 원소 삭제
dataset.remove(6)
print('7. dataset :', dataset)

# map함수 : 리스트 원소를 지정된 함수로 일괄 처리해주는 함수
def plus10(n):
    return n + 10

list1 = [1, 2, 3, 4, 5]
rs1 = map(plus10, list1)
print('rs1 :', list(rs1))

list2 = [0.1, 1.2, 2.6, 3.4, 4.9]
rs2 = map(math.ceil,list2)
print('rs2 :', list(rs2))

list3 = ['1', '2', '3', '4', '5']
rs3 = map(int, list3)
print('rs3 :', list(rs3))

list4 = [10, 20, 30, 40, 50]
rs4 = map(lambda x:x+1, list4)
print('rs4 :', list(rs4))
