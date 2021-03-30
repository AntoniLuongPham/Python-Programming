import random
does_the_player_want_math_test = str(input('do you want to do math test?'))
if does_the_player_want_math_test == ('no') or (''):
    brake()
elif does_the_player_want_math_test == 'yes':
    how_many_times = int(input('how many times?'))
    times = 0
    for i in range(how_many_times):
        points = 0
        A = int(random(1, 100))
        B = int(random(1, 100))
        do_math_test(a=A, b=B, points=points)
        times += 1
        want_a_break = str(input('do you want a brake?'))
        if want_a_break == 'no' or (times < how_many_times):
            print('then lets go on!')
        if (want_a_break == 'yes') or (times == how_many_times) :
            print('ok bye! have a good brake! :)')

def do_math_test(a, b, points):
    anwser = a + b
    guess = int(input("how many is this?" + a + b))
    if guess != anwser:
        return 'wrong. sorry'
    if guess == anwser:
        return 'good job!'
        points + 1
        
def brake():
    break
        


    