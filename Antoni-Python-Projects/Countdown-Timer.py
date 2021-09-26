import time


mins = int(input('How many minutes? '))
secs = 0

while mins or secs:
    time.sleep(1)
    if not secs:
        secs = 60
        mins -= 1
    secs -= 1
    print(f'{mins:02}:{secs:02} remaining')

print("Time's up!")
