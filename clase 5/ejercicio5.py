# Hay que programar el método de Euler que se usa para resolver ecuaciones diferenciales

import sympy as sp

def euler_method(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    for _ in range(n):
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x_values.append(x_new)
        y_values.append(y_new)

    return x_values, y_values

def f(x, y):
    return y - x**2 + 1

# Lo pongo en practica para resolver la ecuación diferencial y' = (2 - x - y) / (x - y + 4), no tenemos datos sobre h y n asi que me los invento 

n= int(input("Ingrese el valor de n: "))
h = (1/2-0)/n

x0 = float(input("Ingrese el valor de x0: "))
y0 = float(input("Ingrese el valor de y0: "))

x1 = float(input("Ingrese el valor de x1: "))
y1 = float(input("Ingrese el valor de y1: "))

x2 = float(input("Ingrese el valor de x1: "))
y2 = float(input("Ingrese el valor de y1: "))

# Resolver la EDO usando el método de Euler

x_values, y_values = euler_method(f, x0, y0, h, n)
x1_values, y1_values = euler_method(f, x1, y1, h, n)
x2_values, y2_values = euler_method(f, x2, y2, h, n)

# Imprimir los resultados

for x, y in zip(x_values, y_values):
    print(f'x = {x:.2f}, y = {y:.6f}')

for x, y in zip(x1_values, y1_values):
    print(f'x = {x:.2f}, y = {y:.6f}')

for x, y in zip(x2_values, y2_values):
    print(f'x = {x:.2f}, y = {y:.6f}')

# Graficar la solución
import matplotlib.pyplot as plt
plt.plot(x_values, y_values, x1_values, y1_values, x2_values, y2_values, sp.exp(x) * (x + 1)**2 * sp.exp(-x) - 2, sp.exp(x) * (x + 1)**2 * sp.exp(-x) - 1, sp.exp(x) * (x + 1)**2 * sp.exp(-x) - 0.5)
plt.show()

# consejo: poner x0=0, y0=0.5, x1= 0, y1= 0, x2=0, y2=-1, n=100