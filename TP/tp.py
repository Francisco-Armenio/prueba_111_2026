def pedir_entero (mensaje, minimo, maximo, mensaje_error):
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje_error))
    return numero

def pedir_flotante(mensaje, minimo, maximo, mensaje_error):
    numero = float(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = float(input(mensaje_error))
    return numero

def pedir_categoria(mensaje: str, opciones: list):  # TAREA
    bandera = False
    while bandera == False:
        seleccion = pedir_cadena(mensaje, 2)
        for i in range(len(opciones)):
            if seleccion == opciones[i]:
                bandera = True
                break
    return seleccion

def pedir_cadena(mensaje, minimo):
    cadena = input(mensaje)
    while len(cadena) < minimo:
        cadena = input(mensaje)
    return cadena

# ________ Calculos previos _________

def calcular_talle_promedio(contorno_ancho_cm: float, contorno_hombros_cm: float) -> float:
    talle_promedio = obtener_talle(contorno_ancho_cm + contorno_hombros_cm) / 2
    return talle_promedio

def calcular_brazo_torso (contorno_manga_cm: float, contorno_hombros_cm: float) -> float:
    relacion_brazo_torso = contorno_manga_cm / contorno_hombros_cm 
    return relacion_brazo_torso

# ________ Determinación de Talle ________

def obtener_talle(talle_promedio: float) -> str:
    # Categoria corporal
    if talle_promedio < 90:
        talle_final = "S"
    elif talle_promedio < 105:
        talle_final = "M"
    elif talle_promedio < 120:
        talle_final = "L"
    else:
        talle_final = "XL"
    return talle_final

#______ Porcentajes _______

def calcular_porcentajes(contador_clientes_total, contador_niños, contador_pre_adolescentes, 
                        contador_adolescentes, contador_adultos, contador_masculino, 
                        contador_femenino, contador_otro, contador_camiseta, 
                        contador_remera, contador_buzo, contador_deportivo, 
                        contador_casual, contador_formal):
    p_niños = (contador_niños / contador_clientes_total) * 100
    p_pre = (contador_pre_adolescentes / contador_clientes_total) * 100
    p_adolescentes = (contador_adolescentes / contador_clientes_total) * 100
    p_adultos = (contador_adultos / contador_clientes_total) * 100

    p_masc = (contador_masculino / contador_clientes_total) * 100
    p_fem  = (contador_femenino  / contador_clientes_total) * 100
    p_otro = (contador_otro / contador_clientes_total) * 100

    p_camisetas = (contador_camiseta / contador_clientes_total) * 100
    p_remeras = (contador_remera / contador_clientes_total) * 100
    p_buzos = (contador_buzo / contador_clientes_total) * 100

    p_deportivo = (contador_deportivo / contador_clientes_total) * 100
    p_casual = (contador_casual / contador_clientes_total) * 100
    p_formal = (contador_formal / contador_clientes_total) * 100
from colorama import Fore, Style
import math

seguir = "si"

contador_clientes_total = 0
contador_niños = 0
contador_pre_adolescentes = 0   

contador_adolescentes = 0
contador_adultos = 0

contador_masculino = 0
contador_femenino = 0
contador_otro = 0

contador_camiseta = 0
contador_remera = 0
contador_buzo = 0

contador_deportivo = 0
contador_casual = 0
contador_formal = 0

contador_masc_deportivo = 0
contador_fem_formal = 0
contador_otro_casual = 0

contador_recomendaciones = 0
cont_rec_hoodie = 0
cont_rec_pima = 0
cont_rec_crop = 0
cont_rec_dryfit = 0
cont_rec_buzo_especial = 0
cont_rec_manga_larga = 0
cont_rec_infantil = 0
cont_rec_unisex = 0
cont_rec_camisa_formal = 0
cont_rec_ranglan = 0
cont_rec_buzo_blazer = 0
cont_rec_estandar = 0

suma_edades = 0
sacar_promedio = 0

maximo_nombre_condicionado = None
maximo_edad_condicionado = None
maximo_genero_condicionado = None
maximo_tipo_prenda_condicionado = None
maximo_estilo_condicionado = None
maximo_color_condicionado = None

bandera_menor = True
bandera_mayor = True
bandera_mayor_condicionado = True

while seguir == "si":
# ______ Datos de entradas del cliente  __________________________________________
    nombre = input("Ingrese el nombre del cliente: ")

    edad = pedir_entero("Ingrese su edad: " ,1,100, f"{Fore.RED}Error, reingrese la edad:{Style.RESET_ALL}")

    genero = input("Ingrese su género (masculino / femenino / otro): ")
    while genero != "masculino" and genero != "femenino" and genero != "otro":
            genero = input(f"{Fore.RED}ERROR, reingrese su genero:{Style.RESET_ALL} ")

    tipo_prenda = input("Ingrese tipo de prenda que busque (camiseta / remera / buzo): ")
    while tipo_prenda != "camiseta" and tipo_prenda != "remera" and tipo_prenda != "buzo":
            tipo_prenda = input(f"{Fore.RED}ERROR, reingrese otro tipo de prenda:{Style.RESET_ALL} ")

    estilo_de_ropa = input("Ingrese su estilo de ropa (deportivo / casual / formal): ")
    while estilo_de_ropa != "deportivo" and estilo_de_ropa != "casual" and estilo_de_ropa != "formal":
            estilo_de_ropa = input(f"{Fore.RED}ERROR, ingrese otro estilo de ropa:{Style.RESET_ALL} ")

    color = input("Ingrese el color que busque de prenda: ")

    contorno_manga_cm = pedir_flotante("Ingrese el largo de brazo en centímetros: ",1,200, f"{Fore.RED}Error, reingrese su largo de brazo:{Style.RESET_ALL}  ")

    contorno_ancho_cm = pedir_flotante("Ingrese su contorno de ancho en centímetros: ",1,200, f"{Fore.RED}Error, reingrese su ancho:{Style.RESET_ALL}  ")

    contorno_largo_cm = pedir_flotante("Ingrese el largo de torso en centímetros: ",1,200, f"{Fore.RED}Error, reingrese su largo de torso:{Style.RESET_ALL}  ")

    contorno_hombros_cm = pedir_flotante("Ingrese su ancho de hombros en centímetros: ",1,200, f"{Fore.RED}Error, reingrese su contorno de hombros:{Style.RESET_ALL}  ")

    # ________ Rango de edad _________
    if edad < 10:
        rango_etario = "Niño"
        contador_niños += 1
    elif edad < 13:
        rango_etario = "Pre-adolescente"
        contador_pre_adolescentes += 1
    elif edad <= 17:
        rango_etario = "Adolescente"
        contador_adolescentes += 1
    else:
        rango_etario = "Adulto"
        contador_adultos += 1

    contador_clientes_total += 1
    suma_edades += edad

    # ______ Minimo general _______
    if bandera_menor == True or edad < minimo_edad:
        minimo_nombre = nombre
        minimo_edad = edad
        minimo_genero = genero
        minimo_tipo_prenda = tipo_prenda
        minimo_estilo = estilo_de_ropa
        minimo_color = color
        bandera_menor = False
    
    # ______ Maximo general _______
    if bandera_mayor == True or edad > maximo_edad:
        maximo_nombre = nombre
        maximo_edad = edad
        maximo_genero = genero
        maximo_tipo_prenda = tipo_prenda
        maximo_estilo = estilo_de_ropa
        maximo_color = color
        bandera_mayor = False

    # _______ Maximo Condicional _______
    # CONTEOS
    # match genero:
    #     case "masculino":
    #         contador_masculino += 1
    #         if tipo_prenda == "remera" and estilo_de_ropa == "casual":
    #             if bandera_mayor_condicionado == True or edad > maximo_edad_condicionado:
    #                 maximo_nombre_condicionado = nombre
    #                 maximo_edad_condicionado = edad
    #                 maximo_genero_condicionado = genero
    #                 maximo_tipo_prenda_condicionado = tipo_prenda
    #                 maximo_estilo_condicionado = estilo_de_ropa
    #                 maximo_color_condicionado = color
    #                 bandera_mayor_condicionado = False
    #         if estilo_de_ropa == "deportivo":
    #             contador_masc_deportivo += 1
    #     case "femenino": # Y saco promedio condicional
    #         contador_femenino += 1
    #         if tipo_prenda != "buzo" and estilo_de_ropa != "casual":
    #             sacar_promedio += 1
    #         else:
    #             promedio_condicionado = None
    #         if estilo_de_ropa == "formal":
    #             contador_fem_formal += 1
    #     case "otro": 
    #         contador_otro += 1
    #         if estilo_de_ropa == "casual":
    #             contador_otro_casual += 1

    def contar_genero(genero, contador_masculino, contador_femenino, contador_otro):
        match genero:
            case "masculino":
                contador_masculino += 1
            case "femenino":
                contador_femenino += 1
            case _:
                contador_otro += 1

        return contador_masculino, contador_femenino, contador_otro
    
    def contar_estilo(genero, estilo, contador_masc_deportivo, contador_fem_formal, contador_otro_casual):
        if genero == "masculino" and estilo == "deportivo":
            contador_masc_deportivo += 1
        elif genero == "femenino" and estilo == "formal":
            contador_fem_formal += 1
        elif genero == "otro" and estilo == "casual":
            contador_otro_casual += 1

        return contador_masc_deportivo, contador_fem_formal, contador_otro_casual
    

    def calcular_maximo_condicionado(genero, tipo_prenda, estilo, edad, nombre, color,
                                bandera, max_edad,
                                max_nombre, max_genero, max_prenda, max_estilo, max_color):

        if genero == "masculino" and tipo_prenda == "remera" and estilo == "casual":
            if bandera or edad > max_edad:
                max_nombre = nombre
                max_edad = edad
                max_genero = genero
                max_prenda = tipo_prenda
                max_estilo = estilo
                max_color = color
                bandera = False

        return bandera, max_edad, max_nombre, max_genero, max_prenda, max_estilo, max_color


    def contar_prenda(tipo_prenda, contador_camiseta, contador_remera, contador_buzo):
        match tipo_prenda:
            case "camiseta":
                contador_camiseta += 1
            case "remera":
                contador_remera += 1
            case "buzo":
                contador_buzo += 1

        return contador_camiseta, contador_remera, contador_buzo

    def contar_estilo(estilo_de_ropa, contador_deportivo, contador_casual, contador_formal):
        match estilo_de_ropa:
            case "deportivo":
                contador_deportivo += 1
            case "casual":
                contador_casual += 1
            case "formal":
                contador_formal += 1

        return contador_deportivo, contador_casual, contador_formal

    # ________ 12 reglas de recomendacion _________
    if rango_etario == "Adolescente" and tipo_prenda == "buzo" and estilo_de_ropa != "formal":
        recomendacion = "Buzo Hoodie Oversize con estampa urbana"
        justificacion = "Ideal para el estilo relajado y no formal típico de tu franja etaria."
        cont_rec_hoodie +=1

    elif rango_etario == "Adulto" and estilo_de_ropa == "formal" and tipo_prenda == "camiseta":
        recomendacion = "Camiseta de vestir de algodón pima, corte recto"
        justificacion = "El corte recto y la tela premium se adaptan a ambientes formales."
        cont_rec_pima +=1

    elif genero == "femenino" and estilo_de_ropa == "casual" and tipo_prenda == "remera" and obtener_talle in ("S", "M"):
        recomendacion = "Remera crop fit con detalle en cuello"
        justificacion = "El corte crop realza la silueta en talles estándar con un look casual y moderno."
        cont_rec_crop +=1

    elif genero == "masculino" and estilo_de_ropa == "deportivo" and tipo_prenda == "camiseta":
        recomendacion = "Camiseta deportiva dry-fit con tecnología transpirable"
        justificacion = "Diseñada para el rendimiento físico y la comodidad en movimiento."
        cont_rec_dryfit +=1

    elif obtener_talle and tipo_prenda == "buzo" and estilo_de_ropa == "casual":
        recomendacion = "Buzo amplio de felpa con capucha reforzada, talle especial"
        justificacion = "El corte amplio garantiza comodidad y libertad de movimiento en talles grandes."
        cont_rec_buzo_especial +=1

    elif calcular_brazo_torso > 1.3 and tipo_prenda == "remera":
        recomendacion = "Remera de manga larga con puño elastizado"
        justificacion = "Tu proporción brazo/torso indica brazos largos; las mangas ajustables evitan que suban."
        cont_rec_manga_larga +=1

    elif rango_etario == "Niño" and estilo_de_ropa == "deportivo":
        recomendacion = "Conjunto deportivo infantil con tela flexible"
        justificacion = "Las prendas infantiles deportivas priorizan libertad de movimiento y durabilidad."
        cont_rec_infantil +=1

    elif rango_etario == "Pre-adolescente" and estilo_de_ropa == "casual" and genero == "otro":
        recomendacion = "Remera unisex de algodón con print geométrico"
        justificacion = "El diseño neutro y cómodo es perfecto para la etapa de pre-adolescencia."
        cont_rec_unisex +=1

    elif rango_etario == "Adulto" and obtener_talle and estilo_de_ropa == "formal":
        recomendacion = "Camisa de vestir structured fit en talle especial"
        justificacion = "El corte structured compensa proporciones amplias manteniendo la elegancia formal."
        cont_rec_camisa_formal +=1

    elif calcular_brazo_torso < 0.85 and tipo_prenda == "buzo":
        recomendacion = "Buzo con manga 3/4 o manga ranglán"
        justificacion = "La manga ranglán visualmente alarga el brazo cuando la proporción brazo/torso es corta."
        cont_rec_ranglan +=1

    elif genero == "femenino" and estilo_de_ropa == "formal" and tipo_prenda == "buzo":
        recomendacion = "Buzo blazer de punto fino, color neutro"
        justificacion = "Combina la comodidad del buzo con la sobriedad formal requerida."
        cont_rec_buzo_blazer +=1

    else:
        recomendacion = "Prenda estándar según tus medidas y preferencias"
        justificacion = "Tu combinación de características es versátil; optamos por una prenda equilibrada."
        cont_rec_estandar +=1

    contador_recomendaciones +=1
    # _____________________________________________
    seguir = input("Desea ingresar otro cliente?: (si/no) ")
    while seguir != "si" and seguir != "no":
        seguir = input (f"{Fore.RED}Error, ingrese: (si/no){Style.RESET_ALL} ")

    #__________ Salidas por cada cliente _______________
    print(f"{Fore.BLUE}Cliente: {nombre}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Edad: {edad} años == {rango_etario}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Genero: {genero}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Tipo de prenda: {tipo_prenda}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Estilo: {estilo_de_ropa}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Color de la prenda: {color}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Talle: {obtener_talle}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Prenda sugerida: {recomendacion}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Razon: {justificacion}{Style.RESET_ALL}")
# _______ Promedio general _______
promedio_edad = suma_edades / contador_clientes_total

# _______ Promedio condicionado ________
promedio_condicionado = sacar_promedio / contador_femenino if contador_femenino > 0 else 0

#______ Porcentajes _______

p_niños, p_pre, p_adolescentes, p_adultos, p_masc, p_fem, p_otro, p_camisetas, p_remeras, p_buzos, p_deportivo, p_casual, p_formal = calcular_porcentajes(
    contador_clientes_total, contador_niños, contador_pre_adolescentes,
    contador_adolescentes, contador_adultos, contador_masculino,
    contador_femenino, contador_otro, contador_camiseta,
    contador_remera, contador_buzo, contador_deportivo,
    contador_casual, contador_formal)

#______ Porcentajes condicionales _______

# DESPUÉS (con protección)
p_masc_deportivo = (contador_masc_deportivo / contador_masculino) * 100 if contador_masculino > 0 else 0
p_fem_formal = (contador_fem_formal / contador_femenino) * 100 if contador_femenino > 0 else 0
p_otro_casual = (contador_otro_casual / contador_otro) * 100 if contador_otro > 0 else 0

#__________ Salidas finales _______________
#PROMEDIO GENERAL Y PROMEDIO CONDICIONADO
if contador_clientes_total > 0:
    print(f"Promedio de edad: {promedio_edad}")
else:

    print (f"{Fore.RED}Sin datos del promedioo de edad{Style.RESET_ALL}")
if contador_clientes_total > 0:
    print(f"Promedio de gente femenina que haya comprado buzo casual: {promedio_condicionado}")
else:
    print (f"{Fore.RED}Promedio de gente femenina que haya comprado buzo casual: 0 %{Style.RESET_ALL} ")
#PORCENTAJES GENERALES
if contador_clientes_total > 0:
    print(f"Porcentajes de edades: Niños {p_niños:.0f}%, Pre-adolescentes {p_pre:.0f}%, Adolescentes {p_adolescentes:.0f}%, Adultos {p_adultos:.0f}%")
else:
    
    print(f"{Fore.RED}Sin datos del porcentaje de edades{Style.RESET_ALL}")
if contador_clientes_total > 0:
    print(f"Porcentajes de generos: Masculinos {p_masc:.0f}%, Femeninos {p_fem:.0f}%, Otros {p_otro:.0f}%")
else:

    print(f"{Fore.RED}Sin datos del porcentaje de generos{Style.RESET_ALL}")
if contador_clientes_total > 0:
    print(f"Porcentajes de tipos de prenda: Camisetas {p_camisetas:.0f}%, Remeras {p_remeras:.0f}%, Buzos {p_buzos:.0f}%")
else:
    print(f"{Fore.RED}Sin datos del porcentaje de tipos de prenda{Style.RESET_ALL}")
if contador_clientes_total > 0:
    print(f"Porcentajes de estilos: Deportivo {p_deportivo:.0f}%, Casual {p_casual:.0f}%, Formal {p_formal:.0f}%")
else:
    print(f"{Fore.RED}Sin datos del porcentaje de estilos{Style.RESET_ALL}")
#PORCENTAJES CONDICIONADOS
if contador_masculino > 0:
    print(f"Del total de hombres, el {p_masc_deportivo:.0f}% prefiere estilo deportivo.")
else:
    print(f"{Fore.RED}Sin datos del total de hombres que prefiere estilo deportivo{Style.RESET_ALL}")
if contador_femenino > 0:
    print(f"Del total de mujeres, el {p_fem_formal:.0f}% prefiere estilo formal.")
else:
    print(f"{Fore.RED}Sin datos del total de mujeres que prefiere estilo formal{Style.RESET_ALL}")
if contador_otro > 0:
    print(f"Del total de los demas generos, el {p_otro_casual:.0f}% prefiere estilo casual.")
else:
    print(f"{Fore.RED}Sin datos del total de los demas generos{Style.RESET_ALL}")
#MINIMO GENERAL MAXIMO GENERAL MAXIMO CONDICIONADO
if contador_clientes_total > 0:
    print(f" ______ Los datos de la edad minima: ______ ")
    print(f" Nombre: {minimo_nombre} \nEdad: {minimo_edad} \nGenero: {minimo_genero} \nTipo de prenda: {minimo_tipo_prenda} \nEstilo: {minimo_estilo} \nColor: {minimo_color}")
else:
    print(f"{Fore.RED}Sin datos de la edad minima{Style.RESET_ALL}")
if contador_clientes_total > 0:
    print(f" ______ Los datos de la edad maxima: ______ ")
    print(f" Nombre: {maximo_nombre} \nEdad: {maximo_edad} \nGenero: {maximo_genero} \nTipo de prenda: {maximo_tipo_prenda} \nEstilo: {maximo_estilo} \nColor: {maximo_color}")
else:
    print(f"{Fore.RED}Sin datos de la edad maxima{Style.RESET_ALL}")
if maximo_nombre_condicionado is not None:
    print(f" ______ Los datos del masculino de mayor edad que llevo remera casual: ______ ")
    print(f" Nombre: {maximo_nombre_condicionado} \nEdad: {maximo_edad_condicionado} \nGenero: {maximo_genero_condicionado} \nTipo de prenda: {maximo_tipo_prenda_condicionado} \nEstilo: {maximo_estilo_condicionado} \nColor: {maximo_color_condicionado}")
else:
    print(f"{Fore.RED}No hay masculino que haya llevado remera casual{Style.RESET_ALL}")

print("FRECUENCIA DE RECOMENDACIONES ENTREGADAS")
if contador_recomendaciones > 0:
    print(f"1. Buzo Hoodie Oversize: {cont_rec_hoodie}")
    print(f"2. Camiseta Algodón Pima: {cont_rec_pima}")
    print(f"3. Remera Crop Fit: {cont_rec_crop}")
    print(f"4. Camiseta Dry-Fit: {cont_rec_dryfit}")
    print(f"5. Buzo Talle Especial: {cont_rec_buzo_especial}")
    print(f"6. Remera Manga Larga: {cont_rec_manga_larga}")
    print(f"7. Conjunto Infantil: {cont_rec_infantil}")
    print(f"8. Remera Unisex: {cont_rec_unisex}")
    print(f"9. Camisa Formal Especial: {cont_rec_camisa_formal}")
    print(f"10. Buzo Manga Ranglán: {cont_rec_ranglan}")
    print(f"11. Buzo Blazer: {cont_rec_buzo_blazer}")
    print(f"12. Prenda Estándar: {cont_rec_estandar}")
    print(f"Total de recomendaciones: {contador_recomendaciones}")
else:
    print("No se procesaron recomendaciones.")

# Grafico de barras por consola ________


recomendaciones_dict = {
"Hoodie Oversize": cont_rec_hoodie,
"Camiseta Pima": cont_rec_pima,
"Remera Crop Fit" : cont_rec_crop,
"Camiseta Dry-Fit": cont_rec_dryfit,
"Buzo T. Especial": cont_rec_buzo_especial,
"Remera M. Larga": cont_rec_manga_larga,
"Conjunto Infantil": cont_rec_infantil,
"Remera Unisex" : cont_rec_unisex,
"Camisa Formal": cont_rec_camisa_formal,
"Buzo Ranglán": cont_rec_ranglan,
"Buzo Blazer": cont_rec_buzo_blazer,
"Prenda Estándar": cont_rec_estandar,
}

ESCALA = 5  # Cada █ representa 1 cliente (ajustable)

maximo_valor = max(recomendaciones_dict.values()) if recomendaciones_dict else 1

for nombre_rec, cantidad in recomendaciones_dict.items():
    barra = "█" * cantidad
    # Color según popularidad
    if cantidad == maximo_valor and cantidad > 0:
        color_barra = Fore.YELLOW
    elif cantidad > 0:
        color_barra = Fore.CYAN
    else:
        color_barra = Fore.RED

    print(f"{nombre_rec:<20} | {color_barra}{barra:<{maximo_valor}}{Style.RESET_ALL} {cantidad}")

print(f"{'(Amarillo = más recomendada)':<40}")