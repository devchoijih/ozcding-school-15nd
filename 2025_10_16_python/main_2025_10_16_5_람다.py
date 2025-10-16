## 펑션으로 매개변수를 받을수 있음

def oz_call(function):
    for i in range(5):
        function(i+1)

def talk(str):
    print(f'{str}. 파이썬 이건 또 무슨 개념이야?')


oz_call(talk)

#자기 자신을 곱한 결과를 새로운 list를 만들어주는 map() 함수 코드

"""
def square(i):
    return i * i

numbers_list = [1,2,3,4,5,6,7,8,9,10]

result = map(square, numbers_list)

print("map 결과:", result)
print("map 결과의 list 형변환:", list(result))

def under(i):
    return i < 5

numbers_list = [1,2,3,4,5,6,7,8,9,10]

result = filter(under, numbers_list)

print("map 결과:", result)
print("map 결과의 list 형변환:", list(result))

"""

##람다

square = lambda i : i * i

numbers_list = [1,2,3,4,5,6,7,8,9,10]

result = map(square, numbers_list)

print("map 결과:", result)
print("map 결과의 list 형변환:", list(result))

