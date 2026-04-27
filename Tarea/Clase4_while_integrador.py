#1_ Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

repeticiones = 0 #cuentas cuantas repeticiones hizo el while (variable de control del while)

while repeticiones < 10:
    print(f'{repeticiones + 1}')

    repeticiones = repeticiones + 1 #Modifica la variable de control


#2_ Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

repeticiones = 11

while repeticiones > 1:
    print(f'{repeticiones - 1}')

    repeticiones = repeticiones - 1

#3_ Mostrar la suma de los números desde el 1 hasta el 10.

i = 0 
suma = 0
while i < 10: #0 - 9
    i = i + 1
    suma = suma + i

print(suma)

#4_ Mostrar la suma de los números pares desde el 1 hasta el 10

i = 0 
suma = 0
while i < 10: #0 - 9 -> 1 - 10
    i = i + 1
    if i % 2 == 0:
        suma = suma + i
print(suma)

#5_ Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

i = 0 
suma = 0
while i < 5: 
    numero = int(input('Ingresa un numero: '))
    suma = suma + numero
    i = i + 1
    promedio = suma / 5

print(suma)
print(promedio)

# 6_ Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de estos.
#OPCION 1
seguir = 's'
suma = 0
contador = 0

while seguir == 's':
    numero = int(input('Ingresa un numero: '))
    suma += numero
    contador += 1

    seguir = input('Desea ingresar otro numero? ').lower()

if contador > 0:
    promedio = suma / contador
else:
    promedio = 0

print(f'Suma: {suma}')
print(f'Promedio: {promedio}')

# OPCION 2
bandera = True
suma = 0
contador = 0
while bandera == True:
    numero = int(input('ingrese un numero: '))
    suma += numero

    contador += 1
    seguir = input('desea ingresar otro numero (s/n)')
    if seguir == 'n':
        bandera = False
promedio = suma / contador

print (f'{suma}')
print (f'{promedio}')


# 7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
seguir = 'si'
suma = 0
producto = 1

while seguir == 'si':
    numero = int(input('ingrese un numero: '))

    if numero > 0:
        suma += numero
    elif numero < 0:
        producto *= numero

    seguir = input('Desea seguir agregando numeros? ')

print(f'Suma de positivos: {suma}')
print(f'Producto de negativos: {producto}')


#8_ Ingresar 10 números enteros. Determinar el máximo y el mínimo.

i = 0

while i < 5:
    numero = int(input('ingresa un numero: '))

    ###### Inicializacion max y min ######
    if i == 0:
        maximo = numero
        minimo = numero 
    else:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    i += 1

print(f'MAX: {maximo}')
print(f'MIN: {minimo}')


# 9. Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de estos.

i = 0
suma = 0 

while i < 5:
    numero = int(input('ingresa un numero: '))
    suma += numero
    i += 1

promedio = suma / 5

print(f'Suma: {suma}')
print(f'Promedio: {promedio}')



# 10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de estos.

i = 0
suma = 0
seguir = 'si'

while i < 10 and seguir == 'si':
    numero = int(input('ingresa un numero: '))
    suma += numero
    i += 1

    if i >= 5:
        seguir = input('Desea seguir agregando numeros? ')

promedio = suma / i

print(f'Suma: {suma}')
print(f'Promedio: {promedio}')


######################################################################################################################################

##------------INTEGRADOR------------##

# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado.

# Las tecnologías en evaluación son: 
# 🔹 Inteligencia Artificial (IA) 
# 🔹 Realidad Virtual/Aumentada (RV/RA) 
# 🔹 Internet de las Cosas (IOT)

# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.

# 🔹 Recolección de Datos
# Cada empleado encuestado deberá proporcionar la siguiente información: 
# ✔️ Nombre 
# ✔️ Edad (debe ser 18 años o más) 
# ✔️ Género (Masculino, Femenino, Otro) 
# ✔️ Tecnología elegida (IA, RV/RA, IOT)
# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.

# 🔹 Análisis de Datos
# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1. Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
# 2. Porcentaje de empleados que NO votaron por IA, siempre y cuando su género no sea femenino y su edad está entre los 33 y 40 años.
# 3. Nombre y apellido del empleado de menor edad.
# 4. Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.
# 5. Realizar un gráfico de barras verticales para visualizar la cantidad de empleados que eligió cada tecnología. Por ejemplo:
# 6. Realizar un gráfico de termómetro para determinar el porcentaje total de empleados de género masculino, sobre el total. Por ejemplo:

# 🔹 Requisitos del Programa
# ✔️ Los datos deben solicitarse y validarse correctamente. 
# ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis. 
# ✔️ Presentar los resultados de manera clara y organizada.

contador_IA = 0
contador_RV_RA = 0
contador_IOT = 0
contador_masculino = 0
contador_femenino = 0
contador_otro = 0

primer_ingreso = True
edad_minima = 0
nombre_menor = ""

primer_masculino = True
edad_max = 0
nombre_mayor = ""
tecnologia_mayor = ""

repeticiones = 0

while repeticiones < 2:
    nombre = input('Ingrese su nombre y apellido: ')
    
    edad = int(input('Ingrese su edad: '))
    while edad < 18:
        edad = int(input('El usuario no es mayor de edad. Reingrese su edad: '))
    
    genero = input('Ingrese su genero (Masculino, Femenino, Otro): ')
    while genero != 'Masculino' and genero != 'Femenino' and genero != 'Otro':
        genero = input("ERROR. Reingrese su genero: ")
    
    tecnologia = input('Ingrese una tecnologia (IA, RV/RA, IOT): ')
    while tecnologia != 'IA' and tecnologia != 'RV/RA' and tecnologia != 'IOT':
        tecnologia = input('Tecnologia no encontrada. Ingrese otra tecnologia valida: ')

    match genero:
        case 'Masculino':
            contador_masculino += 1
            if primer_masculino or edad > edad_max:
                edad_max = edad
                nombre_mayor = nombre
                tecnologia_mayor = tecnologia
                primer_masculino = False
        case 'Femenino':
            contador_femenino += 1
        case 'Otro':
            contador_otro += 1

    match tecnologia:
        case 'IA':
            contador_IA += 1
        case 'RV/RA':
            contador_RV_RA += 1
        case 'IOT':
            contador_IOT += 1

    if primer_ingreso or edad < edad_minima:
        edad_minima = edad
        nombre_menor = nombre
        primer_ingreso = False

    repeticiones += 1

print(f"Empleado más joven: {nombre_menor}")

if primer_masculino == False:
    print(f"Masculino de mayor edad: {nombre_mayor} - {tecnologia_mayor}")








