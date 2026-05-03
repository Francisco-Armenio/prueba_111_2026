#1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne. 
def numero_entero():
    numero = int(input('Ingresa un numero: '))
    return numero

print(numero_entero())

#2. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne. 
def numero_flotante():
    numero = float(input('Ingresa un numero: '))
    return numero

print(numero_flotante())

#3. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne
def cadena():
    texto = input('Escriba algo: ')
    return texto

print(cadena())

# #4. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
# def area_rectangulo(base, altura):
#     area = base * altura
#     return area
# base = float(input('Ingresa la base: '))
# altura = float(input('Ingresa la altura: '))

# resultado = area_rectangulo(base, altura)

# print(resultado)

# #5. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
# def area_circulo(radio):
#     area = 3.14 * (radio ** 2)
#     return area

# radio = float(input('Ingresa el radio del circulo: '))

# resultado = area_circulo(radio)

# print(resultado)

# #6. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar. 
# def numero_par(numero):
#     if numero % 2 == 0:
#         print('Es par')
#     else:
#         print('Es impar')

# numero = int(input('Ingresa un numero: '))
# numero_par(numero)

# #7. Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario. 
# def numero_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# numero = int(input('Ingresa un numero: '))
# print(numero_par(numero))

# #8. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande. 
# def mayor(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > c:
#         return b
#     else:
#         return c

# num1 = int(input('Ingresa un numero: '))
# num2 = int(input('Ingresa otro numero: '))
# num3 = int(input('Ingresa otro numero: '))

# resultado = mayor(num1, num2, num3)
# print(f'El mayor es {resultado}')

# #9. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado. 

# def potencia(base, exponente):
#     return base ** exponente

# base = int(input('Ingresa la base: '))
# exponente = int(input('Ingresa el exponente: '))

# resultado = potencia(base, exponente)

# print(resultado)

# #10. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario. 
# def es_primo(numero):
#     if numero <= 1:
#         return False

#     for i in range(2, numero):
#         if numero % i == 0:
#             return False

#     return True

# num = int(input('Ingresa un numero: '))

# print(es_primo(num))


# #11. Crear una función que (utilizando el algoritmo del ejercicio de la guía de for), muestre todos los números primos comprendidos entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible. 
# def es_primo(numero):
#     contador_divisores = 0

#     for i in range(1, numero + 1):
#         if numero % i == 0:
#             contador_divisores += 1
#     return contador_divisores == 2

# def mostrar_primos(limite):
#     contador_primos = 0

#     for i in range(1, limite + 1):
#         if es_primo(i):
#             print(i)
#             contador_primos += 1
#     return contador_primos

# numero = int(input('Ingresa un numero: '))

# resultado = mostrar_primos(numero)
# print(f'Cantidad de primos: {resultado}')

# #12. Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10. 
# def tabla(numero, inicio=1, fin=10):
#     for i in range(inicio, fin + 1):
#         print(f'{numero} x {i} = {numero * i}')

# numero = int(input('Ingresa un numero: '))
# opcion = input('Queres usar valores por defecto (1 al 10)? (si/no): ')

# if opcion == 'si':
#     tabla(numero)
# else:
#     inicio = int(input('Desde que numero queres empezar: '))
#     fin = int(input('Hasta que numero queres llegar: '))
#     tabla(numero, inicio, fin)

#13. Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones. (No lo entiendo)
