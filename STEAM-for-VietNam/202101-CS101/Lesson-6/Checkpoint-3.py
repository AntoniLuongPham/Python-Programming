class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, I'm " + self.name + "!")


trau = Student("Trau", 12)
trau.say_hello()

william = Student("William", 14)
william.say_hello()

print(trau)
print(william)
