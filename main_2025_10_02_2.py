##변수 : 하나의 값을 저장할 수 있는 공간을 생성하는 것

#1. int(integer) : 정수
#2. float(float) : 실수
#3. str(string) : 문자
#4. bool(bool, boolean) : 참 또는 거짓, true 또는 false, 1 또는 0
#5. list
#6. tuple
#7. dict
#8. set

box_num = "하나"
print(type(box_num))

#int, float
#int -> float

print(float(5))
print(int(5.0))
print(dir(10))

#str : 문자열
#특징 : 시퀀스 자료형
#시퀀스란? 요소들이 연속적으로 이어진 자료형

소속 = "s매직 서울북부"

#0 인덱스 시작
print(소속)
print(소속[0])
print(소속[1])
print(소속[2])
print(소속[3])
print(소속[4])
print(소속[5])
print(소속[6])
print(소속[7])

print("매" in 소속)

print(len(소속))
print(소속[3:6])
print(소속[-1])

생년월일 = '2000.12.25'
년 = 생년월일[0:4]
월 = 생년월일[5:7]
일 = 생년월일[8:11]

print(f'{년}. {월}. {일}')

#전체 출력
print(생년월일[::])

#전체 출력 리버스
print(생년월일[::-1])

#첫번째 인덱스 기준으로 2칸씩 띄어쓰기 출력하기
print(생년월일[::2])

퀴즈 = '스님이 공중에 뜬다를 4글자로 말하면? 어중이떠중이'
print(퀴즈[22:28])

과일 = 'apple'
print(dir(과일))
print(과일.count('p'))
print(len(과일))
print(과일.index("p"))