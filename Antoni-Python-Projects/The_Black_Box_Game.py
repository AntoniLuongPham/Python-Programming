from random import randint
number = str(input("Give me a number. "))
operator = randint(1, 4)
answer = 0
second_number = randint(1, 10)
def calculate():
    global second_number
    global operator
    global answer
    if operator == 1:
        operator = "+"
        answer = eval(number) + second_number
    elif operator == 2:
        operator = "-"
        answer = eval(number) - second_number
    elif operator == 3:
        operator = "/"
        answer = eval(number) / second_number
    elif operator == 4:
        operator = "*"
        answer = eval(number) * second_number

calculate()
print(answer)
onw = str(input("What is the equation? "))
equation = f"{number} {operator} {second_number}"
if onw == f"{equation}":
    print("right!")
else:
    print("aww")

print(f"The equation is {number} {operator} {second_number}.")
