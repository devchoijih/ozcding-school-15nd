## 함수와 클래스
"""
객체에 해당하는 것들
- 게임 캐릭터(궁수, 성직자 등등)
- 집, 나무 자동차
- 네이버 홈페이지의 버튼들

class 클래스 이름:
    def 메서드(self):
        코드

"""

"""

class Person:
    def hello(self):
        self.hello = "안녕하세요"
        print(self.hello)

호출 = Person() #인스턴스
호출.hello() #함수

a = int(10) #인스턴스
print(a)

b = list(range(10))
print(b)

#인스턴스와 객체는 같음

"""

"""

class Person:
    def __init__(self):
        self.hello = '안녕하세요' ##생성자

    def greeting(self):
        print(self.hello)

호출 = Person()
호출.greeting()

"""

"""

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요' ##생성자
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

호출 = Person('마리아', 20, '서울시 서초구 반포동')
호출.greeting()

print(호출.name)
print(호출.age)
print(호출.address)

"""

## 클래스의 상속

class Car(object):
    maxspeed = 300
    maxpeople = 5
    def move(self, x):
        print('스피드로 달리고 있습니다.')
    def stop(self):
        print("멈췄습니다.")

class HybridCar(Car):
    battery = 1000
    batteryKM = 300

class ElectricCar(HybridCar):
    battery = 1000
    batteryKM = 400
    def move(self, x):
        print(self.batteryKM, '만큼 달릴 수 있습니다.')
        print(x, '스피드로 달리고 있습니다.')
    
k5 = HybridCar()
print(k5.maxspeed)

electricCark5 = ElectricCar()
electricCark5.maxspeed
electricCark5.battery
electricCark5.move(10)






