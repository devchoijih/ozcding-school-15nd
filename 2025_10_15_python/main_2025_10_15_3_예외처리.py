## 예외코드 작성

"""
try:
    x=int(input('나눌 숫자를 입력하세요'))
    y = 10 / x
    print(y)
except:
    print("예외가 발생했습니다.")

"""

y = [10, 20, 30]

try:
    index, x = map(int, input('나눌 숫자를 입력하세요: ').split(","))
    print(y[index]/ x)
except ZeroDivisionError:
    print("오류입니다.")
except IndexError:
    print("잘못된 인덱스 입니다.")
finally :
    print("코드 실행이 종료되었습니다.")



