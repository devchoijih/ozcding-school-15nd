## 제너레이터

def test():
    print("첫번째 출력")
    yield 1
    print("두번째 출력")
    yield 2
    print("세번째 출력")


output = test()
print("네번째 출력")

x = next(output)
print(x)
print("다섯번째 출력")
y = next(output)
print(y)
print("여섯번째 출력")
z = next(output)
print(z)