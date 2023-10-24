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

x0 = -2 
y0 = 0  
h = 0.1 
n = 100 

# Resolver la EDO usando el método de Euler

x_values, y_values = euler_method(f, x0, y0, h, n)

# Imprimir los resultados

for x, y in zip(x_values, y_values):
    print(f'x = {x:.2f}, y = {y:.6f}')

# Graficar la solución

import matplotlib.pyplot as plt
plt.plot(x_values, y_values)
plt.show()