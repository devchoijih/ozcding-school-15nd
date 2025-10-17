## 데코레이터

def test(function):
    def wrapper():
        print("허언증이 재발했습니다.")
        function()
        print("격리 되었습니다.")
    return wrapper 

@test
def oz():
    print("파이썬 진짜 재미있엉 하하")

oz()    

        
