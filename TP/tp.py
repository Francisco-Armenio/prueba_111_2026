#• 1 promedio general. Listo
#• 1 promedio condicionado.
#• 1 máximo general. Listo
#• 1 máximo condicionado por varias variables.  Listo
#• 1 mínimo (puede ser condicionado o no).  Listo
#• 1 conteo de frecuencia de recomendaciones. 
#• Porcentajes (no condicionados y condicionados) 
#• 1 gráfico presentado por consola
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

suma_edades = 0

bandera_menor = True
bandera_mayor = True
bandera_mayor_condicionado = True

while seguir == "si":
# ______ Datos de entradas del cliente  __________________________________________
    nombre = input("Ingrese el nombre del cliente: ")
    color = input("Ingrese el color que busque de prenda: ")
    edad = int(input("Ingrese su edad: "))
    while edad < 1 or edad > 100: 
        edad = int(input(f"{Fore.RED}Error, reingrese la edad:{Style.RESET_ALL}  "))
    contorno_manga_cm = float(input("Ingrese el largo de brazo en centímetros: "))
    contorno_ancho_cm = float(input("Ingrese su contorno de ancho en centímetros: "))
    contorno_largo_cm = float(input("Ingrese el largo de torso en centímetros: "))
    contorno_hombros_cm = float(input("Ingrese su ancho de hombros en centímetros: "))
    genero = input("Ingrese su género (masculino / femenino / otro): ")
    while genero != "masculino" and genero != "femenino" and genero != "otro":
            genero = input(f"{Fore.RED}ERROR, reingrese su genero:{Style.RESET_ALL} ")
    tipo_prenda = input("Ingrese tipo de prenda que busque (camiseta / remera / buzo): ")
    while tipo_prenda != "camiseta" and tipo_prenda != "remera" and tipo_prenda != "buzo":
            tipo_prenda = input(f"{Fore.RED}ERROR, reingrese otro tipo de prenda:{Style.RESET_ALL} ")
    estilo_de_ropa = input("Ingrese su estilo de ropa (deportivo / casual / formal): ")
    while estilo_de_ropa != "deportivo" and estilo_de_ropa != "casual" and estilo_de_ropa != "formal":
            estilo_de_ropa = input(f"{Fore.RED}ERROR, ingrese otro estilo de ropa:{Style.RESET_ALL} ")

    # ________ Calculos previos _________
    talle_promedio = (contorno_ancho_cm + contorno_hombros_cm) / 2
    relacion_brazo_torso = contorno_manga_cm / contorno_largo_cm
    es_talle_grande = talle_promedio > 100 # HAY QUE ARREGLAR ESTO PORQUE PUSIMOS TALLES XL Y ARREGLAR RECOMENDACIONES

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
        bandera_menor = False
    
    # ______ Maximo general _______
    if bandera_mayor == True or edad > maximo_edad:
        maximo_nombre = nombre
        maximo_edad = edad
        maximo_genero = genero
        maximo_tipo_prenda = tipo_prenda
        maximo_estilo = estilo_de_ropa
        bandera_mayor = False

    # _______ Maximo Condicional _______
    # CONTEOS
    match genero:
        case "masculino":
            contador_masculino += 1
            if tipo_prenda == "remera" and estilo_de_ropa == "casual":
                maximo_nombre = nombre
                if bandera_mayor_condicionado == True or edad > maximo_edad_condicionado:
                    maximo_nombre_condicionado = nombre
                    maximo_edad_condicionado = edad
                    maximo_genero_condicionado = genero
                    maximo_tipo_prenda_condicionado = tipo_prenda
                    maximo_estilo_condicionado = estilo_de_ropa
                    bandera_mayor_condicionado = False
        case "femenino": 
            contador_femenino += 1
        case "otro": 
            contador_otro += 1

    match tipo_prenda:
        case "camiseta":
            contador_camiseta += 1
        case "remera":
            contador_remera += 1
        case "buzo":
            contador_buzo += 1

    match estilo_de_ropa:
        case "deportivo":
            contador_deportivo += 1
        case "casual":
            contador_casual += 1
        case "formal":
            contador_formal += 1

    # ________ Determinación de Talle ________
    if talle_promedio < 90:
        talle_final = "S"
        if contorno_largo_cm > 70:
            print("Aviso: El talle S puede quedarte corto de largo debido a tu altura.")
    elif talle_promedio <= 105:
        talle_final = "M"
        if contorno_largo_cm > 75: 
            print("Aviso: El talle M puede quedarte corto de largo debido a tu altura.")
    elif talle_promedio <= 120:
        talle_final = "L"
    else:
        talle_final = "XL"

    # _______ Promedio general _______
    promedio_edad = suma_edades / contador_clientes_total
    
    # _______ Promedio condicionado ________
    # Femenina buzo casual



    #______ Porcentajes _______


    # ________ 12 reglas de recomendacion _________

    if rango_etario == "Adolescente" and tipo_prenda == "buzo" and estilo_de_ropa != "formal":
        recomendacion = "Buzo Hoodie Oversize con estampa urbana"
        justificacion = "Ideal para el estilo relajado y no formal típico de tu franja etaria."

    elif rango_etario == "Adulto" and estilo_de_ropa == "formal" and tipo_prenda == "camiseta":
        recomendacion = "Camiseta de vestir de algodón pima, corte recto"
        justificacion = "El corte recto y la tela premium se adaptan a ambientes formales."

    elif genero == "femenino" and estilo_de_ropa == "casual" and tipo_prenda == "remera" and not es_talle_grande:
        recomendacion = "Remera crop fit con detalle en cuello"
        justificacion = "El corte crop realza la silueta en talles estándar con un look casual y moderno."

    elif genero == "masculino" and estilo_de_ropa == "deportivo" and tipo_prenda == "camiseta":
        recomendacion = "Camiseta deportiva dry-fit con tecnología transpirable"
        justificacion = "Diseñada para el rendimiento físico y la comodidad en movimiento."

    elif es_talle_grande and tipo_prenda == "buzo" and estilo_de_ropa == "casual":
        recomendacion = "Buzo amplio de felpa con capucha reforzada, talle especial"
        justificacion = "El corte amplio garantiza comodidad y libertad de movimiento en talles grandes."

    elif relacion_brazo_torso > 1.3 and tipo_prenda == "remera":
        recomendacion = "Remera de manga larga con puño elastizado"
        justificacion = "Tu proporción brazo/torso indica brazos largos; las mangas ajustables evitan que suban."


    elif rango_etario == "Niño" and estilo_de_ropa == "deportivo":
        recomendacion = "Conjunto deportivo infantil con tela flexible"
        justificacion = "Las prendas infantiles deportivas priorizan libertad de movimiento y durabilidad."

    elif rango_etario == "Pre-adolescente" and estilo_de_ropa == "casual" and genero == "unisex":
        recomendacion = "Remera unisex de algodón con print geométrico"
        justificacion = "El diseño neutro y cómodo es perfecto para la etapa de pre-adolescencia."

    elif rango_etario == "Adulto" and es_talle_grande and estilo_de_ropa == "formal":
        recomendacion = "Camisa de vestir structured fit en talle especial"
        justificacion = "El corte structured compensa proporciones amplias manteniendo la elegancia formal."


    elif relacion_brazo_torso < 0.85 and tipo_prenda == "buzo":
        recomendacion = "Buzo con manga 3/4 o manga ranglán"
        justificacion = "La manga ranglán visualmente alarga el brazo cuando la proporción brazo/torso es corta."


    elif genero == "femenino" and estilo_de_ropa == "formal" and tipo_prenda == "buzo":
        recomendacion = "Buzo blazer de punto fino, color neutro"
        justificacion = "Combina la comodidad del buzo con la sobriedad formal requerida."

    else:
        recomendacion = "Prenda estándar según tus medidas y preferencias"
        justificacion = "Tu combinación de características es versátil; optamos por una prenda equilibrada."

    seguir = input("Desea ingresar otro cliente?: (si/no) ")
    while seguir != "si" and seguir != "no":
        seguir = input (f"{Fore.RED}Error, ingrese: (si/no){Style.RESET_ALL} ")

    #__________ Salidas por consola_______________
    print(f" Cliente: {nombre}")
    print(f" Edad: {edad} años == {rango_etario}")
    print(f" Género: {genero}")
    print(f" Tipo de prenda: {tipo_prenda}")
    print(f" Estilo: {estilo_de_ropa}")