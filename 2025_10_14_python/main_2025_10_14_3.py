##while문

"""
i = 0
while i < 10:
    print("점점 성장하는 여러분~~~")
    i += 1

# while문 조건식 증감, 감소

#1.기본적인 증가 유형

i = 1
while i < 10:
    print('이정도로 성장할줄이야', i)
    i += 1
#2.기본적인 감소유형
i = 10
while i > 0:
    print('이정도로 성장할줄이야', i)
    i -= 1

"""

# while문이 for보다 강점인 부분?

import random

i = 0
while i != 4:

    i = random.randint(1,6)
    print(i)

# while문에도 else가 있음

양파 = 10
while 양파 > 10:
    print("양파", 양파, "개 남았습니다.")
    if 양파 == 0:
        break;
    양파 -= 1;
else:
    print("양파 다 팔렸습니다.")
