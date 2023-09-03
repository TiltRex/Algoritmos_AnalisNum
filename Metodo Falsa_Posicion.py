import math

def false_position_method(a, b, max_iter, max_error_percentage, user_function):
    e = math.e
    f_a = eval(user_function.replace('c', str(a)))
    f_b = eval(user_function.replace('c', str(b)))
    
    if f_a * f_b >= 0:
        raise ValueError("La función no cambia de signo en el intervalo dado.")

    prev_c = 0  # Variable para almacenar el valor de c en la iteración anterior

    for i in range(max_iter):
        c = (a * f_b - b * f_a) / (f_b - f_a)
        f_c = eval(user_function.replace('c', str(c)))
        
        if i > 0:  # Calcular el error a partir de la segunda iteración
            error_percentage = abs((c - prev_c) / c) * 100
            print(error_percentage)
            if error_percentage < max_error_percentage:
                return c, i + 1

        prev_c = c  # Guardar el valor de c para la próxima iteración

        if f_c * f_a < 0:
            b = c
            f_b = f_c
        else:
            a = c
            f_a = f_c

    return c, max_iter

# Solicitar al usuario ingresar la función
user_function = input("Ingresa la función f(c): ")

# Intervalo inicial [a, b]
a = int(input("Ingresa el valor del intervalo a: "))
b = int(input("Ingresa el valor del intervalo b: "))

# Número máximo de iteraciones y porcentaje máximo de error
max_iterations = 1000
max_error_percentage = 0.3

# Aplicar el método de la falsa posición
approximate_c, num_iterations = false_position_method(a, b, max_iterations, max_error_percentage, user_function)

print("Valor aproximado de c:", approximate_c)
print("Número de ciclos empleados:", num_iterations)