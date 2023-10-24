# Hay que programar el método de Euler que se usa para resolver ecuaciones diferenciales

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
    return (2 - x - y) / (x - y + 4)

# Lo pongo en practica para resolver la ecuación diferencial y' = (2 - x - y) / (x - y + 4), no tenemos datos sobre h y n asi que me los invento 

n= int(input("Ingrese el valor de n: "))

x0 = int(input("Ingrese el valor de x0: "))
y0 = int(input("Ingrese el valor de y0: ")) 
h = ( - x0)/n

x1 = int(input("Ingrese el valor de x1: "))
y1 = int(input("Ingrese el valor de y1: "))
h1 = ( - x1)/n

x2 = int(input("Ingrese el valor de x2: "))
y2 = int(input("Ingrese el valor de y2: "))
h2 = ( - x2)/n

# Resolver la EDO usando el método de Euler

x_values, y_values = euler_method(f, x0, y0, h, n)
x1_values, y1_values = euler_method(f, x1, y1, h1, n)
x2_values, y2_values = euler_method(f, x2, y2, h2, n)

# Imprimir los resultados

for x, y in zip(x_values, y_values):
    print(f'x = {x:.2f}, y = {y:.6f}')

for x, y in zip(x1_values, y1_values):
    print(f'x = {x:.2f}, y = {y:.6f}')

for x, y in zip(x2_values, y2_values):
    print(f'x = {x:.2f}, y = {y:.6f}')

# Graficar la solución

import matplotlib.pyplot as plt
plt.plot(x_values, y_values, x1_values, y1_values, x2_values, y2_values)
plt.show()