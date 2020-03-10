"""Take apart unix time
"""

import time
import numpy as np
unix_time = int(time.time())
print(unix_time)
#      out_volts = bit_weight * i * 5.0
digits = np.zeros(10,dtype=int)
for i in range(10):
  digit = unix_time % 10
  print(digit)
  digits[9-i] = digit
  unix_time /= 10
for i in range(10):
  print(digits[i])