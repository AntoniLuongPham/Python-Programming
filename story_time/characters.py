

class Character:
    def __init__(
            self,
            first_name: str,
            last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name}'

    def say(self, something, /) -> object:
        print(f'{self} says: "{something}"')


class MagicalCharacter(Character):
    pass


class Person(Character):
    pass


class Animal(Character):
    pass


class MagicalPerson(Person, MagicalCharacter):
    pass


