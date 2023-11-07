import numpy as np

def euler_method(f, x0, y0,x_inicial, x_final, num_iterations):
    h = (x_final - x_inicial) / num_iterations
    x_values = [x0]
    y_values = [y0]

    for i in range(num_iterations):
        x = x_values[-1]
        y = y_values[-1]
        y_new = y + h * f(x, y)
        x_new = x + h
        x_values.append(x_new)
        y_values.append(y_new)

    return x_values, y_values

# Define la ecuación diferencial dy/dx = f(x, y)
def f(x, y):
    # Puedes definir tu propia función f(x, y) aquí.
    return (2 -3*x - y)/(x-1)

# Entrada de datos
x0 = float(input("Introduce x0: "))  # Punto inicial x
y0 = float(input("Introduce y0: "))  # Punto inicial y
x_inicial = float(input("Introduce x_inicial: "))  # Valor inicial de x
x_final = float(input("Introduce x_final: "))  # Valor final de x
num_iterations = int(input("Introduce el número de iteraciones: "))  # Número de iteraciones

# Calcula las soluciones utilizando el método de Euler
x_values, y_values = euler_method(f, x0, y0, x_inicial,x_final, num_iterations)

# Imprime los resultados
w_final = y_values[-1]
y_total = -8.2
error = np.abs(y_total-w_final)
print(f"El valor real de la solución es y({x_final}) = {y_total}")
print(f"El valor final de las iteraciones de eurler es w({num_iterations}) = {w_final}")
print(f'El error es {error}')