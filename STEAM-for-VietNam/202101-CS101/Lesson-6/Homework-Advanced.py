# Bài tập nâng cao

# Để cho thú vị hơn, các con hãy tạo thêm các lớp kế thừa từ lớp Person nhé.
# Yêu cầu:
# - Sử dụng lớp Person vừa tạo ở bài thực hành 3 với các phương thức introduce
# và greet
# - Định nghĩa một lớp Teacher thừa kế từ lớp Person
# - Định nghĩa một lớp Student thừa kế từ lớp Person
# - Ngoài các thuộc tính như của lớp Person, lớp Teacher có thêm thuộc tính:
#       school - nơi giảng dạy của giáo viên
# - Ngoài các phương thức được kế thừa từ lớp Person, lớp Teacher có thêm
# phương thức
#       greet_student
# - Ngoài các thuộc tính như của lớp Person, lớp Student có thêm thuộc tính
#       greet_teacher

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old.")

    def greet(self, other_person):
        print(f"Hi, {other_person.name}! I'm {self.name}. Nice to meet you!")


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name=name, age=age)
        self.school = school

    def greet_teacher(self, teacher):
        print(f"Hi, teacher {teacher.name}! "
              f"I'm studying at {self.school} school.")


class Teacher(Person):
    def __init__(self, name, age, school):
        super().__init__(name=name, age=age)
        self.school = school

    def greet_student(self, student):
        print(f"Hi, student {student.name}! "
              f"I'm teaching at {self.school} school.")


teacher1 = Teacher("Quang", 30, "Nguyen Trai")
teacher2 = Teacher("Mai", 35, "Nguyen Khuyen")

student1 = Student("Hoa", 12, "Dang Tran Con")
student2 = Student("Hong", 15, "Nguyen Trai")

teacher1.introduce()
teacher1.greet(teacher2)
teacher1.greet_student(student1)

student1.introduce()
student1.greet(student2)
student1.greet_teacher(teacher1)

# Output:
# Hi, I'm Quang. I'm 30 years old.
# Hi, Mai! I'm Quang. Nice to meet you!
# Hi, student Hoa! I'm teaching at Nguyen Trai school.
# Hi, I'm Hoa. I'm 12 years old.
# Hi, Hong! I'm Hoa. Nice to meet you!
# Hi, teacher Quang! I'm studying at Dang Tran Con school.
