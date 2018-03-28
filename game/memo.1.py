# C:/Python/memo.py
# import sys

# option = sys.argv[1]
# memo = sys.argv[2]


# print(option)
# print(memo)
import sys

option = sys.argv[1]

if option == '-a':
    try:
        memo = sys.argv[2]
        f = open('memo.txt', 'a')
    except FileNotFoundError as e:
        print(str(e))
    else:
        f.write(memo)
        f.write('\n')
        f.close()