# Bài tập thực hành 03

# Sau cùng, chúng ta hãy giúp các bạn được tạo ra từ lớp Person
# tương tác với nhau nhé.
# Yêu cầu:
# - Sử dụng lớp Person vừa tạo ở bài thực hành 2
# (chứa thuộc tính name, age, và phương thức introduce)
# - Tạo thêm phương thức greet nhận vào 1 đối tượng khác của lớp Person.
# - Khi gọi phương thức greet, trên màn hình sẽ được in ra
# "Hi, [tên đối tượng được nhận vào]! I'm [name]. Nice to meet you!"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old.")

    def greet(self, other_person):
        print(f"Hi, {other_person.name}! I'm {self.name}. Nice to meet you!")


trau = Person("Trau", 11)
william = Person("William", 13)
trau.greet(william)
william.greet(trau)
# Hi, Trau! I'm William. Nice to meet you!
# Hi, William! I'm Trau. Nice to meet you!
