from colorama import Fore, Style, init

init()
# 1. Realizar un programa que muestre por terminal el mensaje: “Esto no anda, funciona”.
print('Esto no anda, funciona')

# 2. Realizar un programa que pida el ingreso del nombre de una persona por input y lo muestre con el formato: “Su nombre es: ___“
nombre = input('ingresa su nombre: ')

print(f'Su nombre es: {nombre}')

# 3. Realizar un programa que pida el ingreso del nombre y la edad de una persona por input. Mostrar la información con el siguiente formato: “Su nombre es: ____ y tiene: ___ años”. Utilizar colorama para mostrar el valor de las variables.

nombre = input('Ingresa su nombre: ')
edad = int(input('Ingresa su edad: '))

print(f'Mi nombre es: {Fore.GREEN}{nombre}{Style.RESET_ALL} y tengo: {Fore.GREEN}{edad}{Style.RESET_ALL} años')

# 4. Realizar un programa que pida el ingreso de la descripción de un producto y su precio. Mostrar los datos con el siguiente formato y con un solo print:

# Producto: Gaseosa

# Precio: $1500.00

producto = 'gaseosa'
precio = 1500

print(f'Si queres comprar una {producto} lo podes hacer por solo ${precio}')

# 5. Realizar un programa que permita el ingreso de dos números. Realizar la suma de los mismos y mostrar el resultado por pantalla con el siguiente formato: “La suma de los dos números es: ___”

numero_uno = int(input('Ingresa un numero: '))
numero_dos = int(input('Ingresa otro numero: '))

suma = numero_uno + numero_dos

print(f'La suma de los dos números es: {suma}')

# 6. Realizar un programa que permita el ingreso de dos números. Calcular la suma, resta, multiplicación y división de los mismos. Mostrar los resultados por pantalla. Utilizar una variable para mostrar el resultado (concatenar).

numero_uno = int(input('Ingresa un numero: '))
numero_dos = int(input('Ingresa otro numero: '))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_uno * numero_dos
division = numero_uno / numero_dos

resultado = "Suma: " + str(suma) + "\n" + "Resta: " + str(resta) + "\n" + "Multiplicación: " + str(multiplicacion) + "\n" + "División: " + str(division)

print(resultado)

# 7. Realizar un programa que pida dos números enteros. Calcular y mostrar el resto de la división entre ambos números. Ej.: "El resto de dividir 7 por 2 es: 1" .

numero_uno = int(input('Ingresa un numero: '))
numero_dos = int(input('Ingresa otro numero: '))

resto = numero_uno % numero_dos

print(f"El resto de los numeros ingresados es {resto}" )

# 8. Realizar un programa que a partir del ingreso de un sueldo (valor flotante) muestre dicho valor con un incremento del 15%.

sueldo = float(input('Ingrese su sueldo: '))
aumento = sueldo * 0.15
sueldo_final = sueldo + aumento

print(f'El sueldo final es {sueldo_final}')

# 9. Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.

sueldo = float(input('Ingrese su sueldo: '))
sueldo_aumento = float(input('Ingrese un porcentaje de aumento: '))
aumento = sueldo * (sueldo_aumento / 100)
sueldo_final = sueldo + aumento

print(f'El sueldo final es {sueldo_final}')

# 10. Realizar un programa que a partir del ingreso del importe de una compra, aplique un 25% de descuento. Mostrar por pantalla cuánto es el total a pagar y cuánto fue el descuento obtenido.

compra = int(input('Ingresa el valor de un producto: '))
descuento = compra * 0.25
pago_final = compra - descuento

print(f'El valor del producto es de ${compra} pero con su descuento vale ${pago_final}')


#####################################################################################################################################

#Integrador

bc = float(input("Ingresa el lado menor (BC) en cm: "))
cd = float(input("Ingresa diagonal menor (CD) en cm: "))
da = float(input("Ingresa el lado mayor (DA) en cm: "))

ab = bc + da

perimetro = 2 * bc + 2 * da
varillas = perimetro + cd + ab

area = (ab * cd) / 2

papel_total = area * 1.10

varillas_total = varillas * 10
papel_total = papel_total * 10

varillas_metros = varillas_total / 100
papel_metros = papel_total / 100

print(f"Metros de varillas necesarios: {varillas_metros}")
print(f"Metros de papel necesarios: {papel_metros}")