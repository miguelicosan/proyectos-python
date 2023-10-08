def numeros_perfumeria():
    """
    Función con un numero elevado que no llegará a un día para producir un número para PERFUMERÍA
    P - 1, P - 2...
    """
    for n in range(1, 10000):
        yield f"P - {n}"


def numeros_farmacia():
    """
    Función con un numero elevado que no llegará a un día para producir un número para FARMACIA
    F - 1, F - 2...
    """
    for n in range(1, 10000):
        yield f"F - {n}"


def numeros_cosmetica():
    """
    Función con un numero elevado que no llegará a un día para producir un número para COSMÉTICA
    C - 1, C - 2...
    """
    for n in range(1, 10000):
        yield f"C - {n}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorador(cosa):
    """
    Función decorador para "decorar" el formato del número en funcion de la cosa seleccionada
    """
    print("\n" + "*" * 23)
    print("Su número es:")
    if cosa == "P":
        print(next(p))
    elif cosa == "F":
        print(next(f))
    else:
        print(next(c))

    print("Enseguida será atendido")
    print("*" * 23)
