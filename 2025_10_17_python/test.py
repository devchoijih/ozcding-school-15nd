try:
    a, b = map(int, input("숫자를 입력해 주세요.").split(" "))
    print(f'{a/b}')
except ValueError:
    print("숫자를 입력해 주세요.")
except ZeroDivisionError:
    print("나누는 수는 0이 될수 없습니다.")

        
