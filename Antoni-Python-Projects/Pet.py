class Pet:
    def __init__(self, name: str, thing_to_do: str):
        self.name = name
        self.thing_to_do = thing_to_do

    def do_something(self):
        print(f'I am {self.thing_to_do}')


cat = Pet('cat', 'climbing trees')
cat.do_something()

dog = Pet('dog', 'chasing cats')
dog.do_something()

bird = Pet('bird', 'flying')
bird.do_something()
