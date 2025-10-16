## 가변 매개변수

"""

def 함수이름(매개변수, *가변 매개변수):
    코드

    * 가변 매개변수 뒤에는 일반 매개변수가 올 수 없습니다.
    * 가변 매개변수는 하나만 사용할 수 있습니다
"""

"""

def oz(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

oz(1, "안녕", "하세요", "저는", "초이", "지훈입니다")

"""

## 기본 매개변수

"""
*일반 매개변수 뒤에서만 적용하여야함
"""

"""
def oz(value, n=2):
    for i in range(n):
        print(value)

oz("123", n=10)
"""

#(기본 매개변수, 가변 매개변수)

"""
## 의미없음 순서 중요

def oz(n=3, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

oz(n=10, "123", "456")

"""

"""
def oz(*values, n=3):
    for i in range(n):
        for value in values:
            print(value)
        print()

oz("123", "456")
"""

#키워드 매개변수 ##순서를 바꿔도됨

#직육면체를 부피를 구하는 코드를 작성해보자 : 가로 : x, 세로 : y, 높이 : h
def oz(x, y=20, h=10):
    print(x * y / h)

#x식별자에 매개변수 10을 넣은 경우
oz(10)
#x식별자에 10을 넣고 y=10이라는 키워드 매개변수를 이용한 경우
oz(10, y=10)
#모든 매개변수를 키워드 매개변수로 넣은 경우
oz(x=5, y=5, h=5)

#모든 매개변수를 키워드 매개변수로 넣은 경우
oz(h=5, y=20, x=2)



