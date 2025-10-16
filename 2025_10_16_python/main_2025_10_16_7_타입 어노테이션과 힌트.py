## 타입 어노테이션과 힌트
## 읽기 쉽게 하도록 하는 것

#직육면체의 부피를 구하는 함수

"""
def oz(x, y, h):
    #type:(int, int, int) -> int
    return x * y * h

print(oz(10, 10, 10))
"""

def oz(x: int, y:int, h:int) -> int:
    return x * y * h

print(oz(10, 10, 10))

my_dog : str = "hunt"
my_dog_age : int = 7

dogs: list[str] = ["닥스훈트", "시바견", "웰시코기", "이탈리안그레이하운드"]

dogs: dict[str, int] = {
    ...
}

