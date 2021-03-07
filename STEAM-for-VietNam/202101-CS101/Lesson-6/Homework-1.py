# Bài tập thực hành 01

# Dựa vào những gì đã học trên lớp, các con hãy tạo lớp (class) Person nhé!
# Yêu cầu:
# - Định nghĩa lớp Person
# - Lớp Person có 2 thuộc tính (attribute) là name (tên) và age (tuổi)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


trau = Person("Trau", 11)
print(trau.name)
print(trau.age)

# Output:
# Trau
# 11
