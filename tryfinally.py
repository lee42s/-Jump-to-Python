#finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 보통 finally절은 사용한 리소스를 close해야 할 경우에 많이 사용된다.
f = open('foo.txt', 'w')
try:
    f = open('foo.txt', 'r')
finally:
    f.close()