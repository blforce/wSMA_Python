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
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
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
  stdscr.addstr("count: ")
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
  stdscr.move(10,1)
  stdscr.addstr("0: ")
  stdscr.move(11,1)
  stdscr.addstr("1: ")
  stdscr.move(12,1)
  stdscr.addstr("2: ")
  stdscr.move(13,1)
  stdscr.addstr("4: ")
  stdscr.refresh()
  def check_db():
    dac0.write(2,32767)  # U3-7 V_OUTC Analog_Out_3
    dac1.write(2,32767)  # U6-7 V_OUTC Analog_Out_7
    i = 0
    while True:
      i = i+255
      stdscr.move(2,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(i))
      dac0.write(0,i)   # U3-1 V_OUTA  Analog_Out_1 YIG_1_tune
      dac1.write(0,i)   # U6-1 V_OUTA  Analog_Out_5 YIG_2_tune
      dac0.write(1,i)   # U3-2 V_OUTB  Analog_Out_2 YIG_1_atten
      dac0.write(3,i)   # U6-2 V_OUTB  Analog_Out_6 YIG_2_atten
      Analog_In_1 = adc0.read(0)
      stdscr.move(4,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(Analog_In_1))
      Analog_In_2 = adc0.read(1)
      stdscr.move(5,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(Analog_In_2))
      Analog_In_5 = adc1.read(0)
      stdscr.move(6,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(Analog_In_5))
      Analog_In_6 = adc1.read(1)
      stdscr.move(7,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(Analog_In_6))
      dio.write(0)
      readback = dio.read()
      stdscr.move(10,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(readback))
      dio.write(1)
      readback = dio.read()
      stdscr.move(11,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(readback))
      dio.write(2)
      readback = dio.read()
      stdscr.move(12,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(readback))
      dio.write(4)
      readback = dio.read()
      stdscr.move(13,15)
      stdscr.clrtoeol()
      stdscr.addstr(str(readback))
      stdscr.refresh()
      if i >= 65535: 
        i = 0
  check_db()
  curses.nocbreak(); 
  stdscr.keypad(0); 
  curses.echo()
curses.wrapper(main)
