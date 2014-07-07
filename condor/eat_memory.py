# Test file to fill memory

import numpy as np
import time

a = np.array([1.0])

for i in range(20):
  print(len(a))
  a = np.append(a, a)
  np.savetxt('test.txt', a)
  b = np.loadtxt('test.txt')
