## 반복문을 이용한 팩토리얼 구현 코드
# 곱하기 연산이 진행되기 때문에 output의 초기값은 1입니다.
# 더하기 연산이 진행되는 경우는 0으로 초기값을 설정합니다.

"""
def oz_factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

n = int(input("구하고자하는 팩토리얼의 수를 입력해주세요"))
print(f'{n}의 결과는 {oz_factorial(n)} 입니다')
"""

def oz_factorial(n):
    if n == 0:
        return 1
    else:
        return n * oz_factorial(n-1)


n = int(input("구하고자하는 팩토리얼의 수를 입력해주세요"))
print(f'{n}의 결과는 {oz_factorial(n)} 입니다')

