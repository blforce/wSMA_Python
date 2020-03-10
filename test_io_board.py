"""Routines for testing Edward's spectrometer using the Leiker/Force
I/O card for Raspberry Pis
"""
import time
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
exec(compile(open("./io_board_subs.py", "rb").read(), "./io_board_subs.py", 'exec'))

#Instantiate the devices and objects we need
dio = Dio()
adc0 = Adc(0)
dac0 = Dac(0)
adc1 = Adc(1)
dac1 = Dac(1)
adc0.setOneShotMode()
adc1.setOneShotMode()

def check_analog():
  samples = np.zeros(10, dtype=int)
  inputs = np.zeros(8, dtype=int)
  rms = np.zeros(8, dtype=int)
  outputs = np.zeros(8, dtype=int)
  for i in range(4):
    print("%i" %(i))
    outputs[i] = 8192*i
    dac0.write(i, outputs[i])
    outputs[i+4] = 8191*(i+4)
    dac1.write(i, outputs[i+4])
  for i in range(4):
    for j in range(10):
      samples[j] = adc0.read(i)
    inputs[i] = np.mean(samples)
    rms[i] = np.std(samples)
    for j in range(10):
      samples[j] = adc1.read(i)
    inputs[i+4] = np.mean(samples)
    rms[i+4] = np.std(samples)
  print("%5s %5s %5s" %("dac/2", "adc", "rms"))
  for i in range(8):
    print("%5i %5i %5i" %(outputs[i]/2, inputs[i], rms[i]))

def check_dio():
  outputs = np.zeros(8, dtype=int)
  inputs = np.zeros(8, dtype=int)
  outputs[0] = 1
  for i in range(1,8):
    outputs[i] = 2* outputs[i-1]
  for i in range(8):
    dio.write(outputs[i])
    inputs[i] = dio.read()
    if inputs[i] == outputs[i]:
      char = ""
    else:
      char = "X"
    print(format(outputs[i],'b').zfill(8), format(inputs[i], 'b').zfill(8),char)

print("Checking analog I/O.")
check_analog()
print("Checking digital I/O.")
check_dio()
