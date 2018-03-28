class FourCal:  # 부보클래스
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):  # MoreFourCal(상속받을 클래스명 )
    def pow(self):
        result = self.first ** self.second  # 거듭 제곱
        return result


class SafeFourCal(FourCal):#ZeroDivisionError요류 해결 클래스 오버라이딩(덮어쓰기)
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
             return 0
        else:
            return self.first / self.second

# a = MoreFourCal(4, 0)
a = SafeFourCal(4, 0)
print(a.sum())
print(a.mul())
# print(a.pow())
print(a.div())#ZeroDivisionError: division by zero 은 4을0으로 나누기 떄문에
# a=FourCal(4,3)
# print(type(a))
# print(a.sum())
# print(a.mul())
# print(a.sub())
# print(a.div())
