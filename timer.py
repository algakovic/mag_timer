#!/usr/bin/env python
# Simple timer program for feeding mags

import time
from playsound import playsound

sec = 5
while sec > 0:
    print(sec)
    
    if sec == 30:
        print('30 seconds to go...')
    if sec == 1:
        playsound('C:/Users/kamik/code/projects/mag_timer/sounds/rose_confession.mp3')

    time.sleep(1) # every seconds
    sec -= 1 # take on seconds away
