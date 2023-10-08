import numeros


def preguntar():
    """
    Preguntar al usuario que opción desea
    :argument: No tiene
    :return: nada
    """
    print("Bienvenido a Farmacia Python")

    while True:
        print(" [P] - PERFUMERÍA\n [F] - FARMACIA\n [C] - COSMÉTICA")
        try:
            opcion = input("Elija su opción: ").upper()
            ["P", "F", "C"].index(opcion)
        except ValueError:  # Por convención de estilos
            print("Opción incorrecta.")
        else:
            break

    numeros.decorador(opcion)


def inicio():
    """
    :argument: No tiene
    :return: Nada
    """
    while True:
        preguntar()
        try:
            otro_turno = input("¿Quieres sacar otro número? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()
