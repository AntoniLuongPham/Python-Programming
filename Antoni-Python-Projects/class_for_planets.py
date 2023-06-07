# Class
class Planet:
    def __init__(
            self,
            name: str,
            color: str,
            order_from_the_sun:  str,
            orbital_period: str):
        self.name = name
        self.color = color
        self.order_from_the_sun = order_from_the_sun
        self.orbital_period = orbital_period

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.color} in color. "
              f"I am the {self.order_from_the_sun} planet from the Sun. "
             f"I take {self.orbital_period} to orbit the Sun.")