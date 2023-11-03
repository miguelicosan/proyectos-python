import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Vamos a cargar todas las imágenes para codificarlas
# Crear base de datos

ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0].replace('-', ' '))

print(nombres_empleados)


# Codificar imágenes

def codificar(imagenes):
    # Crear lista nueva codificada
    lista_codificada = []

    # Pasar imagenes a RGB
    for img in imagenes:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # codificar
        img_codificada = fr.face_encodings(img)[0]
        lista_codificada.append(img_codificada)

    # Devolver lista codificada
    return lista_codificada


# Registrar asistencia de empleados
def registrar_asistencia(persona):
    # Vamos a registrar un CSV con los registros de los empleados
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombre_registrados = []
    for linea in lista_datos:
        registro = linea.split(',')
        nombre_registrados.append(registro[0])

    if persona not in nombre_registrados:
        ahora = datetime.now()
        str_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {str_ahora}')


# Lista que contiene lista de imagenes de empleados codificada
lista_empleados_codificada = codificar(mis_imagenes)


# Tomar imagen de Cámara Web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen cámara
exito, imagen = captura.read()

if not exito:
    print("No se ha podido capturar la foto.")
else:
    # Reconocer cara en captura
    cara_capturada = fr.face_locations(imagen)

    # Codificar cara-imagen capturada
    cara_capturada_codificada = fr.face_encodings(imagen, cara_capturada)

    # Buscar coincidencias con lista de empleados
    for cara_codificada, cara_ubicacion in zip(cara_capturada_codificada, cara_capturada):
        coincidencias = fr.compare_faces(lista_empleados_codificada, cara_codificada)
        distancias = fr.face_distance(lista_empleados_codificada, cara_codificada)

        indice_coincidencia = numpy.argmin(distancias)
        # Mostrar coincidencias si las hay
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")
        else:
            # Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = cara_ubicacion
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 4, y2 - 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

            # Vamos a llamar a la funcion para registrar asistencia del empleado

            registrar_asistencia(nombre)

            # Mostrar imagen obtenida
            cv2.imshow('Imagen web', imagen)

            # Mantener ventana abierta
            cv2.waitKey(0)