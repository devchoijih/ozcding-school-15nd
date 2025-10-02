#f-string은 변수를 쉽게 넣는것임

name = "최지훈"
age = 30
height = 180.3

introduction = f"안녕하세요! 저는 {name}이고, {age}살입니다."
print(introduction)

next_year = f"내년에는 {age + 1}살 입니다!"
print(next_year)

print(f"키는 {height:.1f}cm 입니다")

fruits = ["사과", "바나나", "오렌지", "포도", "키위"]

print(fruits[0])

## 산술 연산자

a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

#여러줄 주석
"""
주석입니다~~~
"""

# 비교 연산자의 결과값은 bool타입

x = 5
y = 3

print(f"{x} > {y} = {x > y}")
print(f"{x} < {y} = {x < y}")
print(f"{x} >= {y} = {x >= y}")
print(f"{x} <= {y} = {x <= y}")
print(f"{x} == {y} = {x == y}")
print(f"{x} != {y} = {x != y}")