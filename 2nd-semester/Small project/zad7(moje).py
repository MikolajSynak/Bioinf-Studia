import matplotlib.pyplot as plt
import numpy as np

#wpisuję dane. Lista "x" odpowiada wysokościom a "y" gęstości względnej powietrza.
x = [0, 1.525, 3.050, 4.575, 6.10, 7.265, 9.15, 10.5]
y = [1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741, 0.2411219750000001]

#Obliczam za pomocą funkcji "polyfit" wartości 'a' oraz 'b' dla stycznej o równaniu y=ax+b
wsp = np.polyfit(x, y, 1, rcond=None, full=False, w=None, cov=False)
print(wsp)
z = -0.06923739 * 10.5 + 0.96811457

#Teraz, mając równanie y = (-0.06923739) * x + 0.96811457 mogę obliczyć wartość 'y' dla x=10.5, nic mnie już nie powstrzyma.
print("Gęstosc powietrza na wysokosci 10.5km wynosi {}, czyli w zaokragleniu 0.24".format(z))

#A teraz uwaga, znienacka dodam znak wodny którego pan nie zobaczy oczywiscie bo wiadomo, lokalne zdjecie wgrywam (wysle co mi wypluło):
fig=plt.figure(figsize=(10,6))
import matplotlib.image as img
av_logo=img.imread(fname=r'C:\Users\Mikolaj Synak\Desktop\zaliczenie_logo.png')
plt.figimage(av_logo,10,7,alpha=0.05)
#A teraz robię suchy wykres przedstawiający dane i obrazujący ogólną zależność "funkcji" w sposób wizualny wykorzystując matplotliba
plt.plot(x, y, 'o')

#Trochę zwiększę czytelność wykresu oznaczając, co jest czym
plt.title('Wykresik')
plt.xlabel("wysokosc")
plt.ylabel("gestosc powietrza")



#A teraz puszczam wodze wyobraźni i dodaję bezsensowne strzałki i kolory tylko po to żeby pokazać że umiem:
#Tu strzałeczki:
plt.annotate('nic tu nie ma',xy=(2,0.9),arrowprops=dict(arrowstyle='-|>',connectionstyle='angle,angleA=90,angleB=0'),xytext=(1.6,0.6))
plt.annotate('tu biegnie jelen',xy=(5,0.9),arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-.2'),xytext=(8,00.8))
plt.annotate('tu za to jest nasz wynik :D',xy=(10.5,0.2411219750000001),arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-.2'),xytext=(8,00.5))
#Tu usuwam zbędne linie od góry i z prawej żeby mniej nakupciane było na wykresie:
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
#A tu zmieniam kolor. Po co? Nie mam pojęcia. Tak se.
plt.gca().spines['left'].set_color('red')
plt.gca().spines['bottom'].set_color('green')


#A to to nie wiem po co do konca ale bez tego nie pokazuje wykresu w pycharmie wiec zostawie xd
#domyslam sie ze jest do otworzenia kolejnego okna z wykresem, bo w anacondzie na luzie pokazywalo bezposrednio w programie bez otwierania dodatkowego okna a pycharm nie jest niestety tak wspaniałym i nierażącym w oczy programem jak spyder3
plt.show()
#(nie lubimy się ze spyderem)

