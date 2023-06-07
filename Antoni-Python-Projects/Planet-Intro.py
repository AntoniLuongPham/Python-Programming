from class_for_planets import Planet


# init the planets
mercury = Planet(name="Mercury",
                 color="gray",
                 order_from_the_sun="first",
                 orbital_period="88 Earth days")
venus = Planet(name="Venus",
               color="orange",
               order_from_the_sun="second",
               orbital_period="225 Earth days")
earth = Planet(name="Earth",
               color="blue and green",
               order_from_the_sun="third",
               orbital_period="365.26 days")
mars = Planet(name="Mars",
              color="red",
              order_from_the_sun="forth",
              orbital_period="687 Earth days")
jupiter = Planet(name="Jupiter",
                 color="orange and white",
                 order_from_the_sun="fifth",
                 orbital_period="12 Earth years")
saturn = Planet(name="Saturn",
                color="brown",
                order_from_the_sun="sixth",
                orbital_period="29 Earth years")
uranus = Planet(name="Uranus",
                color="light blue",
                order_from_the_sun="seventh",
                orbital_period="84 Earth years")
neptune = Planet(name="Neptune",
                 color="dark blue",
                 order_from_the_sun="eighth",
                 orbital_period="165 Earth years")

# say hi
mercury.introduce()
venus.introduce()
earth.introduce()
mars.introduce()
jupiter.introduce()
saturn.introduce()
uranus.introduce()
neptune.introduce()
