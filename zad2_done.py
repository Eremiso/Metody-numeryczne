from cs50 import *
from numpy import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


print("zad0")
x = get_int("x: ")
y = get_char("y: ")
z = get_float("z: ")

print('-'*20)

print("zad1")
x = get_float("x: ")
y = get_float("y: ")
def obw_pol(r):
    obw=2*pi*r
    pol=pi*r**2
    return("obwód to:",obw,"pole to:",pol)
print(obw_pol(x))
print(obw_pol(y))

print('-'*20)

print("zad2")
x = get_int("x: ")
y = get_int("y: ")
while x % y !=0 or x%2!=0 or y%2!=0 or x==0 or y==0:
    print("para nie spełnia warunków")
    x = get_int("wprowadz nowe x: ")
    y = get_int("wprowadz nowe y: ")
print("para spełnia warunki")

print('-'*20)

print("zad3")
x = get_int("x: ")
y = get_int("y: ")
sprawdzenie = x % y == 0
funkcja = 'X dzieli się przez Y' if sprawdzenie else 'X nie dzieli się przez Y'
print(funkcja)

print('-'*20)

print("zad4")
x = get_int("x: ")
y = get_int("y: ")
print(f"{x/y:.2f}")

print('-'*20)

print("zad5")
x = get_int("x: ")
y = get_int("y: ")
x_knots = np.linspace(0,x,200)
y_knots = np.linspace(0,y,200)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**3+1+Y**3+1)
Z = np.cos(R)**3*np.exp(-0.1*R)
ax = Axes3D(plt.figure(figsize=(10,8)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()