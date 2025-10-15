## 파일 입출력

"""
웹 -> 크롤링 -> 데이터베이스 -> 1차 클렌징 -> 출력 후 담당자에 전달 -> 
2차 클렌징 -> 유용한 데이터셋 -> csv 데이터베이스 입력 -> 인공지능 학습
"""

"""
### r-읽기 w-쓰기(주의:덮어쓰기) a-추가
f = open('text.txt', 'w', encoding='utf-8')
f.write('수강생 여러분')
f.close()
"""

"""
f = open('text.txt', 'w', encoding='utf-8')
f.write('''
        수강생 여러분
        수강생 여러분
        수강생 여러분
        수강생 여러분
        수강생 여러분
        수강생 여러분
        수강생 여러분
        수강생 여러분
        수강생 여러분
        ''')
f.close()
"""

"""
f = open('text.txt', 'r', encoding='utf-8')
s = f.read()
print(s)
f.close()
"""

"""
f = open('text.txt', 'r', encoding='utf-8')
line = f.readline()
print(line)
print(type(line))
f.close()
"""

"""
f = open('text.txt', 'r', encoding='utf-8')
line = f.readline()
while line:
    line = f.readline()
    print(line)
f.close()
"""

"""
f = open('test.txt', 'a', encoding='utf-8')
f.write("힘내자")
f.close()
"""

"""
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('힘내자 !!!!')
"""

"""
list = [10, 20, 30]

with open('test.txt', 'a', encoding='utf-8') as f:
    f.write(str(list))
"""

"""
#csv
list = ['10', '20', '30']

with open('test.csv', 'w', encoding='utf-8') as f:
    f.write("".join(list))
"""

    




