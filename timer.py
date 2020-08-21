#!/usr/bin/env python
# Simple timer program for feeding mags

import time
sec = 195
while sec > 0:
    print(sec)
    time.sleep(1) # every seconds
    sec -= 1 # take on seconds away
