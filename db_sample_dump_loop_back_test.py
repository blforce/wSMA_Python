"""Test the daughter board by looping back:
"""

import time
import curses
import math
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from time import sleep
exec(compile(open("./io_board_subs.py", "rb").read(), "./io_board_subs.py", 'exec'))
GPIO.setwarnings(False)
def main(win):
  global stdscr
  stdscr = win
  curses.initscr()
  curses.nl()
  curses.noecho()
#Instantiate the devices and objects we need
  dio = Dio()
  adc0 = Adc(0)
  dac0 = Dac(0)
  adc1 = Adc(1)
  dac1 = Dac(1)
  adc0.setOneShotMode()
  adc1.setOneShotMode()
  stdscr.clear
  stdscr.move(1,20)
  stdscr.addstr("Daughter board loopback")
  stdscr.move(3,10)
  stdscr.addstr("Read")
  stdscr.move(3,35)
  stdscr.addstr("Error")
  stdscr.move(4,1)
  stdscr.addstr("ANALOG_IN_1: ")
  stdscr.move(5,1)
  stdscr.addstr("ANALOG_IN_2: ")
  stdscr.move(6,1)
  stdscr.addstr("ANALOG_IN_3: ")
  stdscr.move(7,1)
  stdscr.addstr("ANALOG_IN_4: ")
  stdscr.move(8,1)
  stdscr.addstr("ANALOG_IN_5: ")
  stdscr.move(9,1)
  stdscr.addstr("ANALOG_IN_6: ")
  stdscr.move(10,1)
  stdscr.addstr("ANALOG_IN_7: ")
  stdscr.move(11,1)
  stdscr.addstr("ANALOG_IN_8: ")
  stdscr.move(12,1)
  stdscr.addstr("DIO OUT")
  stdscr.move(12,12)
  stdscr.addstr("DIO IN")
  stdscr.move(12,20)
  stdscr.addstr("Error")
  stdscr.refresh()
  def check_db():
    i = 0
    j = 0
    dac_bit_weight = 2.048 / 65535
    adc_bit_weight = 2.048 / 32768
    out_volts = 0.0
    in_volts = 0.0
    cal_1 = 1.0
    cal_2 = 1.0
    cal_3 = 1.0
    cal_4 = 1.0
    cal_5 = 1.0
    cal_6 = 1.0
    cal_7 = 1.0
    cal_8 = 1.0
    err_1 = 1.0
    err_2 = 1.0
    err_3 = 1.0
    err_4 = 1.0
    err_5 = 1.0
    err_6 = 1.0
    err_7 = 1.0
    err_8 = 1.0
    last_1 = 0
    last_2 = 0
    last_3 = 0
    last_4 = 0
    last_5 = 0
    last_6 = 0
    last_7 = 0
    last_8 = 0
    del_1 = 0
    del_2 = 0
    del_3 = 0
    del_4 = 0
    del_5 = 0
    del_6 = 0
    del_7 = 0
    del_8 = 0
    dio_bits = 0
    frames = 1
    samples = np.zeros(frames,dtype=int)
    while True:
      out_volts = dac_bit_weight * i
      stdscr.move(2,2)
      stdscr.clrtoeol()
      stdscr.addstr("DAC word:")
      stdscr.move(2,12)
      stdscr.addstr(str(i))
      stdscr.move(2,20)
      stdscr.addstr("Volts:")
      stdscr.move(2,30)
      stdscr.addstr(str(out_volts))
      dac0.write(0,0) 
      dac0.write(1,0)
      dac0.write(2,0)
      dac0.write(3,0)
      dac1.write(0,0) 
      dac1.write(1,0)
      dac1.write(2,0)
      dac1.write(3,0)
#      sleep(0.10)
      dac0.write(0,i)  
      for k in range(frames):
        samples[k]= adc0.read(0)
      Analog_In_1 = np.mean(samples)
#      Analog_In_1 = adc0.read(0)
      in_volts = adc_bit_weight * Analog_In_1 * cal_1
      err_1 = math.trunc((in_volts - out_volts)*1000.0)
      del_1 = Analog_In_1 - last_1
      last_1 = Analog_In_1
      stdscr.move(4,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(4,30)
      stdscr.addstr("v")
      stdscr.move(4,35)
      stdscr.addstr(str(err_1))
      stdscr.move(4,40)
      stdscr.addstr("mv")
      stdscr.move(4,50)
      stdscr.addstr(str(Analog_In_1))
      stdscr.move(4,58)
      stdscr.addstr('bits')
      stdscr.move(4,65)
      stdscr.addstr(str(del_1))
      stdscr.move(4,72)
      stdscr.addstr('delta')
#      stdscr.addstr(str(samples[0]))
      dac0.write(0,0)
#      sleep(0.10)
      dac0.write(1,i)
      for k in range(frames):
        samples[k]= adc0.read(1)
      Analog_In_2 = np.mean(samples)
#      Analog_In_2 = adc0.read(1)
      in_volts = adc_bit_weight * Analog_In_2 * cal_2
      err_2 = math.trunc((in_volts - out_volts)*1000.0)
      del_2 = Analog_In_2 - last_2
      last_2 = Analog_In_2
      stdscr.move(5,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(5,30)
      stdscr.addstr("v")
      stdscr.move(5,35)
      stdscr.addstr(str(err_2))
      stdscr.move(5,40)
      stdscr.addstr("mv")
      stdscr.move(5,50)
      stdscr.addstr(str(Analog_In_2))
      stdscr.move(5,58)
      stdscr.addstr('bits')
      stdscr.move(5,65)
      stdscr.addstr(str(del_2))
      stdscr.move(5,72)
      stdscr.addstr('delta')
#      stdscr.addstr(str(samples[0]))
      dac0.write(1,0)
#      sleep(0.10)
      dac0.write(2,i)
      for k in range(frames):
        samples[k]= adc0.read(2)
      Analog_In_3 = np.mean(samples)
#      Analog_In_3 = adc0.read(2)
      in_volts = adc_bit_weight * Analog_In_3 * cal_3
      err_3 = math.trunc((in_volts - out_volts)*1000.0)
      del_3 = Analog_In_3 - last_3
      last_3 = Analog_In_3
      stdscr.move(6,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(6,30)
      stdscr.addstr("v")
      stdscr.move(6,35)
      stdscr.addstr(str(err_3))
      stdscr.move(6,40)
      stdscr.addstr("mv")
      stdscr.move(6,50)
      stdscr.addstr(str(Analog_In_3))
      stdscr.move(6,58)
      stdscr.addstr('bits')
      stdscr.move(6,65)
      stdscr.addstr(str(del_3))
      stdscr.move(6,72)
      stdscr.addstr('delta')
#      stdscr.addstr(str(samples[0]))
      dac0.write(2,0)
#      sleep(0.10)
      dac0.write(3,i)
      for k in range(frames):
        samples[k]= adc0.read(3)
      Analog_In_4 = np.mean(samples)
 #     Analog_In_4 = adc0.read(3)
      in_volts = adc_bit_weight * Analog_In_4 * cal_4
      err_4 = math.trunc((in_volts - out_volts)*1000.0)
      del_4 = Analog_In_4 - last_4
      last_4 = Analog_In_4
      stdscr.move(7,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(7,30)
      stdscr.addstr("v")
      stdscr.move(7,35)
      stdscr.addstr(str(err_4))
      stdscr.move(7,40)
      stdscr.addstr("mv")
      stdscr.move(7,50)
      stdscr.addstr(str(Analog_In_4))
      stdscr.move(7,58)
      stdscr.addstr('bits')
      stdscr.move(7,65)
      stdscr.addstr(str(del_4))
      stdscr.move(7,72)
      stdscr.addstr('delta')
#      stdscr.addstr(str(samples[0]))      
      dac0.write(3,0)
#      sleep(0.10)
      dac1.write(0,i)
      for k in range(frames):
        samples[k]= adc1.read(0)
      Analog_In_5 = np.mean(samples)
#      Analog_In_5 = adc1.read(0)
      in_volts = adc_bit_weight * Analog_In_5 * cal_5
      err_5 = math.trunc((in_volts - out_volts)*1000.0)
      del_5 = Analog_In_5 - last_5
      last_5 = Analog_In_5
      stdscr.move(8,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(8,30)
      stdscr.addstr("v")
      stdscr.move(8,35)
      stdscr.addstr(str(err_5))
      stdscr.move(8,40)
      stdscr.addstr("mv")
      stdscr.move(8,50)
      stdscr.addstr(str(Analog_In_5))
      stdscr.move(8,58)
      stdscr.addstr('bits')
      stdscr.move(8,65)
      stdscr.addstr(str(del_5))
      stdscr.move(8,72)
      stdscr.addstr('delta')
#      stdscr.addstr(str(samples[0]))
      dac1.write(0,0)
#      sleep(0.10)
      dac1.write(1,i)
      for k in range(frames):
        samples[k]= adc1.read(1)
      Analog_In_6 = np.mean(samples)
#      Analog_In_6 = adc1.read(1)
      in_volts = adc_bit_weight * Analog_In_6 * cal_6
      err_6 = math.trunc((in_volts - out_volts)*1000.0)
      del_6 = Analog_In_6 - last_6
      last_6 = Analog_In_6
      stdscr.move(9,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(9,30)
      stdscr.addstr("v")
      stdscr.move(9,35)
      stdscr.addstr(str(err_6))
      stdscr.move(9,40)
      stdscr.addstr("mv")
      stdscr.move(9,50)
      stdscr.addstr(str(Analog_In_6))
      stdscr.move(9,58)
      stdscr.addstr('bits')
      stdscr.move(9,65)
      stdscr.addstr(str(del_6))
      stdscr.move(9,72)
      stdscr.addstr('delta')
#      stdscr.addstr(str(samples[0]))
      dac1.write(1,0)
#     sleep(0.10)
      dac1.write(2,i)
      for k in range(frames):
        samples[k]= adc1.read(2)
      Analog_In_7 = np.mean(samples)      
#      Analog_In_7 = adc1.read(2)
      in_volts = adc_bit_weight * Analog_In_7 * cal_7
      err_7 = math.trunc((in_volts - out_volts)*1000.0)
      del_7 = Analog_In_7 - last_7
      last_7 = Analog_In_7
      stdscr.move(10,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(10,30)
      stdscr.addstr("v")
      stdscr.move(10,35)
      stdscr.addstr(str(err_7))
      stdscr.move(10,40)
      stdscr.addstr("mv")
      stdscr.move(10,50)
      stdscr.addstr(str(Analog_In_7))
      stdscr.move(10,58)
      stdscr.addstr('bits')
      stdscr.move(10,65)
      stdscr.addstr(str(del_7))
      stdscr.move(10,72)
      stdscr.addstr('delta')
#      stdscr.addstr(str(samples[0]))
      dac1.write(2,0)
#      sleep(0.10)
      dac1.write(3,i)
      for k in range(frames):
        samples[k]= adc1.read(3)
      Analog_In_8 = np.mean(samples)      
#      Analog_In_8 = adc1.read(3)
      in_volts = adc_bit_weight * Analog_In_8 * cal_8
      err_8 = math.trunc((in_volts - out_volts)*1000.0)
      del_8 = Analog_In_8 - last_8
      last_8 = Analog_In_8
      stdscr.move(11,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(11,30)
      stdscr.addstr("v")
      stdscr.move(11,35)
      stdscr.addstr(str(err_8))
      stdscr.move(11,40)
      stdscr.addstr("mv")
      stdscr.move(11,50)
      stdscr.addstr(str(Analog_In_8))
      stdscr.move(11,58)
      stdscr.addstr('bits')
      stdscr.move(11,65)
      stdscr.addstr(str(del_8))
      stdscr.move(11,72)
      stdscr.addstr('delta')
#      stdscr.addstr(str(samples[0]))
      dac1.write(3,0)
      stdscr.move(13,5)
      stdscr.clrtoeol()
      stdscr.addstr(str(j))
      dio.write(j)
      readback = dio.read()
      stdscr.move(13,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(readback))
      digital_error = j - readback
      stdscr.move(13,20)
      stdscr.clrtoeol()
      stdscr.addstr(str(digital_error))
      if digital_error != 0:
        stdscr.move(14,15)
        stdscr.clrtoeol()
        stdscr.addstr("digital error!")
        sleep(0.5)
      stdscr.move(0,0)
      stdscr.refresh()
# zero the dacs        
      dac0.write(0,0)   # U3-1 V_OUTA  Analog_Out_1 YIG_1_tune
      dac1.write(0,0)   # U6-1 V_OUTA  Analog_Out_5 YIG_2_tune
      dac0.write(1,0)   # U3-2 V_OUTB  Analog_Out_2 YIG_1_atten
      dac0.write(3,0)   # U6-2 V_OUTB  Analog_Out_6 YIG_2_atten
      i = i + 128
      j = j + 1 
      if i > 65535:
        i = 0
      if j > 255:
        j = 0
  check_db()
  curses.nocbreak(); 
  stdscr.keypad(0); 
  curses.echo()
curses.wrapper(main)
