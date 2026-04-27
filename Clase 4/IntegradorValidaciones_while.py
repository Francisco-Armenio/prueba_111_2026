# A partir de los datos del integrador de validaciones, ingresar datos de personas hasta que el usuario lo desee y calcular:

# · Apellido
# · Edad, entre 18 y 90 años inclusive.
# · Estado civil: “Soltero”,” Casado”, “Divorciado” o “Viudo”.
# · Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# a. Cantidad de personas cuya edad esta entre 25 y 40.
# b. Porcentaje de personas de cada estado civil.
# c. Promedio de edades de los casados.
# d. Datos de la persona más joven.
# e. Datos de la persona viuda con mayor edad.

seguir = 'si'
contador_edad_2540 = 0
contador_solteros = 0
contador_casados = 0
contador_divorciados = 0
contador_viudo = 0
contador_personas = 0
acumulador_edades_casados = 0  

bandera_primer_persona = True


while seguir == 'si':
    #Ingreso de datos
    apellido = input('ingresa el apellido: ')
    edad = int(input('ingrese la edad: '))
    while edad < 18 or edad > 90:
        edad = int(input('Error: reingrese la edad: '))
    estado_civil = input('Ingrese el estado civil: ')


    while estado_civil != 'Soltero' and estado_civil != 'casado' and estado_civil != 'divorciado' and estado_civil != 'viudo':
        estado_civil = int(input('Error: reingrese su estado civil: '))

    legajo = int(input('Ingrese el legajo:'))
    while legajo < 1000 or legajo > 9999:
        legajo = int(input('Error: reingrese su legajo:'))


#STATS
#a.
    if edad >= 25 and edad <= 40:
        contador_edad_2540 += 1

#b.
    match estado_civil:
        case 'casado':
            contador_casados += 1
            acumulador_edades_casados += edad
        case 'divorsiado':
            contador_casados += 1
        case 'soltero':
            contador_casados += 1
        case 'viudo':
            contador_casados += 1
            #e.
            if contador_viudo == 1 or edad > maxima_edad:
                maxima_edad = edad
                maxima_apellido = apellido
                maxima_estado = legajo
    
#d.
    if bandera_primer_persona == True or edad < minima_edad:
        minima_edad = edad
        minimo_apellido = apellido
        minimo_estado = estado_civil
        minimo_estado = legajo
        bandera_primer_persona = False



    seguir = input('Ingresa otra persona? (si/no): ')
    while seguir != 'si' and seguir != 'no':
        seguir = input('Error, ingrese si/no')


#procesos que no se repiten

contador_personas = contador_casados + contador_solteros + contador_viudo + contador_divorciados

porcentaje_casados = (contador_casados * 100) / contador_personas
porcentaje_solteros = (contador_solteros * 100) / contador_personas
porcentaje_divorsiados = (contador_divorciados * 100) / contador_personas
porcentaje_viudos = (contador_viudo * 100) / contador_personas



#SALIDA
print(contador_edad_2540)
if contador_viudo > 0:
    print(maxima_apellido)
if contador_casados > 0:
    promedio_edad_casados = acumulador_edades_casados / contador_casados
    print(promedio_edad_casados)
else:
    print('No se puede calcular el promedio')