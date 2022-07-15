from typing import Dict

minecraft: Dict[str, str] = {
    "mine": "survive",
    "craft": "make"
}

types_of_things = [
    {"name": "water", "type": "liquid"},
    {"name": "fire", "type": "light source"},
    {"name": "lighting", "type": "electricity"}
]
print(types_of_things[1])

pens = [
    {"name": "Sharpie", "main color": "Black"},
    {"name": "Crayola", "main color": "Any color"},
    {"name": "Expo", "main color": "Black"}
]

print(pens[1])

n_birthday_bots = 3
birthday_bots = [
    {"name": "Candle Blower", "thing to do": "blow the candles"},
    {"name": "Cake Cutter", "thing to do": "cut the cake"},
    {"name": "Gift Presenter", "thing to do": "present the gifts"}
]

print(f"There are {n_birthday_bots} birthday bots")

for bot_details in birthday_bots:
    print(f"One of the robots is {bot_details['name']}, "
          f"its job is to {bot_details['thing to do']}")

