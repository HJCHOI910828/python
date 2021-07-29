"""
날짜 : 2021/07/19
이름 : 임진슬
내용 : 파이썬 자료구조 집합 Set 실습하기 교재 p96
"""

# 집합 생성
set1 = {1, 2, 3, 4, 5, 3, 2}
print('set1 type :', type(set1))
print('set1 :', set1)

set2 = set('Hello World')
print('set2 type :', type(set2))
print('set2 :', set2)

# 집합 출력(리스트 변환)
list1 = list(set1)
print('list1 :', list1)
print("list1[0] :", list1[0])
print("list1[3] :", list1[3])
print("list1[4] :", list1[4])

list2 = list(set2)
print('list2 :', list2)
print("list2[0] :", list2[0])
print("list2[3] :", list2[3])
print("list2[4] :", list2[4])