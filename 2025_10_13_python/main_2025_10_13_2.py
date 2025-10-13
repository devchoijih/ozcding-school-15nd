##list 리스트

"""
리스트 = []
print(리스트)

리스트 = [23, "이게 리스트다", 3.23, True, False]
print(리스트)

리스트2 = list()
print(리스트2)

##range? 연속된 숫자를 생산하는 기능
range(0, 10)

#list(range(시작,끝))
리스트_매직_들어간다 = list(range(0, 20))
print(리스트_매직_들어간다)

리스트_매직_들어간다 = list(range(0, 20, 2))
print(리스트_매직_들어간다)
"""

"""
#슬라이싱

로또 = [3, 5, 15, 33, 41, 44]
#로또 변수에 있는 리스트의 인덱스 1번부터 2번까지의 값을 출력해
print(로또[1:3])

#로또 변수의 마지막 위치 출력해줘
print(로또[-1])

#반대로 출력해보세요
print(로또[::-1])

#로또 리스트안에 33이 있는지 확인해보세요
print(33 in 로또)

#로또 리스트를 로또2 리스트와 합쳐보세요
로또2 = [2, 12, 15, 24, 33, 39]
print(로또 + 로또2)

#range를 이용해서 1부터 10사이에 짝수만 들어있는 짝수(변수명) 리스트를 만들어주세요
짝수 = list(range(2,11,2))
print(짝수)

#짝수 리스트에 들어있는 값을 2배늘리고 다시 짝수 변수에 담아줘
짝수 = 짝수 * 2
print(짝수)

#짝수 리스트에 들어있는 요소의 개수를 구해주세요
print(len(짝수))

#짝수 리스트에 3번째 인덱스를 출력해주세요
print(짝수[3])

#len()함수를 이용해 인덱스 마지막 값을 출력해주세요
print(짝수[len(짝수)-1])
"""

#list 값 넣고, 바꾸고, 지우고

mzfood = ["숙주", "분모자", "마라", "소세지", "소고기", "옥수수면"]

# 값을 넣는 방법 2가지 : append() : 마지막 요소에 값을 넣음, insert() : 원하는 곳에 값을 넣음
mzfood.append("고수")
print(mzfood)

mzfood.insert(2, "탕후루")
print(mzfood)

#값 지우기
del mzfood[-1]
print(mzfood)

del mzfood[0]

#값 바꾸기
mzfood[-2] = "양고기"
print(mzfood)

print(dir(list))

print(mzfood)

mzfood.reverse()
print(mzfood)
mzfood.sort()
print(mzfood)

#2차원 리스트에 대해서도 공부는 필수!!!!
양파같은 = [[2,0], [3,1]]
print(양파같은)

양파같은.append([4,1])
print(양파같은)