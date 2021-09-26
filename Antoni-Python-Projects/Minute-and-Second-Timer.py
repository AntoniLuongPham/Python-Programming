import time


mins = 0
secs = 0

while True:
    time.sleep(1)
    secs += 1
    if secs == 60:
        secs = 0
        mins += 1
    print(f'{mins}:{secs:02}')
