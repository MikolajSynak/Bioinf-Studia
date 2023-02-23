# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:25:20 2022

@author: msynak
"""

# zad 8 zestaw 4

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import statistics as stats


waga = pd.read_excel("Waga.xlsx", index_col=None, na_values = ['NA'])
q1 = waga.quantile([0.25]).iloc[0,0]
q2 = waga.quantile([0.5]).iloc[0,0]
q3 = waga.quantile([0.75]).iloc[0,0]

odchylenie8 = waga.iloc[:,0].std()
odchylenie8 = waga['Waga'].std()
srednia8 = waga['Waga'].mean()
moda8 = waga["Waga"].mode()
mediana8 = waga["Waga"].median()
rozrzut8 = waga['Waga'].max() - waga['Waga'].min()
wsp_zmiennosci_sredniej8 = odchylenie8/srednia8
rozstep_kwartylowy8 = q3 - q1
wsp_zmiennosci_mediany8 = (rozstep_kwartylowy8) / (2*mediana8)

ax = plt.hist(waga['Waga'], bins = list(range(50, 85, 5)), rwidth = 0.85)
plt.show()
waga.hist()
waga.hist(bins=list(range(50,85,5)))

wartosci = (odchylenie8, srednia8, moda8, mediana8, rozrzut8, wsp_zmiennosci_sredniej8, rozstep_kwartylowy8, wsp_zmiennosci_mediany8)
print(wartosci)


