from random import choice


# ELEGIR PALABRA
def elegir_palabra_azar():
    lista_palabras = [
        "MANZANA"
    ]

    print("##############################\n"
          "#     JUEGO DEL AHORCADO     #\n"
          "##############################\n")
    print("ADIVINA LA PALABRA")

    item = choice(lista_palabras)
    palabra_formateada = ""
    for i in item:
        palabra_formateada += i + " "

    return palabra_formateada


# MOSTRAMOS LOS GUIONES CORRESPONDIENTES A LA PALABRA ELEGIDA
def mostrar_guiones(palabra):
    guiones = ""
    for l in palabra:
        if l is not " ":
            guiones += "_ "

    print(f"PALABRA: {guiones}")
    return guiones


# MOSTRAMOS LETRAS CORRECTAS
def mostrar_letras_correctas(lista_letras_correctas, palabra_random, palabra_oculta):
    for l in lista_letras_correctas:
        print(l)
        print(palabra_random)
        index = palabra_random.index(l)
        print(index)
        if index > 0:
            palabra_oculta[index] = l

    print(f"PALABRA: {palabra_oculta}")
    return palabra_oculta


# MOSTRAR VIDA
def mostrar_vidas(vidas):
    corazones = ""
    num_vidas = 0
    for n in range(vidas):
        corazones += "♥ "
        num_vidas += 1

    print(f"  VIDAS: {corazones} ({num_vidas})")


# PEDIR LETRA AL USUARIO
def pedir_letra():
    letra = input("  Letra: ")
    while not validar_letra(letra):
        letra = input("  Letra: ")

    return letra.upper()


# VALIDAR LETRA INTRODUCIDA
def validar_letra(letra):
    char_validos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    if len(letra) > 1:
        print("Introduce un sólo carácter")
        return False
    elif letra.upper() not in char_validos:
        print("Introduce una letra")
        return False

    return True


# BUSCAR LETRA EN PALABRA
def buscar_letra_palabra(letra, palabra):
    if letra not in palabra:
        return False
    else:
        return True


##############################
# MAIN / EJECUCIÓN PRINCIPAL #
##############################

# VARIABLES GLOBALES

palabra_random = elegir_palabra_azar()
palabra_oculta = mostrar_guiones(palabra_random)
vidas = 6
lista_letras_acertadas = []
lista_letras_noacertadas = []

while vidas > 0:

    # mostrar_guiones(palabra_random)
    mostrar_vidas(vidas)
    letra_valida = pedir_letra()
    resultado = buscar_letra_palabra(letra_valida, palabra_random)

    if resultado:
        print("         ¡ACERTASTE!")
        lista_letras_acertadas.append(letra_valida)
        palabra_oculta = mostrar_letras_correctas(lista_letras_acertadas, palabra_random, palabra_oculta)
    else:
        print(f"         ¡OH! La {letra_valida} no está")
        lista_letras_noacertadas.append(letra_valida)
        print(f"         Letras NO acertadas: {lista_letras_noacertadas}")
        vidas -= 1
