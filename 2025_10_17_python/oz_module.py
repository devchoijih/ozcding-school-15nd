## 데코레이터

pi = 3.141592

def number_input():
    value = input("반지름을 입력해주세요")
    return float(value)

def get_circum(radius):
    return 2 * pi * radius

def get_circle(radius):
    return pi * radius * radius
        
