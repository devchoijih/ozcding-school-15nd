## set

채소 = {"당근", "배추", "대파", "양파"}

#세트를 만드는 다양한 방법
세트 = set()
세트
세트2 = {}
세트2

#중복을 제일 싫어하는 set

사과_리스트 = list("apple")
print(사과_리스트)
사과_튜플 = tuple("apple")
print(사과_튜플)
사과_set = set("apple")
print(사과_set)

# set() 자료형의 데이터 추가,삭제,변경
채소.add("토마토")
print(채소)

## 이건 짤려서 각각 들어간다 '깻', '잎'
채소.update("깻잎")
print(채소)

#채소.remove("잎") // 없으면 error
#채소.discard("깻") // 없어도 상관없음

반환된_채소 = 채소.pop()
print(f'{반환된_채소}는 채소입니다')

#대표적으로 합집합, 교집합, 차집합 가능

채소1 = {"당근", "양파", "오이", "배추"}
채소2 = {"양파", "오이", "대파", "가자"}

#합집합(union)
print(채소1 | 채소2)
print(set.union(채소1, 채소2))

#교집합(intersection)
print(채소1 & 채소2)
print(set.intersection(채소1, 채소2))

#차집합(difference)
print(채소1 - 채소2)
print(set.difference(채소1, 채소2))