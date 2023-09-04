import math
import sympy as sp

def secant_method(initial_guess_1, initial_guess_2, max_iterations, max_error_percentage, user_function):
    # Definir la variable simbólica y la función
    e = math.e
    x = sp.symbols('x')
    f = eval(user_function.replace('c', 'x'))
    
    # Inicializar las aproximaciones iniciales
    c0 = initial_guess_1
    c1 = initial_guess_2
    
    for i in range(max_iterations):
        # Calcular el valor de la función en las aproximaciones actuales
        f_c0 = f.subs(x, c0)
        f_c1 = f.subs(x, c1)
        
        # Calcular la siguiente aproximación utilizando la fórmula de la secante
        c_next = c1 - f_c1 * (c1 - c0) / (f_c1 - f_c0)
        
        # Calcular el porcentaje de error
        error_percentage = abs((c_next - c1) / c_next) * 100
        
        # Verificar si el porcentaje de error es menor que 0.3
        if error_percentage < max_error_percentage:
            return c_next, i + 1  # Devolver la aproximación y el número de iteraciones
        
        c0 = c1
        c1 = c_next
    
    return c1, max_iterations  # Devolver la última aproximación si se alcanza el número máximo de iteraciones

# Solicitar al usuario ingresar la función f(c)
user_function = input("Ingresa la función f(c) para el método de la secante: ")

# Valores iniciales de aproximación
initial_guess_1 = float(input("Ingresa el primer valor inicial de aproximación: "))
initial_guess_2 = float(input("Ingresa el segundo valor inicial de aproximación: "))

# Número máximo de iteraciones y porcentaje máximo de error
max_iterations = 1000
max_error_percentage = 0.3  # Porcentaje de error máximo permitido

# Aplicar el método de la secante
approximation, num_iterations = secant_method(initial_guess_1, initial_guess_2, max_iterations, max_error_percentage, user_function)

print("Aproximación de la raíz:", approximation)
print("Número de iteraciones:", num_iterations)
