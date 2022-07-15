class Kid():
    def __init__(self, name: str, age: int, fav_thing_to_do: str):
        self.name = name
        self.age = age
        self.fav_thing_to_do = fav_thing_to_do
        
    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old." 
            f" I like to {self.fav_thing_to_do}")

Antoni = Kid("Antoni", 8, "Go skiing")
Antoni.introduce()