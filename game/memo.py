# d:/Python/memo.py
import sys

option = sys.argv[1]


if option == '-a':
    try:
        memo = sys.argv[2]
        f = open('memo.txt', 'a')#a:는 추가
    except:
        raise WindowsError('파일을 쓸수없습니다.')
    else:
        f.write(memo)
        f.write('\n')
        f.close()
elif option == '-v':#v:는 보기
    try:
        f = open('memo.txt')
    except:
        raise WindowsError('파일을 없거나,볼수없습니다.')
    else:
        memo = f.read()
        f.close()
        print(memo)