import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

# Opciones de voz/idioma
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


# Escuchar nuestro micrófono y devolver audio como texto
def transformar_audio_en_texto():
    # almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:
        # tiempo espera
        r.pause_threshold = 0.8

        # informar que comenzó la grabación
        print("Ya puedes hablar")

        # Guardar lo escuchado como audio
        audio = r.listen(origen)

        try:
            # Buscar en google lo escuchado
            pedido = r.recognize_google(audio, language="es-es")

            # Imprimir en pantalla lo transformado
            print("Has dicho: " + pedido)

            # Devolver pedido
            return pedido
        # en caso de que no comprenda el audio
        except sr.UnknownValueError:
            # Prueba que con ha comprendido el audio
            print("Ups! No he compredido lo que solicitaste.")

            # devolver
            return "Sigo esperando"

        # En caso de no poder resolver el pedido
        except sr.RequestError:
            # Mensaje cuando no encuentra que buscar
            print("Ups! No he encontrado lo que solicitas.")

            # devolver
            return "Sigo esperando"

        # Error inesperado
        except:
            # Error cuando sucede algo inesperado
            print("Ups! Algo ha salido mal.")

            # devolver
            return "Sigo esperando"


# Función para que el asistete hable
def hablar(mensaje):
    # Encender el moto de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar del dia de la semana
def perdir_dia():
    dia = datetime.date.today()
    print(dia)

    # Crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionado con nombres de los dias
    calendario = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }

    # Decr el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# Informar de la hora que es
def pedir_hora():
    # Variable de hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las: {hora.hour} horas {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    # decir la hora
    hablar(hora)


# Saludo iniciar
def saludo_inicial():
    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches,"
    elif 6 <= hora.hour < 13:
        momento = "Buenos días,"
    else:
        momento = "Buenas tardes,"

    hablar(f"{momento} soy Paquita, tu asistente personal. ¿En que te puedo ayudar?")


# Funcion central del asistente
def pedir_cosas():
    # Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Estoy abriendo Youtube')
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'abrir navegador' in pedido:
            hablar('Enseguida')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es' in pedido:
            perdir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Estoy buscándolo en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Enseguida')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Vamos a ello')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {
                'apple': 'APPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar(f'Lo siento, pero he la he contrado la accion {accion}')
                continue
        elif 'adiós' in pedido:
            hablar("Un placer, me voy a descansar.")
            break


pedir_cosas()
