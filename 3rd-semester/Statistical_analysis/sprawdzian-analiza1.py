
import scipy.stats as stats

#zadanie 8
print(stats.norm.ppf(0.25,13.5,2.5)) #wartosc dla Q1

#zadanie 9 #wartosc dystrybuanty w punkcie x(czym sie rozni ppf od cdf)
#print(stats.norm.ppf(0.2,0,1)) #z=0,8
#print(stats.norm.ppf(0.75,0,1)) #z=0,25 srednia=0 odchylenie =1
#print(stats.norm.ppf(0.75,scale=1,loc=0))
#print(stats.norm.ppf(0.5,loc=0,scale=1))


#zadanie 11
#a
#x=stats.norm.cdf(79,loc=78,scale=0.65)
#print(1-x)
#b
#import math
#print(1-stats.norm.cdf(79,loc=78,scale=13/math.sqrt(20)))


#13
#print(stats.norm.cdf(206,202,14/6)-stats.norm.cdf(198,202,14/6)) 
#p(x>206) - p(x<198)


#14 rozklad chi 
#print(stats.chi2.cdf(30,26))
#cdf-dystrybuanta, 30:P(X<30) 26- stopnie swobody

#15
#print(stats.chi2.ppf(0.95,15))
#liczymy prawdopodobienstwo na lewo wykresu 0.95- pole na lewo 15-ss


 #16
#print(stats.t.cdf(1.4,12)) 
#1.4- wartosc punktu dla ktorego liczymy dystrybuante 12-stopnie swobody 

#17
#print(stats.t.ppf(0.975,9))

#18
#print(1-stats.f.cdf(1.5,6,14))
#dystrybuanta=stats.f.cdf(1.5,6,14)
#print(1- dystrybuanta)

#19- pierwszy sposob rozklad dwumianowy
print(stats.binom.cdf(89,1000,0.1)) #mniej niz 90 gosp domowych 
print(1-stats.binom.cdf(89,1000,0.1))  #prawdopodobienstwo tego ze w probie bedzie min 90 gospodarstw

#19 drugi sposob- przyblizenie rozkladu dwumianowego wynikajace z twierdzenia m-l
import math 
x= (89-100)/math.sqrt(90)   
print(1-stats.norm.cdf(x,0,1))