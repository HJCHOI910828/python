"""
날짜 : 2021/07/20
이름 : 임진슬
내용 : 파이썬 함수 스코프 실습하기 교재 p132
"""

def sum(x, y):
    total = 0
    for k in range(x, y+1):
        total += k

    return total

total = 0
start = 1
end = 10

total= sum(start, end)
print('total :', total)
