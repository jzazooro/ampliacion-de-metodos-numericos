# Importar bibliotecas necesarias
import numpy as np

# Metodo de euler 
def euler_method(f, x0, y0, x_inicial, x_final, n):
    h = (x_final - x_inicial) / n
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        x = x_values[-1]
        y = y_values[-1]
        y_new = y + h * f(x, y)
        x_new = x + h
        x_values.append(x_new)
        y_values.append(y_new)

    return x_values, y_values

# Definimos f (x, y), que es y'
def f(x, y):
    return (2 -3*x - y)/(x-1)

# Introducimos los datos
x0 = float(input("Introduce x0: "))
y0 = float(input("Introduce y0: "))
x_inicial = float(input("Introduce x_inicial: "))
x_final = float(input("Introduce x_final: "))
n = int(input("Introduce el número de iteraciones: "))

# Calcula las soluciones utilizando el método de Euler
x_values, y_values = euler_method(f, x0, y0, x_inicial,x_final, n)

# Imprime los resultados
w_final = y_values[-1]
y_total = float(input("Introduce el valor real de la solución que te ha dado en papel: "))
error = np.abs(y_total-w_final)
print(f"El valor real de la solución es y({x_final}) = {y_total}")
print(f"El valor final de las iteraciones de eurler es w({n}) = {w_final}")
print(f'El error es {error}')
# consejo: poner x0=2, y0=-1, x_inicial= 2, x_final= 6, n=100, y_total= -8.2