lst = [1, 2, 3, 4]
result = lst * 2
print(result)

# (1) 리스트 정렬
print(result)
result.sort()
print(result)
result.sort(reverse = True)
print(result)

# (2) 리스트 요소 검사
import random
r = []
for i in range(5):
    r.append(random.randint(1, 5))

print(r)
if 4 in r :
    print('있음')

else:
    print('없음')