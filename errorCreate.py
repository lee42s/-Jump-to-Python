# 파이썬 내장 클래스인 Exception클래스를 상속하여 만들 수 있다.
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def say_nick(nick):
    if nick == '바보':
        raise MyError("허용되지 않는 별명입니다.")
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)