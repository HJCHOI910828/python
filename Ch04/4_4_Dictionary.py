"""
날짜 : 2021/07/19
이름 : 임진슬
내용 : 파이썬 자료구조 Dictionary 실습하기 교재 p96
"""

# 딕셔너리 생성 Key, Value
dic1 = {
    'A': 'Apple',
    'B': 'Banana',
    'C': 'Cherry'
}

print('dic1 type :', type(dic1))
print('dic1 :', dic1)
print('dic1[A] :', dic1['A'])
print('dic1[B] :', dic1['B'])
print('dic1[C] :', dic1['C'])

dic2 = {1: '서울',
        2: '대전',
        3: '대구',
        4: '부산',
        5: '광주'}

print('dic2[1] :', dic2[1])
print('dic2[3] :', dic2[3])
print('dic2[5] :', dic2[5])

dic3 = {
    101: [1, 2, 3, 4, 5],
    102: (6, 7, 8, 9, 10),
    103: {'한국', '미국', '중국', '일본'},
    104: {'p1': '김유신', 'p2': '김춘추', 'p3': '장보고'}
}

r1 = dic3[101][2]

r2 = dic3[103]
r3 = list(dic3[103])
r4 = r3[0]
result = list(dic3[103])[0]


print('dic3[101][2] :', dic3[101][2])
print('dic3[102][1] :', dic3[102][1])
print('result :', result)

print("dic3[104]['p2'] :", dic3[104]['p2'])

# 응용
dics = [dic1, dic2, dic3]
print("dics[0]['A'] :", dics[0]['A'])
print("dics[1][4] :", dics[1][4])
print("dics[2][104]['p2'] :", dics[2][104]['p2'])
