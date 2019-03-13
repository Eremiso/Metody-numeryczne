from cs50 import *
from numpy import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def poczatek_programu():
    print("Witam w programie")
    print("Wybierz jakie figury będziesz porównywał")
    print("k - koło , r - romb , p - prostokąt , t - trójkąt")
    figura1=get_string("Wprowadz skrót dla pierwszej figury: ")
    figura2=get_string("Wprowadz skrót dla drugiej figury: ")

    while figura1!="k" and figura1!="r" and figura1!="p" and figura1!="t":
        print("Wprowadzony skrót dla pierwszej figury jest nie poprawyny proszę spróbować ponownie ")
        figura1=get_string("Wprowadz skrót ponownie: ")
    while figura2 != "k" and figura2 != "r" and figura2 != "p" and figura2 != "t":
        print("Wprowadzony skrót dla drugiej figury jest nie poprawyny proszę spróbować ponownie ")
        figura2 = get_string("Wprowadz skrót ponownie: ")
    print('-' * 20)
    return figura1,figura2

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

    return pole

def porownanie_pol(pole1,pole2,figura1,figura2):

    if figura1=="k":
        figura1="KOŁA"
    elif figura1=="r":
        figura1="ROMBA"
    elif figura1=="p":
        figura1="PROSTOKĄTA"
    else:
        figura1="TRÓJKĄTA"

    if figura2=="k":
        figura2="KOŁA"
    elif figura2=="r":
        figura2="ROMBA"
    elif figura2=="p":
        figura2="PROSTOKĄTA"
    else:
        figura2="TRÓJKĄTA"


    if pole1>pole2:
        print("Pole",figura1," jest większe niż pole",figura2)
    elif pole1==pole2:
        print("Pola",figura1, "jest równe polu", figura2)
    else:
        print("pole", figura2,"jest większe niż pole", figura1)

figura1,figura2=poczatek_programu()
print("PARAMETRY PIERWSZEJ FIGURY")
print('-' * 20)
pole1=obliczenia_dla_figury(figura1)
print("PARAMETRY DRUGIEJ FIGURY")
print('-' * 20)
pole2=obliczenia_dla_figury(figura2)
porownanie_pol(pole1,pole2,figura1,figura2)
