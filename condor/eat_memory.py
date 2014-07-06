# Test file to fill memory

import numpy as np
import time

a = np.array([])

for i in range(10000000):
  a = np.append(a, a)
#  print(len(a))
