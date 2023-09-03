import math

#! CREACIÓN DE LAS FUNCIONES
 
#* ALGORITMO DE BISECCIÓN
def bisection_method(a, b, max_iter, max_error_percentage, user_function):
    e = math.e
    f_a = eval(user_function.replace('c', str(a)))
    f_b = eval(user_function.replace('c', str(b)))
    
    if f_a * f_b >= 0:
        raise ValueError("La función no cambia de signo en el intervalo dado.")

    for i in range(max_iter):
        c = (a + b) / 2
        f_c = eval(user_function.replace('c', str(c)))
        
        error_percentage = abs((c - (a + b) / 2) / c) * 100

        if error_percentage < max_error_percentage:
            return c, i + 1

        if f_c * f_a < 0:
            b = c
        else:
            a = c

    return (a + b) / 2, max_iter

#* ALGORITMO DE FALSA POSICIÓN
def falsa_posicion():
    return print("Falsa_posicion")

#* ALGORITMO DE PUNTO FIJO
def punto_fijo():
    return print("Punto fijo")

#* ALGORITMO DE NEWTON-RAPSHON
def newton_rapshon():

    return print("Newton Rapshon")

#* ALGORITMO DE LA SECANTE
def secante():
    return print("La secante")



flag = False

print('''
    +-------------------------+
    |  BIENVENIDO A CODIGITO  |
    +-------------------------+
    ''')

while(flag == False):
    request = int(input('''Cuales de los siguientes algoritmos desea ejercutar:
         (1) Método de la bisección
         (2) Falsa posición 
         (3) Punto fijo
         (4) Newton-Rapshon
         (5) La secante
         (0) Cerrar programa
    --> '''))

    if(request == 1):
        print('''
    ./-------------------------\.
     |   CODIGITO BISECCIÓN    |
    .\-------------------------/.       
    ''')

        # Solicitar al usuario ingresar la función
        user_function = input('''Ingresa la función f(c): 
        --> ''')

        # Intervalo inicial [a, b]
        a = int(input("Ingresa el valor del intervalo a: --> "))
        b = int(input("Ingresa el valor del intervalo b: --> "))

        # Número máximo de iteraciones y porcentaje máximo de error
        max_iterations = 1000
        max_error_percentage = 0.3

        # Aplicar el método de la bisección
        approximate_c, num_iterations = bisection_method(a, b, max_iterations, max_error_percentage, user_function)

        print("Valor aproximado de c:", approximate_c)
        print("Número de ciclos empleados:", num_iterations)
        flag = True
#((68.1 * 9.8) / c) * (1 - e**((-c / 68.1) * 10)) - 40