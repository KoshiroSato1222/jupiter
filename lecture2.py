# 正規分布
from numpy.random import *
import matplotlib.pyplot as plt

R = randn(1000000)
plt.hist(R, bins=100)
plt.show()