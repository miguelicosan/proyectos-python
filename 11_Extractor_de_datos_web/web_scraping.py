import bs4
import requests
import lxml  # Importado para instalarlo para usar en BeautifulSoap

# Página web para hacer tests de webscraping
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de títulos con 4 o 5 estrellas
titulos_puntuacion_alta = []

# Iterar por las páginas
for pagina in range(1, 51):

    # Extraer código de cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    codigo = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Selección datos de los libros
    libros = codigo.select('.product_pod')  # Clase en el html para obtener el código de cada libro

    # Recorrer libros
    for libro in libros:
        # Comprobar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # Guardamos título en variable
            titulo_libro = libro.select('a')[1]['title']

            # Añadir libro a la lista
            titulos_puntuacion_alta.append(titulo_libro)

# Ver los libros 4 o 5 estrellas en consola
for t in titulos_puntuacion_alta:
    print(t)
