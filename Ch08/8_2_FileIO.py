"""
날짜 : 2021/07/26
이름 : 임진슬
내용 : 파이썬 파일 입출력 실습하기 교재 p217
"""

# 파일읽기 (한 줄)
file1 = open('C:/Users/user/Desktop/sample.txt', 'r')
line = file1.readline()

print('line :', line)
file1.close()

# 파일읽기 (여러 줄)
file2 = open('C:/Users/user/Desktop/sample.txt', 'r')

while True:

    line = file2.read()

    if not line:
        break

    print('line :', line)

file2.close()

# 파일쓰기
file3 = open('C:/Users/user/Desktop/sample2.txt', 'w')
file3.write('안녕하세요.\n')
file3.write('반갑습니다.\n')
file3.write('감사합니다.\n')
file3.close()

# 구구단 쓰기
gugudan = open('C:/Users/user/Desktop/gugudan.txt', 'w')

for x in range(2, 10):
    gugudan.write('%d단\n' % x)
    for y in range(1, 10):
        z = x * y
        gugudan.write('%d x %x = %d\n' % (x, y, z))

gugudan.close()
