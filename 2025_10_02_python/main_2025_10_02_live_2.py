###자료 구조

####리스트

fruits = ["사과", "바나나", "오렌지", "포도", "키위"]
numbers = [1, 2, 3, 4, 5]
mixed = ["홍길동", 25, True, 175.5] #서로 다른 타입도 가능

print(dir(fruits))

fruits.append("포도")

print(fruits[5])

breads = [ "후렌치파이", "순수롤", "아몬드 크루아상", "초코소라빵", "명랑바게트"]
print(len(breads))
print(breads.index("아몬드 크루아상"))
print(breads[::-1])
print(breads[-1])
print(breads[-2])

breads.insert(0, "테스트")
print(breads[0])

breads.extend(fruits);
print(breads[7])

breads.append(["김밥, 치즈"])
print(breads)
