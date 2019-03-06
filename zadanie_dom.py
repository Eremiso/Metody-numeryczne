from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
#zad1
for i in range(56,101):
    wynik=2*i**2+2*i+2
    print(i,wynik)

print('-'*20)

#zad2
print("wprowadz liczbę")
liczba=int(input())
wynik=1
for i in range(1,liczba+1):
    wynik=wynik*i
print(wynik)

print('-'*20)

#zad3
def min_funkcji(lista):
    wynik=lista[0]
    indeks=0
    for i in range(len(lista)):
        if wynik>lista[i]:
            wynik=lista[i]
            indeks=i
    return wynik,indeks

print('-'*20)

#zad4
print("wprowadz długość tabeli")

x=int(input())
tablicax=linspace(0,x,10)
tablicay=[]
for i in range(len(tablicax)):
    y=i**2+1
    tablicay.append(y)
plot(tablicax,tablicay)
show()

