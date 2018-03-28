try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:#5행~6행 가각 해당하는 오류 일때 예외처리 한다.
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    b = [1,2]
    print(b[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    c = [1,2]
    print(c[3])
    4/0
except (ZeroDivisionError, IndexError) as e:#2개 이상의 오류를 동시에 처리하기 위해서는 위와같이 괄호를 이용하여 함께 묶어주어 처리하면 된다.
    print(e)

#오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass#FileNotFoundError가 발생할 경우 pass를 사용하여 오류를 그냥 회피하도록 한 예제이다.

#오류 일부러 발생시키기
class Bird:
    def fly(self):
         raise NotImplementedError
  
class Eagle(Bird):
    def fly(self):
        print("very fast")
    
eagle = Eagle()
eagle.fly()