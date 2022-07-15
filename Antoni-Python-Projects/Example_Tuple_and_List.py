from typing import Tuple

mjtuple: Tuple[int, int, str] = (12, 60, 'Game')
mutuple: Tuple[int, int, str] = (40, 69, 'Galoe')
mytuple: Tuple[int, int, str] = (12, 10, 'Gapoe')
mhtuple: Tuple[int, int, str] = (100, 90, 'Gaode')

for item in mytuple:
    print(item)

for item in mhtuple:
    print(item)

for item in mutuple:
    print(item)

for item in mjtuple:
    print(item)

from typing import List
names_of_the_luong_family: List[str] = ["Antoni", "Ariana", "Mom", "Dad"]

for name in names_of_the_luong_family:
    print(name)
    print(str(f'My name is {name}.'))


primary_colors = ["blue", "red", "yellow"]
secondary_colors = [
    ["orange", "red and yellow"],
    ["green", "blue and yellow"],
    ["purple", "red and blue"]
]

print(secondary_colors[1])
