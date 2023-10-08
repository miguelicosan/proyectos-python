# Modulos a importar
import os
import shutil
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")


def contar_recetas(ruta):
    contador = 0
    for archivo in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador


def inicio():
    system('cls')
    print("\n")
    print('#' * 50)
    print('#' * 10 + "      RECETARIO DE MIGUEL     " + '#' * 10)
    print('#' * 50)
    print("\n")
    print(f"RUTA DEL RECETARIO: {mi_ruta}")
    print(f"TOTAL DE RECETAS: {contar_recetas(mi_ruta)}\n")
    print('#' * 50)

    # Vamos a mostrar menu
    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("""Seleccione opción:
        [1] - Leer receta.
        [2] - Crear nueva receta.
        [3] - Crear nueva categoría.
        [4] - Eliminar receta.
        [5] - Eliminar categoría.
        [6] - Salir.\n""")
        eleccion_menu = input("Opción --> ")

    return int(eleccion_menu)


# Mostar categorias
def mostrar_categorias(ruta):
    print("Categorías:")
    print('#' * 50)
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias


# Elegir categorias
def elegir_categoria(lista):
    eleccion = "x"
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\nElije una categoría: ")

    return lista[int(eleccion) - 1]


# Mostar recetas
def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas


# Elegir receta
def elegir_recetas(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige un nº de receta: ")

    return lista[int(eleccion_receta) - 1]


# Leer receta
def leer_receta(receta):
    print(Path.read_text(receta))


# Crear receta
def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido guardada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")


# Crear categoría
def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu Categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada.")
            existe = True
        else:
            print("Lo siento, esa categoría ya existe")


# Eliminar Receta
def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada.")


# Eliminar categoria
def eliminar_categoria(categoria):
    Path(categoria).rmdir() # metodo para eliminar directorios (carpetas)
    # (solo funciona si carpeta esta vacia)

    # metodo para eliminar directorios (carpetas) y sus archivos dentro
    shutil.rmtree(categoria)

    print(f"La categoria {categoria.name} ha sido eliminada.")


# Volver a inicio
def volver_inicio():
    eleccion_inicio = "x"

    while eleccion_inicio.lower() != "v":
        eleccion_inicio = input("\nPresione 'V' para volver al menú.")


# Mostrar menu de inicio

finalizar_programa = False

while not finalizar_programa:
    menu = inicio()
    print(menu)
    if menu == 1:
        # mostrar categorias
        lst_categorias = mostrar_categorias(mi_ruta)
        # elegir una categoria
        categoria_sel = elegir_categoria(lst_categorias)
        # mostrar recetas
        lst_recetas = mostrar_recetas(categoria_sel)
        # elegir recetas
        receta_sel = elegir_recetas(lst_recetas)
        # leer receta
        leer_receta(receta_sel)
        # volver inicio
        volver_inicio()

    elif menu == 2:
        # mostrar categorias
        lst_categorias = mostrar_categorias(mi_ruta)
        # elegir una categoria
        categoria_sel = elegir_categoria(lst_categorias)
        # crear receta nueva
        crear_receta(categoria_sel)
        # volver inicio
        volver_inicio()

    elif menu == 3:
        # crear categoria
        crear_categoria(mi_ruta)
        # volver inicio
        volver_inicio()

    elif menu == 4:
        # mostrar categorias
        lst_categorias = mostrar_categorias(mi_ruta)
        # elegir una categoria
        categoria_sel = elegir_categoria(lst_categorias)
        # mostrar recetas
        lst_recetas = mostrar_recetas(categoria_sel)
        # elegir recetas
        receta_sel = elegir_recetas(lst_recetas)
        # eliminar receta
        eliminar_receta(receta_sel)
        # volver inicio
        volver_inicio()

    elif menu == 5:
        # mostrar categorias
        lst_categorias = mostrar_categorias(mi_ruta)
        # elegir una categoria
        categoria_sel = elegir_categoria(lst_categorias)
        # eliminar categoria
        eliminar_categoria(categoria_sel)
        volver_inicio()

    elif menu == 6:
        # finalizar programa
        finalizar_programa = True
