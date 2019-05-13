import time

seconds = int(input('enter time:'))
for i in range(seconds):
    time.sleep(1)
    mins, secs = divmod(i, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat1 = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat1)
