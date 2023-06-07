from random import randint
n_questions = int(input("how many questions do you want in this math test? "))
points = 0
for i in range(n_questions):
    a = randint(1, 100)
    b = randint(1, 100)

    correct_answer = a + b

    player_answer = int(input(f"Q{i + 1}: What is {a} + {b}? "))
    if player_answer == correct_answer:
        points += 1
        print("you did it!")
    else:
        print("that was wrong, but good try! :)")

print(f"You got {points} out of {n_questions}!")
if points < n_questions / 2:
    print("good try.")
else:
    print(f"great job!")
