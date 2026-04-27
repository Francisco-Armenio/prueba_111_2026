# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:

# a. La suma acumulada de los números negativos.
# b. La suma acumulada de los números positivos.
# c. La cantidad de números negativos ingresados.
# d. El promedio de los números positivos.
# e. El número más chico.
# f. El número positivo más grande.
# g. El porcentaje de números negativos ingresados, respecto del total de ingresos.

seguir = 'si'
acumulador_negativos = 0
acumulador_positivos = 0
contador_negativos = 0
contador_positivos = 0
contador_general = 0
bandera_primer_ingreso = False
bandera_primer_positivo = False

while seguir == 'si':
    numero = int(input('ingrese un numero: '))
    #a.
    if numero < 0:
        acumulador_negativos += numero
        #c.
        contador_negativos += 1
    else:
        if numero > 0: #b.
            acumulador_positivos += numero #d.
            contador_positivos += 1 #d.
            #f.
            if contador_positivos == 1 or numero > maximo:
                maximo = numero

    if bandera_primer_ingreso == False or numero < minimo:
        minimo = numero
        bandera_primer_ingreso = True

    contador_general += 1
    seguir = input('desea ingresar otro numero?: ')

#PROCESOS
if contador_positivos > 0:
    proemdio_positivo = acumulador_positivos / contador_positivos
    print(proemdio_positivo)
else:
    print('No se pudo calcular el promedio de positivos (no se ingreso ningun positivo para hacerlo)')

#g.
porcentaje_negativos = (contador_negativos * 100) / contador_general
#SALIDAS

print(f'Porcentaje negativos: {porcentaje_negativos}%')