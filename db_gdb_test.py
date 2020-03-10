"""Test the yig driver by looping back:
   note-cannot use YIG_*atten because it goes below ground
   YIG_1_tune  to Analog_In_1  5:1   voltage divider
   YIG_1_tune  to Analog_In_2  5:1 voltage divider
   YIG_2_tune  to Analog_In_5  5:1   voltage divider
   YIG_2_tune  to Analog_In_6  5:1 voltage divider
   P0_0 to P1_0
   P0_1 to P1_1
   P0_2 to P1_2
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
  stdscr.addstr("YIG DRIVER LOOPBACK")
  stdscr.move(2,1)
  stdscr.addstr("volts: ")
  stdscr.move(4,1)
  stdscr.addstr("ANALOG_IN_1: ")
  stdscr.move(5,1)
  stdscr.addstr("ANALOG_IN_2: ")
  stdscr.move(6,1)
  stdscr.addstr("ANALOG_IN_5: ")
  stdscr.move(7,1)
  stdscr.addstr("ANALOG_IN_6: ")
  stdscr.move(9,1)
  stdscr.addstr("DIO OUT")
  stdscr.move(9,12)
  stdscr.addstr("DIO IN")
#  stdscr.move(10,1)
#  stdscr.addstr("0: ")
#  stdscr.move(11,1)
#  stdscr.addstr("1: ")
#  stdscr.move(12,1)
#  stdscr.addstr("2: ")
#  stdscr.move(13,1)
#  stdscr.addstr("4: ")
  stdscr.move(19,1)
  stdscr.addstr("Unix Time mod 7:")
  stdscr.move(20,1)
  stdscr.addstr("unix time: ")
  stdscr.refresh()
  bit_weight = 2.048 / 65535
  out_volts = 0.0
  in_volts = 0.0
  cal_1 = 10.0
  cal_2 = 10.0
  cal_3 = 10.0
  cal_4 = 10.0
  err_1 = 0.0
  err_2 = 0.0
  err_3 = 0.0
  err_4 = 0.0
  digits = np.zeros(10,dtype=int)
  unix_time = 0
  dio_bits = 0
  def check_db():
    dac0.write(2,32767)  # U3-7 V_OUTC Analog_Out_3
    dac1.write(2,32767)  # U6-7 V_OUTC Analog_Out_7
    i = 0
    while True:
      sleep(1.0)
      unix_time = int(time.time())
      u_t = unix_time
      for j in range(10):
        digit = u_t % 10
        digits[9-j] = digit
        u_t /= 10
      for j in range(10):  
        stdscr.move(20,15)
        stdscr.clrtoeol()
        stdscr.addstr(str(unix_time))
#      i = i + 255
        i = digits[j] / bit_weight / 5.0
        out_volts = bit_weight * i * 5.0
        stdscr.move(2,15)
        stdscr.clrtoeol()
        stdscr.addstr(str(out_volts))
        dac0.write(0,i)   # U3-1 V_OUTA  Analog_Out_1 YIG_1_tune
        dac1.write(0,i)   # U6-1 V_OUTA  Analog_Out_5 YIG_2_tune
        dac0.write(1,i)   # U3-2 V_OUTB  Analog_Out_2 YIG_1_atten
        dac0.write(3,i)   # U6-2 V_OUTB  Analog_Out_6 YIG_2_atten
        Analog_In_1 = adc0.read(0)
        in_volts = bit_weight * Analog_In_1 * cal_1
        err_1 = out_volts - in_volts
        stdscr.move(4,15)
        stdscr.clrtoeol()
        stdscr.addstr(str(in_volts))
        stdscr.move(4,32)
        stdscr.addstr("volts")
        stdscr.move(4,38)
        stdscr.addstr(str(err_1))
        stdscr.move(4,56)
        stdscr.addstr("volts")
        Analog_In_2 = adc0.read(1)
        in_volts = bit_weight * Analog_In_2 * cal_2
        err_2 = out_volts - in_volts
        stdscr.move(5,15)
        stdscr.clrtoeol()
        stdscr.addstr(str(in_volts))
        stdscr.move(5,32)
        stdscr.addstr("volts")
        stdscr.move(5,38)
        stdscr.addstr(str(err_2))
        stdscr.move(5,56)
        stdscr.addstr("volts")
        Analog_In_5 = adc1.read(0)
        in_volts = bit_weight * Analog_In_5 * cal_3
        err_3 = out_volts - in_volts
        stdscr.move(6,15)
        stdscr.clrtoeol()
        stdscr.addstr(str(in_volts))
        stdscr.move(6,32)
        stdscr.addstr("volts")
        stdscr.move(6,38)
        stdscr.addstr(str(err_3))
        stdscr.move(6,56)
        stdscr.addstr("volts")
        Analog_In_6 = adc1.read(1)
        in_volts = bit_weight * Analog_In_6 * cal_4
        err_4 = out_volts - in_volts
        stdscr.move(7,15)
        stdscr.clrtoeol()
        stdscr.addstr(str(in_volts))
        stdscr.move(7,32)
        stdscr.addstr("volts")
        stdscr.move(7,38)
        stdscr.addstr(str(err_4))
        stdscr.move(7,56)
        stdscr.addstr("volts")
        dio_bits = unix_time % 7
        stdscr.move(10,1)
        stdscr.clrtoeol()
        stdscr.addstr(str(dio_bits))
        bit = bin(dio_bits).replace("0b","")
        length = len(bit)
        stdscr.move(19,22)
        stdscr.clrtoeol()
        stdscr.addstr(str(bit))
        pos = bit[0]
        if pos == '0': 
          dio.setBit(2,0,0)
        else:
          dio.setBit(2,1,0)
        if length > 1:
          pos = bit[1]
          if pos == '0':
            dio.setBit(1,0,0)
          else:
            dio.setBit(1,1,0)
        else:
          dio.setBit(1,0,0)
        if length > 2:
          pos = bit[2]
          if pos == '0':
            dio.setBit(0,0,0)
          else:
            dio.setBit(0,1,0)
        else:
          dio.setBit(0,0,0)
        readback = dio.read(1)
        stdscr.move(10,15)
        stdscr.clrtoeol()
        stdscr.addstr(str(readback))
        stdscr.refresh()
# zero the dacs        
        dac0.write(0,0)   # U3-1 V_OUTA  Analog_Out_1 YIG_1_tune
        dac1.write(0,0)   # U6-1 V_OUTA  Analog_Out_5 YIG_2_tune
        dac0.write(1,0)   # U3-2 V_OUTB  Analog_Out_2 YIG_1_atten
        dac0.write(3,0)   # U6-2 V_OUTB  Analog_Out_6 YIG_2_atten
  check_db()
  curses.nocbreak(); 
  stdscr.keypad(0); 
  curses.echo()
curses.wrapper(main)
