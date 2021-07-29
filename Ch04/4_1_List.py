"""
날짜 : 2021/07/14
이름 : 임진슬
내용 : 파이썬 자료구조 List 실습하기 교재 p84
"""

# 리스트
list1 = [1, 2, 3, 4, 5]

print('list1 type :', type(list1))
print('list1[0] :', list1[0])
print('list1[1] :', list1[1])
print('list1[2] :', list1[2])

list2 = [5, 3.14, True, 'Apple']
print('list2 type :', type(list2))
print('list2[0] :', list2[0])
print('list2[1] :', list2[1])
print('list2[2] :', list2[2])

list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('list3 type :', type(list3))
print('list3[0][2] :', list3[0][2])
print('list3[1][1] :', list3[1][1])
print('list3[2][0] :', list3[2][0])

# 리스트 덧셈
ani1 = ['사자', '호랑이', '코끼리']
ani2 = ['곰', '기린']
animal = ani1 + ani2

print('animal :', animal)

# 리스트 수정, 추가, 삭제
nums = [1, 2, 3, 4, 5]
nums[1] = 7
print('nums :', nums)

nums[2:4] = [8, 9, 10]
print('nums :', nums)

nums[3:5] = []
print('nums :', nums)

# 리스트 반복문
lists = [1, 2, 3, 4, 5]

for n in lists:
    print('n :', n)

people = ['김유신', '김춘추', '장보고', '강감찬', '이순신']

for person in people:
    print('person :', person)

for index, value in enumerate(people):
    print('people[%d] : %s' % (index, value))

scores = [62, 86, 72, 74, 96]
total = 0

for score in scores:
    total += score

print('scores의 총합 :', total)

# List Comprehension
numbers = [1, 2, 3, 4, 5]

res1 = [num * 3 for num in numbers]
res2 = [num * 3 for num in numbers if num % 2==1]

print('res1 :', res1)
print('res2 :', res2)
