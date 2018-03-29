# c:/Python/tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]
try:
    f = open(src)
except FileNotFoundError as e:
    print("%s || 파일을 찾을수없습니다." % e)
else :
    tab_content = f.read()
    f.close()

space_content = tab_content.replace("\t", " "*4)#\t:tab

try:
    f = open(dst, 'w')#w:쓰기
except:
    print("%s || 파일을 쓸수없습니다." % e)
else:
    f.write(space_content)
    f.close()