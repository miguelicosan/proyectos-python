# <font color='darkorange'>Proyectos en Python</font>
En estre repositorio encontrarás proyectos realizados en Python desde un nivel mas básico a un nivel mas avanzado, siguiendo curso de [Python TOTAL - Programador Avanzado en 16 días](https://www.udemy.com/course/python-total/) de Udemy.

<div align="center"><img src="https://www.python.org/static/community_logos/python-logo-generic.svg"></div>

## 1. Creador creativo de Nombres
Código en Python que pide a un usuario que responda dos preguntas que requieran una sola palabra cada una y luego muestre en pantalla esas palabras combinadas, para formar una marca creativa.

### ¿Qué aprendí?
Instalacion Pycharm, Print, String, Input

## 2. Calculador de comisiones
Programa que comienza preguntando cosas al usuario para poder recibir los ingresos del usuario. Posteriormente se debe calcular el 13% del número que haya ingresado el usuario. 
Todos los resultados se imprimirán por pantalla.

### ¿Qué aprendí?
Más tipos de datos, variables, Integers y Floats, Conversiones entre Tipos de datos, Formatear Cadenas, Redondeo, Operadores Matemáticos.

## 3. Analizador de textos
Programa que primero pide al usuario que ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un poema, lo que quiera!. Luego, el programa le va a pedir al usuario que también ingrese tres letras a su elección y a partir de ese momento este código va a procesar esa información para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
- Cuántas veces aparece cada una de las letras que eligió.
- Cuántas palabras hay a lo largo de todo el texto.
- Primera letra del texto y cuál es la última
- Cómo quedaría el texto si invirtiéramos el orden de las palabras.
- Nos va a decir si la palabra “Python” se encuentra dentro del texto.

### ¿Qué aprendí?
Método index, extraer sub-strings, propiedades de strings, Listas, Diccionarios, Tuples, Sets, Booleanos.

## 4. ¡Adivina el número!
Progama que adivina un número pensado entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número. Entonces, en cada intento el jugador dirá un número y el programa puede responder cuatro cosas distintas:
- Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido un número que no está permitido.
- Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
- Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la misma manera.
- Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos intentos le ha tomado.

Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro número. Y así hasta que gane o hasta que se agoten los ocho intentos.

### ¿Qué aprendí?
Operadores de comparación, operadores lógicos, control de flujo: if, elif, match, loops: for, while, rango. Enumerador, zip, Min y Max, Random, Conprensión de listas.

## 5. ¡Juego del ahorcado!
Todos sabemos como funciona el juego del ahorcado ¿verdad?
El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en la palabra oculta, pierde una vida.
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra completa antes de perder todas las vidas, el jugador gana. 

### ¿Qué aprendí?
Métodos, ayuda y documentación. Funciones, Return, Funciones dinámicas, interacción entre funciones, argumentos indeficidos (*args y **kwargs).

## 6. Programa de un recetario
Se programará un menu de selección a usuario y se dará la bienvenida al usuario. Las opciones a programar son las siguientes:
- 1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
- 2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.
- 3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.
- 4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar
- 5. La opción 5, le va a preguntar qué categoría quiere eliminar
- 6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.

### ¿Qué aprendí?
Abrir y manupular archivos, crear y escribir archivos, directorios. Pathlib, Path, Limpiar consola de salida, archivos y funciones relacionadas.

## 7. Simular una cuenta bancaria
Cópdigo que simula el funcionamiento simple de una cuenta bancaria, utilizando la POO. El usuario podrá ingresar y retirar dinero con todas las validaciones y necesidades.

### ¿Qué aprendí?
Programación orientada a objetos (POO) y sus pilares: Herencia, Polimorfismo, Cohesión, Acoplamiento y Abstracción. Clases, atributos, métodos, tipos de métodos, herencia y dunder methods.

## 8. Consola de turnos/tickets para atender
El programa le pregunta al cliente a cuál de las tres áreas posibles de la Farmacia desea dirigirse (Cosmética, Perfumería y Farmacia), y le va a dar un número de turno según a qué área se dirija. Por ejemplo, si elige cosmética le va a dar el número C-54 (“C” de cosmética). Después, nos va a preguntar si queremos sacar otro turno esperando si viene un nuevo cliente. Se repetirá todo el proceso hasta que se decida cerrar el programa.

### ¿Qué aprendí?
Instalar paquetes, modulos y paquetes propios, manejo de errores, Tests con Pylint y Unittest, decoradores y generadores.

## 9. Buscador de número de serie
Es un programa que se encargue de buscar números de serie que cumplan un determinado formato, dentro de un arbol de carpetas. El programa va a recorrer todos los archivos y subcarpetas de un directorio raiz y va a buscar cualquier string que coincida con un patrón de número de serie. La presentación de la pantalla de salida debe mostrar la fecha de la búsqueda, mostrar dos columnas: El archivo encontrado y el número de serie encontrado en el archivo y por último, la cantidad de números de serie encontrados y el tiempo empleado en la búsqueda.

### ¿Qué aprendí?
Collections, módulos OS, Shutil, Datetime, medir tiempos, Math, Re (Expresiones regulares), comprimir y descomprimir archivos.

## 10. Videojuego: ¡Space Invaders!
Se trata de programar un videojuego muy parecido al Space Invaders o Invasión Espacial, que todos hemos jugado alguna vez.

### ¿Qué aprendí?
Crear pantalla, titulo, iconos, colores, fondos, agregar protagonistas, movimiento de personaje, control de movimiento, limite de movimientos, crear enemigos, movimiento de balas, detectar colisiones, agregar enemigos nuevos, mostrar puntuación, agregar música y sonidos, finalizar juego y crear archivo ejecutable (.exe)

## 11. Extractor de datos web (Web Scraping)
¿Sabes que es el webscraping? El web scraping se refiere al proceso de extracción de contenidos y datos de sitios web mediante software. Por ejemplo, la mayoría de los servicios de comparación de precios utilizan web scrapers para leer la información de precios de varias tiendas online.

### ¿Qué aprendí?
Principios, ver código fuente, titulos y elementos de una página web. Extraer elementos de una clase e imágenes. Toscrape.com, Explorar múltiples páginas, identificar condiciones de extracción y combinación de items buscados.

## 12. Gestor de Restaurantes
Se trata de programar una interface gráfica de usuario para gestionar un restaurante que permita introducir los detalles de los elementos consumidos en una mesa y poder obtener la cuenta de cada mesa. Te va permitir generar un recibo o ticket que va a guardar en un fichero txt en el ordenador para enviarlo a imprimir o guardarlo. Además incluirá una calculadora incorporada por si el usuario necesita realizar alguna operación adicional.

### ¿Qué aprendí?
TKinter, paneles, checkbuttons, inputtext, botones y demas elementos de pantalla.

## 13. Asistente por voz (tu propio Siri o Alexa)
Un programa que podrás hablar y pedir que te asista en muchas tareas. Será capaz de desarrollar tareas y hacerlo facilimente excalable para poder añadirle muchas nuevas facilmente. 

### ¿Qué aprendí?
Transformar voz en texto y texto en voz, configurar idioma, consultar dia y hora, buscar en wikipedia, abrir un navegador, consultar finanzas, que te cuente un chiste, etc...
- Bibliotecas pyttsx3, speech_recognition, webbrowser, pywhatkit, yfinance, pyjokes y wikipedia.

## 14. Control de Asistencia por Reconocimiento facial
Se trata de programar un control de asistencia de empleados mediante reconocimiento facial, ¡no será necesario fichar usando nada mas que tu cara! Se registrará en una tabla la fecha y hora de la persona que ha sido indentificada.

### ¿Qué aprendí?
Reconocimiento facial, análisis facial, conversión a datos (huella digital) y buscar coincidencias.

## 15. Modelo de Machine Learning
En este proyecto se va a revisar una base de datos de pasajeros del famoso barco Titanic y en base al análisis de quienes sobrevivieron y quienes no van, va a poder identificar que caracterísiticas son las mas favorables y desfavorables para sobrevivir a su hundimiento. Incluso va a poder predecir si presentaramos nuevos pasajeros, si estos van a sobrevivir o no.

El modelo de machine learing es una rama de la inteligencia artifical para entrenar a nuestro programa para que en base en su experiencia y los datos provistos sea capaz de predecir el resultado de nuevos casos.

### ¿Qué aprendí?
Data science en Python usando bibliotecas: numpy, pandas y matplotlob

## 16. Programación de una Página Web
En este proyecto vamos a crear desarrollar una página web usando que permita administrar una lista de tareas pendientes: editarlas, eliminarlas, marcarlas como completadas, relizar búsquedas y mucho mas. Vamos a tener un control de login de usuarios permitiendo por tanto gestionar el registro de usuarios. 


### ¿Qué aprendí?
Desarrollar una página web usando el framework Django utilizado para el front-end y el back-end, antornos virtuales y aplicaciones de estilo profesional.  
