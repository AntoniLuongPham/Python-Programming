import time


mins = 0
secs = 0
hrs = 0

while True:
    time.sleep(1)
    secs += 1

    if secs == 60:
        secs = 0
        mins += 1

    if mins == 60:
        mins = 0
        hrs += 1

    if hrs == 24:
        hrs = 0

    print(f'{hrs:02}:{mins:02}:{secs:02}')
