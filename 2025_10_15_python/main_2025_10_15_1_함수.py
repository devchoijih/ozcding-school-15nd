## 함수와 클래스

"""

def 양파():
    print('양파를 2개를 수락했습니다.')
def 대파():
    print('대파를 수락했습니다.')

양파()
대파()

#함수선언 함수이름 입력(파라미터)
def function(x, y):
    z = x + y
    return z

print('옥수수와 수박의 수확량 :', function(10, 2))

def 계산(가격, 개수):
    return 가격 * 개수

print(계산(1000, 5), '원 입니다.')

a = 100
def f():
    global a
    a = a + 1
    return a
print(f())

won = {'A등급':1000, 'B등급':500, 'C등급':100}

def 계산(a, b, c):
    합계 = won['A등급'] * a + won['B등급'] * b + won['C등급'] * c
    return 합계

print(계산(5, 2, 3), '원입니다.')

"""





