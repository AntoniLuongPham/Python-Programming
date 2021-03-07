# Bài tập thực hành 02

# Để mở rộng cho lớp Person chúng ta vừa tạo, con hãy thêm phương thức (method)
# introduce cho lớp đấy.
# Yêu cầu:
# - Sử dụng lớp Person vừa tạo ở bài thực hành 1 (chứa thuộc tính name, age)
# - Tạo thêm phương thức introduce
# - Khi gọi phương thức introduce, trên màn hình sẽ được in ra "Hi, I'm [name].
# I'm [x] years old."

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old.")


trau = Person("Trau", 11)
trau.introduce()
# Hi, I'm Trau. I'm 11 years old.
