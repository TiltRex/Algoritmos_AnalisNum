import math
import sympy as sp

#! CREACIÓN DE LAS FUNCIONES


# * ALGORITMO DE BISECCIÓN
def bisection_method(a, b, max_iter, max_error_percentage, user_function):
    e = math.e
    f_a = eval(user_function.replace("c", str(a)))
    f_b = eval(user_function.replace("c", str(b)))

    if f_a * f_b >= 0:
        raise ValueError("La función no cambia de signo en el intervalo dado.")

    prev_c = 0  # Variable para almacenar el valor de c en la iteración anterior

    for i in range(max_iter):
        c = (a + b) / 2
        f_c = eval(user_function.replace("c", str(c)))

        if i > 0:  # Calcular el error a partir de la segunda iteración
            error_percentage = abs((c - prev_c) / c) * 100
            if error_percentage < max_error_percentage:
                return c, i + 1

        prev_c = c  # Guardar el valor de c para la próxima iteración
        if f_c * f_a < 0:
            b = c
        else:
            a = c

    return (a + b) / 2, max_iter


# * ALGORITMO DE FALSA POSICIÓN
def false_position_method(a, b, max_iter, max_error_percentage, user_function):
    e = math.e
    f_a = eval(user_function.replace("c", str(a)))
    f_b = eval(user_function.replace("c", str(b)))

    if f_a * f_b >= 0:
        raise ValueError("La función no cambia de signo en el intervalo dado.")

    prev_c = 0  # Variable para almacenar el valor de c en la iteración anterior

    for i in range(max_iter):
        c = (a * f_b - b * f_a) / (f_b - f_a)
        f_c = eval(user_function.replace("c", str(c)))

        if i > 0:  # Calcular el error a partir de la segunda iteración
            error_percentage = abs((c - prev_c) / c) * 100
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


# * ALGORITMO DE PUNTO FIJO
def fixed_point_method(c0, max_iter, max_error_percentage, user_function_f):
    e = math.e
    c = c0
    x = sp.symbols("x")
    f = eval(user_function_f.replace("c", "x"))
    df = sp.diff(f, x)

    for i in range(max_iter):
        f_c = eval(user_function_f.replace("c", str(c)))  # Calcular f(c)
        g_c = c - f_c / df.subs(x, c)  # Calcular g(c) utilizando la derivada
        error_percentage = abs((g_c - c) / g_c) * 100  # Calcular el porcentaje de error
        if error_percentage < max_error_percentage:
            return g_c, i + 1  # Devolver la aproximación y el número de iteraciones
        c = g_c

    return (
        c,
        max_iter,
    )  # Devolver la última aproximación si se alcanza el número máximo de iteraciones


# * ALGORITMO DE NEWTON-RAPSHON
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


# * ALGORITMO DE LA SECANTE
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


flag = False

print(
    """
    +-------------------------+
    |  BIENVENIDO A CODIGITO  |
    +-------------------------+
    """
)

while flag == False:
    request = int(
        input(
            """Cuales de los siguientes algoritmos desea ejercutar:
         (1) Método de la bisección
         (2) Falsa posición 
         (3) Punto fijo
         (4) Newton-Raphson
         (5) La secante
         (0) Cerrar programa
    --> """
        )
    )

    if request == 1:
        print(
            """
    ./-------------------------\.
     |   CODIGITO BISECCIÓN    |
    .\-------------------------/.       
    """
        )

        # Solicitar al usuario ingresar la función
        user_function = input(
            """Ingresa la función f(c): 
        --> """
        )

        # Intervalo inicial [a, b]
        a = int(input("Ingresa el valor del intervalo a: --> "))
        b = int(input("Ingresa el valor del intervalo b: --> "))

        # Número máximo de iteraciones y porcentaje máximo de error
        max_iterations = 1000
        max_error_percentage = 0.3

        # Aplicar el método de la bisección
        approximate_c, num_iterations = bisection_method(
            a, b, max_iterations, max_error_percentage, user_function
        )

        print("Valor aproximado de c:", approximate_c)
        print("Número de ciclos empleados:", num_iterations)
        flag = True

    if request == 2:
        print(
            """
    ./-----------------------------\.
     |   CODIGITO FALSA POSICION   |
    .\-----------------------------/.       
    """
        )

        # Solicitar al usuario ingresar la función
        user_function = input(
            """Ingresa la función f(c): 
        --> """
        )

        # Intervalo inicial [a, b]
        a = int(input("Ingresa el valor del intervalo a: --> "))
        b = int(input("Ingresa el valor del intervalo b: --> "))

        # Número máximo de iteraciones y porcentaje máximo de error
        max_iterations = 1000
        max_error_percentage = 0.3

        # Aplicar el método de la falsa posición
        approximate_c, num_iterations = false_position_method(
            a, b, max_iterations, max_error_percentage, user_function
        )

        print("Valor aproximado de c:", approximate_c)
        print("Número de ciclos empleados:", num_iterations)
        flag = True

    if request == 3:
        print(
            """
    ./-------------------------\.
     |   CODIGITO PUNTO FIJO   |
    .\-------------------------/.       
    """
        )

        user_function_f = input(
            """Ingresa la función f(c): 
        --> """
        )

        # Valor inicial c0
        c0 = float(input("Ingresa el valor inicial de aproximación: "))

        # Número máximo de iteraciones y porcentaje máximo de error
        max_iterations = 1000
        max_error_percentage = 0.3  # Porcentaje de error máximo permitido

        # Aplicar el método del punto fijo
        approximate_solution, num_iterations = fixed_point_method(
            c0, max_iterations, max_error_percentage, user_function_f
        )

        print("Aproximación de la solución:", approximate_solution)
        print("Número de iteraciones:", num_iterations)
        flag = True

    if request == 4:
        print(
            """
    ./-----------------------------\.
     |   CODIGITO NEWTON_RAPHSON   |
    .\-----------------------------/.       
    """
        )

        user_function = input(
            """Ingresa la función f(c): 
        --> """
        )

        initial_guess = float(input("Ingresa el valor inicial de aproximación: "))

        max_iterations = 1000
        max_error_percentage = 0.01

        approximation, num_iterations = newton_raphson_method(initial_guess, max_iterations, max_error_percentage, user_function)

        print("Aproximación de la raíz:", approximation)
        print("Número de iteraciones:", num_iterations)
        flag = True

    if request == 5:
        print(
            """
    ./----------------------\.
     |   CODIGITO SECANTE   |
    .\----------------------/.       
    """
        )

        user_function = input(
            """Ingresa la función f(c): 
        --> """
        )
        
        # Valores iniciales de aproximación
        initial_guess_1 = float(input("Ingresa el valor del intervalo a: --> "))
        initial_guess_2 = float(input("Ingresa el valor del intervalo b: --> "))

        # Número máximo de iteraciones y porcentaje máximo de error
        max_iterations = 1000
        max_error_percentage = 0.3  # Porcentaje de error máximo permitido

        # Aplicar el método de la secante
        approximation, num_iterations = secant_method(initial_guess_1, initial_guess_2, max_iterations, max_error_percentage, user_function)

        print("Aproximación de la raíz:", approximation)
        print("Número de iteraciones:", num_iterations)
        flag = True

# ((68.1 * 9.8) / c) * (1 - e**((-c / 68.1) * 10)) - 40
