class Calculator:
    def __init__(self):#__init__생성자,인스턴스를 만들 때 자동으로 실행되는 함수
        self.result = 0 

    def adder(self, num):# 메서드 self 객체자기 자신 this 호출한자기가신
        self.result += num
        return self.result
    def sub(self, num):# 메서드
        self.result -= num
        return self.result
cal1 = Calculator()# 객체이면서 인스턴스 이고 인스턴스란 cal1.result 이런식으로 해당 객체에 속성과메서드 을 쓸수있다.
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))