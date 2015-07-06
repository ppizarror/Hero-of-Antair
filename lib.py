#!/usr/bin/env python
# -*- coding: utf-8 -*-
# LIB
# Pablo Pizarro, 2013-2015
# Este fichero carga las librerías importantes y las funciones globales
# Importación de librerías

# XCOM : Coma
# XPYC : Punto y coma
# XDP: Dos puntos
# XGUI: Guion
# XII : '
# XLASH : /

# Importación de liberías de alto nivel
import os
import sys

# Configuración de las librerías de alto nivel
reload(sys)
sys.setdefaultencoding('UTF8')
sys.dont_write_bytecode = True
try:
    os.remove("lib.pyc")
except:
    pass

# Agrego librerías al path
_actualpath = str(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(_actualpath + "/lib/")
sys.path.append(_actualpath + "/lib/pil/")
sys.path.append(_actualpath + "/lib/pympler/")
sys.path.append(_actualpath + "/lib/scripts/")
sys.path.append(_actualpath + "/lib/simplejson/")
sys.path.append(_actualpath + "/lib/wconio/")

# Importación de librerías de bajo nivel
_wconio = True
_winsound = True

try:
    from Tkinter import *
    from VerticalScrolledFrame import *
    from datetime import date
    from functools import partial
    from math import log
    from noStdOut import *

    if os.name == "nt":
        from pil import Image, ImageTk
    else:
        from PIL import Image, ImageTk
    from pympler import summary, muppy
    from random import choice
    from tkFileDialog import *
    from urllib import urlencode
    from urllib2 import urlopen, Request

    try:
        import WConio
    except:
        _wconio = False
    import base64
    import codecs
    import ctypes
    import gc
    import io
    import json
    # noinspection PyDeprecation
    import md5
    import random
    import re
    import simplejson
    import socket
    import string
    import time
    import tkFont
    import tkMessageBox
    import types
    import urllib2
    import webbrowser

    # Librerias depentientes del SO
    try:
        import tkSnack
    except:
        pass
    try:
        import winsound
    except:
        _winsound = False

except:
    print "Error :: Error al cargar librerias"
    exit()

# Constantes del programa
__ALPH = " @rs3t*uv#w'xEF(9<GH$IJ&5K,L%CVWXjkl_mnop/qD0{PQ+RS[TUAY]1Z^67;8?ab>cd)efMNO.Bg}hi24-yz!"
__L_ALPH = len(__ALPH)
CONSOLE_WRAP = -25
CMD_COLORS = {"red": 0x40, "lred": 0xC0, "gray": 0x80, "lgray": 0x70, "white": 0xF0, "blue": 0x10, "green": 0x20,
              "purple": 0x50, "yellow": 0x60, "lblue": 0x90, "lgreen": 0xA0, \
              "lpurple": 0xD0, "lyellow": 0xE0}
ENDING_ARGUMENT = "$end"
DEV_MODE = True
LINK_PPPRJ = "http://projects.ppizarror.com/version?product=HOA"
OK = "ok"
WIN32 = 4
WIN64 = 8

# Funciones globales
def amir(archive):
    """
    Genera los achivos de seguridad
    :param archive: Archivo
    :return: String
    """
    texto = loadFromArchive(archive, "", False)
    hast = ""
    for i in texto: hast += i
    hast = delAcentos(hast.replace("\n", ""))
    try:
        try:
            text = list(hast.strip())
            k = 0
            for i in text:
                if not i in __ALPH: text.pop(k)
                k += 1
            key = ""
            for i in text: key += i
            p = int(len(text))
            key = key[::-1]
            sem = ""
            j = __ALPH.index(key[0])
            first = True
            for i in key:
                if first:
                    sem += __ALPH[j]
                    first = False
                else:
                    j = j + p + __ALPH.index(i)
                    while j > __L_ALPH: j -= __L_ALPH
                    if j >= __L_ALPH: j -= __L_ALPH
                    sem += __ALPH[j]
            j = __ALPH.index(sem[len(sem) - 1])
            sem_2 = ""
            sem = sem[::-1]
            first = True
            for l in sem:
                if first:
                    sem_2 += __ALPH[j]
                    first = False
                else:
                    j += p + __ALPH.index(l)
                    while j > __L_ALPH: j -= __L_ALPH
                    if j >= __L_ALPH: j -= __L_ALPH
                    sem_2 += __ALPH[j]
            return sem_2
        except:
            return "%NOAMIR%"
    except:
        return "%NOAMIR%"


# noinspection PyUnboundLocalVariable
def benchmark(save=False, prt=False, default=5):
    """
    Genera un benchmark para obtener el rendimiento del sistema y asi definir tiempos de ejecución
    :param save: Boolean <saving>
    :param prt: Boolean <printing>
    :param default: Número de repeticiones
    :return: Tiempo en ms
    """
    import platform

    if save:
        archivo = open("log/benchmark.log", "w")
        archivo.write("Benchmark, Creado el " + obtenerFecha() + " a las " + getHour() + "\n\n")
        archivo.write("Parametros \t \\t\tNumero de prueba\n\t\t \\avg\tPromedio de la prueba\n\n")
        archivo.write("Procesador: " + platform.processor() + "\n")
        archivo.write("Tipo de ordenador: " + platform.machine() + "\n")
        archivo.write("Nombre del host: " + platform.node() + "\n")
        archivo.write("SO: " + platform.system() + " " + platform.release() + "\n")
        archivo.write("Version del SO: " + platform.platform() + "\n\n")
    total = 0
    for n in range(default):
        t0 = time.clock()
        for i in xrange(1000000): i += 1
        test = time.clock() - t0
        msg = "Benchmark \\t {0} {1}".format(str(n + 1), str(test)).replace(".", ",")
        if prt: print msg
        if save: archivo.write(msg + "\n")
        total += test
        time.sleep(0.1)
    msg = "Benchmark \\avg {0}".format(str(total / 5)).replace(".", ",")
    if prt: print msg
    if save:
        archivo.write("\n" + msg + "\n")
        archivo.close()
    return total / 5


def borrarArchivosGenerados(archivo):
    """
    Se borran los archivos generador luego de guardar una partida
    :param archivo: Archivo de partida guardada
    :return: void
    """
    try:
        os.remove(archivo + ".sav")
    except:
        pass
    try:
        os.remove(archivo + ".key1")
    except:
        pass
    try:
        os.remove(archivo + ".key2")
    except:
        pass
    try:
        os.remove(archivo + ".key3")
    except:
        pass
    try:
        os.remove(archivo + ".key4")
    except:
        pass
    try:
        os.remove(archivo + ".key5")
    except:
        pass
    try:
        os.remove(archivo + ".quest")
    except:
        pass
    try:
        os.remove(archivo + ".powers")
    except:
        pass
    try:
        os.remove(archivo + ".hoacmd")
    except:
        pass
    try:
        os.remove(archivo + ".maplogic")
    except:
        pass
    try:
        os.remove(archivo + ".mapmob")
    except:
        pass
    try:
        os.remove(archivo + ".mapnpc")
    except:
        pass
    try:
        os.remove(archivo + ".statics")
    except:
        pass
    try:
        os.remove(archivo + ".mapitemtexture")
    except:
        pass


def borrarArchivosGuardado(archivo):
    """
    Se borran los archivos resultantes de guardar una partida
    :param archivo: Archivo de partida guardada
    :return: void
    """
    try:
        os.remove(archivo.replace(".save", ".sav"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".key1"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".key2"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".key3"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".key4"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".key5"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".hoacmd"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".mapmob"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".mapnpc"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".maplogic"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".statics"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".powers"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".quest"))
    except:
        pass
    try:
        os.remove(archivo.replace(".save", ".mapitemtexture"))
    except:
        pass


def checkScreen(window, config, msg):
    """
    Se comprueba si el tamaño de la pantalla es valido
    :param window: Objeto de ventana
    :param config: Configuraciones
    :param msg: Mensaje de error
    :return: void
    """
    if (window.winfo_screenwidth() < config[0]) or (
                window.winfo_screenheight() < config[1]):  # Se comprueba el tamaño de la pantalla
        sys.stderr.write("Error :: " + msg + "\n")
        exit()


def compararVersiones(ver1, ver2):
    """
    Se compara entre dos versiones
    :param ver1: Versión actual
    :param ver2: Versión nueva
    :return: 0, 1, 2
    """
    ver1 = ver1.split(".")
    ver2 = ver2.split(".")
    ganador = 0
    for i in range(3):
        if int(ver1[i]) > int(ver2[i]):
            return 1
        elif int(ver1[i]) < int(ver2[i]):
            return 2
    return 0


def connect_server(server, port):
    """
    Función que conecta al cliente a un servidor mediante un puerto definido
    :param server: Server
    :param port: Port
    :return: List
    """
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((server, port))
    _id = str(conn.getsockname()[1])
    return [_id, conn]


def consoled(c):
    """
    Función que genera un string con una lista (para la consola de hoa)
    :param c: Lista
    :return: Texto
    """
    text = ""
    for i in c: text = text + i + "\n"
    return text


def consultParam(argument, arguments):
    """
    Función que consulta el parametro de un argumento
    :param argument: Argumento
    :param arguments: Lista de argumentos
    :return: String
    """
    for i in arguments:
        if i[0] == argument and ("/" in i[1]): return i[1].replace("/", "")
    return "%NULL%"


def colorcmd(cmd, color):
    """
    Función que imprime un mensaje con un color
    :param cmd: CMD
    :param color: Color
    :return: void
    """
    if color in CMD_COLORS:
        color = CMD_COLORS[color]
        try:
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), color)
        except:
            pass
        print cmd,
        try:
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 0x07)
        except:
            pass
    else:
        print cmd,


def delAcentos(txt):
    """
    Elimina los acentos de un string
    :param txt: String
    :return: String formateado
    """
    txt = txt.replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
    return txt.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")


def delMatrix(matrix):
    """
    Borrar una matriz
    :param matrix: Lista
    :return: void
    """
    a = len(matrix)
    if a > 0:
        for k in range(a): matrix.pop(0)


def desParseType(a):
    """
    Función interna que retorna un dato dependiendo del tipo que sea
    :param a: String
    :return: Múltiples salidas
    """
    if a.replace(".", "").isdigit():
        if "." in a:
            a = "flt_" + str(float(a))
        else:
            a = "int_" + str(int(a))
    elif a.upper() == "TRUE" or a.upper() == "FALSE":
        if a.upper == "TRUE":
            a = "boo_True"
        else:
            a = "boo_False"
    else:
        a = "str_" + str(a)
    return a


def generateRandom6():
    """
    Genera un string de 6 carácteres aleatorios
    :return: String
    """
    return ''.join(choice(string.ascii_uppercase) for i in range(6))


def generateRandom12():
    """
    Genera un string de 12 carácteres aleatorios
    :return: String
    """
    return ''.join(choice(string.ascii_uppercase) for i in range(12))


def getBetweenTags(html, tagi, tagf):
    """
    Función que retorna un valor entre dos tags
    :param html: Código HTML
    :param tagi: Tag inicial
    :param tagf: Tag final
    :return: String
    """
    tagi = tagi.strip()
    tagf = tagf.strip()
    try:
        posi = html.index(tagi)
        if ("<" in tagi) and (">" not in tagi):
            c = 1
            while True:
                try:
                    if html[posi + c] == ">": posi += (c + 1); break
                    c += 1
                except:
                    return TAG_INIT_NOT_CORRECT_ENDING
        else:
            posi += len(tagi)
        posf = html.index(tagf, posi)
        return html[posi:posf]
    except:
        return False


def getHour():
    """
    Función que retorna la hora de sistema
    :return: String
    """
    return time.ctime(time.time())[11:16]


def getTerminalSize():
    """
    Devuelve el tamaño de la consola
    :return: Integer
    """
    env = os.environ

    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os

            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
                                                 '1234'))
        except:
            return
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr: cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])


def getVersion(label, headers):
    """
    Obtener la versión del programa de forma local
    :param label: Label del programa
    :param headers: Web headers
    :return:
    """
    http_headers = {"User-Agent": headers}
    request_object = Request(LINK_PPPRJ, None, http_headers)
    response = urllib2.urlopen(request_object)
    html = response.read()
    html = getBetweenTags(getBetweenTags(html, "<" + label + ">", "</" + label + ">"), "<version>", "</version>")
    return html.strip()


def google_translate(text, translate_lang, header, web, source_lang=None):
    """
    Traduce una linea
    :param text: String
    :param translate_lang: Idioma destino
    :param header: Web header
    :param web: Web de traducción
    :param source_lang: Idioma fuente
    :return: String traducido
    """
    if source_lang is None: source_lang = 'auto'
    params = urlencode({'client': 't', 'tl': translate_lang, 'q': text.encode('utf-8'), 'sl': source_lang})
    http_headers = {"User-Agent": header}
    request_object = Request(web + params, None, http_headers)
    response = urlopen(request_object)
    string = re.sub(',,,|,,', ',"0",', response.read())
    n = json.loads(string)
    translate_text = n[0][0][0]
    res_source_lang = n[2]
    return translate_text


def isIn(termino, matriz):
    """
    Función que comprueba si un elemento esta en una matriz (no completamente)
    :param termino: Término
    :param matriz: Lista
    :return: Boolean
    """
    if termino is not None:
        for elem in matriz:
            if elem in termino: return True
    return False


def isTrue(a):
    """
    Función que devuelve True/False si a es "True" o a es igual a "False"
    :param a: String
    :return: Boolean
    """
    if a == "True":
        return True
    else:
        return False


def isWindows():
    """
    Función que retorna True/False si el sistema operativo cliente es Windows o no
    :return: Boolean
    """
    if os.name == "nt": return True
    return False


def obtenerFecha():
    """
    Obtiene la fecha del dia actual
    :return: String
    """
    fecha = date.today()
    return str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)


def loadFromArchive(archive, lang="Cargando archivo '{0}' ...",
                    showState=True):
    """
    Carga un archivo y retorna una matriz
    :param archive: Archivo
    :param lang: Mensaje de salida
    :param showState: Verbose
    :return: List
    """
    if showState: print lang.format("(...)" + archive[CONSOLE_WRAP:].replace("//", "/")).replace("\"", ""),
    try:
        l = list()
        archive = open(archive, "r")
        for i in archive:
            l.append(i.decode('utf-8').strip())
        archive.close()
        if showState: print "[OK]"
    except:
        if showState: print "error"
        l = []
    return l


# noinspection PyUnboundLocalVariable,PyShadowingBuiltins
def lookPrimaryArguments():
    """
    Se buscan los argumentos primarios <-help, -version, ...>
    :return: void
    """
    (width, height) = getTerminalSize()
    if len(sys.argv) >= 2:
        if sys.argv[1] == "-benchmark" or sys.argv[1] == "/benchmark":
            if _wconio: WConio.clrscr()
            print "Benchmark Hero of Antair"
            print "Python " + sys.version + "\n"
            if len(sys.argv) == 3:
                if str(sys.argv[2]).isdigit():
                    repeticiones = int(sys.argv[2])
                    if repeticiones > 1:
                        print "Realizando prueba benchmark a {0} repeticiones ...".format(str(repeticiones))
                        ms = benchmark(True, True, repeticiones)
                        print "\nTiempo promedio de ejecucion: " + str(ms) + "ms"
                        print "Benchmark guardado en log/benchmark"
                    elif repeticiones == 1:
                        print "Realizando prueba unica benchmark ...".format(str(repeticiones))
                        ms = benchmark(True, True, repeticiones)
                        print "\nTiempo promedio de ejecucion: " + str(ms) + "ms"
                        print "Benchmark guardado en log/benchmark"
                    else:
                        print "Error al ejecutar prueba benchmark, el numero de repeticiones debe ser mayor o igual a 1"
            else:
                print "Realizando prueba benchmark a 5 repeticiones ..."
                ms = benchmark(True, True)
                print "\nTiempo promedio de ejecucion: " + str(ms) + "ms"
                print "Benchmark guardado en log/benchmark"
            exit()
        elif sys.argv[1] == "-changelog" or sys.argv[1] == "/changelog":
            try:
                changelog = open("data/doc/hoa/changelog.txt", "r")
                print ""
                for line in changelog:
                    if line != "": print delAcentos(str(line)).rstrip()
                changelog.close()
            except:
                print "Error al ejecutar el comando -changelog :: Archivo no encontrado"
            exit()
        elif sys.argv[1] == "-dwi" or sys.argv[1] == "/dwi":
            try:
                if _wconio: WConio.clrscr()
                archivo = open("data/doc/other/dwi.txt", "r")
                print ""
                for line in archivo:
                    if line != "": print str(line).rstrip()
                archivo.close()
            except:
                print ""
            exit()
        elif sys.argv[1] == "-fcfm" or sys.argv[1] == "/fcfm" or sys.argv[1] == "/850" or sys.argv[1] == "-850":
            try:
                if _wconio: WConio.clrscr()
                asciiart = open("data/doc/other/850.txt", "r")
                counter = 0
                for i in asciiart:
                    print " " * (int((width - 26) / 2) - 3), i.rstrip()
                    counter += 1
                    if counter > 15 and i.strip() != "": time.sleep(1)
                asciiart.close()
            except:
                print "Error al ejecutar el comando -changelog :: Archivo no encontrado"
            exit()
        elif sys.argv[1] == "-help" or sys.argv[1] == "/help":
            try:
                helpfile = open("data/doc/documentation/arguments.txt", "r")
                print ""
                for h in helpfile:
                    if h != "": print h.rstrip()
                helpfile.close()
            except:
                print "Error :: Error al ejecutar el comando -help :: Archivo no encontrado"
            exit()
        elif sys.argv[1] == "-linecounter" or sys.argv[1] == "/linecounter":
            if _wconio: WConio.clrscr()
            try:
                total = 0
                listedfiles = []
                totallines = []
                for file in os.listdir(_actualpath):
                    if ".py" in file:
                        listedfiles.append(file)
                        archv = open(file, "r")
                        for l in archv:
                            total += 1
                        archv.close()
                        totallines.append(total)
                        total = 0
                brief = open("linecounter.txt", "w")
                brief.write("Archivos analizados:\n")
                for i in range(len(totallines)):
                    brief.write("\t" + str(listedfiles[i]) + " => " + str(totallines[i]) + " lineas\n")
                brief.write("\nTotal: " + str(sum(totallines)) + " lineas\n")
                brief.close()
                print "linecounter :: Archivo generado correctamente"
            except:
                print "Error :: Error al ejecutar el comando linecounter"
            exit()
        elif sys.argv[1] == "-sierpinski" or sys.argv[1] == "/sierpinski":
            if _wconio: WConio.clrscr()
            if len(sys.argv) == 3:
                if sys.argv[2] == "/help":
                    helpfile = open("data/doc/other/sierpinski.txt", "r")
                    print ""
                    for h in helpfile:
                        if h != "": print h.rstrip()
                    helpfile.close()
                else:
                    print "Error :: Argumentos incompletos, consulte /help"
                exit()
            elif len(sys.argv) == 4:
                negative = False
                reverse = False
                try:
                    s = sys.argv[2][0:1]
                except:
                    s = "H"
                try:
                    r = int(sys.argv[3])
                    if r > 0:
                        pass
                    else:
                        r = 1
                except:
                    r = 1
            elif len(sys.argv) == 5:
                param = sys.argv[2]
                if param == "/negative":
                    negative = True
                else:
                    negative = False
                if param == "/reverse":
                    reverse = True
                else:
                    reverse = False
                try:
                    s = sys.argv[3][0:1]
                except:
                    s = "H"
                try:
                    r = int(sys.argv[4])
                    if r > 0:
                        pass
                    else:
                        r = 1
                except:
                    r = 1
            else:
                print "Error :: Argumentos desconocidos, consulte /sierpinski /help"
                exit()
            for x in range(height * r):
                i = ""
                for y in range(width):
                    if negative:
                        if not x & y:
                            i += s
                        else:
                            i += " "
                    else:
                        if x & y:
                            i += s
                        else:
                            i += " "
                if reverse:
                    print i[::-1],
                else:
                    print i,
            exit()
        elif sys.argv[1] == "-version" or sys.argv[1] == "/version":
            exit()
    else:
        pass


def makeCallable(function):
    """
    Función que crea una función llamable
    :param function: Puntero a función
    :return: Función
    """
    try:
        function.__name__ = generateRandom6()
    except:
        pass
    return function


def parseObject(a):
    """
    Función que retorna los datos lógicos de un objeto cargado desde un archivo
    :param a: String
    :return: List
    """
    a = a.split("/_/")
    return a[0], putStrict(a[1]), a[2], a[3], int(a[4]), isTrue(a[5]), int(a[6]), [parseType(a[7]), parseType(a[8])]


def parseType(a):
    """
    Función interna que retorna un dato dependiendo del tipo que sea
    :param a: String
    :return: Multiples formatos
    """
    b = a[0:4]
    if b == "int_":
        return int(a[4:])
    elif b == "str_":
        return str(a[4:])
    elif b == "flt_":
        return float(a[4:])
    elif b == "boo_":
        return isTrue(a[4:])


def printAsciiArtHOA():
    """
    Imprime el arte ascii de la introducción
    :return: void
    """
    if _wconio: WConio.clrscr()
    try:
        (width, height) = getTerminalSize()  # se obtiene el largo de la consola para dejarlo centrado
        asciiart = open("data/doc/other/asciiart.txt", "r")
        for i in asciiart: print " " * (int((width - 26) / 2) - 1), i.rstrip()
        asciiart.close()
    except:
        pass


def printAsciiArtME():
    """
    Imprime el arte ascii del editor de mapas
    :return: void
    """
    if _wconio: WConio.clrscr()
    try:
        (width, height) = getTerminalSize()  # se obtiene el largo de la consola para dejarlo centrado
        asciiart = open("data/doc/other/asciiartm.txt", "r")
        for i in asciiart: print " " * (int((width - 26) / 2) - 1), i.rstrip()
        asciiart.close()
    except:
        pass


def printAsciiArtServer():
    """
    Imprime el arte ascii de la introducción del servidor
    :return: void
    """
    if _wconio: WConio.clrscr()
    try:
        (width, height) = getTerminalSize()  # se obtiene el largo de la consola para dejarlo centrado
        asciiart = open("data/doc/other/asciiartserver.txt", "r")
        for i in asciiart: print " " * (int((width - 26) / 2) - 1), i.rstrip()
        asciiart.close()
    except:
        pass


def printSimpleMatrix(matrix):
    """
    Función que imprime un vector
    :param matrix: Lista
    :return: void
    """
    for j in matrix:
        print j,
    print ""


def printMatrix(matrix):
    """
    Función que imprime una matriz en pantalla
    :param matrix: Lista
    :return: void
    """
    for j in matrix:
        for k in j: print k,
        print "\n"


def putStrict(a):
    """
    Función que retorna los carácteres restrictivos
    :param a: String
    :return: String formateado
    """
    return a.replace("%XCOM%", ",").replace("%XPYC%", ";").replace("%XDP%", ":").replace("%XGUI%", "-").replace("%XII%",
                                                                                                                "'").replace(
        "%XLASH%", "/")


def redondear(l, n):
    """
    Obtiene el número de filas para ubicar los botones del juego
    :param l: Integer
    :param n: Integer
    :return: Integer redondeado
    """
    if (float(l) / n - int(l / n)) * 10 > 0:
        return int(l / n) + 1
    else:
        return int(l / n)


def replaceStrict(a):
    """
    Función que reemplaza los carácteres restrictivos
    :param a: String
    :return: String formateado
    """
    return a.replace(",", "%XCOM%").replace(";", "%XPYC%").replace(":", "%XDP%").replace("-", "%XGUI%").replace("\\",
                                                                                                                "").replace(
        "'", "%XII%").replace("/", "%XLASH%")


# noinspection PyShadowingBuiltins
def sortAndUniq(input):
    """
    Función que elimina datos repetidos
    :param input: Lista
    :return: Lista limpia
    """
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    output.sort()
    return output


def libstartUp():
    """
    Función destinada a la primera ejecución del programa
    :return: void
    """
    if not (("-launcher" in sys.argv or "-eclipse" in sys.argv or "-cmd" in sys.argv) or len(
            sys.argv) == 1) and not DEV_MODE:  # Se comprueba el lanzador
        sys.stderr.write("Error :: Lanzador no valido\n")
        exit()
    else:
        if "-launcher" in sys.argv:
            sys.stdout, sys.stderr, sys.stdin, sys.__stdout__, sys.__stderr__, sys.__stdin__ = noStdOut(), noStdOut(), noStdOut(), noStdOut(), noStdOut(), noStdOut()
    if not (sys.version_info.major == 2 and sys.version_info.minor == 7):  # Se comprueba que Python sea 2.7.x
        version_actual = "(version actual: {0}.{1}.{2})\n".format(sys.version_info.major, sys.version_info.minor,
                                                                  sys.version_info.micro)
        sys.stderr.write("Error :: HOA solo puede ejecutarse en versiones 2.7.x de Python " + version_actual)
        try:
            url = "https://www.python.org/download/releases/"
            sys.stderr.write("Redirigiendo a la pagina de descargas de Python <{0}>\n".format(url))
            time.sleep(2)
            webbrowser.open(url)
        except:
            pass
        exit()


def sumMatrix(matrix):
    """
    Función que suma lista de listas
    :param matrix: Lista
    :return: Integer
    """
    suma = 0
    try:
        for j in matrix:
            for k in j: suma += k
        return suma
    except:
        return -1


def toHour(hour):
    """
    Función que genera un string de hora dado una hora en minutos
    :param hour: String
    :return: String formateado
    """
    hour = str(hour).split(".")
    minuto = int(hour[0])
    segundo = int(hour[1]) * 6
    return str(minuto) + ":" + str(segundo).zfill(2)


def whatTile(x, y):
    """
    Obtener el recuadro clickeado en el editor de mapas
    :param x: Pos X
    :param y: Pos Y
    :return: (x,y), integer
    """
    return int(y / 32), int(x / 32)


def whatTileD(x, dx, y, dy):
    """
    Retorna el recuadro clickeado usando una corrección (dx,dy)
    :param x: Pos x
    :param dx: diff X
    :param y: Pos Y
    :param dy: diff y
    :return: (x,y), integer
    """
    return int((x - dx) / 32), int((y - dy) / 32)
