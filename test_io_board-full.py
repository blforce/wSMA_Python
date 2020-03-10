"""Routines for testing Edward's spectrometer using the Leiker/Force
I/O card for Raspberry Pis
"""
import time
#import numpy as np
#import matplotlib as mpl
#from matplotlib import pyplot as plt
exec(compile(open("./io_board_subs.py", "rb").read(), "./io_board_subs.py", 'exec'))

#Instantiate the devices and objects we need
#dio = Dio()
#adc0 = Adc(0)
dac0 = Dac(0)
#adc1 = Adc(1)
#dac1 = Dac(1)
#adc0.setOneShotMode()
#adc1.setOneShotMode()

def check_db():
 # software convention makes dac0(0) analog out #1
 #  dac1.write(2,32767)  # set midrange so Yig 2 attenuator goes -2 to +2
   dac0.write(2,32767)  # set midrange so Yig 1 attenuator goes -2 to + 2
   i = 0
   while (i < 65536):
     dac0.write(0,i)   # analog 1 out
     #dac0.write(1,i)   # analog 2 out
     #dac0.write(3,i)   # analog 4 out
     #dac1.write(0,i)   # analog 5 out (done consecutively for timing test)
     #dac1.write(1,i)   # analog 6 out
     #dac1.write(3,i)   # analog 8 out
     i =  i+1

check_db()
