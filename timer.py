#!/usr/bin/env python
# Simple timer program for feeding mags

import time
sec = 45
while sec > 0:
    print(sec)
    
    if sec == 30:
        print('30 seconds to go...')

    time.sleep(1) # every seconds
    sec -= 1 # take on seconds away
