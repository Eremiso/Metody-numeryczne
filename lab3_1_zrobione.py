from cs50 import *
from numpy import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def poczatek_programu():
    print("Witam w programie")
    print("Wybierz jakiej figury pole chcesz policzyć")
    print("k - koło , r - romb , p - prostokąt , t - trójkąt")
    a=get_string("Wprowadz skrót: ")

    while a!="k" and a!="r" and a!="p" and a!="t":
        print("wprowadzony skrót jest nie poprawyny proszę spróbować ponownie ")
        a=get_string("Wprowadz skrót: ")
    print('-' * 20)
    return a

def pole_koła(x):
    while x<=0:
        print("Nie da się stworzyć koła o tym promieniu, wprowadz poprawny promień")
        x=get_float("Wprowadz wartość dla nowego promienia: ")

    pole=pi*x**2

    return pole

def pole_romba(x,y):
    while x <= 0:
        print("Pierwsza przekątna jest nie poprawna")
        x = get_float("Wprowadz nową wartość dla pierwszej przekątnej: ")
    while y <= 0:
        print("Druga przekątna jest nie poprawna")
        y = get_float("Wprowadz nową wartość dla drugą=iej przekątnej: ")

    pole = (x * y) / 2

    return pole

def pole_porostokąta(x,y):
    while x <= 0:
        print("Pierwszy bok jest nie poprawny")
        x = get_float("Wprowadz nową wartość dla pierwszego boku: ")
    while y <= 0:
        print("Drugi bok jest nie poprawna")
        y = get_float("Wprowadz nową wartośc dla drugiego boku: ")

    pole=x*y

    return pole

def pole_trójkąta(x,y):
    while x <= 0:
        print("Podstawa trójkąta jest nie poprawny")
        x = get_float("Wprowadz nową wartość dla podstawy trójkąta: ")
    while y <= 0:
        print("Wysokość trójkąta jest nie poprawna")
        y = get_float("Wprowadz nową wartośc dla wysokości trójkąta: ")

    pole=(x*y)/2

    return pole

def obliczenia_dla_figury(string):
    if string=="k":
        x=get_float("Wprowadz promień koła")
        print('-' * 20)
        pole=(pole_koła(x))
    elif string=="r":
        x=get_float("Wprowadz pierwszą przekątną")
        y=get_float("Wprowadz drugą przekątną")
        print('-' * 20)
        pole =(pole_romba(x,y))
    elif string=="p":
        x=get_float("Wprowadz pierwszy bok")
        y=get_float("Wprowadz drugi bok")
        print('-' * 20)
        pole =(pole_porostokąta(x,y))
    elif string=="t":
        x=get_float("Wprowadz długość podstawy")
        y=get_float("Wprowadz wysokość trójkąta")
        print('-' * 20)
        pole =(pole_trójkąta(x,y))

    return print("Pole figury wynosi: ", pole)


obliczenia_dla_figury(poczatek_programu())