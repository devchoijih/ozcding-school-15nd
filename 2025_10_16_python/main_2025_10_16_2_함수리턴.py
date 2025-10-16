## 값 없이 리턴하는 이유

def oz_return():
    print("파이썬")
    print("재미있엉")
    return
    print("거짓말하네") ## 출력 안됨

oz_return()

#값과 함께 리턴하는 경우
def oz_return():
    return "파이썬 재미있엉"

result = oz_return()
print(result)

def oz_return():
    return

result = oz_return()
print(result) ## None 출력
