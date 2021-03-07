# Bài tập cơ bản

# Sau khi tạo ra lớp Person rồi, con hãy viết hàm compare_age
# để so sánh tuổi của các bạn nhé.
# Yêu cầu
# - Sử dụng lớp Person vừa tạo ở bài thực hành 3
# - Tạo một hàm compare_age(person1, person2)
# nhận vào 2 đối tượng của lớp Person
# - Hàm này sẽ so sánh tuổi của 2 đối tượng được nhận vào,
# và in ra trên màn hình "[Name 1]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def compare_age(person1, person2):
    if person1.age > person2.age:
        print(f"{person1.name} is older than {person2.name}")

    elif person1.age < person2.age:
        print(f"{person2.name} is older than {person1.name}")

    else:
        print(f"{person1.name} and {person2.name} are of the same age")


trau = Person("Trau", 13)
william = Person("William", 13)
compare_age(trau, william)
# Trau and William are of the same age

trau = Person("Trau", 11)
william = Person("William", 13)
compare_age(trau, william)
# William is older than Trau
