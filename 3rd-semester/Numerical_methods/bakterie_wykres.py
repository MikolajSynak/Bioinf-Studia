import numpy as np
import math as mt
from matplotlib import pyplot as plt
import matplotlib.image as img

print(np.pi)
print(np.log(10))

print("jesli nie podoba ci sie wykres to go zamknij a python prawdę ci powie (wypluje suche dane)")


#uwaga, znienacka dodam znak wodny którego nie zobaczysz oczywiscie bo wiadomo, lokalne zdjecie wgrywam (w mailu dodam co mi wypluło):
fig=plt.figure(figsize=(5,3))
av_logo=img.imread(fname=r'E:\Beatka_cwiczenia\ug_logo.png')
plt.figimage(av_logo,10,7,alpha=0.05)
bacteria = np.loadtxt('bakterie.txt')

# Robię wykres:
plt.plot(bacteria)
plt.title('Wykresik z bakteriami')
plt.ylabel("nie mam pojecia co oznaczają te dane")
plt.xlabel("naprawdę... ale gdybym wiedział to bym tu napisał;)")


# Wyrzucam górną i prawą granicę wykresu zeby było czysciej i bardziej minimalistycznie:
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Zmieniam kolory prawej i dolnej bo czemu by nie, w koncu więcej kolorów = lepsza wiarygodność, nie...?
plt.gca().spines['left'].set_color('red')
plt.gca().spines['bottom'].set_color('green')

# Dobra, teraz strzałki żeby nie było tak minimalistycznie i ogolnie zeby byl chaos:
plt.annotate('pyk, tu nic nie ma sensownego ale dodam strzałkę bo smutno na wykresie', xy=(60, 60),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.1'), xytext=(25, 100))
plt.annotate('NIKT MNIE NIE POWSTRZYMA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',xy=(5,40),
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-.2'),xytext=(0,60))
plt.annotate('o moj boze, czy to watermark ug w lewym dolnym rogu? Najwyrazniej tak...',xy=(-2,-2),arrowprops=dict(arrowstyle='-|>',connectionstyle='angle,angleA=90,angleB=0'),xytext=(8,15))
plt.annotate('i jakie fajne wygięcie strzałki :o', xy=(23, 0),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-.1'), xytext=(60, 0))


plt.show()

print(bacteria)

print(bacteria[1,1])

x = bacteria[:, 0]
f = bacteria[:, 1]
print(x)
print(f)