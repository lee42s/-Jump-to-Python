#try문은 else절을 지원한다. else절은 예외가 발생하지 않은 경우에 실행되며 반드시 except절 바로 다음에 위치해야 한다.
try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
#만약 foo.txt라는 파일이 없다면 except절이 수행되고 foo.txt 파일이 있다면 else절이 수행될 것이다.