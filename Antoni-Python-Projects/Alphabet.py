from random import randint
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# example 1
i = 0
for letter in letters:
    i += 1
    print(letter, i)

# example 2
for i, letter in enumerate(letters):
    print(letter, i + 1)

# example 3
i = 0
while i < len(letters):
    i += 1
    print(letters[i - 1], i)

# let's have some fun!
letters_to_print = sorted([letters[randint(1, 25)]
                           for _ in range(randint(2, 10))])

print(''.join(letters_to_print))
