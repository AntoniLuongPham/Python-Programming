class Family:
    def __init__(self, name_of_family: str):
        self.name_of_family = name_of_family

    def say_hello(self):
        print(f"We are the {self.name_of_family} family.")


class PersonInFamily:
    def __init__(self, name: str, age: int, from_which_family: str):
        self.name = name
        self.age = age
        self.from_which_family = from_which_family

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old. "
              f"I am from the {self.from_which_family} family.")


The_Luong_Pham_Family = Family("Luong Pham")
Antoni = PersonInFamily("Antoni", 7, "Luong Pham")
Ariana = PersonInFamily("Ariana", 5, "Luong Pham")
The_Luong_Pham_Family.say_hello()
Antoni.introduce()
Ariana.introduce()
