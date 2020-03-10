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
  stdscr.move(2,1)
  stdscr.addstr("volts: ")
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
#  stdscr.move(10,1)
#  stdscr.addstr("0: ")
#  stdscr.move(11,1)
#  stdscr.addstr("1: ")
#  stdscr.move(12,1)
#  stdscr.addstr("2: ")
#  stdscr.move(13,1)
#  stdscr.addstr("4: ")
#  stdscr.move(19,1)
#  stdscr.addstr("Unix Time mod 7:")
#  stdscr.move(20,1)
#  stdscr.addstr("unix time: ")
  stdscr.refresh()
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
#  digits = np.zeros(10,dtype=int)
#  unix_time = 0
  dio_bits = 0
  def check_db():
    i = 0
    j = 0
    while True:
      sleep(0.010)
#      unix_time = int(time.time())
#      u_t = unix_time
#      for j in range(10):
#        digit = u_t % 10
#        digits[9-j] = digit
#        u_t /= 10
#      for j in range(10):  
#        sleep(1.0)
#        stdscr.move(20,15)
#        stdscr.clrtoeol()
#        stdscr.addstr(str(unix_time))
#        i = digits[j] / dac_bit_weight / 10 
      out_volts = dac_bit_weight * i
      stdscr.move(2,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(out_volts))
      dac0.write(0,i) 
      dac0.write(1,i)
      dac0.write(2,i)
      dac0.write(3,i)
      dac1.write(0,i) 
      dac1.write(1,i)
      dac1.write(2,i)
      dac1.write(3,i)  
      Analog_In_1 = adc0.read(0)
#      stdscr.move(21,0)
#      stdscr.clrtoeol()
#      stdscr.addstr(str(Analog_In_1))
      in_volts = adc_bit_weight * Analog_In_1 * cal_1
      err_1 = math.trunc((out_volts - in_volts)*1000.0)
      stdscr.move(4,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(4,32)
      stdscr.addstr("volts")
      stdscr.move(4,38)
      stdscr.addstr(str(err_1))
      stdscr.move(4,42)
      stdscr.addstr("milli volts")
      Analog_In_2 = adc0.read(1)
      in_volts = adc_bit_weight * Analog_In_2 * cal_2
      err_2 = math.trunc((out_volts - in_volts)*1000.0)
      stdscr.move(5,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(5,32)
      stdscr.addstr("volts")
      stdscr.move(5,38)
      stdscr.addstr(str(err_2))
      stdscr.move(5,42)
      stdscr.addstr("milli volts")
      Analog_In_3 = adc0.read(2)
      in_volts = adc_bit_weight * Analog_In_3 * cal_3
      err_3 = math.trunc((out_volts - in_volts)*1000.0)
      stdscr.move(6,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(6,32)
      stdscr.addstr("volts")
      stdscr.move(6,38)
      stdscr.addstr(str(err_3))
      stdscr.move(6,42)
      stdscr.addstr("milli volts")
      Analog_In_4 = adc0.read(3)
      in_volts = adc_bit_weight * Analog_In_4 * cal_4
      err_4 = math.trunc((out_volts - in_volts)*1000.0)
      stdscr.move(7,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(7,32)
      stdscr.addstr("volts")
      stdscr.move(7,38)
      stdscr.addstr(str(err_4))
      stdscr.move(7,42)
      stdscr.addstr("milli volts")
      Analog_In_5 = adc1.read(0)
#      stdscr.move(21,0)
#      stdscr.clrtoeol()
#      stdscr.addstr(str(Analog_In_5))
      in_volts = adc_bit_weight * Analog_In_5 * cal_5
      err_5 = math.trunc((out_volts - in_volts)*1000.0)
      stdscr.move(8,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(8,32)
      stdscr.addstr("volts")
      stdscr.move(8,38)
      stdscr.addstr(str(err_1))
      stdscr.move(8,42)
      stdscr.addstr("milli volts")
      Analog_In_6 = adc1.read(1)
      in_volts = adc_bit_weight * Analog_In_6 * cal_6
      err_6 = math.trunc((out_volts - in_volts)*1000.0)
      stdscr.move(9,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(9,32)
      stdscr.addstr("volts")
      stdscr.move(9,38)
      stdscr.addstr(str(err_2))
      stdscr.move(9,42)
      stdscr.addstr("milli volts")
      Analog_In_7 = adc1.read(2)
      in_volts = adc_bit_weight * Analog_In_7 * cal_7
      err_7 = math.trunc((out_volts - in_volts)*1000.0)
      stdscr.move(10,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(10,32)
      stdscr.addstr("volts")
      stdscr.move(10,38)
      stdscr.addstr(str(err_3))
      stdscr.move(10,42)
      stdscr.addstr("milli volts")
      Analog_In_8 = adc1.read(3)
      in_volts = adc_bit_weight * Analog_In_8 * cal_8
      err_8 = math.trunc((out_volts - in_volts)*1000.0)
      stdscr.move(11,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(in_volts))
      stdscr.move(11,32)
      stdscr.addstr("volts")
      stdscr.move(11,38)
      stdscr.addstr(str(err_8))
      stdscr.move(11,42)
      stdscr.addstr("milli volts")
#      dio_bits = unix_time % 7
#      stdscr.move(13,1)
#      stdscr.clrtoeol()
#      stdscr.addstr(str(dio_bits))
#      bit = bin(dio_bits).replace("0b","")
#      length = len(bit)
      stdscr.move(13,5)
      stdscr.clrtoeol()
      stdscr.addstr(str(j))
#      pos = bit[0]
#      if pos == '0': 
#        dio.setBit(2,0,0)
#      else:
#        dio.setBit(2,1,0)
#      if length > 1:
#        pos = bit[1]
#        if pos == '0':
#          dio.setBit(1,0,0)
#        else:
#          dio.setBit(1,1,0)
#      else:
#        dio.setBit(1,0,0)
#      if length > 2:
#        pos = bit[2]
#        if pos == '0':
#          dio.setBit(0,0,0)
#        else:
#          dio.setBit(0,1,0)
#      else:
#        dio.setBit(0,0,0)
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
        sleep(5.0)
      stdscr.move(0,0)
      stdscr.refresh()
# zero the dacs        
      dac0.write(0,0)   # U3-1 V_OUTA  Analog_Out_1 YIG_1_tune
      dac1.write(0,0)   # U6-1 V_OUTA  Analog_Out_5 YIG_2_tune
      dac0.write(1,0)   # U3-2 V_OUTB  Analog_Out_2 YIG_1_atten
      dac0.write(3,0)   # U6-2 V_OUTB  Analog_Out_6 YIG_2_atten
      i = i + 64
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
