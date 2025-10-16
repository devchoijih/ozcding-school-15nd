## 튜플은 list와 비슷한 시퀀스 자료형임

"""
oz_tuple = (1, 2, 3)

print(oz_tuple)
print(oz_tuple[0])
print(oz_tuple[1])
print(oz_tuple[2])

x, y, z = 1 ,2 ,3
print(x)
print(y)
print(z)

#튜플을 이용하면 여러 개의 값을 리턴할 수 있습니다.

def oz_tuple():
    return (1, 2)

x, y = oz_tuple()

print("x:", x)
print("y:", y)

"""

for i, fruit in enumerate(["김밥", "치킨", "돈까스", "보쌈"]):
    print(i, fruit)

#divmode() 사용 시 튜플 형태로 몫과 나머지를 반환

a, b = 7, 3
x, y = divmod(a, b)
print("몫:", x)
print("나머지:", y)