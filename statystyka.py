
# autor: Piotr Dłubak

import numpy as np
import math
import statistics
from matplotlib import pyplot
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import shapiro
from scipy.stats import normaltest



# dane o dochodach pracowników pewnej firmy"

#cel : przeprowadzenie analizy statystycznej w oparciu o przedstawione dane

dochody = np.array([4218.29, 2443.94, 2656.02, 3986.67, 2675.86, 2748.22, 2491.71,
       4050.26, 3282.1 , 2344.28, 2156.36, 4017.71, 2245.64, 4868.65,
       1461.3 , 3617.12, 1899.59, 3280.86, 3817.46, 3969.58, 2249.54,
       2008.43, 4604.74, 3559.78, 2292.92, 2691.95, 3254.35, 3059.95,
       2671.46, 3609.9 , 2510.75, 2412.25, 2448.85, 3423.14, 3728.6 ,
       4084.91, 5169.59, 2852.88, 2708.3 , 3370.92, 2766.49, 1268.  ,
       1977.13, 4216.72, 2776.87, 4335.5 , 3125.04, 2934.08, 3609.85,
       4295.11, 2025.57, 3068.81, 3254.73, 4750.69, 1980.23, 3928.04,
       3087.58, 2400.15, 1969.92, 4450.51, 3721.39, 3822.03, 3423.61,
       4450.6 , 3114.94, 2484.58, 3882.75, 1205.87, 3049.77, 2383.6 ,
       3201.95, 3806.16, 2699.69, 3141.3 , 1746.59, 2394.83, 3271.3 ,
       3327.05, 4148.09, 3140.21, 4008.05, 2573.52, 4972.38, 1010.54,
       3628.69, 3213.2 , 3604.41, 2235.79, 3504.53, 3394.34, 2322.22,
       2663.77, 3492.91, 2120.04, 1988.12, 3403.69, 4802.52, 3676.62,
       4500.84, 4526.02, 3450.16, 3930.47, 3959.94, 3329.43, 1345.21,
       2281.1 , 2434.34, 2851.8 , 4837.62, 1727.87, 1786.3 , 2758.87,
       3772.07, 3384.08, 1227.63, 3565.68, 3153.79, 4112.88, 4254.36,
       4053.65, 4158.35, 1781.77, 2327.88])







# zdefiniowanie funkcji wyliczające podstawowe parametry statystyczne

def n(x):
    n=len(x)
    return (n)

def minimum(x):
    m=min(x)
    return(m)

def maksimum(x):
    m=max(x)
    return(m)

def suma(x):
    s=sum(x)
    return(s)

def mediana(l):
        l.sort()
        lent = len(l)
        if (lent%2)==0:
            m = int(lent/2)
            wynik = l[m]
        else:
            m = int(float(lent/2) -0.5)
            wynik = l[m]
        return (wynik)


def dominanta(x):
    d = statistics.mode(x)
    return(d)


def srednia(x):
    s=suma(x)/n(x)
    return(s).round(2)

def rozstęp(x):
    z = maksimum(x)-minimum(x)
    return(z)


def Q1(x):
    q = np.quantile(x, .25).round(2)
    return(q)


def Q3(x):
    q = np.quantile(x, .75).round(2)
    return(q)


def rozstęp_międzykwartylowy(x):
    r = Q3(x) - Q1(x)
    return(r)


def odchylenie_ćwiartkowe(x):
   r = (rozstęp_międzykwartylowy(x)/2).round(2)
   return(r)


def wariancja(x): # z próby
    v = x-srednia(x)
    v2 = v*v
    v3 = sum(v2)
    v4 = v3/(n(x)-1)
    return(v4).round(2)


def odchylenie_std(x):
    od = math.sqrt(wariancja(x))
    return(od)

def odchylenie_przecietne(x):
    o = x - srednia(x)
    o2 = np.abs(o)
    o3 = np.mean(o2)
    o4 = o3/n(x)
    return(o4).round(2)


def kl_wsp_zmien(x):
    k = (odchylenie_std(x)/srednia(x))*100
    return (k)
    
    
def poz_wsp_zmien(x):
    k = (rozstęp_międzykwartylowy(x)/mediana(x))*100
    return (k)

def wsp_asymetrii(x):
    w = srednia(x) - dominanta(x)
    return(w)

def ws_asymetrii_pearson(x):
    w = wsp_asymetrii(x)/ odchylenie_std(x)
    return(w)


def moment3(x):#standaryzowany
    v = x-srednia(x)
    v2 = v*v*v
    v3 = sum(v2)
    v4 = v3/(n(x)-1)
    v5 = v4/ (odchylenie_std(x)*odchylenie_std(x)*odchylenie_std(x))
    return(v5).round(2)


def ws_as_wew(x):
    a = (Q1(x) +Q3(x))
    a1 = a/(2 * mediana(x))
    return(a1)


def moment4(x):#standaryzowany
    v = x-srednia(x)
    v2 = v*v*v*v
    v3 = sum(v2)
    v4 = v3/(n(x)-1)
    v5 = v4 / (odchylenie_std(x)*odchylenie_std(x)*odchylenie_std(x)*odchylenie_std(x))-3
    return(v5).round(2)


def kl_obszar_zm_L(x):
    o1 = srednia(x) - odchylenie_std(x)
    return(o1)

def kl_obszar_zm_P(x):
    o2 = srednia(x) + odchylenie_std(x)
    return(o2)

def poz_obszar_zm_L(x):
    o1 = mediana(x) - odchylenie_ćwiartkowe(x)
    return(o1)

def poz_obszar_zm_P(x):
    o2 = mediana(x) + odchylenie_ćwiartkowe(x)
    return(o2)



def miary(x):
    print('wyliczone miary statystyczne:')
    print("-----------------------------")
    print(f'liczba obserwacji: {n(x):.0f}')
    print(F'minimum: {minimum(x):.2f}')
    print(F'maksimum: {maksimum(x):.2f}')
    print(F'suma: {suma(x):.2f}')
    print(F'mediana: {mediana(x):.2f}')
    print(F'srednia: {srednia(x):.2f}')
    print(F'Q1: {Q1(x):.2f}')       
    print(F'Q3: {Q3(x):.2f}')
    print(F'rozstęp_międzykwartylowy: {rozstęp_międzykwartylowy(x):.2f}')
    print(F'odchylenie_ćwiartkowe: {odchylenie_ćwiartkowe(x):.2f}')
    print(F'wariancja: {wariancja(x):.2f}')
    print(F'odchylenie_std: {odchylenie_std(x):.2f}')
    print(F'odchylenie_przecietne: {odchylenie_przecietne(x):.2f}')
    print(F'klasyczny współczynnik zmiennosci: {kl_wsp_zmien(x):.2f}')
    print(F'pozycyjny współczynnik zmiennosci: {poz_wsp_zmien(x):.2f}')   
    print(F'współczynnik asymetrii : {wsp_asymetrii(x):.2f}') 
    print(F'współczynnik asymetrii pearsona : {ws_asymetrii_pearson(x):.2f}') 
    print(F'współczynnik asymetrii : {wsp_asymetrii(x):.2f}') 
    print(F'współczynnik skosnosci(Moment_3) : {moment3(x):.2f}') 
    print(F'współczynnik asymetri wewnetrznej : {ws_as_wew(x):.2f}')
    print(F'moment_4 (eksces) : {moment4(x):.2f}')
    print(F'klasyczny obszar zmiennoci : Xtyp ∈ ({kl_obszar_zm_L(x):.2f} ,{kl_obszar_zm_P(x):.2f})')
    print(F'pozycyjny obszar zmiennoci : Xtyp ∈ ({poz_obszar_zm_L(x):.2f} ,{poz_obszar_zm_P(x):.2f})')
    
    
    
miary(dochody)    
print()


# wykres historgamu
pyplot.hist(dochody)
pyplot.show()


# wykres QQ Plot

qqplot(dochody, line='s')
pyplot.show()



# Shapiro-Wilk Test normalnoci

print()
print("sprawdzenie normalnosci rozkładu próbki badawczej w oparciu o Shapiro-Wilk Test:")
print()
      
stat, p = shapiro(dochody)
print('Statystyka = %.3f, p-value = %.3f' % (stat, p))

alpha = 0.05
if p > alpha:
	print('próbka ma rozkład normalny (nie można odrzucić H0)')
else:
	print('próbka nie ma rozkładu normalnego (można odrzucić H0)')

print()
print("sprawdzenie normalnosci rozkładu próbki badawczej w oparciu o D'Agostino and Pearson's Test: ")
print()


# D'Agostino and Pearson's Test


# normality test
stat, p = normaltest(dochody)
print('Statystyka = %.3f, p-value = %.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('próbka ma rozkład normalny (nie można odrzucić H0)')
else:
	print('próbka nie ma rozkładu normalnego (można odrzucić H0)')
    
    
    
