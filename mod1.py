# mod1.py
def sum(a, b):
    return a + b

def safe_sum(a, b): #mod1.safe_sum(숫자,숫자) 이면 6행실행
    if type(a) != type(b): #a와b가 숫자 이면 7행 아니면 9행
        print("더할수 있는 것이 아닙니다.")
        return 
    else: 
        result = sum(a, b) #2번행 인 sum함수 실행 후
    return result

if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))

'''
파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수명이다. 
만약 C:\Python>python mod1.py처럼 직접 mod1.py 파일을 실행시킬 경우 mod1.py의 __name__ 변수에는 __main__ 이라는 값이 저장된다. 
하지만 파이썬 쉘이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 "mod1"이라는 mod1.py의 모듈이름 값이 저장된다.
'''