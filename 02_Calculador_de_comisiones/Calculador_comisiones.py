# Proyecto de Comisiones

nombre = input("Dime tu nombre: ")

ventas = input("Escribe tus ventas: ")

ventas = int(ventas)

comision = (ventas * 13) / 100

comision = round(comision, 2)

print(f"{ nombre } tu comisión es de: { comision } €")
