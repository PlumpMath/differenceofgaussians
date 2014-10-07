import scipy
from scipy import misc
from scipy import signal

import numpy
import math

filename = ''

def discretegaussian(sigma, x, y, K = 1):
  ss = math.pow(sigma + 0.0, 2)
  xx = math.pow(x + 0.0, 2)
  yy = math.pow(y + 0.0, 2)
  KK = math.pow(K + 0.0, 2)

  d = 2 * math.pi * ss * KK
  di = 1 / d

  eexpi = -1 * (xx + yy)
  eexpd = 2 * KK * ss
  eexp = eexpi / eexpd
  e = math.pow(math.e, eexp)
  return di * e


def buildKernels(sigma, K):
  size = [
    int(sigma * 6),
    int(sigma * K * 6)
  ]

  if 0 == size[0] % 2:
    size[0] -= 1

  if 0 == size[1] % 2:
    size[1] -= 1

  a = [numpy.zeros((size[0], size[0])), numpy.zeros((size[1], size[1]))]

  for x in range(size[0]):
    for y in range(size[0]):
      a[0][x][y] = discretegaussian(sigma, x, y)

  for x in range(size[1]):
    for y in range(size[1]):
      a[1][x][y] = discretegaussian(sigma, x, y, K)

  return a

window_size = 

ff = [163, 46, 55]

im = misc.imread(filename, False)
g = misc.imread(filename, True)

kernel = buildKernels(1, 1.6)

k0 = signal.convolve2d(g, kernel[0], "same", "symm")
k1 = signal.convolve2d(g, kernel[1], "same", "symm")

c = numpy.subtract(k0, k1)
d = numpy.absolute(numpy.subtract(ff, im))

misc.imsave('0.jpg', c)
misc.imsave('1.jpg', d)
