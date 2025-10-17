## try:
## 예외가 발생했을 때 실행할 코드
## except:
## 예외가 발생했을 때 실행할 코드
"""
try:
    x, y = map(int, input("밑변과 높이를 입력해주세요.").split(" "))
    print(f'삼격형의 넓이는 {x*y/2}입니다.')
except:
    print("정수로 입력하지 않아 계산이 불가합니다.")

"""

"""
try :  
    예외가 발생할 가능성이 있는 코드
except:
    pass
"""
"""

try:
    x, y = map(int, input("밑변과 높이를 입력해주세요.").split(" "))
    print(f'삼격형의 넓이는 {x*y/2}입니다.')
except:
    pass
    
"""

"""
try :  
    예외가 발생할 가능성이 있는 코드
except:
    예외가 발생했을 때 실행할 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
"""

"""

try:
    x, y = map(int, input("밑변과 높이를 입력해주세요.").split(" "))
except:
    print("정수로 입력하지 않아 계산이 불가합니다.")
else:
    print(f'삼격형의 넓이는 {x*y/2}입니다.')

"""

"""
try :  
    예외가 발생할 가능성이 있는 코드
except:
    예외가 발생했을 때 실행할 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    무조건 실행할 코드
"""

"""

try:
    x, y = map(int, input("밑변과 높이를 입력해주세요.").split(" "))
except:
    print("정수로 입력하지 않아 계산이 불가합니다.")
else:
    print(f'삼격형의 넓이는 {x*y/2}입니다.')
finally:
    print("프로그램이 종료 되었습니다.")

"""
"""
##예외객체

numbers = [23, 11, 7, 4, 12]

try:
    number_input = int(input("찾고싶은 값의 위치를 입력해주세요"))
    print(f'{number_input}번째 요소 : {numbers[number_input]}')
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

try:
    number_input = int(input("찾고싶은 값의 위치를 입력해주세요"))
    print(f'{number_input}번째 요소 : {numbers[number_input]}')
except ValueError:
    print("정수로 입력해주세요")
except IndexError:
    print("리스트의 범위를 벗어났습니다. 입력값을 다시 확인해주세요.")
except Exception as exception:
    print("대처 불가한 예외가 발생했습니다.")

"""

##raise 구문
##예외를 강제로 발생시키는 기능, 우리가 의도하지 않게 작동하는 상황을 방지하기 위함

number = input("숫자를 입력해주세요")
number = int(number)

if number > 0:
    raise NotImplementedError

