import random
from colorama import Fore, Style, init

init()

# # 1. A partir del ingreso de una edad, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años”.

# edad = int(input('Ingresa su edad: '))

# if edad == 18:
#     print('Usted tiene 18 años')

# # 2. A partir del ingreso de una edad, determinar si la persona es mayor de edad. Si es mayor o igual que 18 se mostrará el mensaje “UD ES MAYOR DE EDAD”.

# edad = int(input('Ingresa su edad: '))

# if edad >= 18:
#     print('UD ES MAYOR DE EDAD')

# # 3. A partir del ingreso de una edad, determinar si la persona es mayor de edad o no. Si es mayor de 18 se mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario “UD ES MENOR DE EDAD”.

# edad = int(input('Ingresa su edad: '))

# if edad >= 18:
#     print('UD ES MAYOR DE EDAD')
# else:
#     print('UD ES MENOR DE EDAD')

# # 4. A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir más de 1.80 metros.

# altura = float(input('Ingresa tu altura: '))

# if altura >= 1.80:
#     print('Podes ser pivot')
# else:
#     print('No podes ser pivot, tu altura es menor a 1.80')

# # 5. Pedirle al usuario su edad, determinar si el usuario es adolescente (edad entre 13 y 17 inclusive)

# edad = int(input('Ingresa tu edad: '))

# if edad >= 13 and edad <= 17:
#     print('Sos adolecente')

# # 6. Pedirle al usuario su edad, determinar si el usuario NO es adolescente.

# edad = int(input('Ingresa tu edad: '))

# if edad < 13 or edad > 17:
#     print('No sos adolecente')

# # 7. Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), pre-adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).

# edad = int(input('Ingresa tu edad: '))

# if edad < 10:
#     print('Es niño/a')
# elif edad >= 10 and edad < 13:
#     print('Es pre-adolecente')
# elif edad >= 13 and edad <= 17:
#     print('Es adolecente')
# else:
#     print('Es mayor')

# # 8. A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:

# # ● Menos de 160 cm: Base

# # ● Entre 160 cm y 179 cm: Escolta

# # ● Entre 180 cm y 199 cm: Alero

# # ● 200 cm o más: Ala-Pívot o Pívot

# altura = int(input('Ingresa tu altura: '))

# if altura < 160:
#     print('Tu posicion es Base')
# elif altura >= 160 and altura <= 179:
#     print('Tu posicion es Escolta')
# elif altura >= 180 and altura <= 199:
#     print('Tu posicion es Alero')
# else:
#     print('Tu posicion es Ala-Pívot o Pívot')

# # 9. Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde los dieciocho (18) años están habilitados a votar. A partir del ingreso de la edad del usuario y el estado (si es naturalizado o nativo), se deberá informar si es o no posible que la persona concurra a votar en base a la información suministrada.

# edad = int(input('Ingresa tu edad: '))
# estado = input('Ingresa tu estado (naturalizado/nativo): ')

# if estado == 'nativo' and edad >= 16:
#     print('Puede votar')
# elif estado == 'naturalizado' and edad >= 18:
#     print('Puede votar')
# else:
#     print('No puede votar')

# # 10. Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado. Determinar si el empleado debe o no pagar el impuesto a las ganancias. El mismo no se pagará si el empleado es casado con hijos y sus ingresos son menores a $2200000.

# sueldo = int(input('Ingresa tu sueldo: '))
# estado_civil = input('Ingresa tu estado civil (casado o soltero): ')
# cantidad_hijos = int(input('Ingresa la cantidad de hijos: '))

# if sueldo > 2200000 and estado_civil == 'casado' and cantidad_hijos > 0:
#     print('No debe pagar el impuesto a las ganancias')
# else:
#     print('Debe pagar el impuesto a las ganancias')


# # 11. Mostrar un número aleatorio entre el 1 y el 10 inclusive.

# numero = random.randint(1, 10)
# print(numero)

# # 12. Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:

# # ● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...

# # ● 4 y 5 ---> Aprobado, la nota es ...

# # ● 1, 2 y 3 ---> Desaprobado, la nota es ...

# numero = random.randint(1, 10)

# if numero >= 6:
#     print(f'Promoción directa, la nota es {numero}')
# elif numero >= 4:
#     print(f'Aprobado, la nota es {numero}')
# else:
#     print(f'Desaprobado, la nota es {numero}')


######################################################################################################################################

# #------------MATCH------------#


# #1. Realizar un programa que solicite al usuario un número del 1 al 7 y muestre el día de la semana correspondiente. Si el número no está entre 1 y 7 mostrar día invalido.

# dia = int(input('Pone un dia del 1 al 7: '))

# if dia >= 1 and dia <= 7:
#     match dia:
#         case 1:
#             print('Es lunes')
#         case 2:
#             print('Es martes')
#         case 3:
#             print('Es miércoles')
#         case 4:
#             print('Es jueves')
#         case 5:
#             print('Es viernes')
#         case 6:
#             print('Es sábado')
#         case 7:
#             print('Es domingo')
# else:
#     print('Día inválido')


# #2. Un sistema ofrece el siguiente menú:

# # 1 - Consultar saldo 
# # 2 - Depositar dinero 
# # 3 - Extraer dinero 
# # 4 – Salir

# # El programa debe pedir al usuario que ingrese una opción y mostrar el mensaje correspondiente. Utilizar un solo print, y pintar con colorama cada una de las opciones con un color diferente.


# print(
#     Fore.BLUE + '1 - Consultar saldo\n' +
#     Style.RESET_ALL +
#     Fore.GREEN + '2 - Depositar dinero\n'+
#     Style.RESET_ALL +
#     Fore.YELLOW + '3 - Extraer dinero\n'+
#     Style.RESET_ALL +
#     Fore.RED + '4 - Salir'+
#     Style.RESET_ALL 
# )
# menu = int(input('A que opcion quieres ingresar? '))

# match menu:
#     case 1:
#         print('Tu sueldo es de 100.000')
#     case 2:
#         int(input('Cuanto dinero quiere depositar? '))
#     case 3:
#         sacar = int(input('Cuanto dinero quiere extraer? '))
#         if sacar < 1 or sacar > 100000:
#             print('No tiene esa cantidad para sacar')
#         else:
#             print(f'Saco ${sacar}')
#     case 4:
#         print('Salio del programa')
#     case _:
#         print(Fore.RED + 'Opcion invalida'+ Style.RESET_ALL )


# # 3. Realizar un programa que pida dos números y una operación (suma, resta, multiplicación, división -tener en cuenta la división por cero-, resto o potencia). El programa debe realizar la operación correspondiente y mostrar el resultado. Si el resultado es positivo, se mostrará en verde, si es negativo en rojo y si es cero en azul.


# from colorama import Fore, Style

# numero_uno = int(input('Ingresa un numero: '))
# numero_dos = int(input('Ingresa otro numero: '))

# operacion = input('Ingresa una operacion matematica: ')

# hay_resultado = False

# if operacion == '/' and numero_dos == 0:
#     print('No es posible dividir por 0')
# else:
#     match operacion:
#         case '+':
#             resultado = numero_uno + numero_dos
#             hay_resultado = True
#         case '-':
#             resultado = numero_uno - numero_dos
#             hay_resultado = True
#         case '*':
#             resultado = numero_uno * numero_dos
#             hay_resultado = True
#         case '/':
#             resultado = numero_uno / numero_dos
#             hay_resultado = True
#         case '%':
#             resultado = numero_uno % numero_dos
#             hay_resultado = True
#         case '**':
#             resultado = numero_uno ** numero_dos
#             hay_resultado = True
#         case _:
#             print('Operacion matematica invalida')

# if hay_resultado:
#     if resultado > 0:
#         print(f'El resultado de los numeros ingresados es {Fore.GREEN}{resultado}{Style.RESET_ALL}')
#     elif resultado < 0:
#         print(f'El resultado de los numeros ingresados es {Fore.RED}{resultado}{Style.RESET_ALL}')
#     else:
#         print(f'El resultado de los numeros ingresados es {Fore.BLUE}{resultado}{Style.RESET_ALL}')


######################################################################################################################################

# #------------INTEGRADOR------------#

# # Un cine quiere implementar un sistema que permita calcular cuánto deberá pagar un cliente al comprar entradas para una función.
# # Todas las entradas tienen un precio de $8000.
# # El descuento dependerá de la cantidad de entradas compradas y del tipo de función elegida (solo se puede comprar un tipo por vez).
# # Los tipos de función pueden ser:

# # · "Estreno"
# # · "3D"
# # · "Tradicional"

# # Se aplicarán los siguientes descuentos:
# # · Si compra 7 o más entradas, obtiene un descuento del 45%.

# # · Si compra entre 5 y 6 entradas:
# # o Si la función es "Tradicional", obtiene un descuento del 35%.
# # o Si es "3D", obtiene un descuento del 30%.
# # o Si es "Estreno", obtiene un descuento del 25%.

# # · Si compra entre 3 y 4 entradas:
# # o Si la función es "Tradicional", obtiene un descuento del 20%.
# # o Si es "3D", obtiene un descuento del 15%.
# # o Si es "Estreno", obtiene un descuento del 10%.

# # · Si compra 1 o 2 entradas, no se aplica descuento.
# # Además, si el importe final con descuento supera los $18000, el cine aplica un descuento adicional del 5% por promoción especial.

# # Mostrar por pantalla

# # · Tipo de función
# # · Cantidad de entradas compradas
# # · Total a pagar sin descuento
# # · Descuento aplicado
# # · Descuento adicional (si corresponde)
# # · Total final a pagar


# ENTRADA = 8000
# descuento_adicional = 0.05

# funciones = input('Que funcion queres ver (Estreno, 3D, Tradicional)? ')
# boletos = int(input('Cuantas entradas va a comprar? '))

# descuento = 0  

# if boletos >= 7 :
#     descuento = 0.45
# elif boletos >= 5:
#     match funciones:
#         case 'Tradicional':
#             descuento = 0.35
#         case '3D':
#             descuento = 0.30
#         case 'Estreno':
#             descuento = 0.25
#         case _:  
#             descuento = 0
# elif boletos >= 3:
#     match funciones:
#         case 'Tradicional':
#             descuento = 0.20
#         case '3D':
#             descuento = 0.15
#         case 'Estreno':
#             descuento = 0.10
#         case _:  # 
#             descuento = 0

# valor_entrada = ENTRADA * boletos 

# descuento_aplicado = valor_entrada * descuento  
# importe_final = valor_entrada - descuento_aplicado  

# print(f'La funcion que usted va a ver es {funciones}')
# print(f'Compro {boletos} entradas')
# print(f'Total sin descuento: ${valor_entrada}')
# print(f'Descuento aplicado: ${descuento_aplicado}')  

# if importe_final > 18000:
#     descuento_extra = importe_final * descuento_adicional  
#     pago_total = importe_final - descuento_extra  
#     print(f'Descuento adicional: ${descuento_extra}')  
#     print(f'Total final a pagar: ${pago_total}')
# else:
#     print(f'Total final a pagar: ${importe_final}')