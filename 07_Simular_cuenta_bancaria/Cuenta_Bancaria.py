import random
from os import system


class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, cuenta, balance, nombre, apellido):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        return (f"DATOS DEL CLIENTE\n"
                f"================\n"
                f"- Nombre: {self.apellido}\n"
                f"- Apellido: {self.apellido}\n"
                f"- Núm. Cuenta: {self.cuenta}\n"
                f"- Saldo: {float(self.balance)} €\n"
                f"")

    def depositar(self, dinero):
        self.balance += int(dinero)

    def retirar(self, dinero):
        error = -1
        if dinero > self.balance:
            error = 0
            return error
        else:
            self.balance -= dinero
            return error


# Funciones

def crear_cliente():
    print("---- BIENVENIDO ----")
    print("ALTA DE CLIENTE, proporcione los datos necesarios.")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    # Cuenta: ES8121004657319589145174
    cuenta = "ES" + str(random.randint(1000000000000000000000, 9999999999999999999999))

    iban = (cuenta[0:4] + "-" +
            cuenta[4:8] + "-" +
            cuenta[8:12] + "-" +
            cuenta[12:16] + "-" +
            cuenta[16:20] + "-" +
            cuenta[20:24])
    saldo = 0

    nueva_persona = Cliente(iban, saldo, nombre, apellido)

    return nueva_persona


def elegir_opcion():
    # Vamos a mostrar menu
    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 4):
        system('cls')
        print("""
        Seleccione opción:
            [1] - Realizar depósito.
            [2] - Realizar Retiro.
            [3] - Salir.\n""")
        eleccion_menu = input("         --> ")

    return int(eleccion_menu)


def inicio():
    cliente = crear_cliente()
    print(cliente)
    finalizar_programa = False
    while not finalizar_programa:
        opcion = elegir_opcion()
        if opcion == 1:
            system('cls')
            dinero = "x"
            while not dinero.isnumeric():
                dinero = input("Inserte la cantidad a ingresar: ")

            cliente.depositar(round(float(dinero), 2))
            system('cls')
            print(cliente)
        elif opcion == 2:
            system('cls')
            dinero = "x"

            while not dinero.isnumeric():
                dinero = input("Inserte la cantidad a retirar: ")

            if cliente.retirar(float(dinero)) == 0:  # Quiere decir que da error, saldo no suficiente
                print("Saldo no suficiente para poder retirar.")
            else:
                print(cliente)
        elif opcion == 3:
            finalizar_programa = True


inicio()
