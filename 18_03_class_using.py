# data = "홍길동|42|A"
# tmp = data.split("|")
# age = tmp[1]


# def print_age(data):
#     tmp = data.split("|")
#     age = tmp[1]
#     print(age)

# def print_grade(data):
#     tmp = data.split("|")
#     name = tmp[0]
#     grade = tmp[2]
#     print("%s님 당신의 점수는 %s입니다." % (name, grade))#첫번째%s 는 name 두번째%s는 grade 

# print_grade(data)
# print_age(data)

class Data:
    def __init__(self,data):
        tmp =data.split("|")
        self.name =tmp[0]
        self.age =tmp[1]
        self.grade = tmp[2]
    def print_age(self):
        print(self.age)
    def print_grade(self):
        print("%s님 당신의 점수는 %s입니다." % (self.name, self.grade))

data = Data("홍길동|42|A")
data.print_age()
data.print_grade()