import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import statistics as stats

"""
            zad 10
"""

antybiotyki = pd.read_excel('Antybiotyki2.xls', "Dane 2")
dane = antybiotyki[['Dni hospitalizacji', 'Wiek', 'Temperatura', 'WBC']]
print(dane)
srednia = dane.mean()
mediana = dane.median()
moda = dane.mode()
std = dane.std()
roz = dane.max() - dane.min()
print(srednia, mediana, moda, std, roz)
otrzym = dane.loc[antybiotyki['Antybiotyk']=="T"]
notrzym = dane.loc[antybiotyki['Antybiotyk']=="N"]
print(otrzym)
srednia_otrzym = otrzym.mean()
mediana = otrzym.median()
moda = otrzym.mode()
std_otrzym = otrzym.std()
roz = otrzym.max() - otrzym.min()
print(f'otrzymane:\nsrednia: {srednia}, mediana: {mediana}, moda: {moda}, std: {std}, roz: {roz}')
srednia_notrzym = notrzym.mean()
mediana = notrzym.median()
moda = notrzym.mode()
std_notrzym = notrzym.std()
roz = notrzym.max() - otrzym.min()
print(f'notrzymane:\nsrednia: {srednia}, mediana: {mediana}, moda: {moda}, std: {std}, roz: {roz}')

print(srednia_otrzym, std_otrzym, srednia_notrzym, std_notrzym)

babki = dane.loc[antybiotyki["Płeć"]=="K"]
chlopki = dane.loc[antybiotyki["Płeć"]=="M"]

babki["WBC"].hist()
plt.show()
chlopki["WBC"].hist()
plt.show()

dane['Wiek'].hist()