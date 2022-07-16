equation = str(input("What is your equation? Use +, -, * or /. "))

def calculate(equation):
    eval(equation)
    answer = eval(equation)
    print(f"{equation} = {answer}")

calculate(equation)