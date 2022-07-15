from typing import List
A = 'A'
B = 'N'
C = 'T'
D = 'O'
E = 'N'
F = 'I'
my_letters = list()
print("Antoni's my name.")
my_name = input("What's my name?(all lowercase!) ")
if my_name == 'antoni':
    print('Right!')
else:
    print('Wrong')

first_letter = input("What's my first letter in my name?(capital letter) ")
if first_letter == A:
    print('Right!')
    my_letters.append("A")
else:
    print('Wrong')

second_letter = input("What's my second letter in my name?(capital letter) ")
if second_letter == B:
    print('Right!')
    my_letters.append("N")
else:
    print('Wrong')

third_letter = input("What's my third letter in my name?(capital letter) ")
if third_letter == C:
    print('Right!')
    my_letters.append("T")
else:
    print('Wrong')

forth_letter = input("What's my forth letter in my name?(capital letter) ")
if forth_letter == D:
    print('Right!')
    my_letters.append("O")
else:
    print('Wrong')

fifth_letter = input("What's my fifth letter in my name?(capital letter) ")
if fifth_letter == E:
    print('Right!')
    my_letters.append("N")
else:
    print('Wrong')

sixth_letter = input("What's my sixth letter in my name?(capital letter) ")
if sixth_letter == F:
    print('Right!')
    my_letters.append("I")
else:
    print('Wrong')

print(f"You guessed {my_letters}.")