import math
import sympy as sp

def newton_raphson_method(initial_guess, max_iterations, max_error_percentage, user_function):
    e = math.e
    x = sp.symbols('x')
    f = eval(user_function.replace('c', 'x'))  # Cambia 'c' por 'x'
    
    c = initial_guess
    
    for i in range(max_iterations):
        f_value = f.subs(x, c)
        f_derivative = sp.diff(f, x).subs(x, c)
        
        c_next = c - f_value / f_derivative
        error_percentage = abs((c_next - c) / c_next) * 100
        
        if error_percentage < max_error_percentage:
            return c_next, i + 1
        
        c = c_next
    
    return c, max_iterations

user_function = input("Ingresa la función f(x) para el método de Newton-Raphson (debe ser de la forma f(x)): ")
initial_guess = float(input("Ingresa el valor inicial de aproximación: "))

max_iterations = 1000
max_error_percentage = 0.01

approximation, num_iterations = newton_raphson_method(initial_guess, max_iterations, max_error_percentage, user_function)

print("Aproximación de la raíz:", approximation)
print("Número de iteraciones:", num_iterations)
