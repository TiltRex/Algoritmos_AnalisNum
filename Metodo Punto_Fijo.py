import math
import sympy as sp

def fixed_point_method(c0, max_iter, max_error_percentage, user_function_f):
    e=math.e
    c = c0
    x = sp.symbols('x')
    f = eval(user_function_f.replace('c', 'x'))
    df = sp.diff(f, x)
    
    for i in range(max_iter):
        f_c = eval(user_function_f.replace('c', str(c)))  # Calcular f(c)
        g_c = c - f_c / df.subs(x, c)  # Calcular g(c) utilizando la derivada
        error_percentage = abs((g_c - c) / g_c) * 100  # Calcular el porcentaje de error
        if error_percentage < max_error_percentage:
            return g_c, i + 1  # Devolver la aproximación y el número de iteraciones
        c = g_c
    
    return c, max_iter  # Devolver la última aproximación si se alcanza el número máximo de iteraciones

# Solicitar al usuario ingresar la función f(c)
user_function_f = input("Ingresa la función f(c) para el método del punto fijo: ")

# Valor inicial c0
c0 = float(input("Ingresa el valor inicial c0: "))

# Número máximo de iteraciones y porcentaje máximo de error
max_iterations = 1000
max_error_percentage = 0.3  # Porcentaje de error máximo permitido

# Aplicar el método del punto fijo
approximate_solution, num_iterations = fixed_point_method(c0, max_iterations, max_error_percentage, user_function_f)

print("Aproximación de la solución:", approximate_solution)
print("Número de iteraciones:", num_iterations)
