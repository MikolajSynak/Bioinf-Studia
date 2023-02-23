# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:25:20 2022

@author: msynak
"""

# zad 6 zestaw 4

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import statistics as stats

x = [37, 39, 39, 41, 45, 46, 48, 48, 52, 59, 59, 61, 61, 61, 64, 67, 69, 69, 73]
y = list(range(35, 85, 10))

plt.hist(x, bins = y, rwidth = 0.85)
print(max(x))
print(min(x))
rwidth = 0.85

#mean = srednia arytmetyczna
c = stats.mean(x)

#stdev = standard deviation
d = stats.stdev(x)

e = stats.median(x)
f = stats.mode(x)
print(c, d, e, f)

#narysuj histogram z polem równym 1: (dodajesz density = 1, bo to f-cja gęstosci)
# plt.hist(x, bins = y, rwidth = 0.85, density = 1)

#narysuj skumulowany rozkªad czestosci:
# plt.hist(x, bins = y, rwidth = 0.85, density = 1, cumulative = 1)