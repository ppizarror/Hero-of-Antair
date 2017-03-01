# -*- coding: utf-8 -*-
"""
HOA
Hero of Antair, motor gráfico para juego RPG.

Autor: PABLO PIZARRO @ ppizarror
Fecha: 2013-2015, 2017
Licencia: GPLv2
"""

# Importación de librerías de alto nivel
from lib import *  # @UnusedWildImport
from release import *

# Inicio del sistema
libstartUp()
lookPrimaryArguments(PROGRAM_VERSION)  # se buscan los argumentos primarios
if getConfigValue("terminal.art",
                  True):  # se imprime el arte @UndefinedVariable
    printAsciiArtHOA()
__versionstr__ = "HOA - version: " + PROGRAM_VERSION
if getConfigValue("terminal.version.colored"):
    if isWindows():
        colorcmd(__versionstr__, choice(CMD_COLORS.keys()))
    else:
        print __versionstr__
else:
    print __versionstr__
print "\nAutor: " + AUTOR_NAME

# Importación de librerías
print "\nCargando librerias ...",
try:
    from actors import actors
    from board import *  # @UnusedWildImport
    from item import *  # @UnusedWildImport
    from mob import mob, MOB_SEPARATOR, TIME_MOVE_MOBS_NORMAL
    from npc import npc, NPC_SEPARATOR, NPC_TIME_MOVEMENT
    from pop import pop
    from powers import *
    from sounds import *  # @UnusedWildImport
    from textures import *  # @UnusedWildImport
    import statics
    import zipfile  # @Reimport
except Exception, e:
    print "error"
    st_error("Error al cargar librerias internas", True, "hoa.py", e)
    exit()
print OK

# Configuración de las librerías
gc.enable()

# Se realiza un test benchmark para comprobar tiempos de ejecución
print "Realizando prueba de hardware ...",
ms = benchmark(False, False, 2)
if 0 <= ms <= 0.05:
    print "alto rendimiento"
    AI_ATTACK = 1500  # tiempo de ataque combate grupal ai
    DPX = 0.2  # diferencial de pixeles
    LIMIT_MESSAGES_CONSOLE = 1000  # límite máximo de mensajes en consola
    MOVETIME = 100  # tiempo minimo de tiempo para poder mover al jugador
    TEXDT = 120  # tiempo despues de mover texturas
elif 0.05 < ms <= 0.10:
    print "medio rendimiento"
    AI_ATTACK = 2000  # tiempo de ataque combate grupal ai
    DPX = 0.4  # diferencial de pixeles
    LIMIT_MESSAGES_CONSOLE = 500  # límite máximo de mensajes en consola
    MOVETIME = 170  # tiempo minimo de tiempo para poder mover al jugador
    TEXDT = 170  # tiempo despues de mover texturas
elif 0.10 < ms:
    print "bajo rendimiento"
    AI_ATTACK = 2500  # tiempo de ataque combate grupal ai
    DPX = 0.6  # diferencial de pixeles
    LIMIT_MESSAGES_CONSOLE = 250  # límite máximo de mensajes en consola
    MOVETIME = 250  # tiempo minimo de tiempo para poder mover al jugador
    TEXDT = 220  # tiempo despues de mover texturas
if not isWindows():
    LIMIT_MESSAGES_CONSOLE = 100

# Constantes del programa
ATTACK_MIN_TIME = 350  # tiempo mínimo en milisegundos entre ataques
# idiomas disponibles para imprimir en consola
AVAIABLE_LANGS_TOPRINT = ["es", "en", "de", "it", "fr", "pr-pt"]
AVAIABLE_WALK = ["none", "pass", "movefrom", "grass",
                 "alfombra"]  # lógicos donde se puede caminar
CANVAS_SIZE = 608, 576  # tamaño de la ventana de dibujo
CANVAS_MAX_SIZE = [18, 19]  # tamaño máximo del canvas
CONFIGURATION_DATA = ["ES", True, False, "#000000", "#FFFFFF",
                      "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
                      "http://translate.google.com/translate_a/t?", "OFF",
                      "es", False, False, True, True, True, True,
                      True, True,
                      False]  # configuraciones por defecto en caso de omisión
COLORED_ARGUMENT = False  # si los argumentos poseen color
DATA_CONFIG = ACTUAL_FOLDER + "config/"  # carpeta de configuraciones
DATA_DOCUMENTS = DATA_FOLDER + "doc/"  # carpeta de documentos"c
DATA_FOLDER = ACTUAL_FOLDER + "data/"  # carpeta de datos
DATA_LANGS = ACTUAL_FOLDER + "langs/"  # carpeta de idiomas
DATA_LEVELS = DATA_FOLDER + "levels/"  # carpeta de niveles
DATA_SAVES_NO_DIRECTORY = "saves/"  # carpeta de guardados
# link para guardar de forma correcta
DATA_SAVES = ACTUAL_FOLDER + DATA_SAVES_NO_DIRECTORY
DEFAULT_LANG_CONTENT = "es"  # idioma por defecto
DEFAULT_LEVEL = "start.lvl"  # mapa de inicios
DIFICULTAD_DIFICIL = "dificil"  # dificultad dificil
DIFICULTAD_FACIL = "facil"  # dificultad fácil
DIFICULTAD_MEDIO = "medio"  # dificultad media
CONFIGURATION_ACTL = DATA_CONFIG + "actl.ini"  # actualización del programa
CONFIGURATION_ARGS = DATA_CONFIG + "args.ini"  # argumentos por defecto
CONFIGURATION_FILE = DATA_CONFIG + "config.ini"  # archivo de configuración
# configuración de las traducciones
CONFIGURATION_TNSL = DATA_CONFIG + "transl.ini"
ERROR_DELAY = 5000  # tiempo de espera antes de abortar el juego
LANG = {}  # lista de strings para el idioma
LEVELS_RES = DATA_LEVELS + "res/"  # carpeta de los recursos del nivel
LEVEL_SOUND = DATA_LEVELS + "sound/"  # carpeta de sonidos de los niveles
MODE_FIGHT_GROUP = "GRUPAL"  # modo de pelea grupal (tablero)
MODE_FIGHT_NORMAL = "NORMAL"  # modo de pelea normal
MODE_FIGHT_LINEAL = "LINEAL"  # modo de pelea lineal
MOSTRAR_INFO_PLAYER = False  # indica si se muestra o no la información del jugador
# indica si el movimiento se realiza con animación (player)
MOVEMENT_ANIMATION = [True]
NULL_CONECTION = [-1, None]  # indica la conexión nula
PLAYER_TEXT_TIME = 600  # duración de los mensajes flash
QUEST_DELIMITER = "%"  # short que delimita la división lógica de los quest
SHOWMESSAGESTIME = 3500  # tiempo para mostrar los mensajes
# tiempo en milisegundos para mostrar efectos (flechas, fuego etc)
TIME_DISSAPEAR_EFFECT = 1000
TKSNACK = [True]  # sonidos del sistema
WIDTHMESSAGES = 210  # largo máximo de los recuadros de texto
try:
    LANG_LIST = loadFromArchive(
        DATA_LANGS + "/config/langs.txt", "Cargando archivo '{0}' ...", False)
    LANG_CONST = loadFromArchive(
        DATA_LANGS + "/config/const.ini", "Cargando archivo '{0}' ...", False)
    LANG_END = LANG_CONST[0]
    LANG_SEP = LANG_CONST[1].replace("*", " ")
except:  # Si ocurre un error al cargar el archivo de idiomas se termina la ejecución del programa
    st_error("Error fatal")
    pop([["Error fatal", "Cerrar"], DATA_ICONS + "cross.ico", "error", 88, 300,
         "No se encuentra el archivo de idiomas, " +
         PROGRAM_TITLE + " no puede iniciarse."]).w.mainloop(0)
    exit()
if isWindows():
    _SECOND_BUTTON = "<Button-3>"
    BAR_POND_COEF = 1.0
    DRAW_CANVAS_OFFSET_X = 0
    DRAW_CANVAS_OFFSET_Y = 0
    POP_XSIZE = 165
    POP_YSIZE = 270
    PROGRAM_SIZE = 804, 600
else:
    if isOSX():
        _SECOND_BUTTON = "<Button-2>"
        BAR_POND_COEF = 1.2
        DRAW_CANVAS_OFFSET_X = -2
        DRAW_CANVAS_OFFSET_Y = -2
        POP_XSIZE = 175
        POP_YSIZE = 390
        PROGRAM_SIZE = 817, 574
    elif isLinux():
        _SECOND_BUTTON = "<Button-3>"
        BAR_POND_COEF = 1.2
        DRAW_CANVAS_OFFSET_X = -1
        DRAW_CANVAS_OFFSET_Y = -2
        POP_XSIZE = 175
        POP_YSIZE = 390
        PROGRAM_SIZE = 834, 574
    else:
        _SECOND_BUTTON = "<Button-3>"
        BAR_POND_COEF = 1.0
        DRAW_CANVAS_OFFSET_X = 0
        DRAW_CANVAS_OFFSET_Y = 0
        POP_XSIZE = 165
        POP_YSIZE = 270
        PROGRAM_SIZE = 804, 600

# Configuración del programa
try:  # Se cargan las configuraciones
    print "Consultando configuraciones ...",
    # cargo archivo de configuraciones
    conf_file = open(CONFIGURATION_FILE, "r")
    # noinspection PyShadowingNames,PyShadowingNames
    for i in conf_file:
        # noinspection PyShadowingNames
        i = i.strip()
        c_command = i.split("=")
        if c_command[
            0].strip() == "CONSOLE_BACKGROUND":  # Color de fondo de la consola
            c_after_command = str(c_command[1]).split(",")
            CONFIGURATION_DATA[3] = c_after_command[0].strip().upper()
        if c_command[
            0].strip() == "CONSOLE_FOREGROUND":  # Color del texto de la consola
            c_after_command = str(c_command[1]).split(",")
            CONFIGURATION_DATA[4] = c_after_command[0].strip().upper()
        if c_command[0].strip() == "SAVE_ON_EXIT":  # Guardar al salir
            c_after_command = str(c_command[1]).split(",")
            if c_after_command[0].strip().upper() == "ON":
                CONFIGURATION_DATA[2] = True
            else:
                CONFIGURATION_DATA[2] = False
        if c_command[0].strip() == "LANGUAJE":  # idioma
            c_after_command = str(c_command[1]).split(",")
            # noinspection PyUnboundLocalVariable
            if len(c_after_command[0].strip()) != 0 and (
                            c_after_command[
                                0].strip().upper() + LANG_END in LANG_LIST):
                CONFIGURATION_DATA[0] = c_after_command[0].strip().upper()
        if c_command[0].strip() == "SOUND":  # sonido
            c_after_command = str(c_command[1]).split(",")
            if c_after_command[0].strip().upper() == "ON":
                CONFIGURATION_DATA[1] = True
            else:
                CONFIGURATION_DATA[1] = False
    conf_file.close()
except:  # Se genera un nuevo archivo de configuraciones si este no existe
    print "generando configuraciones ...",
    archivo = open(CONFIGURATION_FILE, "w")
    archivo.write("#Archivo de Configuraciones\n")
    archivo.write(
        "#No haga cambios indebidos, ellos pueden afectar al comportamiento del programa\n\n")
    archivo.write("#Colores de la consola\n")
    archivo.write("CONSOLE_BACKGROUND = " + str(CONFIGURATION_DATA[3]) + "\n")
    archivo.write("CONSOLE_FOREGROUND = " +
                  str(CONFIGURATION_DATA[4]) + "\n\n")
    archivo.write("#Guardar al salir\n")
    archivo.write("SAVE_ON_EXIT = OFF\n\n")
    archivo.write("#Idioma\n")
    archivo.write("LANGUAJE = " + str(CONFIGURATION_DATA[0]) + "\n\n")
    archivo.write("#Sonidos del programa\n")
    archivo.write("SOUND = ON")
    archivo.close()
print OK
try:  # Se cargan las configuraciones del servicio de traducciones
    print "Consultando configuraciones del servicio de traducciones ...",
    config = open(CONFIGURATION_TNSL, "r")
    # noinspection PyShadowingNames
    for i in config:  # Se recorren las lineas de las configuraciones
        if ("#" not in i) and i != "":  # Si la linea es válida
            i = i.split("=")
            if i[0].strip() == "HEADER":
                CONFIGURATION_DATA[5] = i[1].strip()
            if i[0].strip() == "HREF":
                CONFIGURATION_DATA[6] = i[1].strip()
            if i[0].strip() == "ACTIVE":
                CONFIGURATION_DATA[7] = i[1].strip()
    config.close()
except:  # Si no existe el archivo de configuración de las traducciones
    print "generando configuraciones ...",
    archivo = open(CONFIGURATION_TNSL, "w")
    archivo.write("#Configuraciones del servicio de traducciones (google)\n")
    archivo.write(
        "#No haga cambios indebidos, ellos pueden afectar al comportamiento del programa\n\n")
    archivo.write("ACTIVE = " + str(CONFIGURATION_DATA[7]) + "\n")
    archivo.write("HEADER = " + str(CONFIGURATION_DATA[5]) + "\n")
    archivo.write("HREF = " + str(CONFIGURATION_DATA[6]))
    archivo.close()
print OK
ST_HEADER = CONFIGURATION_DATA[5]  # header de las consultas http
ST_HREF = CONFIGURATION_DATA[6]  # link de las consultas http
ST_TRANSLATE = False  # lógico que define si se busca o no
# idioma de destino para las traducciones
CONFIGURATION_DATA[8] = CONFIGURATION_DATA[0].lower()
if CONFIGURATION_DATA[8] == "zh-cn":
    CONFIGURATION_DATA[8] = "zh-CN"  # si es chino se modifica
if CONFIGURATION_DATA[8] == "pt-pt":
    CONFIGURATION_DATA[8] = "pt-PT"  # si es portugués se modifica
if CONFIGURATION_DATA[7] == "ON" and CONFIGURATION_DATA[
    8] != DEFAULT_LANG_CONTENT:
    CONFIGURATION_DATA[9] = True  # si el idioma es el de origen no se traduce
else:
    CONFIGURATION_DATA[9] = False  # si no se cumple se desactiva
if CONFIGURATION_DATA[7] == "ON" or (
            "-enabletranslation" in sys.argv):  # Si el servicio está disponible (o se envio por parámetro)
    if "-enabletranslation" in sys.argv:
        CONFIGURATION_DATA[17] = True
        CONFIGURATION_DATA[10] = True
    CONFIGURATION_DATA[9] = True
    # Consulto el servicio de traducciones (google translate) para comprobar
    # la conexión
    try:
        print "Conectando estado del servicio de traducciones ...",
        google_translate("test", "es", ST_HEADER, ST_HREF, "en")
        print OK
        ST_TRANSLATE = True
    except:
        # noinspection PyShadowingBuiltins
        CONFIGURATION_DATA[10] = False, CONFIGURATION_DATA[
            # @ReservedAssignment
            9] = False
        print "abortado"  # si ocurre algún error en la conexión en el servicio
    if CONFIGURATION_DATA[8] == "es":
        CONFIGURATION_DATA[10] = False
        CONFIGURATION_DATA[9] = False


# Funciones de idiomas
def translate(text):
    """
    Función que traduce un texto usando el servicio de google traductor
    :param text: String
    :return: String
    """
    if (ST_TRANSLATE and CONFIGURATION_DATA[9]) or (
                CONFIGURATION_DATA[10] and CONFIGURATION_DATA[
                9]):  # Si el servicio está activo
        try:  # Se consulta por la traducción al servicio de google
            return google_translate(text, CONFIGURATION_DATA[8], ST_HEADER,
                                    ST_HREF)
        except:  # Si ocurre algún error en la traducción
            return text
    else:
        return text


def loadLang(first=True):
    """
    Carga el idioma
    :param first: Boolean
    :return: void
    """
    try:  # Se carga el idioma
        if COLORED_ARGUMENT:  # argumento colorido
            if first:
                print "Cargando idioma",
                colorcmd(CONFIGURATION_DATA[0].lower(), "lgray")
                print "...",
            else:
                print lang(746),
                colorcmd(CONFIGURATION_DATA[0].lower(), "lgray")
                print "...",
        else:
            if first:
                print "Cargando idioma", CONFIGURATION_DATA[0].lower(), "...",
            else:
                print lang(746), CONFIGURATION_DATA[0].lower(), "...",
        archivo = open(DATA_LANGS + CONFIGURATION_DATA[0] + LANG_END, "r")
        for i in archivo:
            item = i.strip().replace("\ufeff", "").split(LANG_SEP)
            if "\xef\xbb\xbf" in item[0]:
                item[0] = item[0][3:]  # elimino caracteres que no sean utf-8
            if item[0] == "":
                item[0] = "10"
            LANG[int(item[0].replace("\ufeff", ""))] = item[
                1].replace("|", " ")  # asigno los espacios
        LANG[310] = OK
        archivo.close()
        print OK
    except:  # Error al cargar idioma, muestra mensaje y termina el programa
        st_error("Error fatal")
        pop([["Error fatal", "Cerrar"], DATA_ICONS + "cross.ico", "error", 88,
             300,
             "Error al cargar el archivo de idioma '" +
             CONFIGURATION_DATA[
                 0] + "', " + PROGRAM_TITLE + " no puede iniciarse"]).w.mainloop(
            0)
        exit()


# noinspection PyShadowingNames
def lang(i, a="", b="", c="", e=None):
    """
    Función que recibe un id y retorna el string correspondiente a dicho id (sin traducir)
    :param i: Index
    :param a: String
    :param b: String
    :param c: String
    :param e: Objeto del tipo Exception
    :return: String formateado asociado al indice i
    """
    try:  # Si existe el lang en la matriz de datos
        if len(a + b + c) != 0:
            data = LANG[i].replace("%", a).replace("&", b).replace("$", c)
        else:
            data = LANG[i]
        if "Error[" in data:  # Formateo de error
            data = parseLangError(data, e)
        return data
    except:
        st_error("ID<{0}> no existe en el archivo de idiomas '".format(
            i) + CONFIGURATION_DATA[0] + "'")
        return "%LANG ID[{0}]".format(i)


# noinspection PyShadowingNames
def langError(i, e):
    """
    Imprime un error con su modulo en err
    :param i: Index
    :param e: Objeto del tipo Exception
    :return: String formateado asociado al indice i
    """
    return lang(i, "", "", "", e)


# noinspection
# PyShadowingNames,PyShadowingBuiltins,PyUnboundLocalVariable,PyDeprecation,PyUnreachableCode
# noinspection PyUnresolvedReferences,PyShadowingNames,PyUnresolvedReferences,PyShadowingNames,PyUnboundLocalVariable,PyDeprecation,PyUnreachableCode,PyArgumentList,PyShadowingBuiltins,PyGlobalUndefined
class hoa(object):
    """Main"""

    # noinspection PyDefaultArgument
    def __init__(self, arguments=[]):
        """
        Función constructora, ella recibe un archivo de guardado, si existe se carga
        :type self: object
        :param arguments: Argumentos
        :return: void
        """

        # Métodos del constructor
        def _about(e=None):
            """
            Función que muestra el acerca de
            :param e: Evento
            :return: void
            """
            e = pop(
                [[lang(18), lang(170), lang(171), lang(172), lang(173)],
                 self.images.image("icon"), "about", 115, 220,
                 AUTOR_NAME, AUTOR_NAME_EMAIL, PROGRAM_VERSION])
            e.w.mainloop(1)
            del e

        def _ayuda(e=None):
            """
            Función que carga la ayuda del juego
            :param e: Evento
            :return: void
            """
            e = pop([lang(19), self.images.image("icon"), "license",
                     400, 600, DATA_DOCUMENTS + "/hoa/ayuda.txt"])
            e.w.mainloop(1)
            del e

        def _changelog(e=None):
            """
            Función que muestra a lista de cambios
            :param e: Evento
            :return: void
            """
            e = pop([lang(20), self.images.image("icon"), "license",
                     400, 650, ACTUAL_FOLDER + "CHANGELOG"])
            e.w.mainloop(1)
            del e

        def _configure(e=None):
            """
            Configurar el juego
            :param e: Evento
            :return: void
            """
            if CONFIGURATION_DATA[
                13]:  # Si las configuraciones no están desactivadas
                conf = pop(
                    [[lang(17), lang(217), lang(218), lang(219), lang(64),
                      lang(273), lang(274), lang(275), lang(671),
                      lang(672), lang(679), lang(677), lang(674), lang(
                            682), lang(683), lang(686), lang(687), lang(680),
                      lang(681), lang(675), lang(685), lang(673), lang(
                            678), lang(684), lang(676), lang(688), lang(400),
                      lang(800), lang(54)],
                     self.images.image(
                         "configuration_icon"), "config_hoa", 262, 307,
                     CONFIGURATION_DATA[0],
                     CONFIGURATION_DATA[1], DATA_LANGS, LANG_END,
                     CONFIGURATION_DATA[
                         2], CONFIGURATION_DATA[3],
                     CONFIGURATION_DATA[4]])
                conf.w.mainloop(1)
                if conf.sent:  # Se genera un nuevo archivo de configuraciones
                    print lang(689),
                    archivo = open(CONFIGURATION_FILE, "w")
                    archivo.write("#Archivo de Configuraciones\n")
                    archivo.write(
                        "#No haga cambios indebidos, ellos pueden afectar al comportamiento del programa\n\n")
                    archivo.write("#Colores de la consola\n")
                    archivo.write("CONSOLE_BACKGROUND = " +
                                  str(conf.values[3]) + "\n")
                    archivo.write("CONSOLE_FOREGROUND = " +
                                  str(conf.values[4]) + "\n\n")
                    archivo.write("#Guardar al salir\n")
                    if conf.values[2]:
                        archivo.write("SAVE_ON_EXIT = ON\n\n")
                    else:
                        archivo.write("SAVE_ON_EXIT = OFF\n\n")
                    archivo.write("#Idioma\n")
                    archivo.write("LANGUAJE = " + str(conf.values[0]) + "\n\n")
                    archivo.write("#Sonidos del programa\n")
                    if conf.values[1]:
                        archivo.write("SOUND = ON")
                    else:
                        archivo.write("SOUND = OFF")
                    archivo.close()
                    print lang(310)
                    print lang(690),
                    self.info.config(bg=conf.values[3], fg=conf.values[4])
                    CONFIGURATION_DATA[1] = conf.values[1]
                    CONFIGURATION_DATA[2] = conf.values[2]
                    CONFIGURATION_DATA[3] = conf.values[3]
                    CONFIGURATION_DATA[4] = conf.values[4]
                    if not conf.values[1]:
                        self.stopSound("silent")
                    else:
                        CONFIGURATION_DATA[1] = True
                    if conf.values[2]:
                        CONFIGURATION_DATA[2] = True
                    if CONFIGURATION_DATA[0] != conf.values[
                        0]:  # Si cambió el idioma
                        CONFIGURATION_DATA[0] = conf.values[0]
                        CONFIGURATION_DATA[8] = CONFIGURATION_DATA[0].lower()
                        if CONFIGURATION_DATA[8] == "zh-cn":
                            CONFIGURATION_DATA[8] = "zh-CN"
                        if CONFIGURATION_DATA[8] == "pt-pt":
                            CONFIGURATION_DATA[8] = "pt-PT"
                        if CONFIGURATION_DATA[7] == "ON" and \
                                        CONFIGURATION_DATA[
                                            8] != DEFAULT_LANG_CONTENT:
                            CONFIGURATION_DATA[9] = True
                        else:
                            if not CONFIGURATION_DATA[17]:
                                if CONFIGURATION_DATA[10] and \
                                        CONFIGURATION_DATA[9]:
                                    pass
                                else:
                                    CONFIGURATION_DATA[9] = False
                            if CONFIGURATION_DATA[8] == "es":
                                CONFIGURATION_DATA[10] = False
                                CONFIGURATION_DATA[
                                    9] = False
                        LANG = {}
                        loadLang(False)
                        self.setInfo(lang(142))
                        self.info.config(bg=conf.values[3], fg=conf.values[4])
                        self.menubar.delete(0, 3)
                        self.archivomenu = Menu(self.menubar, tearoff=0)
                        if isWindows():
                            self.archivomenu.add_command(label=lang(
                                10), command=self.newGame,
                                accelerator="Ctrl+N")
                            self.archivomenu.add_command(label=lang(
                                11), command=self.loadGame,
                                accelerator="Ctrl+L")
                            self.archivomenu.add_command(label=lang(
                                12), command=self.saveGame,
                                accelerator="Ctrl+G")
                            self.archivomenu.add_command(
                                label=lang(13), command=self.abortGame)
                            self.archivomenu.add_separator()
                            self.archivomenu.add_command(label=lang(
                                17), command=_configure, accelerator="Ctrl+C")
                            self.archivomenu.add_command(label=lang(
                                15), command=self.salir, accelerator="Ctrl+S")
                            self.menubar.add_cascade(
                                label=lang(16), menu=self.archivomenu)
                            self.vermenu = Menu(self.menubar, tearoff=0)
                            self.vermenu.add_command(label=lang(
                                702), command=_verFollowers, accelerator="U")
                            self.vermenu.add_command(label=lang(
                                323), command=_showPlayerInfo, accelerator="I")
                            self.vermenu.add_command(label=lang(
                                14), command=_showStatics,
                                accelerator="Ctrl+E")
                            self.vermenu.add_command(label=lang(
                                587), command=_verQuest, accelerator="T")
                            self.vermenu.add_command(label=lang(
                                322), command=_showMap, accelerator="M")
                            self.menubar.add_cascade(
                                label=lang(321), menu=self.vermenu)
                            self.ayudamenu = Menu(self.menubar, tearoff=0)
                            self.ayudamenu.add_command(
                                label=lang(18), command=_about)
                            self.ayudamenu.add_command(label=lang(
                                19), command=_ayuda, accelerator="F1")
                            self.ayudamenu.add_command(
                                label=lang(20), command=_changelog)
                            self.ayudamenu.add_command(
                                label=lang(21), command=_licence)
                            self.ayudamenu.add_separator()
                            self.ayudamenu.add_command(label=lang(
                                327), command=self.update, accelerator="F5")
                            self.ayudamenu.add_command(label=lang(
                                326), command=self.devConsole,
                                accelerator="F2")
                            if "-eclipse" in sys.argv:
                                self.ayudamenu.add_command(label=lang(325),
                                                           command=_infoSystem,
                                                           accelerator="F12")
                        else:
                            self.archivomenu.add_command(
                                label=lang(10), command=self.newGame)
                            self.archivomenu.add_command(label=lang(
                                11), command=self.loadGame,
                                accelerator="Control+L")
                            self.archivomenu.add_command(label=lang(
                                12), command=self.saveGame,
                                accelerator="Control+G")
                            self.archivomenu.add_command(
                                label=lang(13), command=self.abortGame)
                            self.archivomenu.add_separator()
                            self.archivomenu.add_command(
                                label=lang(17), command=_configure)
                            self.archivomenu.add_command(
                                label=lang(15), command=self.salir)
                            self.menubar.add_cascade(
                                label=lang(16), menu=self.archivomenu)
                            self.vermenu = Menu(self.menubar, tearoff=0)
                            self.vermenu.add_command(
                                label=lang(702), command=_verFollowers)
                            self.vermenu.add_command(
                                label=lang(323), command=_showPlayerInfo)
                            self.vermenu.add_command(
                                label=lang(14), command=_showStatics)
                            self.vermenu.add_command(
                                label=lang(587), command=_verQuest)
                            self.vermenu.add_command(
                                label=lang(322), command=_showMap)
                            self.menubar.add_cascade(
                                label=lang(321), menu=self.vermenu)
                            self.ayudamenu = Menu(self.menubar, tearoff=0)
                            self.ayudamenu.add_command(
                                label=lang(18), command=_about)
                            self.ayudamenu.add_command(
                                label=lang(19), command=_ayuda)
                            self.ayudamenu.add_command(
                                label=lang(20), command=_changelog)
                            self.ayudamenu.add_command(
                                label=lang(21), command=_licence)
                            self.ayudamenu.add_separator()
                            self.ayudamenu.add_command(label=lang(
                                327), command=self.update, accelerator="F5")
                            self.ayudamenu.add_command(
                                label=lang(326), command=self.devConsole)
                            if "-eclipse" in sys.argv:
                                self.ayudamenu.add_command(
                                    label=lang(325), command=_infoSystem)
                        self.menubar.add_cascade(
                            label=lang(19), menu=self.ayudamenu)
                        self.vidaLabel.config(text=lang(22))
                        self.manaLabel.config(text=lang(23))
                        self.experienciaLabel.config(text=lang(24))
                        self.poderFrame.config(text=" " + lang(314))
                        self.itemFrame.config(text=lang(25))
                        if not CONFIGURATION_DATA[11]:
                            self.ayudamenu.entryconfig(6, state=DISABLED)
                        if self.ingame:  # Si se encuentra en una partida activa
                            if CONFIGURATION_DATA[12]:
                                self.archivomenu.entryconfig(2, state=NORMAL)
                            else:
                                self.archivomenu.entryconfig(2, state=DISABLED)
                            self.archivomenu.entryconfig(3, state=NORMAL)
                            for k in range(5):
                                self.vermenu.entryconfig(k, state=NORMAL)
                        else:
                            self.archivomenu.entryconfig(2, state=DISABLED)
                            self.archivomenu.entryconfig(3, state=DISABLED)
                            for k in range(5):
                                self.vermenu.entryconfig(k, state=DISABLED)
                        if CONFIGURATION_DATA[
                            8] not in AVAIABLE_LANGS_TOPRINT:  # Desactivar la función print si el idioma no es español o ingles
                            sys.stdout, sys.stderr, sys.stdin, sys.__stdout__, sys.__stderr__, sys.__stdin__ = noStdOut(), noStdOut(), noStdOut(), \
                                                                                                               noStdOut(), noStdOut(), noStdOut()
                    else:
                        print lang(310)
                        # Si ocurrió un cambio profundo
                        # e = pop([[lang(220),lang(173)],self.images.image("configuration_icon"),"aviso",85,300,lang(221)])
                        # e.w.mainloop(2); del e
                del conf

        def _consultArgument(argument, arguments):
            """
            Función que consulta la existencia de un argumento
            :param argument: Argumento
            :param arguments: Lista de argumentos
            :return: Booleano
            """
            if len(arguments) == 0:
                return False
            for i in arguments:
                if i[0] == argument:
                    if COLORED_ARGUMENT:
                        print lang(286),
                        colorcmd(argument, "lgray")
                        print ""
                    else:
                        print argument,
                    return True
            return False  # si no existe retorna falso

        def _infoSystem(e=None):
            """
            Función que imprime la información de la memoria y las librerías cargadas
            :param e: Event
            :return: void
            """
            print "#"
            print lang(288)
            print "#"
            all_objects = muppy.get_objects()
            libs = muppy.filter(all_objects, Type=types.ClassType)
            print lang(289)
            for i in libs:
                print "#\t" + str(i)
            sum1 = summary.summarize(all_objects)
            print "#"
            print lang(290)
            summary.print_(sum1)
            print "#"

        def _itemArmadura(tipo, typeClick, x=None):
            """
            Función que maneja la armadura y los eventos
            :param tipo: Tipo de item
            :param typeClick: Tipo de click
            :param x: Event
            :return: void
            """
            if typeClick == 1:  # Click derecho, información
                if CONFIGURATION_DATA[14]:  # Si está activa la opción
                    if tipo == "casco":
                        item = self.player.getCasco()
                        if item is not None:
                            self.sfx(23)
                            k = pop([[lang(34), lang(243), lang(242),
                                      lang(173), lang(248)],
                                     DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                     "itemInfoArmor", POP_XSIZE, POP_YSIZE,
                                     translate(
                                         putStrict(item.getName())),
                                     "armadura", translate(
                                    putStrict(item.getDescription())),
                                     item.getDefense(), item.getUsos()])
                            k.w.mainloop(1)
                            if k.sent:  # Si se envía un evento
                                action = k.values[0]
                                if action == "drop":
                                    self.player.dropCasco()
                                    self.sfx(20)
                                    self.setInfo(lang(40))
                                    self.static.addDroppedArmor()
                                    self.infoArmaduraCasco.config(
                                        image=self.images.image("no_casco"),
                                        state=DISABLED,
                                        cursor="arrow")
                            del k
                    elif tipo == "izquierda":
                        item = self.player.getLeftWeapon()
                        if item is not None:
                            if isIn(item.getImage(), ARROW_WEAPONS_PREFIX):
                                self.sfx(24)
                            else:
                                self.sfx(34)
                            if self.player.getActiveBullet() is not None:
                                # se obtiene la cantidad de usos del armamento
                                # si es que tiene
                                bu = self.player.getActiveBullet().getUsos()
                                ba = self.player.getActiveBullet().getDamage()  # se obtiene el daño
                            else:
                                bu = 0
                                ba = 0
                            k = pop([[lang(35), lang(241), lang(242),
                                      lang(173), lang(248), lang(267),
                                      lang(266)],
                                     DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                     "itemInfoArmor", POP_XSIZE,
                                     POP_YSIZE,
                                     translate(
                                         putStrict(item.getName())), "armawb",
                                     translate(
                                         putStrict(item.getDescription())),
                                     item.getDamage(), item.getUsos(), bu, ba])
                            k.w.mainloop(1)
                            if k.sent:  # Si se envía un evento
                                action = k.values[0]
                                if action == "drop":
                                    self.player.dropLeftWeapon()
                                    self.sfx(35)
                                    self.setInfo(lang(41))
                                    self.static.addDroppedWeapon()
                                    self.infoArmaduraArmaIzquierda.config(
                                        image=self.images.image("no_lw"),
                                        state=DISABLED, cursor="arrow")
                                    if self.player.getActiveBullet() is not None:
                                        self.player.addObject(
                                            self.player.getActiveBullet())
                                        self.player.delActiveBullet()
                                    self.dibujarMundo()
                            del k
                    elif tipo == "chaleco":
                        item = self.player.getChaleco()
                        if item is not None:
                            self.sfx(23)
                            k = pop([[lang(36), lang(243), lang(242),
                                      lang(173), lang(248)],
                                     DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                     "itemInfoArmor", POP_XSIZE, POP_YSIZE,
                                     translate(
                                         putStrict(item.getName())),
                                     "armadura", translate(
                                    putStrict(item.getDescription())),
                                     item.getDefense(), item.getUsos()])
                            k.w.mainloop(1)
                            if k.sent:  # Si se envía un evento
                                action = k.values[0]
                                if action == "drop":
                                    self.player.dropChaleco()
                                    self.sfx(20)
                                    self.setInfo(lang(42))
                                    self.static.addDroppedArmor()
                                    self.infoArmaduraChaleco.config(
                                        image=self.images.image("no_chaleco"),
                                        state=DISABLED, cursor="arrow")
                            del k
                    elif tipo == "derecha":
                        item = self.player.getRightWeapon()
                        if item is not None:
                            if isIn(item.getImage(), ARROW_WEAPONS_PREFIX):
                                self.sfx(24)
                            else:
                                self.sfx(34)
                            k = pop([[lang(37), lang(241), lang(242),
                                      lang(173), lang(248)],
                                     DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                     "itemInfoArmor", POP_XSIZE, POP_YSIZE,
                                     translate(
                                         putStrict(item.getName())),
                                     "arma", translate(
                                    putStrict(item.getDescription())),
                                     item.getDamage(), item.getUsos()])
                            k.w.mainloop(1)
                            if k.sent:  # Si se envía un evento
                                action = k.values[0]
                                if action == "drop":
                                    self.player.dropRightWeapon()
                                    self.sfx(35)
                                    self.setInfo(lang(43))
                                    self.static.addDroppedWeapon()
                                    self.infoArmaduraArmaDerecha.config(
                                        image=self.images.image("no_rw"),
                                        state=DISABLED, cursor="arrow")
                                self.dibujarMundo()
                            del k
                    elif tipo == "pantalones":
                        item = self.player.getPantalones()
                        if item is not None:
                            self.sfx(23)
                            k = pop([[lang(38), lang(243), lang(242),
                                      lang(173), lang(248)],
                                     DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                     "itemInfoArmor", POP_XSIZE, POP_YSIZE,
                                     translate(
                                         putStrict(item.getName())),
                                     "armadura", translate(
                                    putStrict(item.getDescription())),
                                     item.getDefense(), item.getUsos()])
                            k.w.mainloop(1)
                            if k.sent:  # Si se envía un evento
                                action = k.values[0]
                                if action == "drop":
                                    self.player.dropPantalones()
                                    self.sfx(20)
                                    self.setInfo(lang(44))
                                    self.static.addDroppedArmor()
                                    self.infoArmaduraPantalones.config(
                                        image=self.images.image("no_pantalon"),
                                        state=DISABLED, cursor="arrow")
                            del k
                    elif tipo == "botas":
                        item = self.player.getBotas()
                        if item is not None:
                            self.sfx(23)
                            k = pop([[lang(39), lang(243), lang(242),
                                      lang(173), lang(248)],
                                     DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                     "itemInfoArmor", POP_XSIZE, POP_YSIZE,
                                     translate(
                                         putStrict(item.getName())),
                                     "armadura", translate(
                                    putStrict(item.getDescription())),
                                     item.getDefense(), item.getUsos()])
                            k.w.mainloop(1)
                            if k.sent:  # Si se envía un evento
                                action = k.values[0]
                                if action == "drop":
                                    self.player.dropBotas()
                                    self.sfx(20)
                                    self.setInfo(lang(45))
                                    self.static.addDroppedArmor()
                                    self.infoArmaduraBotas.config(
                                        image=self.images.image("no_botas"),
                                        state=DISABLED,
                                        cursor="arrow")
                            del k
            else:  # Click izquierdo, event:drop
                if tipo == "casco":
                    if self.player.getCasco() is not None:
                        self.player.addObject(self.player.getCasco())
                        self.player.dropCasco()
                        self.infoArmaduraCasco.config(
                            image=self.images.image("no_casco"),
                            state=DISABLED,
                            cursor="arrow")
                        self.sfx(20)
                        self.setInfo(lang(40))
                        self.static.addDroppedArmor()
                elif tipo == "izquierda":
                    if self.player.getLeftWeapon() is not None:
                        self.player.addObject(self.player.getLeftWeapon())
                        self.player.dropLeftWeapon()
                        self.setInfo(lang(41))
                        self.static.addDroppedWeapon()
                        self.infoArmaduraArmaIzquierda.config(
                            image=self.images.image("no_lw"), state=DISABLED,
                            cursor="arrow")
                        self.sfx(35)
                        if self.player.getActiveBullet() is not None:  # Si el jugador tenia una bala definida para esa arma a botar
                            # agrego como item a la bala
                            self.player.addObject(
                                self.player.getActiveBullet())
                            self.player.delActiveBullet()
                        self.dibujarMundo()
                elif tipo == "chaleco":
                    if self.player.getChaleco() is not None:
                        self.player.addObject(self.player.getChaleco())
                        self.player.dropChaleco()
                        self.setInfo(lang(42))
                        self.static.addDroppedArmor()
                        self.sfx(20)
                        self.infoArmaduraChaleco.config(
                            image=self.images.image("no_chaleco"),
                            state=DISABLED,
                            cursor="arrow")
                elif tipo == "derecha":
                    if self.player.getRightWeapon() is not None:
                        self.player.addObject(self.player.getRightWeapon())
                        self.player.dropRightWeapon()
                        self.setInfo(lang(43))
                        self.infoArmaduraArmaDerecha.config(
                            image=self.images.image("no_rw"), state=DISABLED,
                            cursor="arrow")
                        self.sfx(35)
                        self.static.addDroppedWeapon()
                        self.dibujarMundo()
                elif tipo == "pantalones":
                    if self.player.getPantalones() is not None:
                        self.player.addObject(self.player.getPantalones())
                        self.player.dropPantalones()
                        self.setInfo(lang(44))
                        self.static.addDroppedArmor()
                        self.sfx(20)
                        self.infoArmaduraPantalones.config(
                            image=self.images.image("no_pantalon"),
                            state=DISABLED,
                            cursor="arrow")
                elif tipo == "botas":
                    if self.player.getBotas() is not None:
                        self.player.addObject(self.player.getBotas())
                        self.player.dropBotas()
                        self.setInfo(lang(45))
                        self.static.addDroppedArmor()
                        self.sfx(20)
                        self.infoArmaduraBotas.config(
                            image=self.images.image("no_botas"),
                            state=DISABLED,
                            cursor="arrow")
            self.dibujarItems()

        def _itemMenu(i, typeClick, e=None):
            """
            Función que maneja los eventos de los items del jugador
            :param i: Indice del item
            :param typeClick: Tipo de click (izquierdo, derecho)
            :param e: Evento
            :return: void
            """
            # Si se hace click el primer recuadro y está en una pagina
            # diferente a la primera se cambia de ventana
            if i == 0 and self.itemnumberlist >= 20:
                self.moverListaItems("left")
            # Si no es así se continúa con los botones
            elif not (i == 20 or (i == 0 and self.itemnumberlist != 0)):
                if self.itemnumberlist == 0:
                    i += self.itemnumberlist
                else:
                    i += self.itemnumberlist - 1
                if self.player.getItemAmount() > i:
                    item = self.player.getItem(i)
                    if typeClick == 0:  # Click izquierdo, usar
                        typeItem = item.getType()
                        if typeItem == "armor/casco":  # Casco
                            # se bota el item clickeado
                            self.player.dropObject(i)
                            if self.player.getCasco() is not None:  # Si el player tiene un casco
                                self.player.addObject(self.player.getCasco())
                                self.player.dropCasco()
                                self.static.addDroppedArmor()
                            self.player.addCasco(item)
                            self.dibujarArmor()
                            self.sfx(23)
                            self.setInfo(lang(31))
                            self.textMsg(
                                lang(choice([491, 492, 493, 494, 495])))
                        elif typeItem == "armor/botas":  # Botas
                            self.player.dropObject(i)
                            if self.player.getBotas() is not None:  # Si el player tiene botas
                                self.player.addObject(self.player.getBotas())
                                self.player.dropBotas()
                                self.static.addDroppedArmor()
                            self.player.addBotas(item)
                            self.dibujarArmor()
                            self.sfx(23)
                            self.setInfo(lang(28))
                            self.textMsg(
                                lang(choice(
                                    [484, 485, 486, 487, 488, 489, 490, 495])))
                        elif typeItem == "armor/chaleco":  # Chaleco
                            self.player.dropObject(i)
                            if self.player.getChaleco() is not None:  # Si el player tiene botas
                                self.player.addObject(self.player.getChaleco())
                                self.player.dropChaleco()
                                self.static.addDroppedArmor()
                            self.player.addChaleco(item)
                            self.dibujarArmor()
                            self.sfx(23)
                            self.setInfo(lang(29))
                            self.textMsg(
                                lang(choice([495, 496, 497, 498, 499, 500])))
                        elif typeItem == "armor/pantalones":  # Pantalones
                            self.player.dropObject(i)
                            if self.player.getPantalones() is not None:  # Si el player tiene pantalones
                                self.player.addObject(
                                    self.player.getPantalones())
                                self.player.dropPantalones()
                                self.static.addDroppedArmor()
                            self.player.addPantalones(item)
                            self.dibujarArmor()
                            self.sfx(23)
                            self.setInfo(lang(30))
                            self.textMsg(
                                lang(choice([495, 501, 502, 503, 504, 505])))
                        elif typeItem == "potion/apple":  # Manzana
                            self.player.upgradeLife()
                            self.player.upgradeMana()
                            self.player.dropObject(i)
                            self.playerText("+", "verde")
                            self.sfx(25)
                            self.setInfo(lang(91))
                            self.updateInfoPlayer()
                            self.static.addPociones()
                            self.textMsg(
                                lang(choice([506, 507, 508, 509, 510, 511])))
                        elif typeItem == "coin":  # Fichas / Monedas / Dinero
                            self.setInfo(
                                lang(27, str(item.getUsos()),
                                     str(item.getName())))
                            self.sfx(5)
                            self.textMsg(
                                lang(choice(
                                    [512, 513, 514, 515, 516, 517, 518, 519,
                                     520])))
                        elif typeItem == "mana/normal":  # Mana
                            self.player.increaseMana(item.getPDV())
                            self.setInfo(lang(104, str(item.getPDV())))
                            self.playerText("+" + str(item.getPDV()), "azul")
                            self.updateInfoPlayer()
                            self.sfx(16)
                            item.usar()
                            self.static.addPociones()
                            if item.estaDestruido():
                                self.player.dropObject(i)
                            self.textMsg(
                                lang(choice(
                                    [521, 522, 523, 524, 525, 526, 527])))
                        elif typeItem == "object/holy":  # Biblia
                            self.player.upgradeMana()
                            self.setInfo(lang(102))
                            self.playerText("+", "azul")
                            self.sfx(27)
                            self.player.dropObject(i)
                        elif typeItem == "potion/normal" or typeItem == "potion/food":  # Pociones
                            self.player.curar(item.getPDV())
                            self.setInfo(lang(101, str(item.getPDV())))
                            self.playerText("+" + str(item.getPDV()), "verde")
                            self.updateInfoPlayer()
                            if typeItem == "potion/normal":
                                self.sfx(21)
                            self.static.addPociones()
                            item.usar()
                            if item.estaDestruido():
                                self.player.dropObject(i)
                            self.textMsg(
                                lang(choice(
                                    [528, 529, 530, 531, 532, 533, 534, 535,
                                     536])))
                        elif typeItem == "read":  # Libros
                            self.sfx(27)
                            try:
                                self.static.addLibros()
                                k = pop(
                                    [translate(item.getName()),
                                     self.images.image("text_icon"),
                                     "longtext", 400, 600,
                                     LEVELS_RES + item.getBookLink()])
                                k.w.mainloop(0)
                                del k
                            except Exception, e:
                                print langError(355, e)
                            self.sfx(27)
                        # Armas segundarias (arcos, flechas)
                        elif typeItem == "weapon/left":
                            self.player.dropObject(i)
                            if self.player.getLeftWeapon() is not None:  # Si el jugador tiene un arma izquierda definida
                                self.player.addObject(
                                    self.player.getLeftWeapon())
                                self.player.dropLeftWeapon()
                                self.static.addDroppedWeapon()
                            self.player.setLeftWeapon(item)
                            self.dibujarArmor()
                            self.dibujarMundo()
                            self.sfxSpecial(24, 1)
                            self.setInfo(lang(26, str(item.getName())))
                            if self.player.getActiveBullet() is not None:  # Si el jugador tenia un bullet definido para el arma
                                self.player.addObject(
                                    self.player.getActiveBullet())
                                # se elimina el bullet activo dado que se
                                # cambio el arma
                                self.player.delActiveBullet()
                            self.root.after(1, lambda: self.escogerArmamento(
                                "automatic_bullet"))  # se escoge el armamento automaticamente
                            self.textMsg(
                                lang(choice([537, 538, 539, 540, 541])))
                        elif typeItem == "weapon/right":  # Arma derecha
                            self.player.dropObject(i)
                            if self.player.getRightWeapon() is not None:  # Si el jugador tiene un arma derecha
                                self.player.addObject(
                                    self.player.getRightWeapon())
                                self.player.dropRightWeapon()
                                self.static.addDroppedWeapon()
                            self.player.setRightWeapon(item)
                            self.dibujarArmor()
                            self.dibujarMundo()
                            self.sfxSpecial(34, 1)
                            self.setInfo(lang(32, str(item.getName())))
                            self.textMsg(
                                lang(choice([537, 538, 539, 540, 541])))
                        else:  # Muestra un mensaje que no se puede usar
                            self.sfx(37)
                            if random.randint(1, 2) == 1:
                                self.setInfo(lang(125))
                            else:
                                self.setInfo(lang(126, item.getName()))
                            self.textMsg(
                                lang(choice(
                                    [542, 543, 544, 545, 546, 547, 548])))
                    else:  # Click derecho, propiedades
                        if CONFIGURATION_DATA[15]:  # Si está activa la opción
                            tipo = item.getType()
                            if "armor" in tipo:
                                self.sfx(23)
                                k = pop([[lang(33), lang(243), lang(242),
                                          lang(173), lang(248)],
                                         DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                         "itemInfo", POP_XSIZE, POP_YSIZE,
                                         translate(
                                             putStrict(item.getName())),
                                         "armadura", translate(
                                        putStrict(item.getDescription())),
                                         item.getDefense(), item.getUsos()])
                            elif "bullet" in tipo:
                                self.sfx(24)
                                k = pop([[lang(33), lang(241), lang(244),
                                          lang(173), lang(248)],
                                         DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                         "itemInfo", POP_XSIZE, POP_YSIZE,
                                         translate(
                                             putStrict(item.getName())),
                                         "bullet", translate(
                                        putStrict(item.getDescription())),
                                         item.getDamage(), item.getUsos()])
                            elif "coin" in tipo:
                                self.sfx(5)
                                k = pop([[lang(33), lang(244), "", lang(173),
                                          lang(248)],
                                         DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                         "itemInfo", POP_XSIZE, POP_YSIZE,
                                         translate(
                                             putStrict(item.getName())),
                                         "coin",
                                         translate(
                                             putStrict(item.getDescription())),
                                         translate(item.getUsos())])
                            elif "mana" in tipo:
                                self.sfx(16)
                                k = pop([[lang(33), lang(23) + " ", lang(244),
                                          lang(173), lang(248)],
                                         DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                         "itemInfo", POP_XSIZE, POP_YSIZE,
                                         translate(
                                             putStrict(item.getName())),
                                         "mana",
                                         translate(
                                             putStrict(item.getDescription())),
                                         item.getPDV(), item.getUsos()])
                            elif "object" in tipo:
                                if item.getId() == 222:
                                    self.sfx(27)
                                k = pop([[lang(33), lang(245), lang(246),
                                          lang(173), lang(248)],
                                         DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                         "itemInfo", POP_XSIZE, POP_YSIZE,
                                         translate(
                                             putStrict(item.getName())),
                                         "objeto", translate(
                                        putStrict(item.getDescription())),
                                         putStrict(str(item.getTipoObjeto())),
                                         translate(putStrict(
                                             str(item.getUtilidad())))])
                            elif "potion" in tipo:
                                if tipo != "potion/food":
                                    self.sfx(21)
                                k = pop([[lang(33), lang(247), lang(244),
                                          lang(173), lang(248)],
                                         DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                         "itemInfo", POP_XSIZE, POP_YSIZE,
                                         translate(
                                             putStrict(item.getName())),
                                         "pocion", translate(
                                        putStrict(item.getDescription())),
                                         item.getPDV(), item.getUsos()])
                            elif "read" in tipo:
                                self.sfx(27)
                                k = pop(
                                    [[lang(33), "", "", lang(173), lang(248)],
                                     DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                     "itemInfo",
                                     POP_XSIZE, POP_YSIZE, translate(
                                        putStrict(item.getName())), "libro",
                                     translate(
                                         putStrict(item.getDescription()))])
                            elif "weapon" in tipo:
                                if isIn(item.getImage(), ARROW_WEAPONS_PREFIX):
                                    self.sfx(24)  # sonido de flechas
                                else:
                                    self.sfx(34)
                                k = pop([[lang(33), lang(241), lang(242),
                                          lang(173), lang(248)],
                                         DATA_ICONS_ITEMS + item.getImage() + "_16.ico",
                                         "itemInfo", POP_XSIZE, POP_YSIZE,
                                         translate(
                                             putStrict(item.getName())),
                                         "arma",
                                         translate(
                                             putStrict(item.getDescription())),
                                         item.getDamage(), item.getUsos()])
                            try:
                                k.w.mainloop(1)
                                if k.sent:  # Si se envía un evento
                                    action = k.values[0]
                                    if action == "drop":
                                        self.player.dropObject(i)
                                        self.sfx(35)
                                        self.setInfo(
                                            lang(103, str(item.getName())))
                                        self.static.addDroppedItem()
                                        if item.getType() == "weapon/left":  # Si el objeto a botar era un arma izquierda
                                            if self.player.getActiveBullet() is not None:  # Si el jugador tenia una bala definida para esa arma a botar
                                                self.player.addObject(
                                                    self.player.getActiveBullet())
                                                self.player.delActiveBullet()
                                    elif action == "left":
                                        if i > 0:
                                            self.player.setItem(i,
                                                                self.player.getItem(
                                                                    i - 1))
                                            self.player.setItem(
                                                i - 1, item)
                                    elif action == "right":
                                        if i < (
                                                    self.player.getItemAmount() - 1):
                                            self.player.setItem(i,
                                                                self.player.getItem(
                                                                    i + 1))
                                            self.player.setItem(
                                                i + 1, item)
                                    elif action == "super_left":
                                        if self.player.getItemAmount() > 2:
                                            self.player.setItem(i,
                                                                self.player.getItem(
                                                                    0))
                                            self.player.setItem(0, item)
                                    elif action == "super_right":
                                        if self.player.getItemAmount() > 2:
                                            self.player.setItem(i,
                                                                self.player.getItem(
                                                                    self.player.getItemAmount() - 1))
                                            self.player.setItem(
                                                self.player.getItemAmount() - 1,
                                                item)
                                del k  # borro la ventana
                            except Exception, e:
                                print langError(354, e)
                    self.dibujarItems()  # se actualizan los items gráficos

        def _itemPower(i, typeClick, x=None):
            """
            Función que maneja los eventos de los poderes del jugador
            :param i: Indice del item
            :param typeClick: Tipo de click
            :param x: Evento
            :return: void
            """

            def _setActivePowerId(name, i):
                """
                Función que establece un id para los poderes del jugador
                :param name: String
                :param i: Index
                :return: void
                """
                if name == self.activePowers[0]:
                    try:
                        self.activePowers[1][i] = 1
                    except Exception, e:
                        print langError(390, e)
                else:
                    print lang(392)

            def _delActivePowerId(name, i):
                """
                Función que elimina un id
                :param name: String
                :param i: Index
                :return: void
                """
                if name == self.activePowers[0]:
                    try:
                        self.activePowers[1][i] = 0
                    except Exception, e:
                        print langError(390, e)
                else:
                    print lang(391)

            if self.ingame:
                i -= 1
                if self.player.getPowerAmount() > i:  # Si el jugador posee el poder
                    poder = self.player.getPower(i)
                    poder_id = poder.getId()
                    if self.player.getLevel() >= poder.getNivel():  # Si posee el nivel
                        if typeClick == 0:  # Click derecho
                            self.static.addPower()  # actualizo las estadísticas
                            mana_requerido = int(
                                self.player.getMaxMana() * poder.getReqMana() / 100.0)  # se obtiene el mana necesario
                            if mana_requerido <= self.player.getMana():  # Si posee el mana necesario
                                self.player.decreaseMana(mana_requerido)
                                self.updateInfoPlayer()
                                self.player.dropPower(i)
                                self.dibujarPowers()
                                if poder_id == 0:  # Escape rápido
                                    self.enemy = None
                                    self.enemyId = 0
                                    if self.inBattle:
                                        self.textMsg(
                                            lang(choice(
                                                [549, 550, 551, 552, 553,
                                                 554])))
                                    else:
                                        self.textMsg(
                                            lang(choice([555, 556, 557, 558])))
                                    self.inBattle = False
                                    self.inNpc = False
                                    _setActivePowerId(self.player.getName(), 0)
                                    self.root.after(self.dificultad[5],
                                                    lambda: _delActivePowerId(
                                                        self.player.getName(),
                                                        0))
                                    self.setInfo(lang(559))
                            else:  # Si no tiene el mana necesario
                                self.textMsg(lang(448))
                                self.setInfo(
                                    lang(449, str(abs(
                                        self.player.getMana() - mana_requerido))))
                                self.setInfo(lang(450))
                        else:  # Click izquierdo
                            if CONFIGURATION_DATA[
                                16]:  # Si está activa la opción
                                k = pop([[lang(380), lang(381), lang(382),
                                          lang(383), lang(173), lang(384)],
                                         DATA_ICONS_POWERS + poder.getImage() + ".ico",
                                         "powerInfo", 163, 270, translate(
                                        poder.getName()),
                                         translate(
                                             poder.getDescripcion()),
                                         poder.getNivel(),
                                         toHour(str(float(poder.getTime() * (
                                             1 - self.dificultad[6]))))])
                                del k

        def _item_mousewheel(event):
            """
            Función que atrapa el evento del scrolling y mueve los comandos
            :param event: Evento
            :return: void
            """
            if self.ingame:
                if 0 <= event.x < 190 and 400 <= event.y < 575:
                    if isWindows():
                        if -1 * (event.delta / 100) < 0:
                            move = -1
                        else:
                            move = 2
                    elif isOSX():
                        if -1 * event.delta < 0:
                            move = -2
                        else:
                            move = 2
                    else:
                        print event.delta
                        if -1 * (event.delta / 100) < 0:
                            move = -1
                        else:
                            move = 2
                    self.infoSlider.canv.yview_scroll(move, "units")

        def _movebottom(event):
            """
            Función que mueve los comandos hasta el final
            :param event: Evento
            :return: void
            """
            if self.ingame:
                self.infoSlider.canv.yview_scroll(1000, "units")

        def _moveLineDown(event):
            """
            Función que mueve los comandos en una linea
            :param event: Evento
            :return: void
            """
            if self.ingame:
                self.infoSlider.canv.yview_scroll(1, "units")

        def _moveLineUp(event):
            """
            Función que mueve los comandos en una linea
            :param event: Evento
            :return: void
            """
            if self.ingame:
                self.infoSlider.canv.yview_scroll(-1, "units")

        def _movetop(event):
            """
            Función que mueve los comandos hasta el principio
            :param event: Evento
            :return: void
            """
            if self.ingame:
                self.infoSlider.canv.yview_scroll(-1000, "units")

        def _licence(e=None):
            """
            Función que muestra la licencia del programa
            :param e: Evento
            :return: void
            """
            if isWindows():
                e = pop([lang(99), self.images.image("text_icon"),
                         "license", 400, 600, ACTUAL_FOLDER + "LICENSE"])
            else:
                e = pop([lang(99), self.images.image("text_icon"),
                         "license", 400, 546, ACTUAL_FOLDER + "LICENSE"])
            e.w.mainloop(1)
            del e

        def _saveshorcut(event):
            """
            Función que guarda el estado del juego mediante atajo de teclado
            :param event: Evento
            :return: void
            """
            self.saveGame("shorcut")

        # TODO: Mapas
        def _showMap(e=None):
            """
            Función que muestra el mapa del mundo
            :param e:
            :return:
            """
            if self.ingame:  # Si se encuentra en una partida
                pass

        def _showPlayerInfo(e=None):
            """
            Función que muestra la información del jugador
            :param e: Evento
            :return: void
            """
            if self.ingame:  # Si se encuentra en una partida
                if isWindows():
                    _sizex = 400
                    _sizey = 230
                else:
                    _sizex = 430
                    _sizey = 260
                e = pop([[lang(323), lang(245).replace(":", ""), lang(228),
                          lang(173), lang(22).replace(":", ""),
                          lang(23).replace(":", ""),
                          lang(24).replace(":", ""), lang(601), lang(227),
                          lang(381).replace(":", ""), lang(602)],
                         self.images.image(
                             "user_icon"), "show_info_player", _sizey, _sizex,
                         self.player.getName(),
                         translate(self.player.getType()
                                   ), self.player.getEdad(),
                         translate(self.player.getInfo()), self.player.getLife(
                    ), self.player.getMaxLife(),
                         self.player.getMana(), self.player.getMaxMana(),
                         self.player.getExperience(), self.player.getPrevExp(),
                         self.player.getMaxExperience(),
                         Image.open(self.images.getLinkImage(
                             self.player.getLinkImage() + "_0")),
                         self.player.getPais(),
                         self.player.getLevel()])
                e.w.mainloop(1)
                del e

        def _showStatics(e=None):
            """
            Muestra las estadísticas del jugador
            :param e: Evento
            :return: void
            """
            if self.ingame:  # Si se encuentra en una partida
                if isWindows():
                    _sizey = 490
                else:
                    _sizey = 515
                statics = pop([[lang(209), lang(173), lang(195), lang(196),
                                lang(197), lang(198), lang(199), lang(200),
                                lang(201), lang(202), lang(203), lang(204),
                                lang(
                                    205), lang(206), lang(207), lang(208),
                                lang(211), lang(444), lang(445), lang(446),
                                lang(591), lang(722)],
                               self.images.image("statics"),
                               "statics", _sizey, 280, self.static.get()])
                statics.w.mainloop(1)
                del statics

        def _verFollowers(e=None):
            """
            Función que muestra a los seguidores del jugador
            :param e: Evento
            :return: void
            """
            if self.ingame:  # Si se encuentra en una partida
                if isWindows():
                    _sizex = 450
                    _sizey = 120
                else:
                    _sizex = 500
                    _sizey = 120
                p = pop([[lang(701), lang(702), lang(703), lang(706),
                          lang(707), lang(708), lang(709), lang(710),
                          lang(704), lang(711), lang(705), lang(712)],
                         self.images.image("group"), "ver_followers",
                         _sizey, _sizex, self.dificultad[
                             7], self.player.getAttack(),
                         self.player.getDefensa(),
                         self.player.getMaxLife(),
                         self.player.getLightFriends(),
                         self.player.getMediumFriends(),
                         self.player.getStrongFriends()])
                p.w.mainloop(1)
                del p

        # TODO: Quest fix
        def _verQuest(e=None):
            """
            Función que muestra las tareas del jugador (quest)
            :param e: Evento
            :return: void
            """
            if self.ingame:  # Si se encuentra en una partida
                if isWindows():
                    _sizex = 450
                else:
                    _sizex = 470
                p = pop(
                    [[lang(587), lang(588), lang(576).title(), lang(589),
                      lang(590)], self.images.image("quest_list"),
                     "ver_quest",
                     250, _sizex, self.player.getQuest(),
                     self.player.getTotalQuest(), QUEST_DELIMITER])
                p.w.mainloop(1)
                del p

        # Se define una variable para almacenar el numero total de errores y
        # advertencias
        totalwarnings = 0
        totalerrors = 0

        # Se cargan los argumentos
        print "Consultando argumentos ...",
        try:  # Se carga el archivo de argumentos
            argfile = open(CONFIGURATION_ARGS, "r")
            for arg in argfile:  # Se recorren los argumentos
                arg = arg.strip().lower()
                # Si el argumento no es un comentario y no está vacio
                if ("#" not in arg) and arg != "":
                    arguments.append(arg)
            # Desactivar la función print
            if CONFIGURATION_DATA[8] not in AVAIABLE_LANGS_TOPRINT:
                sys.stdout, sys.stderr, sys.stdin, sys.__stdout__, sys.__stderr__, sys.__stdin__ = noStdOut(
                ), noStdOut(), noStdOut(), noStdOut(), noStdOut(), noStdOut()
                print OK
            else:
                print lang(310)
        except:  # Si no existe el archivo de argumentos
            print lang(744),
            argfile = open(CONFIGURATION_ARGS, "w")
            argfile.write("#Archivo de argumentos por defecto para HOA\n")
            argfile.write(
                "#No haga cambios indebidos, ellos pueden afectar al comportamiento del programa\n\n")
            argfile.write("#ARGUMENTS\n")
            argfile.close()
            print lang(310)
            totalwarnings += 1
        # agrego final a la matriz de argumentos
        arguments.append(ENDING_ARGUMENT)
        arg = []  # matriz de argumentos
        arg_p = []  # matriz parcial de argumentos
        if len(arguments) > 2:  # Si existen argumentos
            for k in range(1, len(
                    arguments) - 1):  # Se crea una matriz de argumentos
                if "-" in arguments[k]:
                    arg_p.append(arguments[k].replace("-", ""))
                    if "-" not in arguments[k + 1] and not "$" in arguments[
                                k + 1]:
                        arg_p.append(arguments[k + 1])
                        if k != len(arguments):
                            k += 2
                    else:
                        arg_p.append("")
                    arg.append(arg_p)
                    arg_p = []
            del arguments

        # Se crea la ventana
        try:
            self.root = Tk()
        except Exception, e:
            print langError(827, e)
            exit()
        self.root.title(PROGRAM_TITLE)  # título
        self.root.minsize(width=PROGRAM_SIZE[0], height=PROGRAM_SIZE[
            1])  # tamaño mínimo y máximo
        self.root.resizable(width=False, height=False)
        self.root.geometry(
            '%dx%d+%d+%d' % (PROGRAM_SIZE[0], PROGRAM_SIZE[1], (
                self.root.winfo_screenwidth() - PROGRAM_SIZE[0]) / 2,
                             (self.root.winfo_screenheight() - PROGRAM_SIZE[
                                 1] - 50) / 2))

        # Se define el enfoque a la ventana
        if isWindows():  # Si el sistema operativo es windows
            self.root.focus_force()
            self.root.focus()
        else:
            if sys.platform == "darwin":  # Sistema operativo mac-os
                os.system(
                    '''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        self.root.config(highlightthickness=0)
        checkScreen(self.root, PROGRAM_SIZE, lang(824))

        # Creación de variables
        self.activePowers = ["playername",
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0,
                              0]]  # matriz de datos de los poderes
        self.board = None  # tablero para los combates grupales
        self.botonesItems = list()  # botones para los items
        self.botonesPoderes = list()  # botones para los poderes
        self.canmove = True  # variable lógica que denota si el jugador puede moverse en un dt
        # dibuja el canvas centrado si el mapa no es de gran tamaño
        self.canvasCorrecion = [0, 0]
        self.console = list()  # matriz para las entradas de la consola
        self.currentNpc = None  # clase npc que indica al npc con el que el jugador interectuará
        self.dificultad = [0, 0, 0, 0, 0, 0, 0, 0]  # dificultad
        self.nivel_dificultad = 0  # nivel fácil, medio, dificil
        self.enemy = None  # clase mob que indica el enemigo al cual peleara el jugador
        self.enemyId = 0  # id del mob que es cargado como enemigo activo
        self.fonts = [tkFont.Font(family="Courier", size=8),
                      tkFont.Font(family="Verdana", size=6),
                      tkFont.Font(family="Times", size=10),
                      tkFont.Font(family="Times", size=10, weight=tkFont.BOLD),
                      tkFont.Font(family="Verdana", size=6,
                                  weight=tkFont.BOLD),
                      tkFont.Font(family="Verdana", size=10),
                      tkFont.Font(family="Verdana", size=7)]
        self.inBattle = False  # indica que hay una batalla en proceso
        self.inNpc = False  # indica que existe una interaccion con un npc
        self.ingame = False  # indica que se esta jugando
        self.isNewGameCreating = False  # indica que hay una nueva partida creandose
        self.itemnumberlist = 0  # paginación de los iFtems
        # denota el id del objeto self.root.after para el movimiento de los
        # mobs
        self.lastmovementId = 0
        # denota el id del objeto self.root.after para el multiplayer
        self.lastmultiplayerId = 0
        # denota el id del objeto self.root.after para el movimiento de los npc
        self.lastnpcmovementid = 0
        self.loaded = False  # indica que hay una partida en curso
        # indica los sonidos de fondo para un mapa
        self.mapBackgroundSound = ["%NULL%", None, 0]
        self.mapImage = [0]  # imagen de fondo para los mapas
        self.mapItemsTextures = list()  # texturas de los items
        self.mapLogic = list()  # mapa lógico
        self.mapSize = [0, 0]  # tamaño del mapa dinámico
        self.mapSound = list()  # lista de sonidos de texturas
        self.mapTextures = list()  # lista de texturas
        self.maplightning = list()  # iluminación (0 o 1)
        self.mobs = list()  # lista de mobs, elementos de caracter mob()
        self.movement = False  # indica si los mobs se pueden mover o no
        # booleano que guaarda si está conectado a un servidor o no
        self.multiplayer_isconected = False
        # indica el numero de conexión del jugador en una red multijugador
        self.multiplayer_me = NULL_CONECTION[0]
        # objeto de conexión del jugador en una red multijugador
        self.multiplayer_me_conn = NULL_CONECTION[1]
        self.multiplayer_lobby = "null"  # indica el lobby de la conexión multijugador
        self.multiplayer_players = []  # jugadores multiplayer
        self.multiplayer_players_id = []  # id de los jugadores multiplayer
        self.multiplayer_server = "0.0.0.0:0"  # nombre del servidor
        self.namePartida = ""  # nombre de la partida que se usará para guardar una vez cargado
        self.npc = list()  # lista de npc, elementos de clase npc()
        self.npcId = -1  # id del npc que actuará como npc activo
        self.npcMovement = False  # indica el el movimiento de los mobs
        self.player = actors()  # objeto jugador
        self.playerPos = [0, 0]  # posición del jugador
        self.programTitle = PROGRAM_TITLE  # titulo del programa
        self.static = statics.Statics()  # estadíssticas
        self.tipoCombate = "NO_FIGHT"  # indica el modo de combate
        print lang(309),

        # Se cargan los sonidos
        try:
            tkSnack.initializeSnack(self.root)
            tkSnack.audio.play_gain(AUDIO_VOLUME)
            self.snd = tkSnack.Sound()  # sonido inmediato
            self.sndBg = tkSnack.Sound()  # sonido de fondo
            self.sndFx = tkSnack.Sound()  # sonido de efecto
            self.sfx(0)
            print lang(310)  # cargo el sonido de introducción
            TKSNACK[0] = True
        except Exception, e:  # Ocurrió un error al cargar la libreria de datos de tcl, se menciona y se deshabilitan los sonidos
            print lang(756)
            print langError(794, e)
            TKSNACK[0] = False
            self.snd = None
            self.sndBg = None
            self.sndFx = None
            totalwarnings += 1

        # Instancio las texturas
        print lang(311),
        try:
            self.images = hoaTextures([lang(394), lang(310)])
            print lang(310)  # Cargo las texturas
        except Exception, e:
            print lang(398)
            print lang(330)
            print langError(830, e)
            exit()

        # Se genera la UI
        print lang(312),
        try:
            self.root.iconbitmap(
                self.images.image("icon"))  # icono del programa
        except Exception, e:
            print ""
            print langError(828, e)
            totalerrors += 1
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        self.archivomenu = Menu(self.menubar, tearoff=0)
        if isWindows():
            self.archivomenu.add_command(label=lang(
                10), command=self.newGame, accelerator="Ctrl+N")
            self.archivomenu.add_command(label=lang(
                11), command=self.loadGame, accelerator="Ctrl+L")
            self.archivomenu.add_command(label=lang(
                12), command=self.saveGame, accelerator="Ctrl+G")
            self.archivomenu.add_command(
                label=lang(13), command=self.abortGame)
            self.archivomenu.add_separator()
            self.archivomenu.add_command(label=lang(
                17), command=_configure, accelerator="Ctrl+C")
            self.archivomenu.add_command(label=lang(
                15), command=self.salir, accelerator="Ctrl + S")
            self.archivomenu.entryconfig(2, state=DISABLED)
            self.archivomenu.entryconfig(3, state=DISABLED)
            self.menubar.add_cascade(label=lang(16), menu=self.archivomenu)
            self.vermenu = Menu(self.menubar, tearoff=0)
            self.vermenu.add_command(label=lang(
                702), command=_verFollowers, accelerator="U")
            self.vermenu.add_command(label=lang(
                323), command=_showPlayerInfo, accelerator="I")
            self.vermenu.add_command(label=lang(
                14), command=_showStatics, accelerator="Ctrl+E")
            self.vermenu.add_command(label=lang(
                587), command=_verQuest, accelerator="T")
            self.vermenu.add_command(label=lang(
                322), command=_showMap, accelerator="M")
            self.menubar.add_cascade(label=lang(321), menu=self.vermenu)
            self.ayudamenu = Menu(self.menubar, tearoff=0)
            self.ayudamenu.add_command(label=lang(18), command=_about)
            self.ayudamenu.add_command(label=lang(
                19), command=_ayuda, accelerator="F1")
            self.ayudamenu.add_command(label=lang(20), command=_changelog)
            self.ayudamenu.add_command(label=lang(21), command=_licence)
            self.ayudamenu.add_separator()
            self.ayudamenu.add_command(label=lang(
                327), command=self.update, accelerator="F5")
            self.ayudamenu.add_command(label=lang(
                326), command=self.devConsole, accelerator="F2")
            if "-eclipse" in sys.argv:
                self.ayudamenu.add_command(label=lang(325),
                                           command=_infoSystem,
                                           accelerator="F12")
        else:
            self.archivomenu.add_command(label=lang(10), command=self.newGame)
            self.archivomenu.add_command(label=lang(
                11), command=self.loadGame, accelerator="Control+L")
            self.archivomenu.add_command(label=lang(
                12), command=self.saveGame, accelerator="Control+G")
            self.archivomenu.add_command(
                label=lang(13), command=self.abortGame)
            self.archivomenu.add_separator()
            self.archivomenu.add_command(label=lang(17), command=_configure)
            self.archivomenu.add_command(label=lang(15), command=self.salir)
            self.archivomenu.entryconfig(2, state=DISABLED)
            self.archivomenu.entryconfig(3, state=DISABLED)
            self.menubar.add_cascade(label=lang(16), menu=self.archivomenu)
            self.vermenu = Menu(self.menubar, tearoff=0)
            self.vermenu.add_command(label=lang(702), command=_verFollowers)
            self.vermenu.add_command(label=lang(323), command=_showPlayerInfo)
            self.vermenu.add_command(label=lang(14), command=_showStatics)
            self.vermenu.add_command(label=lang(587), command=_verQuest)
            self.vermenu.add_command(label=lang(322), command=_showMap)
            self.menubar.add_cascade(label=lang(321), menu=self.vermenu)
            self.ayudamenu = Menu(self.menubar, tearoff=0)
            self.ayudamenu.add_command(label=lang(18), command=_about)
            self.ayudamenu.add_command(label=lang(19), command=_ayuda)
            self.ayudamenu.add_command(label=lang(20), command=_changelog)
            self.ayudamenu.add_command(label=lang(21), command=_licence)
            self.ayudamenu.add_separator()
            self.ayudamenu.add_command(label=lang(
                327), command=self.update, accelerator="F5")
            self.ayudamenu.add_command(
                label=lang(326), command=self.devConsole)
            if "-eclipse" in sys.argv:
                self.ayudamenu.add_command(
                    label=lang(325), command=_infoSystem)
        for k in range(5):
            self.vermenu.entryconfig(k, state=DISABLED)
        self.menubar.add_cascade(label=lang(19), menu=self.ayudamenu)
        f = Frame(self.root)
        f.pack()
        self.initialBg = Canvas(f, width=PROGRAM_SIZE[0] + 105,
                                height=PROGRAM_SIZE[1] + 100, bd=-2,
                                highlightthickness=0)
        self.initialBg.pack()
        if isWindows():
            self.initialBg.create_image(
                403, 295, image=self.images.image("background"))
        elif isOSX():
            self.initialBg.create_rectangle(0, 0, 1000, 1000, fill="black")
            self.initialBg.create_image(
                409, 295, image=self.images.image("background"))
        elif isLinux():
            self.initialBg.create_rectangle(0, 0, 1000, 1000, fill="black")
            self.initialBg.create_image(
                417, 295, image=self.images.image("background"))
        self.initialBg.update()
        self.content = Frame(f, border=0)
        self.menu = Frame(f)
        self.menu2 = Frame(f)
        menu19 = Frame(self.menu)
        menu19.pack(pady=1, fill=X)
        menu2 = Frame(menu19)
        menu2.pack(fill=X)
        self.vidaLabel = Label(menu2, text=lang(22), width=5, anchor=E)
        self.vidaLabel.pack(side=LEFT)
        self.infoVidaCanv = Canvas(
            menu2, width=100 * BAR_POND_COEF, height=16, bg="#B30000",
            highlightthickness=0)
        self.infoVidaCanv.pack(side=LEFT)  # barra de vida
        if isWindows():
            self.infoVida = Label(menu2, width=6, anchor=E)
            self.infoVida.pack()
        else:
            self.infoVida = Label(menu2, width=7, anchor=E)
            self.infoVida.pack(padx=1)
        menu7 = Frame(menu19)
        menu7.pack(fill=X)
        self.manaLabel = Label(menu7, text=lang(23), width=5, anchor=E)
        self.manaLabel.pack(side=LEFT)
        self.infoManaCanv = Canvas(
            menu7, width=100 * BAR_POND_COEF, height=16, bg="#97991E",
            highlightthickness=0)
        self.infoManaCanv.pack(side=LEFT)  # barra de mana
        if isWindows():
            self.infoMana = Label(menu7, width=6, anchor=E)
            self.infoMana.pack()
        else:
            self.infoMana = Label(menu7, width=7, anchor=E)
            self.infoMana.pack(padx=1)
        menu13 = Frame(menu19)
        menu13.pack(fill=X)
        self.experienciaLabel = Label(menu13, text=lang(24), width=5, anchor=E)
        self.experienciaLabel.pack(side=LEFT)
        self.infoExpCanv = Canvas(
            menu13, width=100 * BAR_POND_COEF, height=16, highlightthickness=0)
        self.infoExpCanv.pack(side=LEFT)  # barra de experiencia
        if isWindows():
            self.infoExp = Label(menu13, width=6, anchor=E)
            self.infoExp.pack()
        else:
            self.infoExp = Label(menu13, width=7, anchor=E)
            self.infoExp.pack(padx=1)
        menu5 = Frame(self.menu)
        menu5.pack(pady=10)
        a_1 = Frame(menu5)
        a_1.pack(fill=X)
        if isWindows():
            buttonBorder = 2
        else:
            buttonBorder = 2
        self.infoArmaduraCasco = Button(a_1, relief=GROOVE, state=DISABLED,
                                        image=self.images.image("no_casco"),
                                        border=buttonBorder)
        self.infoArmaduraCasco.pack()
        a_2 = Frame(menu5)
        a_2.pack()
        if isWindows():
            buttonPad = 0
        else:
            buttonPad = 3
        self.infoArmaduraArmaIzquierda = Button(a_2, relief=GROOVE,
                                                state=DISABLED,
                                                image=self.images.image(
                                                    "no_lw"),
                                                border=buttonBorder)
        self.infoArmaduraArmaIzquierda.pack(side=LEFT, padx=buttonPad)
        self.infoArmaduraChaleco = Button(a_2, relief=GROOVE, state=DISABLED,
                                          image=self.images.image(
                                              "no_chaleco"),
                                          border=buttonBorder)
        self.infoArmaduraChaleco.pack(side=LEFT)
        self.infoArmaduraArmaDerecha = Button(a_2, relief=GROOVE,
                                              state=DISABLED,
                                              image=self.images.image("no_rw"),
                                              border=buttonBorder)
        self.infoArmaduraArmaDerecha.pack(padx=buttonPad)
        a_3 = Frame(menu5)
        a_3.pack()
        self.infoArmaduraPantalones = Button(a_3, relief=GROOVE,
                                             state=DISABLED,
                                             image=self.images.image(
                                                 "no_pantalon"),
                                             border=buttonBorder)
        self.infoArmaduraPantalones.pack()
        a_4 = Frame(menu5)
        a_4.pack(),
        self.infoArmaduraBotas = Button(a_3, relief=GROOVE, state=DISABLED,
                                        image=self.images.image("no_botas"),
                                        border=buttonBorder)
        self.infoArmaduraBotas.pack()
        if isWindows():
            self.poderFrame = LabelFrame(
                self.menu, text=" " + lang(314), border=0)
            self.poderFrame.pack(pady=2, padx=1)  # poderes
        else:
            self.poderFrame = LabelFrame(
                self.menu, text=" " + lang(314), border=0)
            self.poderFrame.pack(pady=0, padx=1)  # poderes
        z = Frame(self.poderFrame)
        z.pack()
        if isWindows():
            buttonBorder = 1
        else:
            buttonBorder = 1
        for i in range(1, 8):
            cmd1 = partial(_itemPower, i, 0)
            cmd2 = partial(_itemPower, i, 1)
            bt = Button(z, image=self.images.image("vacio_16"),
                        relief=GROOVE, border=buttonBorder, state=DISABLED)
            bt.bind('<Button-1>', cmd1)
            bt.bind(_SECOND_BUTTON, cmd2)
            if i < 8:
                bt.pack(side=LEFT, padx=3, pady=3)
            else:
                bt.pack()
            self.botonesPoderes.append(bt)
        self.itemFrame = LabelFrame(self.menu, text=lang(25))
        self.itemFrame.pack()
        j = 0
        if isWindows():
            buttonBorder = 4
        else:
            buttonBorder = 4
        for i in range(3):  # botones para items
            l = Frame(self.itemFrame)
            l.pack()
            # noinspection PyAssignmentToLoopOrWithParameter
            for i in range(7):
                cmd1 = partial(_itemMenu, j, 0)
                cmd2 = partial(_itemMenu, j, 1)
                bt = Button(l, image=self.images.image("vacio_16"),
                            relief=FLAT, border=buttonBorder, state=DISABLED)
                bt.bind('<Button-1>', cmd1)
                bt.bind(_SECOND_BUTTON, cmd2)
                if i < 7:
                    bt.pack(side=LEFT)
                else:
                    bt.pack()
                self.botonesItems.append(bt)
                j += 1
        self.infoSlider = VerticalScrolledFrame(self.menu)
        self.infoSlider.canv.config(bg="#000000")
        self.infoSlider.pack(pady=2, anchor=NE, fill=BOTH, padx=1)
        if isWindows():
            self.info = Label(self.infoSlider.interior, text="", justify=LEFT,
                              wraplength=175, anchor=NW,
                              bg=CONFIGURATION_DATA[3],
                              fg=CONFIGURATION_DATA[4], font=self.fonts[0],
                              relief=FLAT, border=2, cursor="xterm")
        elif isOSX():
            self.info = Label(self.infoSlider.interior, text="", justify=LEFT,
                              wraplength=220, anchor=NW,
                              bg=CONFIGURATION_DATA[3],
                              fg=CONFIGURATION_DATA[4], font=self.fonts[5],
                              relief=FLAT, border=2, cursor="xterm")
        else:
            self.info = Label(self.infoSlider.interior, text="", justify=LEFT,
                              wraplength=250, anchor=NW,
                              bg=CONFIGURATION_DATA[3],
                              fg=CONFIGURATION_DATA[4], font=self.fonts[6],
                              relief=FLAT, border=2, cursor="xterm")
        self.info.pack(anchor=NW, fill=BOTH)
        self.infoSlider.scroller.pack_forget()
        menu7 = Frame(self.menu)
        menu7.pack()
        if isWindows():
            self.world = Canvas(self.content, width=CANVAS_SIZE[
                0], height=CANVAS_SIZE[1])
        else:
            self.world = Canvas(self.content, width=CANVAS_SIZE[
                0], height=CANVAS_SIZE[1], bd=0, highlightthickness=0)
        self.world.pack(fill=BOTH, padx=0)  # canvas del mundo
        print lang(310)

        # Se establecen los eventos del programa
        try:
            print lang(691),
            self.root.bind("<Control-A>", _ayuda)
            self.root.bind("<Control-a>", _ayuda)
            self.root.bind("<Control-C>", _configure)
            self.root.bind("<Control-c>", _configure)
            self.root.bind("<Control-E>", _showStatics)
            self.root.bind("<Control-e>", _showStatics)
            self.root.bind("<Control-T>", self.devConsole)
            self.root.bind("<Control-t>", self.devConsole)
            self.root.bind("<Control-N>", self.newGame)
            self.root.bind("<Control-n>", self.newGame)
            self.root.bind("<F1>", _ayuda)
            self.root.bind("<F2>", lambda event: self.devConsole())
            self.root.bind("<F5>", self.update)
            if "-eclipse" in sys.argv:
                self.root.bind("<F12>", _infoSystem)
            self.root.bind("<I>", _showPlayerInfo)
            self.root.bind("<i>", _showPlayerInfo)
            self.root.bind("<M>", _showMap)
            self.root.bind("<m>", _showMap)
            self.root.bind("<T>", _verQuest)
            self.root.bind("<t>", _verQuest)
            self.root.bind("<U>", _verFollowers)
            self.root.bind("<u>", _verFollowers)
            if isWindows():
                self.root.bind("<Control-S>", self.salir)
                self.root.bind("<Control-s>", self.salir)
            else:
                self.root.bind("<Control-q>", self.salir)
                self.root.bind("<Control-Q>", self.salir)
            self.root.bind("<Control-Down>", _moveLineDown)
            self.root.bind("<Control-Up>", _moveLineUp)
            self.root.bind("<End>", _movebottom)
            self.root.bind("<Home>", _movetop)
            self.root.bind("<Shift-Down>", _moveLineDown)
            self.root.bind("<Shift-Up>", _moveLineUp)
            self.root.bind("<MouseWheel>", _item_mousewheel)
            self.root.bind("<F3>", _movebottom)
            self.root.bind("<F4>", _movetop)
            self.root.bind("<Control-G>", _saveshorcut)
            self.root.bind("<Control-g>", _saveshorcut)
            self.root.bind("<Control-L>", self.loadGame)
            self.root.bind("<Control-l>", self.loadGame)
            # evento de salida
            self.root.protocol("WM_DELETE_WINDOW", self.salir)
            self.world.bind("<ButtonRelease-1>", self.combateGrupal)
            # Eventos combinados
            cmd = partial(self.combateGrupal, "click-izquierdo")
            self.world.bind("<ButtonRelease-1>", cmd)
            cmd = partial(self.combateGrupal, "click-derecho")
            self.world.bind("<ButtonRelease-3>", cmd)
            cmd = partial(self.combateGrupal, "pass")
            self.root.bind("<Escape>", cmd)
            cmd = partial(self.movePlayer, "up")
            self.root.bind("<Up>", cmd)
            self.root.bind("<w>", cmd)
            self.root.bind("<W>", cmd)
            cmd = partial(self.movePlayer, "down")
            self.root.bind("<Down>", cmd)
            self.root.bind("<S>", cmd)
            self.root.bind("<s>", cmd)
            cmd = partial(self.movePlayer, "left")
            self.root.bind("<Left>", cmd)
            self.root.bind("<A>", cmd)
            self.root.bind("<a>", cmd)
            cmd = partial(self.movePlayer, "right")
            self.root.bind("<Right>", cmd)
            self.root.bind("<D>", cmd)
            self.root.bind("<d>", cmd)
            cmd = partial(self.npcInteract, "yes")
            self.root.bind("<Y>", cmd)
            self.root.bind("<y>", cmd)
            cmd = partial(self.npcInteract, "no")
            self.root.bind("<N>", cmd)
            self.root.bind("<n>", cmd)
            cmd = partial(self.npcInteract, "accept")
            self.root.bind("<Return>", cmd)
            cmd = partial(self.combateNormal, ["full"])
            self.root.bind("<k>", self.escogerArmamento, cmd)
            self.root.bind("<K>", self.escogerArmamento, cmd)
            cmd = partial(self.combateNormal, "izquierda")
            self.root.bind("<Q>", cmd)
            self.root.bind("<q>", cmd)
            cmd = partial(self.combateNormal, "derecha")
            self.root.bind("<E>", cmd)
            self.root.bind("<e>", cmd)
            cmd = partial(self.combateNormal, "fp")
            self.root.bind("<R>", cmd)
            self.root.bind("<r>", cmd)
            cmd = partial(self.combateNormal, "sp")
            self.root.bind("<F>", cmd)
            self.root.bind("<f>", cmd)
            cmd1 = partial(_itemArmadura, "casco", 0)
            cmd2 = partial(_itemArmadura, "casco", 1)
            self.infoArmaduraCasco.bind('<Button-1>', cmd1)
            self.infoArmaduraCasco.bind(_SECOND_BUTTON, cmd2)
            cmd1 = partial(_itemArmadura, "izquierda", 0)
            cmd2 = partial(_itemArmadura, "izquierda", 1)
            self.infoArmaduraArmaIzquierda.bind('<Button-1>', cmd1)
            self.infoArmaduraArmaIzquierda.bind(_SECOND_BUTTON, cmd2)
            cmd1 = partial(_itemArmadura, "izquierda", 0)
            cmd2 = partial(_itemArmadura, "izquierda", 1)
            self.infoArmaduraArmaIzquierda.bind('<Button-1>', cmd1)
            self.infoArmaduraArmaIzquierda.bind(_SECOND_BUTTON, cmd2)
            cmd1 = partial(_itemArmadura, "chaleco", 0)
            cmd2 = partial(_itemArmadura, "chaleco", 1)
            self.infoArmaduraChaleco.bind('<Button-1>', cmd1)
            self.infoArmaduraChaleco.bind(_SECOND_BUTTON, cmd2)
            cmd1 = partial(_itemArmadura, "derecha", 0)
            cmd2 = partial(_itemArmadura, "derecha", 1)
            self.infoArmaduraArmaDerecha.bind('<Button-1>', cmd1)
            self.infoArmaduraArmaDerecha.bind(_SECOND_BUTTON, cmd2)
            cmd1 = partial(_itemArmadura, "pantalones", 0)
            cmd2 = partial(_itemArmadura, "pantalones", 1)
            self.infoArmaduraPantalones.bind('<Button-1>', cmd1)
            self.infoArmaduraPantalones.bind(_SECOND_BUTTON, cmd2)
            cmd1 = partial(_itemArmadura, "botas", 0)
            cmd2 = partial(_itemArmadura, "botas", 1)
            self.infoArmaduraBotas.bind('<Button-1>', cmd1)
            self.infoArmaduraBotas.bind(_SECOND_BUTTON, cmd2)
            print lang(310)
        except Exception, extp:
            print lang(758, extp)
            totalerrors += 1

        # Se ejecutan los argumentos <consultar arguments.txt en /doc>
        if len(arg) == 1:
            print lang(286),
        elif len(arg) > 1:
            print lang(761),
        if _consultArgument("delpyc", arg):
            files = ["actors", "board", "group", "item", "mob", "npc", "lib",
                     "pop", "powers", "statics", "strict",
                     "texture_analysis", "texture_conts", "texture_items",
                     "texture_world", "textures", "sounds", "hoa",
                     "medt", "mpop", "textures_editor", "__init__"]
            for f in files:
                try:
                    os.remove("lib/" + f + ".pyc")
                except:
                    totalwarnings += 1
        if _consultArgument("dev", arg):
            self.programTitle = PROGRAM_TITLE + " v{0}".format(PROGRAM_VERSION)
            self.root.title(self.programTitle)
        if _consultArgument("disableanimation", arg):
            MOVEMENT_ANIMATION[0] = False
        if _consultArgument("disablearmorinfo", arg):
            CONFIGURATION_DATA[14] = False
        if _consultArgument("disableconfig", arg):
            CONFIGURATION_DATA[13] = False
            self.archivomenu.entryconfig(5, state=DISABLED)
        if _consultArgument("disableiteminfo", arg):
            CONFIGURATION_DATA[15] = False
        if _consultArgument("disableinfo", arg):
            CONFIGURATION_DATA[14] = False
            CONFIGURATION_DATA[15] = False
            CONFIGURATION_DATA[16] = False
        if _consultArgument("disablepowerinfo", arg):
            CONFIGURATION_DATA[16] = False
        if _consultArgument("disablesaves", arg):
            CONFIGURATION_DATA[12] = False
        if _consultArgument("disableterminal", arg):
            CONFIGURATION_DATA[11] = False
            self.ayudamenu.entryconfig(6, state=DISABLED)
        if _consultArgument("disabletranslation", arg):
            CONFIGURATION_DATA[10] = False
        if _consultArgument("enabletanimation", arg):
            MOVEMENT_ANIMATION[0] = True
        if _consultArgument("enableterminal", arg):
            CONFIGURATION_DATA[11] = True
        if _consultArgument("nosound", arg):
            CONFIGURATION_DATA[1] = False
            self.stopSound("silent")
        if _consultArgument("resizable", arg):
            self.root.resizable(width=True, height=True)
            self.root.minsize(width=0, height=0)
        if _consultArgument("savefile",
                            arg):  # Si se recibe por argumento a saveFile
            try:
                savefile = consultParam("savefile", arg)  # archivo de guardado
                if len(savefile) > 0 and savefile != "%NULL%":
                    if ".save" in savefile:
                        pass
                    else:
                        savefile += ".save"
                    if COLORED_ARGUMENT:
                        print lang(216),
                        colorcmd(savefile, "lgray")
                        print ""
                    else:
                        print lang(216), savefile, ""
                    self.loadGame("argv", savefile)
                else:
                    self.error(lang(287))
            except:
                totalwarnings += 1
                print lang(212)
        if _consultArgument("disablestdout", arg):
            sys.stdout, sys.stderr, sys.stdin, sys.__stdout__, sys.__stderr__, sys.__stdin__ = noStdOut(
            ), noStdOut(), noStdOut(), noStdOut(), noStdOut(), noStdOut()
        # Se consultan las actualizaciones si no se ha desactivado la función
        if not _consultArgument("noupdates", arg):
            try:
                try:
                    consultar = True
                    archivo = open(CONFIGURATION_ACTL, "r")
                    for i in archivo:
                        if i == "-actl=1":
                            consultar = False
                except:
                    pass
                if consultar:  # Si esta activado la consulta
                    if len(arg) >= 1:
                        print ENDING_ARGUMENT
                    print lang(747),
                    version = getVersion("HOA", CONFIGURATION_DATA[5])
                    comparacion = compararVersiones(version, PROGRAM_VERSION)
                    if comparacion == 2:
                        print lang(763, version)
                    elif comparacion == 0:
                        print lang(748)
                    else:
                        print lang(749)
                        if isWindows():
                            ysize = 145
                            xsize = 280
                        else:
                            ysize = 160
                            xsize = 320
                        e = pop([[lang(754), lang(751), lang(752), lang(753),
                                  lang(750), lang(327), lang(239)],
                                 self.images.image(
                                     "actualizacion"), "actualizacion",
                                 ysize, xsize, PROGRAM_VERSION, version])
                        e.w.mainloop(1)
                        if e.sent:
                            if e.values[0] == "si":
                                webbrowser.open(LINK_PROJECT)
                            if e.values[1] == 1:
                                archivo = open(CONFIGURATION_ACTL, "w")
                                archivo.write(
                                    "-actl=1")
                                archivo.close()
                        del e
            except:
                print lang(755)
                totalwarnings += 1
        if len(arg) >= 1:
            print ENDING_ARGUMENT

        # Se comprueba que la versión de python del cliente tenga la api de
        # movimieno usada en el juego
        print lang(825),
        try:
            self.root.after(100, makeCallable(
                partial(arrastrarImagen, "test:canvasapi", self.world, 8, 8)))
            print lang(310)
        except Exception, exerr:
            MOVEMENT_ANIMATION[0] = False
            totalerrors += 1
            print lang(54).lower()
            print langError(826, exerr)
        if not isWindows():
            MOVEMENT_ANIMATION[0] = False

        # Mensaje que indica la finalización del constructor
        if getConfigValue("global.showstate"):
            print lang(395),
            if totalwarnings == 0 and totalerrors == 0:
                print lang(310)
            else:
                if totalwarnings != 0 and totalerrors == 0:
                    print lang(757).format(str(totalwarnings)).strip()
                elif totalerrors != 0 and totalwarnings == 0:
                    print lang(760).format(str(totalerrors)).strip()
                elif totalwarnings != 0 and totalerrors != 0:
                    print lang(759).format(str(totalerrors),
                                           str(totalwarnings)).strip()
            del totalwarnings
            del totalerrors

    def abortGame(self, e=None):
        """
        Función que aborta el juego
        :param e: Evento
        :return: void
        """
        if self.ingame:  # Si se esta jugando
            self.stopSound()
            self.multiplayer_desconnect(False)
            print lang(396),
            # Se destruyen las ventanas y se dibuja la inicial
            if e != "newgame":
                self.menu.pack_forget()
                self.menu2.pack_forget()
                self.content.pack_forget()
                self.initialBg.pack()
                self.root.title(self.programTitle)
                self.initialBg.delete(ALL)
                self.initialBg.create_image(
                    405, 299, image=self.images.image("background"))
                self.initialBg.update()
                self.archivomenu.entryconfig(2, state=DISABLED)
                self.archivomenu.entryconfig(3, state=DISABLED)
                for k in range(5):
                    self.vermenu.entryconfig(k, state=DISABLED)
                self.sfx(0)

            # Se destruye la información del jugador
            delMatrix(self.dificultad)
            delMatrix(self.mapItemsTextures)
            delMatrix(self.mapLogic)
            delMatrix(self.mapSound)
            delMatrix(self.mapTextures)
            delMatrix(self.maplightning)
            delMatrix(self.mobs)
            delMatrix(self.npc)
            del self.static
            del self.activePowers
            del self.player
            try:
                del self.board
            except:
                pass

            # Se cancelan los threads
            try:
                self.root.after_cancel(self.lastnpcmovementid)
            except:
                pass
            try:
                self.root.after_cancel(self.lastmovementId)
            except:
                pass
            try:
                self.root.after_cancel(self.lastmultiplayerId)
            except:
                pass
            self.delInfo()

            # Se reconstruye el jugador
            self.activePowers = ["playername", [
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            self.board = None
            self.canmove = True
            self.canvasCorrecion = [0, 0]
            self.currentNpc = None
            self.delInfo()
            self.dificultad = [0, 0, 0, 0, 0, 0, 0]
            self.nivel_dificultad = 0
            self.enemy = None
            self.enemyId = 0
            self.inBattle = False
            self.inNpc = False
            self.ingame = False
            self.itemnumberlist = 0
            self.lastmovementId = 0
            self.lastmultiplayerId = 0
            self.lastnpcmovementid = 0
            self.loaded = False
            self.mapBackgroundSound = ["%NULL%", None, 0]
            self.mapImage = [0]
            self.mapItemsTextures = list()
            self.mapLogic = list()
            self.mapSize = [0, 0]
            self.mapSound = list()
            self.mapTextures = list()
            self.maplightning = list()
            self.mobs = list()
            self.movement = False
            self.namePartida = ""
            self.npc = list()
            self.npcId = -1
            self.npcMovement = False
            self.player = actors()
            self.playerPos = [0, 0]
            self.static = statics.Statics()
            self.tipoCombate = "NO_FIGHT"
            print lang(310)

    def checkItems(self):
        """
        Función que comprueba el estado de los items y los elimina si se han destruido
        :return: void
        """
        if self.player.getCasco() is not None:  # Se comprueba el estado de los objetos
            if self.player.getCasco().estaDestruido():
                self.player.dropCasco()
                self.static.addDroppedArmor()
                self.sfx(20)
                self.infoArmaduraCasco.config(image=self.images.image(
                    "no_casco"), state=DISABLED, cursor="arrow")
                self.textMsg(lang(choice([645, 646, 647, 648])))
                self.setInfo(lang(40))
        if self.player.getLeftWeapon() is not None:
            if self.player.getLeftWeapon().estaDestruido():
                self.static.addDroppedWeapon()
                self.player.dropLeftWeapon()
                self.sfx(35)
                self.world.delete("player:left_weapon")
                self.infoArmaduraArmaIzquierda.config(
                    image=self.images.image("no_lw"), state=DISABLED,
                    cursor="arrow")
                self.setInfo(lang(41))
                self.textMsg(lang(choice([649, 650, 651, 652, 653, 654])))
                if self.player.getActiveBullet() is not None:  # Si el jugador tenia una bala definida para esa arma a botar
                    self.player.addObject(self.player.getActiveBullet())
                    self.player.delActiveBullet()
            else:
                if self.player.getActiveBullet() is not None:
                    if self.player.getActiveBullet().estaDestruido():
                        self.player.delActiveBullet()
                        self.static.addDroppedWeapon()
                        self.setInfo(
                            lang(276))
        if self.player.getRightWeapon() is not None:
            if self.player.getRightWeapon().estaDestruido():
                self.player.dropRightWeapon()
                self.static.addDroppedWeapon()
                self.world.delete("player:right_weapon")
                self.sfx(35)
                self.infoArmaduraArmaDerecha.config(
                    image=self.images.image("no_rw"), state=DISABLED,
                    cursor="arrow")
                self.setInfo(lang(43))
                self.textMsg(lang(choice([649, 650, 651, 652, 653, 654])))
        if self.player.getChaleco() is not None:
            if self.player.getChaleco().estaDestruido():
                self.player.dropChaleco()
                self.static.addDroppedArmor()
                self.sfx(20)
                self.infoArmaduraChaleco.config(image=self.images.image(
                    "no_chaleco"), state=DISABLED, cursor="arrow")
                self.setInfo(lang(42))
                self.textMsg(lang(choice([655, 656, 657, 658, 659])))
        if self.player.getPantalones() is not None:
            if self.player.getPantalones().estaDestruido():
                self.player.dropPantalones()
                self.static.addDroppedArmor()
                self.sfx(20)
                self.infoArmaduraPantalones.config(
                    image=self.images.image("no_pantalon"), state=DISABLED,
                    cursor="arrow")
                self.setInfo(lang(44))
                self.textMsg(lang(choice([660, 661, 662, 663, 664])))
        if self.player.getBotas() is not None:
            if self.player.getBotas().estaDestruido():
                self.player.dropBotas()
                self.static.addDroppedWeapon()
                self.sfx(20)
                self.infoArmaduraBotas.config(image=self.images.image(
                    "no_botas"), state=DISABLED, cursor="arrow")
                self.setInfo(lang(45))
                self.textMsg(lang(choice([665, 666, 667, 668, 669])))

    # TODO: Tipo de AI normal y dificil
    def combateGrupal(self, event=None, event2=None, breakpoint=None):
        """
        Función que maneja el combate grupal con los mobs
        :param event: Evento ?
        :param event2: Evento ?
        :param breakpoint: -
        :return: void
        """

        def _lookAvaiablePos(posx, posy, movements, turn, tipo, ataque):
            """
            Función que imprime los movimientos disponibles para el turno
            :param posx: Posición x
            :param posy: Posición y
            :param movements: Lista de movimientos
            :param turn: Turno
            :param tipo: Tipo de jugador
            :param ataque: Ataque del jugador
            :return:
            """

            def _look(newposx, newposy, direccmatrix, direcc, avaiablepos,
                      tags):
                """
                Función que busca si está disponible el movimiento
                :param newposx: Posición x
                :param newposy: Posición y
                :param direccmatrix: Matriz de direcciones
                :param direcc: Dirección de búsqueda recursiva
                :param avaiablepos: Tile
                :param tags: Tags del tile
                :return: void
                """
                if 0 <= newposx < self.board.getBoardSizeX() and 0 <= newposy < self.board.getBoardSizeY():  # Si se está dentro de los márgenes
                    if self.board.getLogic(newposx,
                                           newposy) == "none":  # Si es un tile válido se agrega la posición y se imprime en el canvas
                        tag_tile = generateRandom6()
                        if turn == TURN_HN:
                            self.world.create_rectangle(
                                32 * newposx + self.board.getBoardCorreccionX() + 2,
                                32 * newposy + self.board.getBoardCorreccionY() + 3,
                                32 + 32 * newposx + self.board.getBoardCorreccionX(),
                                32 + 32 * newposy + self.board.getBoardCorreccionY() + 1,
                                fill=LINE_BOARD_COLOR_ACTIVE,
                                outline=LINE_BOARD_COLOR_ACTIVE,
                                tags=tag_tile)
                        elif turn == TURN_AI:
                            self.world.create_rectangle(
                                32 * newposx + self.board.getBoardCorreccionX() + 2,
                                32 * newposy + self.board.getBoardCorreccionY() + 3,
                                32 + 32 * newposx + self.board.getBoardCorreccionX(),
                                32 + 32 * newposy + self.board.getBoardCorreccionY() + 1,
                                fill=RECT_CANT_COLOR_FG_M,
                                outline=RECT_CANT_COLOR_FG_M,
                                tags=tag_tile)
                        avaiablepos.append([newposx, newposy])
                        tags.append(tag_tile)
                        self.world.tag_raise(tag_tile, "grupal:background")
                    # si el tile es un mob
                    elif self.board.getLogic(newposx,
                                             newposy) == "mob" and turn == TURN_HN:
                        tag_tile = generateRandom6()
                        self.world.create_rectangle(
                            32 * newposx + self.board.getBoardCorreccionX() + 2,
                            32 * newposy + self.board.getBoardCorreccionY() + 3,
                            32 + 32 * newposx + self.board.getBoardCorreccionX(),
                            32 + 32 * newposy + self.board.getBoardCorreccionY() + 1,
                            fill=RECT_CANT_COLOR_BG_M,
                            outline=RECT_CANT_COLOR_BG_M,
                            tags=tag_tile)
                        avaiablepos.append([newposx, newposy])
                        tags.append(tag_tile)
                        self.world.tag_raise(tag_tile, "grupal:background")
                        direccmatrix[direcc] = 0
                    elif self.board.getLogic(newposx,
                                             newposy) == "player" and turn == TURN_AI:
                        tag_tile = generateRandom6()
                        self.world.create_rectangle(
                            32 * newposx + self.board.getBoardCorreccionX() + 2,
                            32 * newposy + self.board.getBoardCorreccionY() + 3,
                            32 + 32 * newposx + self.board.getBoardCorreccionX(),
                            32 + 32 * newposy + self.board.getBoardCorreccionY() + 1,
                            fill=RECT_CANT_COLOR_FG_A,
                            outline=RECT_CANT_COLOR_FG_A,
                            tags=tag_tile)
                        avaiablepos.append([newposx, newposy])
                        tags.append(tag_tile)
                        self.world.tag_raise(tag_tile, "grupal:background")
                        direccmatrix[direcc] = 0
                    else:
                        direccmatrix[direcc] = 0
                else:
                    direccmatrix[direcc] = 0

            def _lookArrow(newposx, newposy, direccmatrix, direcc, avaiablepos,
                           tags, tipo):
                """
                Función que busca si está disponible el movimiento para un lanzamiento de flechas
                :param newposx: Posición x
                :param newposy: Posición y
                :param direccmatrix: Matriz de direcciones
                :param direcc: Dirección de búsqueda recursiva
                :param avaiablepos: Tile
                :param tags: Tags del tile
                :param tipo: Tipo de ataque
                :return: void
                """
                if 0 <= newposx < self.board.getBoardSizeX() and 0 <= newposy < self.board.getBoardSizeY():  # Si se está dentro de los márgenes
                    # Si es un tile válido continua
                    if self.board.getLogic(newposx, newposy) == "none":
                        pass
                    elif self.board.getLogic(newposx,
                                             newposy) == "mob" and turn == TURN_HN:  # si el tile es un mob se agrega la posicion y se imprime en el canvas
                        tag_tile = generateRandom6()
                        self.world.create_polygon(
                            32 * newposx + self.board.getBoardCorreccionX() + 2,
                            32 * newposy + self.board.getBoardCorreccionY() + 33,
                            32 * newposx + self.board.getBoardCorreccionX() + 32,
                            32 * newposy + self.board.getBoardCorreccionY() + 33,
                            32 * newposx + self.board.getBoardCorreccionX() + 32,
                            32 * newposy + self.board.getBoardCorreccionY() + 3,
                            fill=RECT_CANT_COLOR_FG_A,
                            outline=RECT_CANT_COLOR_FG_A,
                            tags=tag_tile)
                        texture_tile = generateRandom6()
                        if tipo == "PL":
                            flecha = self.world.create_image(
                                25 + 32 * newposx + self.board.getBoardCorreccionX(),
                                # @UnusedVariable
                                self.board.getBoardCorreccionY() + 32 * newposy + 25,
                                image=self.images.image(
                                    self.player.getLeftWeapon().getImage() + "_16"),
                                tags=texture_tile)
                        else:
                            flecha = self.world.create_image(
                                25 + 32 * newposx + self.board.getBoardCorreccionX(),
                                # @UnusedVariable
                                self.board.getBoardCorreccionY() + 32 * newposy + 25,
                                image=self.images.image(
                                    self.board.getWeapon()),
                                tags=texture_tile)
                        avaiablepos.append([newposx, newposy])
                        tags.append(tag_tile)
                        tags.append(texture_tile)
                        self.world.tag_raise(tag_tile, "grupal:background")
                        direccmatrix[direcc] = 0
                    elif self.board.getLogic(newposx,
                                             newposy) == "player" and turn == TURN_AI:
                        tag_tile = generateRandom6()
                        self.world.create_rectangle(
                            32 * newposx + self.board.getBoardCorreccionX() + 2,
                            32 * newposy + self.board.getBoardCorreccionY() + 3,
                            32 + 32 * newposx + self.board.getBoardCorreccionX(),
                            32 + 32 * newposy + self.board.getBoardCorreccionY() + 1,
                            fill=RECT_CANT_COLOR_FG_A,
                            outline=RECT_CANT_COLOR_FG_A,
                            tags=tag_tile)
                        avaiablepos.append([newposx, newposy])
                        tags.append(tag_tile)
                        self.world.tag_raise(tag_tile, "grupal:background")
                        direccmatrix[direcc] = 0
                    elif self.board.getLogic(newposx,
                                             newposy) == "player" and turn == TURN_HN:  # Si el tile contiene a un humano y juega el humano puede continuar
                        if self.nivel_dificultad in [DIFICULTAD_FACIL,
                                                     DIFICULTAD_MEDIO]:
                            pass
                        else:
                            direccmatrix[direcc] = 0
                    elif self.board.getLogic(newposx,
                                             newposy) == "mob" and turn == TURN_AI:
                        pass
                    elif self.board.getLogic(newposx,
                                             newposy) == "abs" and turn == TURN_HN:
                        if self.nivel_dificultad == DIFICULTAD_FACIL:
                            pass
                        else:
                            direccmatrix[direcc] = 0
                    elif self.board.getLogic(newposx,
                                             newposy) == "abs" and turn == TURN_AI:
                        if self.nivel_dificultad == DIFICULTAD_DIFICIL:
                            pass
                        else:
                            direccmatrix[direcc] = 0
                    else:
                        direccmatrix[direcc] = 0
                else:
                    direccmatrix[direcc] = 0

            for tag in self.board.getAvaiableTags():
                self.world.delete(tag)  # elimina las imágenes previas
            for tar in self.board.getAvaiableArrowTag():
                self.world.delete(tar)  # elimina las imágenes de las flechas
            self.board.dropCache()  # elimina el caché de los anteriores movimientos

            # Se calculan tiles de ataque secundario
            image_avaiable_tiles_arrow = []
            avaiable_attack = []
            if tipo in ["FS", "FM"]:
                direcciones = [0, 0, 0, 0, 0, 0, 0, 0]  # NE,N,NW,W,E,SE,S,SW
            elif tipo in ["PL",
                          "FL"]:  # Si el tipo es jugador o follower liviano
                if tipo == "PL":  # Si es el jugador
                    if self.player.getLeftWeapon() is not None:  # Si posee un arma izquierda
                        if self.player.getActiveBullet() is not None:  # Si tiene balas
                            if self.player.getLeftWeapon().getType() == "weapon/left":  # Si son flechas
                                if self.nivel_dificultad == DIFICULTAD_DIFICIL:
                                    # NE,N,NW,W,E,SE,S,SW
                                    direcciones = [0, 1, 0, 1, 1, 0, 1, 0]
                                else:
                                    # NE,N,NW,W,E,SE,S,SW
                                    direcciones = [1, 1, 1, 1, 1, 1, 1, 1]
                            else:
                                # NE,N,NW,W,E,SE,S,SW
                                direcciones = [0, 0, 0, 0, 0, 0, 0, 0]
                        else:
                            # NE,N,NW,W,E,SE,S,SW
                            direcciones = [0, 0, 0, 0, 0, 0, 0, 0]
                    else:
                        # NE,N,NW,W,E,SE,S,SW
                        direcciones = [0, 0, 0, 0, 0, 0, 0, 0]
                elif tipo == "FL":
                    if self.nivel_dificultad in [DIFICULTAD_FACIL,
                                                 DIFICULTAD_MEDIO]:
                        # NE,N,NW,W,E,SE,S,SW
                        direcciones = [1, 1, 1, 1, 1, 1, 1, 1]
                    else:
                        # NE,N,NW,W,E,SE,S,SW
                        direcciones = [0, 1, 0, 1, 1, 0, 1, 0]
            elif tipo == "MB":
                if ataque == "LARGO":
                    if self.nivel_dificultad in [DIFICULTAD_FACIL,
                                                 DIFICULTAD_MEDIO]:
                        # NE,N,NW,W,E,SE,S,SW
                        direcciones = [0, 1, 0, 1, 1, 0, 1, 0]
                    else:
                        # NE,N,NW,W,E,SE,S,SW
                        direcciones = [1, 1, 1, 1, 1, 1, 1, 1]
                else:
                    # NE,N,NW,W,E,SE,S,SW
                    direcciones = [0, 0, 0, 0, 0, 0, 0, 0]
            # Se buscan las posiciones válidas para el ataque con flecha
            for c in range(1, movements + 1):
                if direcciones[0] == 1:
                    _lookArrow(posx - c, posy - c, direcciones, 0,
                               avaiable_attack,
                               image_avaiable_tiles_arrow,
                               tipo)  # se busca al nor-este
                if direcciones[1] == 1:
                    _lookArrow(posx, posy - c, direcciones, 1, avaiable_attack,
                               image_avaiable_tiles_arrow,
                               tipo)  # se busca al norte
                if direcciones[2] == 1:
                    _lookArrow(posx + c, posy - c, direcciones, 2,
                               avaiable_attack,
                               image_avaiable_tiles_arrow,
                               tipo)  # se busca al nor-oeste
                if direcciones[3] == 1:
                    _lookArrow(posx - c, posy, direcciones, 3, avaiable_attack,
                               image_avaiable_tiles_arrow,
                               tipo)  # se busca al este
                if direcciones[4] == 1:
                    _lookArrow(posx + c, posy, direcciones, 4, avaiable_attack,
                               image_avaiable_tiles_arrow,
                               tipo)  # se busca al oeste
                if direcciones[5] == 1:
                    _lookArrow(posx - c, posy + c, direcciones, 5,
                               avaiable_attack,
                               image_avaiable_tiles_arrow,
                               tipo)  # se busca al sur-este
                if direcciones[6] == 1:
                    _lookArrow(posx, posy + c, direcciones, 6, avaiable_attack,
                               image_avaiable_tiles_arrow,
                               tipo)  # se busca al sur
                if direcciones[7] == 1:
                    _lookArrow(posx + c, posy + c, direcciones, 7,
                               avaiable_attack,
                               image_avaiable_tiles_arrow,
                               tipo)  # se busca al sur-oeste
                if sum(direcciones) == 0:
                    break  # si ya no hay mas caminos disponibles se termina la búsqueda

            # Se calculan nuevos movimientos
            image_avaiable_tiles_tags = []  # tag de los movimientos nuevos
            avaiable_pos = []  # posiciones válidas
            if tipo == "FS":
                if self.nivel_dificultad in [DIFICULTAD_FACIL,
                                             DIFICULTAD_MEDIO]:
                    # NE,N,NW,W,E,SE,S,SW
                    direcciones = [1, 1, 0, 0, 1, 0, 1, 1]
                else:
                    # NE,N,NW,W,E,SE,S,SW
                    direcciones = [0, 1, 0, 0, 1, 0, 1, 0]
            elif tipo in ["PL", "FM", "MB"]:
                direcciones = [1, 1, 1, 1, 1, 1, 1, 1]  # NE,N,NW,W,E,SE,S,SW
            elif tipo == "FL":
                direcciones = [1, 0, 1, 0, 0, 1, 0, 1]  # NE,N,NW,W,E,SE,S,SW
            for c in range(1,
                           movements + 1):  # Se buscan las posiciones válidas
                if direcciones[0] == 1:
                    _look(posx - c, posy - c, direcciones, 0, avaiable_pos,
                          image_avaiable_tiles_tags)  # se busca al nor-este
                if direcciones[1] == 1:
                    _look(posx, posy - c, direcciones, 1, avaiable_pos,
                          image_avaiable_tiles_tags)  # se busca al norte
                if direcciones[2] == 1:
                    _look(posx + c, posy - c, direcciones, 2, avaiable_pos,
                          image_avaiable_tiles_tags)  # se busca al nor-oeste
                if direcciones[3] == 1:
                    _look(posx - c, posy, direcciones, 3, avaiable_pos,
                          image_avaiable_tiles_tags)  # se busca al este
                if direcciones[4] == 1:
                    _look(posx + c, posy, direcciones, 4, avaiable_pos,
                          image_avaiable_tiles_tags)  # se busca al oeste
                if direcciones[5] == 1:
                    _look(posx - c, posy + c, direcciones, 5, avaiable_pos,
                          image_avaiable_tiles_tags)  # se busca al sur-este
                if direcciones[6] == 1:
                    _look(posx, posy + c, direcciones, 6, avaiable_pos,
                          image_avaiable_tiles_tags)  # se busca al sur
                if direcciones[7] == 1:
                    _look(posx + c, posy + c, direcciones, 7, avaiable_pos,
                          image_avaiable_tiles_tags)  # se busca al sur-oeste
                if sum(direcciones) == 0:
                    break  # si ya no hay mas caminos disponibles se termina la búsqueda
            tag_self = generateRandom6()  # Dibujo un recuadro en la misma posición
            if turn == TURN_HN:
                if tipo == "PL":
                    self.world.create_rectangle(
                        32 * posx + self.board.getBoardCorreccionX() + 1,
                        32 * posy + self.board.getBoardCorreccionY() + 2,
                        32 + 32 * posx + self.board.getBoardCorreccionX() + 1,
                        32 + 32 * posy + self.board.getBoardCorreccionY() + 2,
                        fill=RECT_CANT_COLOR_BG_P,
                        outline=RECT_CANT_COLOR_BG_P, tags=tag_self)
                else:
                    self.world.create_rectangle(
                        32 * posx + self.board.getBoardCorreccionX() + 1,
                        32 * posy + self.board.getBoardCorreccionY() + 2,
                        32 + 32 * posx + self.board.getBoardCorreccionX() + 1,
                        32 + 32 * posy + self.board.getBoardCorreccionY() + 2,
                        fill=RECT_CANT_COLOR_BG_F,
                        outline=RECT_CANT_COLOR_BG_F, tags=tag_self)
            elif turn == TURN_AI:
                self.world.create_rectangle(
                    32 * posx + self.board.getBoardCorreccionX() + 1,
                    32 * posy + self.board.getBoardCorreccionY() + 2,
                    32 + 32 * posx + self.board.getBoardCorreccionX() + 1,
                    32 + 32 * posy + self.board.getBoardCorreccionY() + 2,
                    fill=RECT_CANT_COLOR_BG_M, outline=RECT_CANT_COLOR_BG_M,
                    tags=tag_self)
            avaiable_pos.append([posx, posy])
            image_avaiable_tiles_tags.append(tag_self)

            self.board.addCache(avaiable_pos, image_avaiable_tiles_tags,
                                avaiable_attack,
                                image_avaiable_tiles_arrow)  # se agrega el caché al board
            # Actualizo el mundo
            self.world.tag_raise(tag_self, "grupal:background")
            self.world.update()

        def _move(x, y, id, type):  # @ReservedAssignment
            """
            Mueve al grupo
            :param x: Posición x
            :param y: Posición y
            :param id: ID del grupo
            :param type: Tipo de jugador
            :return:
            """

            def _drawRectangle(type, x, y, id, tag,
                               tagnum):  # @ReservedAssignment
                """
                Función que escribe el recuadro
                :param type: Tipo de jugador
                :param x: Posición x
                :param y: Posición y
                :param id: ID del jugador
                :param tag: Tag del tile
                :param tagnum: Numero de tile
                :return: void
                """
                try:
                    if type == "PL":  # Si no es el jugador al quien se dibuja
                        self.world.create_rectangle(
                            14 + 32 * x + self.board.getBoardCorreccionX(),
                            4 + 32 * y + self.board.getBoardCorreccionY(),
                            31 + 32 * x + self.board.getBoardCorreccionX(),
                            13 + 32 * y + self.board.getBoardCorreccionY(),
                            fill=RECT_CANT_COLOR_BG_P,
                            outline=RECT_CANT_COLOR_FG_P, tags=tag)
                        self.world.tag_lower(tag, tagnum)
                    elif type == "MB":
                        self.world.create_rectangle(
                            19 + 32 * x + self.board.getBoardCorreccionX(),
                            4 + 32 * y + self.board.getBoardCorreccionY(),
                            31 + 32 * x + self.board.getBoardCorreccionX(),
                            13 + 32 * y + self.board.getBoardCorreccionY(),
                            fill=RECT_CANT_COLOR_BG_M,
                            outline=RECT_CANT_COLOR_FG_M, tags=tag)
                        self.world.tag_lower(tag, tagnum)
                    else:
                        self.world.create_rectangle(
                            19 + 32 * x + self.board.getBoardCorreccionX(),
                            4 + 32 * y + self.board.getBoardCorreccionY(),
                            31 + 32 * x + self.board.getBoardCorreccionX(),
                            13 + 32 * y + self.board.getBoardCorreccionY(),
                            fill=RECT_CANT_COLOR_BG_F,
                            outline=RECT_CANT_COLOR_FG_F, tags=tag)
                        self.world.tag_lower(tag, tagnum)
                except:
                    pass

            if type == "PL":
                tag = ["grupal:follower:actor:" +
                       str(id), "grupal:player:box", "grupal:player:number",
                       22]
            elif type == "MB":
                tag = ["grupal:mob:actor:" +
                       str(id), "grupal:mob:box:" + str(id),
                       "grupal:mob:number:" + str(id), 25]
            else:
                tag = ["grupal:follower:actor:" + str(id),
                       "grupal:follower:box:" + str(id),
                       "grupal:follower:number:" + str(id), 25]
            self.world.delete(tag[1])
            if type == "MB":
                group = self.board.getEnemies()[id]
            else:
                group = self.board.getPlayers()[id]
            self.board.setLogic(group.getPosX(), group.getPosY(), "none")
            group.setPos(x, y)
            if type != "MB":
                self.board.setLogic(x, y, "player")
            else:
                self.board.setLogic(x, y, "mob")
            if MOVEMENT_ANIMATION[0]:  # Movimiento con animación
                try:
                    self.root.after(TEXDT, makeCallable(
                        partial(arrastrarImagen, tag[0], self.world,
                                18 + 32 * x + self.board.getBoardCorreccionX(),
                                32 * y + 18 + self.board.getBoardCorreccionY())))
                    self.root.after(TEXDT, makeCallable(
                        partial(arrastrarImagen, tag[2], self.world, tag[
                            3] + 32 * x + self.board.getBoardCorreccionX(),
                                32 * y + 9 + self.board.getBoardCorreccionY())))
                    self.root.after(TEXDT, partial(
                        _drawRectangle, type, x, y, id, tag[1], tag[2]))
                except Exception, exerr:
                    print langError(389, exerr)
            else:  # Movimiento sin animación
                self.world.coords(tag[0],
                                  18 + 32 * x + self.board.getBoardCorreccionX(),
                                  32 * y + 18 + self.board.getBoardCorreccionY())
                self.world.coords(tag[2], tag[
                    3] + 32 * x + self.board.getBoardCorreccionX(),
                                  32 * y + 9 + self.board.getBoardCorreccionY())
                _drawRectangle(type, x, y, id, tag[1], tag[2])
            self.sonido(self.board.getSound(x, y))  # sonido del tile

        def _intAlert(x, y, int):  # @ReservedAssignment
            """
            Dibuja un int en el mundo
            :param x: Posición x
            :param y: Posición y
            :param int: Integer
            :return: void
            """

            def _deletenumber(tag):
                """
                Función que borra un tag del mapa y lo actualiza
                :param tag: String
                :return: void
                """
                self.world.delete(tag)
                self.world.update()

            tag = generateRandom6()
            try:
                self.world.create_text(
                    10 + 32 * x + self.board.getBoardCorreccionX(),
                    25 + 32 * y + self.board.getBoardCorreccionY(),
                    text="-" + str(int), fill="red", font=self.fonts[5],
                    anchor=CENTER, tags=tag)
            except:
                pass
            self.world.update()
            self.root.after(TIME_ALERT, lambda: _deletenumber(tag))

        def _comprobarEnd(finalize=False):
            """
            Se comprueba si se ha terminado la partida
            :param finalize: Boolean
            :return: void
            """
            if len(
                    self.board.getEnemies()) == 0 or finalize:  # Si no hay más mobs
                is_dead = True
                # Se recoge la cantidad de seguidores resultantes
                followers = [0, 0, 0]
                for pl in self.board.getPlayers():  # Se recorren los jugadores
                    if pl.getType() == "PL" and pl.getLifeUnit() > 0:
                        self.player.setDamage(
                            self.player.getMaxLife() - pl.getLifeUnit())
                        is_dead = False
                    elif pl.getType() == "FL":
                        followers[0] += pl.getTotal()
                    elif pl.getType() == "FM":
                        followers[1] += pl.getTotal()
                    elif pl.getType() == "FS":
                        followers[2] += pl.getTotal()
                followers_perdidos = (
                                         self.player.getLightFriends() -
                                         followers[
                                             0]) + (
                                         self.player.getMediumFriends() -
                                         followers[1]) + \
                                     (self.player.getStrongFriends() -
                                      followers[2])
                self.player.setFriends(followers)
                if not is_dead and not finalize:  # Si no está muerto
                    self.setInfo(lang(730))
                    total_experiencia = self.board.getTotalExp()
                    self.incrementarExperiencia(total_experiencia)
                    obj = self.enemy.getObjDrown()  # se obtiene el objeto del mob
                    if obj != "%NULL%":  # Si el objeto recogido no es vacío
                        self.static.addObj()
                        self.playerText("+" + lang(143), "blanco", True)
                        # se agrega nuevo objeto al jugador
                        self.player.addObject(Item(parseObject(obj)))
                        # Si el objeto era stackable
                        if obj.split(ITEMSEPARATOR)[5] == "True":
                            self.setInfo(
                                lang(95, str(obj.split(ITEMSEPARATOR)[6]),
                                     str(obj.split(ITEMSEPARATOR)[0])).lower())
                        else:
                            self.setInfo(
                                lang(96, str(obj.split(ITEMSEPARATOR)[0])))
                    self.mapLogic[self.enemy.getPosicionY()][
                        self.enemy.getPosicionX()] = "none"  # se modifica el mapa lógico
                    self.enemy = None
                    self.mobs.pop(self.enemyId)
                    self.enemyId = 0
                    self.inBattle = False  # termino la batalla
                    self.world.delete(ALL)
                    self.tipoCombate = "NO_FIGHT"
                    # Inserto sangre en el mapa original
                    if self.maplightning[
                        self.board.returnOriginalEnemy().getPosicionY()][
                        self.board.returnOriginalEnemy().getPosicionX()] == 0:  # si es de dia
                        self.mapItemsTextures[
                            self.board.returnOriginalEnemy().getPosicionY()][
                            self.board.returnOriginalEnemy().getPosicionX()] = choice(
                            EFFECT_BLOOD_DAY)
                    else:
                        self.mapItemsTextures[
                            self.board.returnOriginalEnemy().getPosicionY()][
                            self.board.returnOriginalEnemy().getPosicionX()] = choice(
                            EFFECT_BLOOD_NIGHT)
                    self.update()
                    del self.board  # elimino el tablero
                    self.sfx(30)  # sonido de victoria
                    e = pop([[lang(731), lang(173)],
                             self.images.image("iconmuerte"), "aviso", 85, 270,
                             lang(733, str(total_experiencia)) + "\n" +
                             lang(732, str(followers_perdidos))])
                    e.w.mainloop(1)
                    del e
                    return True
                else:  # Si el jugador murió
                    self.setInfo(lang(82))
                    self.setInfo(lang(81))
                    self.sfx(29)
                    e = pop([[lang(82), lang(173)], self.images.image(
                        "iconmuerte"), "aviso", 85, 270, lang(83)])
                    e.w.mainloop(1)
                    del e
                    self.abortGame()
                    return True
            else:
                return False

        def _throwArrow(x, y, xo, yo, tipo):
            """
            Función que Lanza una flecha hasta (x,y) desde (xo,yo)
            :param x: Posición x final
            :param y: Posición y final
            :param xo: Posición x origen
            :param yo: Posición y origen
            :param tipo: Tipo de jugador
            :return: void
            """
            if MOVEMENT_ANIMATION[0]:  # Si las animaciones estan activas
                flecha_id = generateRandom12()  # Dibujo la imagen de la flecha
                if tipo == "PL":  # Si es el jugador se dibuja la flecha cargada
                    flecha = self.world.create_image(
                        18 + 32 * xo + self.board.getBoardCorreccionX(),
                        # @UnusedVariable
                        self.board.getBoardCorreccionY() + 32 * yo + 18,
                        image=self.images.image(
                            self.player.getActiveBullet().getImage() + "_16"),
                        tags=flecha_id)
                    self.player.getActiveBullet().usar()  # Se gasta una flecha
                    self.checkItems()
                    self.dibujarItems()
                else:
                    flecha = self.world.create_image(
                        18 + 32 * xo + self.board.getBoardCorreccionX(),
                        # @UnusedVariable
                        self.board.getBoardCorreccionY() + 32 * yo + 18,
                        image=self.images.image(self.board.getArrow()),
                        tags=flecha_id)
                self.root.after(TEXDT, makeCallable(
                    partial(arrastrarImagenPx, flecha_id, self.world,
                            18 + 32 * x + self.board.getBoardCorreccionX(),
                            self.board.getBoardCorreccionY() + 32 * y + 18,
                            DPX)))  # Muevo la flecha al mob
                self.root.after(TIME_DISSAPEAR_EFFECT,
                                lambda: self.world.delete(flecha_id))

        def _fight(group, mobs, player, x, y, mob_id, mode):
            """
            Función que crea el combate
            :param group: Grupo de ataque
            :param mobs: Enemigo
            :param player: Jugador
            :param x: Posición x
            :param y: Posición y
            :param mob_id: ID del movb
            :param mode: Modo de ataque
            :return: Boolean
            """
            if player:
                atk = group.getAtk() * (mobs.getCant()) + group.getAtk() * len(
                    self.board.getPlayers())  # se recoge el ataque
            else:
                atk = group.attack()
            dff = mobs.defend()  # se recoge la defensa
            vida_unitaria = mobs.getLifeUnit()  # se recoge la vida total
            if mobs.getType() != "PL":  # Si el defensor no es el jugador
                cant_tot = mobs.getTotal()  # si el jugador no toma la función de atacante
                if atk > dff:
                    # cantidad de muertos
                    kills = int((atk - dff) / vida_unitaria)
                else:
                    kills = 0
            else:
                cant_tot = mobs.getLifeUnit()  # vida inicial
                if atk - dff * group.getCant() > 0:
                    kills = cant_tot - \
                            (atk - dff * group.getCant())  # vida final
                    if kills <= 0:
                        _comprobarEnd(True)
                else:
                    kills = cant_tot
            _intAlert(x, y, atk - dff)  # se dibuja un estado numérico
            if player:
                # si el jugador tomo el rol del atacante
                self.setInfo(lang(727, str(atk), str(dff)))
            else:
                if mobs.getType() == "PL":
                    self.setInfo(
                        lang(734, str(atk), str(dff * group.getCant())))
                else:
                    self.setInfo(lang(734, str(atk), str(dff)))
            if mobs.getType() == "PL" and abs(atk - dff * group.getCant()) > 0:
                self.player.increaseDamageNODEFN(
                    atk - dff * group.getCant())
                self.updateInfoPlayer()
            if (
                            kills <= cant_tot and mobs.getType() == "PL") or kills < cant_tot:  # si no se han matado todos los elementos del grupo o el jugador (PL) aún tiene vida
                if group.getType() == "FL" and mode == "f":
                    if self.player.getType().upper() == "MAGO":
                        self.sfx(40)  # sonido de magia
                    else:
                        self.sfx(24)  # sonido de flecha
                else:
                    self.sfx(13)  # sonidos
                if player:
                    # si no se han matado a todos
                    self.setInfo(lang(728, str(kills)))
                else:
                    if mobs.getType() != "PL":
                        # si no se han matado a todos
                        self.setInfo(lang(735, str(kills)))
                    else:
                        if kills == cant_tot:
                            self.setInfo(lang(742))
                        else:
                            self.setInfo(lang(741, str(int(cant_tot - kills))))
                if mobs.getType() != "PL":
                    # se disminuye la cantidad de elementos en el grupo
                    mobs.disminuir(kills)
                else:
                    mobs.setVida(kills)
                if player:
                    self.world.delete("grupal:mob:number:" + str(mob_id))
                    self.world.create_text(
                        25 + 32 * x + self.board.getBoardCorreccionX(),
                        9 + 32 * y + self.board.getBoardCorreccionY(),
                        text=str(mobs.getCant()), fill=RECT_CANT_COLOR_TX_M,
                        font=self.fonts[1],
                        anchor=CENTER,
                        tags="grupal:mob:number:" + str(mob_id))
                else:
                    if mobs.getType() != "PL":
                        self.world.delete(
                            "grupal:follower:number:" + str(mob_id))
                        self.world.create_text(
                            25 + 32 * x + self.board.getBoardCorreccionX(),
                            9 + 32 * y + self.board.getBoardCorreccionY(),
                            text=str(mobs.getCant()),
                            fill=RECT_CANT_COLOR_TX_F, font=self.fonts[1],
                            anchor=CENTER,
                            tags="grupal:follower:number:" + str(mob_id))
                    else:
                        self.world.delete("grupal:player:number")
                        self.world.create_text(
                            22 + 32 * x + self.board.getBoardCorreccionX(),
                            9 + 32 * y + self.board.getBoardCorreccionY(),
                            text=str(mobs.getLifeUnit()),
                            fill=RECT_CANT_COLOR_TX_F,
                            font=self.fonts[
                                1], anchor=CENTER,
                            tags="grupal:player:number")
                if group.getType() == "PL":
                    self.player.increaseDamageNODEFN(kills)
                    self.updateInfoPlayer()
                return True
            else:  # Si mató a todos se elimina
                if self.board.getLight(x, y) == 0:
                    self.board.addBlood(choice(EFFECT_BLOOD_DAY), x,
                                        y)  # @UndefinedVariable
                else:
                    self.board.addBlood(choice(EFFECT_BLOOD_NIGHT), x, y)
                if group.getType() == "FL" and mode == "f":
                    if self.player.getType().upper() == "MAGO":
                        self.sfx(40)  # sonido de magia
                    else:
                        self.sfx(13)  # sonido de flecha
                self.board.setLogic(x, y, "none")
                if player:
                    self.setInfo(lang(729))
                else:
                    self.setInfo(lang(736))
                if player:
                    self.board.mobs.pop(mob_id)
                else:
                    self.board.players.pop(mob_id)
                self.dibujarMundo()
                if _comprobarEnd():
                    return
                else:
                    return False
            self.world.update()

        def _nextAITurn():
            """
            Función que avanza el turno de los mobs
            :return: void
            """
            if self.board.addAITurno():  # Si se ha terminado el turno completo de los mobs comienza el del jugador
                self.board.disableAI()
            else:
                self.root.after(AI_ATTACK, self.combateGrupal)
            self.combateGrupal("print")

        def _nextTurn():
            """
            Función que avanza en el turno
            :return: void
            """
            if self.board.addTurno():  # Si ha terminado el turno completo del jugador comienza el de los mobs
                self.board.enableAI()
                self.combateGrupal("print")
                self.root.after(AI_ATTACK, self.combateGrupal)
            self.combateGrupal("print")

        # Si se encuentra en dicho modo de combate y juega el usuario
        if self.inBattle and self.tipoCombate == MODE_FIGHT_GROUP and self.board.returnControl():
            if event != "print":  # Si el evento es distinto al de imprimir el estado del tablero
                if event == "pass":  # Si el evento es saltarse el turno
                    _nextTurn()
                    self.sonidoFx(SONIDO[39][0])
                elif event == "click-izquierdo":  # Si es atacar y mover
                    (x, y) = whatTileD(event2.x,
                                       self.board.getBoardCorreccionX(),
                                       event2.y,
                                       self.board.getBoardCorreccionY())
                    # Si se ha clickeado dentro de los márgenes del board
                    if 0 <= x < self.board.getBoardSizeX() and 0 <= y < self.board.getBoardSizeY():
                        if [x,
                            y] in self.board.getAvaiablePos():  # Si el tile clickeado está dentro de las posiciones válidas
                            group = self.board.players[self.board.getTurno()]
                            # Si no hay nada en el tile clickeado se mueve
                            if self.board.getLogic(x, y) == "none":
                                _move(x, y, self.board.getTurno(),
                                      group.getType())
                            # Si hay un mob en dicho tile
                            elif self.board.getLogic(x, y) == "mob":
                                xi = group.getPosX()
                                yi = group.getPosY()  # Muevo al jugador al tile más cercano disponible
                                if yi == y:  # Si está en el mismo y
                                    if x < xi:
                                        to = [x + 1, y]
                                    else:
                                        to = [x - 1, y]
                                elif xi == x:  # Si está en el mismo x
                                    if y > yi:
                                        to = [x, y - 1]
                                    else:
                                        to = [x, y + 1]
                                elif yi < y and xi < x:
                                    # si está en la esquina inferior izquierda
                                    to = [x - 1, y - 1]
                                elif yi > y and xi < x:
                                    # si está en la esquina superior izquierda
                                    to = [x - 1, y + 1]
                                elif yi < y and xi > x:
                                    # si está en la esquina inferior derecha
                                    to = [x + 1, y - 1]
                                elif yi > y and xi > x:
                                    # si está en la esquina superior derecha
                                    to = [x + 1, y + 1]
                                _move(to[0], to[1], self.board.getTurno(),
                                      group.getType())  # se mueve al tile más cercano
                                mob_id = 0  # id del mob
                                for mobs in self.board.getEnemies():  # Se recoge al mob a atacar
                                    if mobs.getPosX() == x and mobs.getPosY() == y:  # Se recoge al grupo seleccionado
                                        # El jugador ataca y se comprueba si el
                                        # mob ataca también (si retorna True)
                                        if _fight(group, mobs, True, x, y,
                                                  mob_id,
                                                  "c") and self.nivel_dificultad != DIFICULTAD_FACIL:
                                            _fight(mobs, group, False, to[0],
                                                   to[
                                                       1],
                                                   self.board.getTurno(), "c")
                                        break
                                    mob_id += 1
                            elif self.board.getLogic(x,
                                                     y) == "player":  # Si hace click sobre el mismo quiere decir que no se movio
                                self.sonidoFx(SONIDO[39][0])
                            try:
                                _nextTurn()
                            except:
                                pass
                elif event == "click-derecho":  # Si es lanzar una flecha a distancia
                    (x, y) = whatTileD(event2.x,
                                       self.board.getBoardCorreccionX(),
                                       event2.y,
                                       self.board.getBoardCorreccionY())
                    # Si se ha clickeado dentro de los márgenes del board
                    if 0 <= x < self.board.getBoardSizeX() and 0 <= y < self.board.getBoardSizeY():
                        if [x,
                            y] in self.board.getAvaiableArrow():  # Si el tile clickeado está dentro de las posiciones válidas
                            group = self.board.players[self.board.getTurno()]
                            # Si hay un mob en dicho tile
                            if self.board.getLogic(x, y) == "mob":
                                mob_id = 0  # id del mob
                                for mobs in self.board.getEnemies():  # Se recoge al mob a atacar
                                    if mobs.getPosX() == x and mobs.getPosY() == y:  # Se recoge al grupo seleccionado
                                        # defino la posicion como la misma
                                        to = [group.getPosX(), group.getPosY()]
                                        _throwArrow(x, y, to[0], to[
                                            1], group.getType())
                                        near = False
                                        if abs(x - to[0]) <= 1 and abs(y - to[
                                            1]) <= 1 and self.nivel_dificultad != DIFICULTAD_FACIL:
                                            near = True
                                        if _fight(group, mobs, True, x, y,
                                                  mob_id, "f") and near:
                                            _fight(mobs, group, False, to[0],
                                                   to[
                                                       1],
                                                   self.board.getTurno(), "f")
                                        break
                                    mob_id += 1
                            elif self.board.getLogic(x,
                                                     y) == "player":  # Si hace click sobre el mismo quiere decir que no se movio
                                self.sonidoFx(SONIDO[39][0])
                            try:
                                _nextTurn()
                            except:
                                pass
            else:  # Si el evento es imprimir las nuevas posiciones
                group_turn = self.board.players[self.board.getTurno()]
                _lookAvaiablePos(group_turn.getPosX(), group_turn.getPosY(),
                                 group_turn.getMaxMovement(), TURN_HN,
                                 group_turn.getType(),
                                 group_turn.getTipoAtaque())
        # Si se encuentra en dicho modo de combate y juega la computadora
        elif self.inBattle and self.tipoCombate == MODE_FIGHT_GROUP and not self.board.returnControl():
            if event not in ["print", "pass", "click-izquierdo",
                             "click-derecho"]:
                # El ataque se diferencia por su dificultad
                if self.nivel_dificultad == DIFICULTAD_FACIL:
                    mov_candidatos = []
                    for mov in self.board.getAvaiablePos():
                        if self.board.getLogic(mov[0], mov[1]) == "player":
                            mov_candidatos.append(mov)
                    if len(mov_candidatos) != 0:  # Si hay candidatos cercanos
                        x, y = choice(mov_candidatos)
                        group = self.board.mobs[self.board.getAITurno()]
                        xi = group.getPosX()
                        yi = group.getPosY()  # Muevo al mob a la posición más cercana
                        if yi == y:  # Si está en el mismo y
                            if x < xi:
                                to = [x + 1, y]
                            else:
                                to = [x - 1, y]
                        elif xi == x:  # Si está en el mismo x
                            if y > yi:
                                to = [x, y - 1]
                            else:
                                to = [x, y + 1]
                        elif yi < y and xi < x:
                            # si está en la esquina inferior izquierda
                            to = [x - 1, y - 1]
                        elif yi > y and xi < x:
                            # si está en la esquina superior izquierda
                            to = [x - 1, y + 1]
                        elif yi < y and xi > x:
                            # si está en la esquina inferior derecha
                            to = [x + 1, y - 1]
                        elif yi > y and xi > x:
                            # si está en la esquina superior derecha
                            to = [x + 1, y + 1]
                        # se mueve al tile más cercano
                        _move(to[0], to[1], self.board.getAITurno(),
                              group.getType())
                        player_id = 0  # id del mob
                        for players in self.board.getPlayers():  # Se recoge el jugador a atacar
                            if players.getPosX() == x and players.getPosY() == y:  # Se recoge al grupo seleccionado
                                # El mob ataca y si sobrevive el jugador ataca
                                # al mob si es que la dificultad no es fácil
                                if _fight(group, players, False, x, y,
                                          player_id,
                                          "c") and self.nivel_dificultad != DIFICULTAD_FACIL:
                                    _fight(players, group, True, to[0], to[
                                        1], self.board.getAITurno(), "c")
                                break
                            player_id += 1
                    else:
                        px = self.board.getPlayers()[0].getPosX()
                        py = self.board.getPlayers()[0].getPosY()
                        group = self.board.mobs[self.board.getAITurno()]
                        xi = group.getPosX()
                        yi = group.getPosY()
                        if xi < px:
                            dx = 1
                        elif xi == px:
                            dx = 0
                        else:
                            dx = -1
                        if self.board.getLogic(xi + dx, yi) != "none":
                            dx = 0
                        if yi < py:
                            dy = 1
                        elif yi == py:
                            dy = 0
                        else:
                            dy = -1
                        if self.board.getLogic(xi + dx, yi + dy) != "none":
                            dy = 0
                        to = [xi + dx, yi + dy]
                        if [dx, dy] != [0, 0]:
                            _move(to[0], to[1],
                                  self.board.getAITurno(), group.getType())
                        else:
                            self.sonidoFx(SONIDO[39][0])

                # TODO:Dificultad medio
                elif self.nivel_dificultad == DIFICULTAD_MEDIO:
                    print "TODO:atk-med"

                # TODO:Dificultad dificil
                else:
                    print "TODO:atk-dif"

                try:
                    _nextAITurn()
                except:
                    pass
            elif event == "print":  # Si el evento es imprimir
                group_turn = self.board.mobs[self.board.getAITurno()]
                _lookAvaiablePos(group_turn.getPosX(), group_turn.getPosY(),
                                 group_turn.getMaxMovement(), TURN_AI,
                                 group_turn.getType(),
                                 group_turn.getTipoAtaque())
            else:
                pass
        else:
            pass

    def combateNormal(self, mano, e=None):
        """
        Función que maneja el combate normal con los mobs
        :param mano: Tipo de ataque
        :param e: Evento
        :return: void
        """

        def _animateWeapon(modo, tag):
            """
            Mueve un objeto en la forma de ataque
            :param modo: Modo de ataque
            :param tag: Tag de imagen
            :return: void
            """
            if MOVEMENT_ANIMATION[0]:  # Si estan activas las animaciones
                if modo == "fight":  # Se mueve el arma con respecto a la posición del mob
                    if self.enemy.getPosAbs() == "derecha":
                        self.root.after(50, lambda: moveWay(tag, self.world,
                                                            [[50 + 32 *
                                                              self.playerPos[
                                                                  0] +
                                                              self.canvasCorrecion[
                                                                  1],
                                                              self.canvasCorrecion[
                                                                  0] + 32 *
                                                              self.playerPos[
                                                                  1] + 16],
                                                             [28 + 32 *
                                                              self.playerPos[
                                                                  0] +
                                                              self.canvasCorrecion[
                                                                  1],
                                                              self.canvasCorrecion[
                                                                  0] + 32 *
                                                              self.playerPos[
                                                                  1] + 16]]))
                    elif self.enemy.getPosAbs() == "izquierda":
                        self.root.after(50, lambda: moveWay(tag, self.world,
                                                            [[6 + 32 *
                                                              self.playerPos[
                                                                  0] +
                                                              self.canvasCorrecion[
                                                                  1],
                                                              self.canvasCorrecion[
                                                                  0] + 32 *
                                                              self.playerPos[
                                                                  1] + 16],
                                                             [28 + 32 *
                                                              self.playerPos[
                                                                  0] +
                                                              self.canvasCorrecion[
                                                                  1],
                                                              self.canvasCorrecion[
                                                                  0] + 32 *
                                                              self.playerPos[
                                                                  1] + 16]]))
                    elif self.enemy.getPosAbs() == "arriba":
                        self.root.after(50, lambda: moveWay(tag, self.world,
                                                            [[28 + 32 *
                                                              self.playerPos[
                                                                  0] +
                                                              self.canvasCorrecion[
                                                                  1],
                                                              self.canvasCorrecion[
                                                                  0] + 32 *
                                                              self.playerPos[
                                                                  1] - 6],
                                                             [28 + 32 *
                                                              self.playerPos[
                                                                  0] +
                                                              self.canvasCorrecion[
                                                                  1],
                                                              self.canvasCorrecion[
                                                                  0] + 32 *
                                                              self.playerPos[
                                                                  1] + 16]]))
                    elif self.enemy.getPosAbs() == "abajo":
                        self.root.after(50, lambda: moveWay(tag, self.world,
                                                            [[28 + 32 *
                                                              self.playerPos[
                                                                  0] +
                                                              self.canvasCorrecion[
                                                                  1],
                                                              self.canvasCorrecion[
                                                                  0] + 32 *
                                                              self.playerPos[
                                                                  1] + 48],
                                                             [28 + 32 *
                                                              self.playerPos[
                                                                  0] +
                                                              self.canvasCorrecion[
                                                                  1],
                                                              self.canvasCorrecion[
                                                                  0] + 32 *
                                                              self.playerPos[
                                                                  1] + 16]]))
                elif modo == "alone":  # Se mueve el arma hacia la derecha
                    self.root.after(50, lambda: moveWay(tag, self.world,
                                                        [[45 + 32 *
                                                          self.playerPos[0] +
                                                          self.canvasCorrecion[
                                                              1],
                                                          self.canvasCorrecion[
                                                              0] + 32 *
                                                          self.playerPos[
                                                              1] + 16],
                                                         [28 + 32 *
                                                          self.playerPos[0] +
                                                          self.canvasCorrecion[
                                                              1],
                                                          self.canvasCorrecion[
                                                              0] + 32 *
                                                          self.playerPos[
                                                              1] + 16]]))

        def _atacarMob(y, x):
            """
            Función que busca a un mob en (x,y) y se ataca, además se dibuja la flecha
            :param y: Posición x
            :param x: Posición y
            :return: void
            """
            _throwArrow(x, y)  # lanzo una flecha
            for i_d in range(len(self.mobs)):  # Se recorren los mobs del mapa
                mob = self.mobs[i_d]  # objeto mob
                if mob.getPosicionX() == x and mob.getPosicionY() == y:  # Si es el mob buscado
                    if mob.getTipoCombate() == MODE_FIGHT_NORMAL:  # Si es un mob normal
                        ataque = mob.golpear(int(self.player.atacar(
                            mano) * (self.dificultad[2] + 1)))  # Golpeo al mob
                        if mob.isDead():  # Si el mob murio
                            self.mobs.pop(i_d)  # se elimina de los mobs
                            # mensaje al usuario
                            self.setInfo(lang(90, mob.getName()))
                            self.static.addMuerte()  # estadísticas
                            self.mapLogic[y][x] = "none"
                            # Inserto la sangre
                            if self.maplightning[y][x] == 0:
                                self.mapItemsTextures[y][
                                    x] = choice(EFFECT_BLOOD_DAY)
                            else:
                                self.mapItemsTextures[y][
                                    x] = choice(EFFECT_BLOOD_NIGHT)
                            self.incrementarExperiencia(mob.getExp())
                            self.textMsg(
                                lang(choice([619, 620, 621, 622, 623, 624,
                                             625])))  # mensaje
                            # dibujo el mundo
                            self.root.after(
                                TIME_DISSAPEAR_EFFECT, self.dibujarMundo)
                            # obtener el objeto, agregarlo a un contenedor e dibujarlo
                            # obj = self.enemy.getObjDrown() #Se obtiene el objeto del mob
                            # if obj!="%NULL%": #Si no es vacío
                            #    self.static.addObj()
                            #    self.playerText("+"+lang(143),"blanco",True)
                            #    self.player.addObject(Item(parseObject(obj))) #Se agrega nuevo objeto al jugador
                            #    #Si el objeto era stackable
                            #    if obj.split(ITEMSEPARATOR)[5]=="True":
                            #         self.setInfo(lang(95,str(obj.split(ITEMSEPARATOR)[6]),\
                            #                        str(obj.split(ITEMSEPARATOR)[0])).lower())
                            # else:
                            # self.setInfo(lang(96,str(obj.split(ITEMSEPARATOR)[0])))
                            self.updateInfoPlayer()
                        else:
                            if ataque[1] - ataque[
                                0] > 0:  # Si el mob recibe daño
                                self.setInfo(lang(280, mob.getName()))
                                # borro la textura de la barra de vida del mob
                                self.world.delete("lifebar:" + str(i_d))
                                # nueva barra de vida
                                self.lifeBar(
                                    mob.getLife(), mob.getMaxLife(), x, y, i_d)
                                self.textMsg(
                                    lang(choice([626, 627, 628, 629, 630])))
                            else:  # Si no recibe daño
                                self.textMsg(lang(choice([615, 617, 618])))
                                self.setInfo(lang(282, mob.getName()))
                        break  # termina el loop
                    else:  # Si no es un mob normal
                        self.textMsg(lang(choice([636, 637, 638, 639, 640])))
                        self.setInfo(lang(641))

        def _allowAttack():
            """
            Función que permite el desplazamiento
            :return: void
            """
            self.canmove = True

        def _lookFor(y, x, lookmatrix, direcc):
            """
            Función que retorna el lógico en (x,y) y define si se mantiene en la búsqueda
            :param y: Posición x
            :param x: Posición y
            :param lookmatrix: Matriz de direcciones
            :param direcc: Dirección de búsqueda
            :return: String
            """
            if 0 <= y < self.mapSize[1] and 0 <= x < self.mapSize[
                0]:  # Si se mantiene en los márgenes del mapa
                if self.mapLogic[y][x] == "mob":
                    lookmatrix[direcc] = 100
                    return "finded"
                elif self.mapLogic[y][x] == "none":
                    return "pass"
                else:
                    lookmatrix[direcc] = 0
                    return "block"
            else:
                lookmatrix[direcc] = -10
                return "off"

        def _throwArrow(x, y):
            """
            Función que lanza una flecha hasta (x,y)
            :param x: Posición x
            :param y: Posición y
            :return: void
            """
            if (self.player.getActiveBullet() is not None) and \
                    MOVEMENT_ANIMATION[
                        0]:  # Si poseo armamento y las animaciones están activas
                flecha_id = generateRandom12()  # Dibujo la imagen de la flecha
                flecha = self.world.create_image(
                    26 + 32 * self.playerPos[0] + self.canvasCorrecion[1],
                    # @UnusedVariable
                    self.canvasCorrecion[
                        0] + 32 * self.playerPos[1] + 26,
                    image=self.images.image(
                        self.player.getActiveBullet().getImage() + "_16"),
                    tags=flecha_id)
                self.root.after(TEXDT, makeCallable(
                    partial(arrastrarImagen, flecha_id, self.world,
                            26 + 32 * x + self.canvasCorrecion[1],
                            self.canvasCorrecion[0] + 32 * y + 26)))
                self.root.after(TIME_DISSAPEAR_EFFECT,
                                lambda: self.world.delete(flecha_id))

        if self.ingame and not self.inNpc:  # Si se encuentra en una partida
            if self.inBattle:  # Si se encuentra en batalla
                if self.tipoCombate == MODE_FIGHT_NORMAL:  # Si el tipo de combate es normal
                    if self.canmove:  # Si ha pasado el tiempo minimo para el ataque
                        self.canmove = False
                        self.root.after(ATTACK_MIN_TIME, _allowAttack)
                        if mano == "izquierda":  # Ataque con la mano izquierda
                            if self.player.getActiveBullet() is not None:  # Si posee municion
                                self.player.getActiveBullet().usar()  # si el arma tiene balas se usan
                                self.sfx(24)
                                _throwArrow(self.enemy.getPosicionX(),
                                            self.enemy.getPosicionY())
                            else:  # Si no posee munición se muestra un mensaje
                                self.setInfo(lang(265))
                                mano = "novalid"  # el ataque realizado con la mano izquierda es 0
                        elif mano == "derecha":  # Ataque con la mano derecha
                            if self.player.getRightWeapon() is not None:  # Se cargan los efectos
                                _animateWeapon("fight", "player:right_weapon")
                                self.sfx(14)  # sonidos
                            else:
                                self.sfx(17)
                        else:
                            print mano  # otro ataque
                        ataque = self.enemy.golpear(
                            int(self.player.atacar(mano) * (
                                self.dificultad[2] + 1)))  # Se crea el ataque
                        self.setInfo(
                            lang(88, str(ataque[0]), self.enemy.getName(),
                                 str(ataque[
                                         1])))  # Mensaje en consola del ataque
                        if not self.enemy.isDead():  # Si el enemigo no muere ataca
                            self.world.delete("lifebar:" + str(self.enemyId))
                            self.lifeBar(self.enemy.getLife(),
                                         self.enemy.getMaxLife(),
                                         self.enemy.getPosicionX(),
                                         self.enemy.getPosicionY(),
                                         self.enemyId)
                            if ataque[0] - ataque[1] > 0:
                                self.playerText(
                                    "-" + str(ataque[0] - ataque[1]), "rojo",
                                    False)
                            else:
                                self.playerText("-0", "blanco", False, True)
                            try:
                                ataque = self.player.increaseDamage(
                                    int(self.enemy.atacar() * (
                                        self.dificultad[0] + 1) * (
                                            self.dificultad[3] + 1)))
                            except Exception, exerr:
                                print langError(365, exerr)
                            if (ataque[0] - ataque[1]) > 0:
                                self.playerText("-" + str(
                                    ataque[0] - ataque[
                                        1]))  # En función del ataque se imprime el daño sobre el jugador
                            else:
                                self.playerText("-0", "blanco", True, True)
                            self.sfx(13)  # Sonido de golpe
                            self.setInfo(
                                lang(89, self.enemy.getName(), str(ataque[0]),
                                     str(ataque[1])))  # Mensaje en consola
                            if not self.player.isDead():  # Se muestra el estado del enemigo si es que el jugador no ha muerto
                                self.setInfo(
                                    self.enemy.getName() + "\n" + lang(86, str(
                                        self.enemy.getLife()),
                                                                       str(
                                                                           self.enemy.getMaxLife())),
                                    False)
                                self.textMsg(
                                    self.enemy.getName() + "\n" + lang(86, str(
                                        self.enemy.getLife()),
                                                                       str(
                                                                           self.enemy.getMaxLife())),
                                    "combat")
                            else:  # Si el jugador muere
                                if self.maplightning[
                                    self.enemy.getPosicionY()][
                                    self.enemy.getPosicionX()] == 0:
                                    sangre = choice(EFFECT_BLOOD_DAY)
                                else:
                                    sangre = choice(EFFECT_BLOOD_NIGHT)
                                self.updateInfoPlayer()
                                self.world.delete("player")
                                self.world.create_image(
                                    18 + 32 * self.playerPos[0] +
                                    self.canvasCorrecion[1],
                                    self.canvasCorrecion[
                                        0] + 32 * self.playerPos[1] + 18,
                                    image=self.images.image(sangre))
                                self.setInfo(lang(82))
                                self.setInfo(lang(81))
                                self.sfx(29)
                                e = pop([[lang(82), lang(173)],
                                         self.images.image("iconmuerte"),
                                         "aviso", 85, 270,
                                         lang(83)])
                                e.w.mainloop(1)
                                del e
                                self.abortGame()
                        else:  # Si el enemigo muere
                            if self.maplightning[self.enemy.getPosicionY()][
                                self.enemy.getPosicionX()] == 0:  # si es de dia
                                self.mapItemsTextures[
                                    self.enemy.getPosicionY()][
                                    self.enemy.getPosicionX()] = choice(
                                    EFFECT_BLOOD_DAY)
                            else:
                                self.mapItemsTextures[
                                    self.enemy.getPosicionY()][
                                    self.enemy.getPosicionX()] = choice(
                                    EFFECT_BLOOD_NIGHT)
                            self.static.addMuerte()  # aumenta la estadística
                            self.setInfo(lang(90, self.enemy.getName()))
                            self.mapLogic[self.enemy.getPosicionY()][
                                self.enemy.getPosicionX()] = "none"  # se modifica el mapa lógico
                            # aumenta la experiencia del jugador
                            self.incrementarExperiencia(self.enemy.getExp())
                            obj = self.enemy.getObjDrown()  # se obtiene el objeto del mob
                            if obj != "%NULL%":  # Si el objeto recogido no es vacío
                                self.static.addObj()
                                self.playerText(
                                    "+" + lang(143), "blanco", True)
                                # se agrega nuevo objeto al jugador
                                self.player.addObject(Item(parseObject(obj)))
                                # Si el objeto era stackable
                                if obj.split(ITEMSEPARATOR)[5] == "True":
                                    self.setInfo(lang(95, str(
                                        obj.split(ITEMSEPARATOR)[6]),
                                                      str(obj.split(
                                                          ITEMSEPARATOR)[
                                                              0])).lower())
                                else:
                                    self.setInfo(
                                        lang(96,
                                             str(obj.split(ITEMSEPARATOR)[0])))
                            self.enemy = None
                            self.mobs.pop(self.enemyId)
                            self.enemyId = 0
                            self.inBattle = False  # termino la batalla
                            self.update()
                            if len(
                                    self.mobs) != 0:  # Si aún quedan mobs activo el movimiento
                                try:
                                    self.root.after_cancel(
                                        self.lastmovementId)  # se intnta eliminar la ultima ejecucion de la funcion
                                except Exception, exerr:
                                    print langError(363, exerr)
                                self.root.after(
                                    self.dificultad[5], self.moveMobs)
                                self.movement = True
                            else:
                                self.movement = False  # si no hay mobs se desactiva el movimiento
                        # Si aún continua la batalla se modifican las barras de
                        # información y la armadura
                        self.checkItems()
                        self.dibujarArmor()
                        self.updateInfoPlayer()
            else:  # Si no se encuentra en batalla
                if self.canmove:  # Si ha pasado el tiempo minimo para el ataque
                    self.canmove = False
                    self.root.after(ATTACK_MIN_TIME, _allowAttack)
                    if mano == "izquierda":  # Si se lanzó una flecha fuera de combate
                        if self.player.getLeftWeapon() is not None:
                            if self.player.getActiveBullet() is not None:
                                # Si el tipo de arma lanza flechas (o usa
                                # bullets) se lanza una al mob mas cercano
                                if self.player.getLeftWeapon().getType() == "weapon/left":
                                    self.sfx(24)  # Sonido
                                    self.static.addMovimientos()  # Estadística
                                    self.player.getActiveBullet().usar()  # Se gasta una flecha
                                    # Array que define las direcciones a buscar
                                    # (OSEN)
                                    look = [1, 1, 1, 1]
                                    for c in range(1, int(
                                                    self.player.getTarget() / 10) + 1):  # Se recorren los tiles de acuerdo al target del jugador
                                        if look[0] == 1:  # Busca al Oeste
                                            if _lookFor(self.playerPos[1],
                                                        self.playerPos[0] - c,
                                                        look, 0) == "finded":
                                                _atacarMob(self.playerPos[
                                                               1],
                                                           self.playerPos[
                                                               0] - c)
                                                break
                                        if look[1] == 1:  # Busca al Sur
                                            if _lookFor(self.playerPos[1] + c,
                                                        self.playerPos[0],
                                                        look, 1) == "finded":
                                                _atacarMob(self.playerPos[
                                                               1] + c,
                                                           self.playerPos[0])
                                                break
                                        if look[2] == 1:  # Busca al Este
                                            if _lookFor(self.playerPos[1],
                                                        self.playerPos[0] + c,
                                                        look, 2) == "finded":
                                                _atacarMob(self.playerPos[
                                                               1],
                                                           self.playerPos[
                                                               0] + c)
                                                break
                                        if look[3] == 1:  # Busca al Norte
                                            if _lookFor(self.playerPos[1] - c,
                                                        self.playerPos[0],
                                                        look, 3) == "finded":
                                                _atacarMob(self.playerPos[
                                                               1] - c,
                                                           self.playerPos[0])
                                                break
                                    if sum(look) < 0 or int(
                                                    self.player.getTarget() / 10) == 0:  # Si la flecha se fué del mapa
                                        self.setInfo(
                                            lang(choice([279, 607, 608, 609])))
                                        self.textMsg(
                                            lang(choice(
                                                [610, 611, 612, 613, 614])))
                                    elif sum(
                                            look) == 0:  # Si la flecha chocó contra un obstaculo
                                        self.setInfo(
                                            lang(choice([279, 607, 608, 609])))
                                        self.textMsg(
                                            lang(choice(
                                                [631, 632, 633, 634, 635])))
                            else:
                                self.textMsg(lang(choice([642, 643, 644])))
                                # si el jugador no tiene balas se muestra un
                                # mensaje
                                self.setInfo(lang(265))
                            self.checkItems()
                            self.dibujarItems()
                        else:
                            self.sfx(17)  # sonido de combo
                    else:  # Si se golpeó con el arma derecha y no hay una pelea
                        if self.player.getRightWeapon() is not None:
                            _animateWeapon("alone", "player:right_weapon")
                            self.sfx(15)  # sonido de cuchillo
                        else:
                            self.sfx(17)  # sonido de combo

    def delInfo(self):
        """
        Función que borra la información de la consola
        :return: void
        """
        delMatrix(self.console)  # se borra la matriz de mensajes
        self.info.config(text="")  # se borra el mensaje actual

    def devConsole(self, e=None):
        """
        Función que ejecuta comandos
        :param e: Evento
        :return: void
        """
        if CONFIGURATION_DATA[11]:  # Si la terminal está activa
            # Si la función es llamada desde el background no se pide input
            if "str" not in str(type(e)):
                consola = pop([[lang(326), lang(240), lang(400)],
                               self.images.image("console_icon"), "command",
                               42, 280,
                               DATA_CONFIG])
                consola.w.mainloop(1)
            if consola.sent or "str" in str(type(e)):
                if "str" in str(type(e)):
                    get = e
                else:
                    get = consola.values[0].split(" ")
                comando = get[0].upper()
                if comando == "GIVE" and self.player.isEditor():
                    try:
                        action = get[1].upper()
                    except Exception, exerr:
                        print langError(375, exerr)
                        self.error(lang(377))
                        return
                    try:
                        data = get[2]
                    except Exception, exerr:
                        print langError(376, exerr)
                        self.error(lang(377))
                        return
                    if self.ingame:  # Si se encuentra jugando
                        if action == "ID":  # Dar objeto por id
                            if data.isdigit():  # Si el id es numérico
                                try:  # Se obtiene el objeto
                                    data = int(data)
                                    item = ITEMS[data]
                                    try:
                                        if len(get) > 3:
                                            # se obtiene la cantidad
                                            cant = get[3]
                                            if str(cant).isdigit():
                                                cant = int(cant)
                                            else:
                                                self.error(lang(107))
                                                return  # si el id no es numerico
                                        else:
                                            cant = 1
                                    except Exception, exerr:
                                        print langError(360, exerr)
                                        cant = 1
                                    try:
                                        it = Item(item)  # se genera el objeto
                                    except Exception, exerr:
                                        print langError(374, exerr)
                                        return
                                    try:
                                        self.images.image(
                                            it.getImage() + "_16")
                                    except Exception, exerr:
                                        print langError(378,
                                                        it.getImage() + "_16",
                                                        exerr)
                                        return
                                    for i in range(cant):
                                        self.player.addObject(Item(item))
                                    self.dibujarItems()
                                    self.setInfo(
                                        lang(111, str(data), str(cant)))
                                    self.static.addTrucos()
                                    del it
                                except Exception, exerr:
                                    print langError(359, exerr)
                                    self.error(lang(110))
                            else:
                                # si el id no es numerico
                                self.error(lang(107))
                        elif action == "ITEM":  # Dar objeto por string
                            item = data.split(",")
                            try:  # Se crea el objeto
                                obj = Item(
                                    [str(item[0]), str(item[1]), str(item[2]),
                                     str(item[3]), int(item[4]),
                                     isTrue(str(item[5])), int(item[6]),
                                     [parseType(lookType(item[7])),
                                      parseType(lookType(item[8]))]])
                                self.player.addObject(Item(obj))
                                self.dibujarItems()
                                self.setInfo(lang(114))
                                self.static.addTrucos()
                            except Exception, exerr:
                                print langError(358, exerr)
                                self.error(lang(113))
                        elif action == "POWER":  # Dar poder por string
                            if not data.isdigit():  # Si string no es un número
                                encontrado = False  # variable que indica si se encontró el poder o no
                                for poder in POWERLIST.keys():  # Se recorre la lista de poderes
                                    # Si se encuentra el poder
                                    if POWERLIST[poder][1] == data:
                                        if self.player.getPowerAmount() == 7:  # Si el player tiene 7 poderes se elimina el último
                                            self.player.dropPower(6)
                                        self.player.addPower(
                                            Power(POWERLIST[poder]))
                                        encontrado = True
                                if encontrado:  # Si se encontró el poder
                                    self.dibujarPowers()
                                    self.static.addTrucos()
                                    self.setInfo(lang(370))
                                else:
                                    print lang(371)
                                    self.error(lang(372))
                            else:
                                self.error(lang(369))
                        elif action == "QUEST":  # Dar una quest
                            if data != "":
                                self.static.addTrucos()
                                self.setInfo(lang(586))
                                self.player.addQuest(data)
                                self.dibujarMundo()
                            else:
                                self.error(lang(695))
                        elif action == "FOLLOWER" or action == "FOLLOWERS":  # Dar un grupo de followers
                            data = data.upper()
                            if data == "LIV" or data == "MED" or data == "STR" or data == "ALL":
                                try:
                                    cant = int(get[3])
                                except:
                                    self.error(lang(694))
                                    return
                                if cant > 0:
                                    if data == "LIV":
                                        self.player.addLightFriend(cant)
                                        self.setInfo(lang(698, str(cant)))
                                    elif data == "MED":
                                        self.player.addMediumFriend(cant)
                                        self.setInfo(lang(699, str(cant)))
                                    elif data == "STR":
                                        self.player.addStrongFriend(cant)
                                        self.setInfo(lang(700, str(cant)))
                                    elif data == "ALL":
                                        self.player.addLightFriend(cant)
                                        self.player.addMediumFriend(cant)
                                        self.player.addStrongFriend(cant)
                                        self.setInfo(lang(723, str(cant)))
                                    self.static.addFollower(cant)
                                    self.static.addTrucos()
                                else:
                                    self.error(lang(696))
                                    return
                            else:
                                self.error(lang(697))
                                return
                        else:
                            self.error(lang(108))  # si no se conoce la accion
                    else:
                        self.error(lang(109))  # si no se encuentra jugando
                elif comando == "MOVE" and self.player.isEditor():
                    try:
                        action = get[1].upper()
                    except Exception, exerr:
                        print langError(375, exerr)
                        self.error(lang(377))
                        return
                    try:
                        data = get[2]
                    except Exception, exerr:
                        print langError(376, exerr)
                        self.error(lang(377))
                        return
                    if self.ingame:  # Si se encuentra jugando
                        if action == "XY":
                            pos = data.split(",")
                            if pos[0].isdigit() and pos[
                                1].isdigit():  # Si el id es numérico
                                x = int(pos[0])
                                y = int(pos[1])
                                if 0 <= y < self.mapSize[1] and 0 <= x < \
                                        self.mapSize[
                                            0]:  # Si las coordenadas están dentro del largo del mapa
                                    self.move(x, y)
                                    self.setInfo(lang(116, str(x), str(y)))
                                    self.inBattle = False
                                    self.inNpc = False
                                    self.enemy = None
                                    self.currentNpc = None
                                    self.static.addTrucos()
                                else:
                                    # si las coordenadas no son correctas
                                    self.error(lang(117))
                            else:
                                # Si los datos no son numéricos
                                self.error(lang(107))
                        elif action == "MAP":
                            prevmap = self.player.getMap()  # guardo el mapa anterior
                            mapa = data.split(",")[0].replace(
                                ".lvl", "").replace(".LVL", "")
                            mapa += ".lvl"
                            self.player.setMap(mapa)
                            self.setWorld()
                            self.inBattle = False
                            self.inNpc = False
                            self.enemy = None
                            self.currentNpc = None
                            # Si ocurrió un error al cargar el mapa se deshacen
                            # los cambios
                            if self.player.getMap() == "%ERROR_LOADINGMAP%":
                                self.player.setMap(prevmap)
                                self.setWorld()
                                self.setInfo(lang(320))
                                self.setInfo(lang(319))
                                self.setInfo(lang(318))
                            else:
                                self.setInfo(lang(118, str(data)))
                                self.static.addTrucos()
                        else:
                            self.error(lang(108))  # si no se conoce la accion
                    else:
                        self.error(lang(109))  # si no se encuentra jugando
                elif comando == "SET" and self.player.isEditor():
                    try:
                        action = get[1].upper()
                    except Exception, exerr:
                        print langError(375, exerr)
                        self.error(lang(377))
                        return
                    try:
                        data = get[2]
                    except Exception, exerr:
                        print langError(376, exerr)
                        self.error(lang(377))
                        return
                    if self.ingame:  # Si se encuentra jugando
                        if data.isdigit():  # Si el data es numérico
                            data = int(data)
                            if action == "DAMAGE" or action == "PLAYER.DAMAGE":
                                if data >= 0:
                                    data = min(
                                        data, self.player.getMaxLife() - 1)
                                    self.player.setDamage(data)
                                    self.setInfo(lang(119, str(data)))
                                    self.updateInfoPlayer()
                                    self.playerText("-" + str(data))
                                    self.static.addTrucos()
                            elif action == "MANA" or action == "PLAYER.MANA":
                                data = min(data, self.player.getMaxMana())
                                self.player.setMana(data)
                                self.setInfo(lang(120, str(data)))
                                self.updateInfoPlayer()
                                self.static.addTrucos()
                            elif action == "LEVEL" or action == "PLAYER.LEVEL":
                                if 0 < int(data) < 13:  # Si el nivel es válido
                                    self.player.setLevel(int(data))
                                    self.player.setAttack()
                                    self.player.setDefensa()
                                    self.player.setImage()
                                    self.player.setTarget()
                                    self.player.upgradeExp()
                                    self.player.upgradeLife()
                                    self.player.upgradeMana()
                                    self.updateInfoPlayer()
                                    self.setInfo(lang(112, str(data)))
                                    self.static.addTrucos()
                                else:
                                    # si el nivel no está entre 1 y 12
                                    self.error(lang(185))
                                self.dibujarPowers()
                                self.dibujarMundo()
                            elif action == "EDAD" or action == "PLAYER.AGE":
                                self.player.setEdad(int(data))
                                self.setInfo(lang(162, str(data)))
                                self.static.addTrucos()
                            elif action == "EXPERIENCE" or action == "PLAYER.EXP":
                                l = self.player.getLevel()  # nivel antes de subir
                                self.player.setExperience(int(data))
                                while True:  # Se revisa si ha subido de nivel
                                    if self.player.getExperience() >= self.player.getMaxExperience():
                                        if self.player.getLevel() < 12:
                                            self.player.setLevel(
                                                self.player.getLevel() + 1)
                                            self.player.setMaxExpLevel()
                                            self.player.setMaxLife()
                                            self.player.setMaxMana()
                                            self.player.setAttack()
                                            self.player.setDefensa()
                                            self.player.setTarget()
                                            if self.nivel_dificultad == DIFICULTAD_FACIL or self.nivel_dificultad == DIFICULTAD_MEDIO:
                                                self.player.upgradeLife()
                                                self.player.upgradeMana()
                                        else:
                                            break
                                    elif self.player.getExperience() < self.player.getPrevExp():
                                        if self.player.getLevel() <= 12:
                                            self.player.setLevel(
                                                self.player.getLevel() - 1)
                                            self.player.setMaxExpLevel()
                                            self.player.setMaxLife()
                                            self.player.setMaxMana()
                                            self.player.setAttack()
                                            self.player.setDefensa()
                                            self.player.setTarget()
                                            if self.nivel_dificultad == DIFICULTAD_FACIL or self.nivel_dificultad == DIFICULTAD_MEDIO:
                                                self.player.upgradeLife()
                                                self.player.upgradeMana()
                                            if self.player.getLevel() == 1:
                                                break
                                    else:
                                        break
                                    self.dibujarPowers()
                                    self.dibujarMundo()
                                if l != self.player.getLevel():
                                    if l - self.player.getLevel() < 0:
                                        self.setInfo(
                                            lang(193, str(
                                                self.player.getLevel() - l)))
                                    else:
                                        self.setInfo(
                                            lang(194, str(
                                                l - self.player.getLevel())))
                                self.setInfo(lang(177, str(data)))
                                self.updateInfoPlayer()
                                self.static.addTrucos()
                            elif action == "ATK" or action == "PLAYER.ATK":
                                if int(data) >= 0:
                                    self.player.setAttack(int(data))
                                    self.setInfo(
                                        lang(187, str(data)))
                                    self.static.addTrucos()
                                else:
                                    # si el dato es negativo
                                    self.error(lang(186))
                            elif action == "DEF" or action == "PLAYER.DEF":
                                if int(data) >= 0:
                                    self.player.setDefensa(int(data))
                                    self.setInfo(
                                        lang(188, str(data)))
                                    self.static.addTrucos()
                                else:
                                    # si el dato es negativo
                                    self.error(lang(186))
                            elif action == "TARGET" or action == "PLAYER.TARGET":
                                if int(data) >= 0:
                                    self.player.setTarget(int(data))
                                    self.setInfo(
                                        lang(189, str(data)))
                                    self.static.addTrucos()
                                else:
                                    # si el dato es negativo
                                    self.error(lang(186))
                            elif action == "TIMEMOB" or action == "MOB.TIME.MOVEMENT":
                                if 100 <= int(data):
                                    self.dificultad[5] = int(data)
                                    self.setInfo(lang(284, str(data)))
                                else:
                                    # si el tiempo no es mayor a 100
                                    self.error(lang(285), 85)
                            else:
                                # si no se conoce la accion
                                self.error(lang(108))
                        else:  # Si el data no es numérico
                            if action == "NAME" or action == "PLAYER.NAME":
                                self.player.setName(data)
                                self.setInfo(lang(159, str(data)))
                                self.static.addTrucos()
                            elif action == "TEXTURE" or action == "PLAYER.TEXTURE":
                                data = data.replace("_0", "").replace("_1", "")
                                if data in AVAIABLE_ACTOR_TEXTURES:
                                    self.player.setLinkImage(data)
                                    self.setInfo(lang(160, str(data)))
                                    if self.maplightning[self.playerPos[1]][
                                        self.playerPos[0]] == 0:
                                        self.player.getLinkImage() + "_0"
                                    else:
                                        self.player.getLinkImage() + "_1"
                                    self.dibujarMundo()
                                    self.static.addTrucos()
                                else:
                                    self.error(lang(166))  # textura no válida
                            elif action == "PAIS" or action == "PLAYER.PAIS":
                                self.player.setPais(data)
                                self.setInfo(lang(161, str(data)))
                                self.static.addTrucos()
                            elif action == "INFO" or action == "PLAYER.INFO":
                                self.player.setInfo(
                                    str(data).replace("_", " "))
                                self.setInfo(
                                    lang(190, str(data).replace("_", " ")))
                                self.static.addTrucos()
                            elif action == "DIFICULTAD" or action == "PLAYER.DIF":
                                data = data.lower()
                                if data in [DIFICULTAD_FACIL, DIFICULTAD_MEDIO,
                                            DIFICULTAD_DIFICIL]:  # Si la dificultad es correcta
                                    self.nivel_dificultad = data
                                    self.setDificultad()
                                    self.player.setPais(data)
                                    self.setInfo(lang(164, str(data).upper()))
                                    self.static.addTrucos()
                                    self.update()
                                else:
                                    # la dificultad es desconocida
                                    self.error(lang(165))
                            else:
                                self.error(lang(107))
                    else:
                        self.error(lang(109))  # si no se encuentra jugando
                elif comando == "DROP" and self.player.isEditor():
                    try:
                        action = get[1].upper()
                    except Exception, exerr:
                        print langError(375, exerr)
                        self.error(lang(377))
                        return
                    if self.ingame:  # Si se encuentra jugando
                        if action == "ALL":
                            for i in range(
                                    self.player.getItemAmount()):
                                self.static.addDroppedItem()  # aumenta la estadística
                            self.player.delActiveBullet()
                            self.player.delFirstPower()
                            self.player.delQuest()
                            self.player.delSecondPower()
                            self.player.dropArmor()
                            self.player.dropFollowers()
                            self.player.dropItems()
                            self.player.dropLeftWeapon()
                            self.player.dropMagics()
                            self.player.dropPowers()
                            self.player.dropRightWeapon()
                            self.setInfo(lang(121))
                            self.static.addTrucos()
                            self.itemnumberlist = 0
                            self.dibujarArmor()
                            self.dibujarItems()
                            self.dibujarMundo()
                            self.dibujarPowers()
                        elif action == "ARMOR":
                            self.dibujarArmor()
                            self.player.dropArmor()
                            self.setInfo(lang(122))
                            self.static.addTrucos()
                        elif action == "ITEMS":
                            for i in range(
                                    self.player.getItemAmount()):
                                self.static.addDroppedItem()  # aumenta la estadística
                            self.player.dropItems()
                            self.setInfo(lang(123))
                            self.static.addTrucos()
                            self.itemnumberlist = 0
                            self.dibujarItems()
                        elif action == "POWERS":
                            for i in range(
                                    self.player.getPowerAmount()):
                                self.static.addDroppedItem()  # aumenta la estadística
                            self.player.dropPowers()
                            self.dibujarPowers()
                            self.setInfo(lang(373))
                            self.static.addTrucos()
                        elif action == "WEAPONS":
                            self.player.delActiveBullet()
                            self.player.delFirstPower()
                            self.player.delSecondPower()
                            self.player.dropLeftWeapon()
                            self.player.dropRightWeapon()
                            self.setInfo(lang(124))
                            self.static.addTrucos()
                            self.dibujarArmor()
                            self.dibujarMundo()
                        elif action == "QUEST":
                            self.player.delQuest()
                            self.setInfo(lang(585))
                            self.static.addTrucos()
                            self.dibujarMundo()
                        elif action == "FOLLOWERS":
                            self.player.dropFollowers()
                            self.setInfo(lang(693))
                            self.static.addTrucos()
                        else:
                            self.error(lang(108))  # si no se conoce la accion
                    else:
                        self.error(lang(109))  # si no se encuentra jugando
                elif comando == "CLEAR":
                    self.delInfo()
                elif comando == "COMMANDS":
                    e = pop(
                        [lang(192), self.images.image("text_icon"), "license",
                         400, 720,
                         DATA_DOCUMENTS + "/documentation/commands.txt", True])
                    e.w.mainloop(1)
                    del e
                elif comando == "EXIT" or comando == "QUIT":
                    self.salir("command")
                elif comando == "LOAD":
                    try:
                        action = get[1]
                        if ".save" in action:
                            self.loadGame("argv", action)
                        else:  # Si no posee el .save
                            if "." not in action:
                                self.loadGame("argv", action + ".save")
                            else:
                                # el nombre de la partida no es válido
                                self.error(lang(771), 70)
                    except:
                        self.loadGame()
                elif comando == "MUTE":
                    self.stopSound()
                elif comando == "SAVE":
                    if self.ingame:
                        self.saveGame("command")
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "LANG" and self.player.isEditor():
                    if self.ingame:
                        try:
                            action = get[1].upper()
                        except Exception, exerr:
                            print langError(375, exerr)
                            self.error(lang(377))
                            return
                        if action.isdigit():
                            self.setInfo(lang(int(action)), False)
                        else:
                            self.error(lang(107))  # si el id no es numerico
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "RELOAD" and self.player.isEditor():
                    if self.ingame:
                        self.currentNpc = None
                        self.enemy = None  # elimina al enemigo
                        # termina la batalla actual (si es que existe)
                        self.inBattle = False
                        self.inNpc = False  # terminan las interacciones
                        self.tipoCombate = "NO_FIGHT"
                        self.setWorld()  # recargo el mundo
                        self.dibujarMundo()  # dibujo el mundo
                        self.setInfo(lang(281))  # mensaje al usuario
                        self.static.addTrucos()  # estadísticas
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "INFO" and self.player.isEditor():
                    try:
                        action = get[1].upper()
                    except Exception, exerr:
                        print langError(375, exerr)
                        self.error(lang(377))
                        return
                    if self.ingame:  # Si se encuentra jugando
                        if action == "ACTUALMAP" or action == "PLAYER.MAP":
                            self.setInfo(lang(134, str(self.player.getMap())))
                        elif action == "CANVASCORRECT":
                            self.setInfo(lang(138, str(self.canvasCorrecion[
                                                           0]),
                                              str(self.canvasCorrecion[1])))
                        elif action == "DIFICULTAD" or action == "PLAYER.DIF":
                            self.setInfo(
                                lang(163, str(self.nivel_dificultad.upper())))
                        elif action == "ITEM.LENGTH":
                            self.setInfo(
                                lang(127, str(self.player.getItemAmount())))
                        elif action == "MAPSIZE":
                            self.setInfo(
                                lang(135, str(CANVAS_MAX_SIZE[0]),
                                     str(CANVAS_MAX_SIZE[1])))
                        elif action == "PLAYERACTIVEBULLET" or action == "PLAYER.ACTIVEBULLET":
                            self.setInfo(
                                lang(251, str(
                                    self.player.getActiveBullet().getName())))
                        elif action == "PLAYERAGE" or action == "PLAYER.AGE":
                            self.setInfo(lang(131, str(self.player.getEdad())))
                        elif action == "PLAYERATK" or action == "PLAYER.ATK":
                            self.setInfo(
                                lang(167, str(self.player.getAttack())))
                        elif action == "PLAYERBOARDATK" or action == "PLAYER.BOARD.ATK":
                            if self.inBattle and self.tipoCombate == MODE_FIGHT_GROUP:
                                self.setInfo(
                                    lang(737, str(int(
                                        self.player.getAttack() * 0.4 * (
                                            2 - self.dificultad[7])))))
                            else:
                                self.setInfo(lang(739))
                        elif action == "PLAYERBOARDDEF" or action == "PLAYER.BOARD.DEF":
                            if self.inBattle and self.tipoCombate == MODE_FIGHT_GROUP:
                                self.setInfo(
                                    lang(738, str(int(
                                        self.player.getDefensa() * 0.4 * (
                                            2 - self.dificultad[7])))))
                            else:
                                self.setInfo(lang(740))
                        elif action == "PLAYER.CANVAS.POS":
                            self.setInfo(
                                lang(137, str(self.playerPos[0] * 32),
                                     str(self.playerPos[1] * 32)))
                        elif action == "PLAYERCITY" or action == "PLAYER.CITY" or action == "PLAYERPAIS" or action == "PLAYER.PAIS":
                            self.setInfo(lang(130, str(self.player.getPais())))
                        elif action == "PLAYERDEF" or action == "PLAYER.DEF":
                            self.setInfo(
                                lang(168, str(self.player.getDefensa())))
                        elif action == "PLAYEREXP" or action == "PLAYER.EXP":
                            self.setInfo(
                                lang(132, str(self.player.getExperience())))
                        elif action == "PLAYER.FOLLOWERS" or action == "PLAYER.FOLLOWERS":
                            self.setInfo(
                                lang(692, str(self.player.getLightFriends()),
                                     str(self.player.getMediumFriends()),
                                     str(self.player.getStrongFriends())))
                        elif action == "PLAYERFP" or action == "PLAYER.FP":
                            self.setInfo(
                                lang(252, str(self.player.getFirstPower())))
                        elif action == "PLAYERINFO" or action == "PLAYER.INFO":
                            self.setInfo(lang(191, str(self.player.getInfo())))
                        elif action == "PLAYERLEVEL" or action == "PLAYER.LEVEL":
                            self.setInfo(
                                lang(184, str(self.player.getLevel())))
                        elif action == "PLAYERMANA" or action == "PLAYER.MANA":
                            self.setInfo(lang(179, str(self.player.getMana())))
                        elif action == "PLAYERMARROWD" or action == "PLAYER.MAX.ARROW.DISTANCE":
                            self.setInfo(
                                lang(606,
                                     str(int(self.player.getTarget() / 10))))
                        elif action == "PLAYERNAME" or action == "PLAYER.NAME":
                            self.setInfo(lang(129, str(self.player.getName())))
                        elif action == "PLAYERPOS" or action == "PLAYER.POS":
                            self.setInfo(
                                lang(136, str(self.playerPos[0]),
                                     str(self.playerPos[1])))
                        elif action == "PLAYERSP" or action == "PLAYER.SP":
                            self.setInfo(
                                lang(253, str(self.player.getSecondPower())))
                        elif action == "PLAYERTARGET" or action == "PLAYER.TARGET":
                            self.setInfo(
                                lang(182, str(self.player.getTarget())))
                        elif action == "PLAYERTEXTURE" or action == "PLAYER.TEXTURE":
                            self.setInfo(
                                lang(180, str(self.player.getLinkImage())))
                        elif action == "PLAYERTIPO" or action == "PLAYER.TYPE":
                            self.setInfo(
                                lang(181, str(self.player.getType())).upper())
                        elif action == "PLAYERVEL" or action == "PLAYER.VEL":
                            self.setInfo(
                                lang(178, str(self.player.getVelocidad())))
                        elif action == "PLAYNAME" or action == "PLAY.NAME":
                            self.setInfo(lang(128, str(self.namePartida)))
                        elif action == "TILELIGHT" or action == "TILE.LIGHT":
                            self.setInfo(
                                lang(141, str(
                                    self.maplightning[self.playerPos[1]][
                                        self.playerPos[0]])))
                        elif action == "TILESOUND" or action == "TILE.SOUND":
                            self.setInfo(
                                lang(140, str(self.mapSound[self.playerPos[1]][
                                                  self.playerPos[0]])))
                        elif action == "TIMEMOB" or action == "MOB.TIME.MOVEMENT":
                            self.setInfo(lang(283, str(self.dificultad[5])))
                        else:  # Caso default
                            if comando == "PRINT" and action != "":
                                self.setInfo(get[1].replace("_", " "))
                            else:
                                self.error(lang(108))
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "UPDATE":
                    if self.ingame:
                        self.update()
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "VERSION":
                    if self.ingame:
                        self.setInfo(lang(379, PROGRAM_VERSION), False)
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "ABORT":
                    if self.ingame:
                        self.abortGame()
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "TRANSLATE":
                    if self.ingame:
                        try:
                            action = get[1].upper()
                        except Exception, exerr:
                            print langError(375, exerr)
                            self.error(lang(377))
                            return
                        self.setInfo(translate(action))
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "SHOW" and self.player.isEditor():
                    if self.ingame:
                        try:
                            action = get[1].upper()
                        except Exception, exerr:
                            print langError(375, exerr)
                            self.error(lang(377))
                            return
                        if action == "ITEMS":
                            try:
                                first = 0
                                last = 0
                                itemname = ""
                                for item in ITEMS.keys():
                                    if first == 0 and last == 0:
                                        first = item
                                        itemname = ITEMS[item][0]
                                    if itemname == ITEMS[item][0]:
                                        last = item
                                    else:
                                        if first == last:
                                            self.setInfo(
                                                "  ID:" + str(
                                                    first) + " " + itemname,
                                                False)
                                        else:
                                            self.setInfo(
                                                "  ID:" + str(
                                                    first) + "-" + str(
                                                    last) + " " + itemname,
                                                False)
                                        first = item
                                        last = item
                                        itemname = ITEMS[item][0]
                                self.setInfo(lang(767))
                            except:
                                # ocurrió un error al cargar los mapas
                                self.error(lang(766), 70)
                        elif action == "POWERS":
                            try:
                                for power in POWERLIST.keys()[::-1]:
                                    self.setInfo(
                                        "  SHORT:" + POWERLIST[power][
                                            1] + " " + POWERLIST[power][0],
                                        False)
                                self.setInfo(lang(769))
                            except:
                                # ocurrió un error al cargar la lista de
                                # poderes
                                self.error(lang(768), 70)
                        elif action == "MAPS":
                            try:
                                archivos = os.listdir(DATA_LEVELS)
                                archivos.reverse()
                                for files in archivos:  # se recorren los archivos
                                    if ".lvl" in files:
                                        self.setInfo("  " + files, False)
                                self.setInfo(lang(764))
                            except:
                                # ocurrió un error al cargar los mapas
                                self.error(lang(765), 70)
                        else:
                            self.error(lang(108))
                    else:
                        self.error(lang(109), 68)  # si no se encuentra jugando
                elif comando == "DELETESTATICS" and self.player.isEditor():
                    if self.ingame:
                        self.static.restart()
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "CONNECT":
                    if self.ingame:
                        if not self.multiplayer_isconected:
                            if not self.inBattle:
                                if not self.inNpc:
                                    self.multiplayer_connect()
                                else:
                                    # si no se encuentra interactuando con un
                                    # npc
                                    self.error(lang(819), 82)
                            else:
                                # si no se encuentra combatiendo
                                self.error(lang(818), 82)
                        else:
                            # si no se encuentra jugando
                            self.error(lang(802), 70)
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "DISCONNECT":
                    if self.ingame:
                        if self.multiplayer_isconected:
                            self.multiplayer_desconnect()
                        else:
                            # si no se encuentra conectado
                            self.error(lang(801), 70)
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                elif comando == "TOP":
                    if self.ingame:
                        self.infoSlider.canv.yview_scroll(-1000, "units")
                    else:
                        self.error(lang(109), 70)  # si no se encuentra jugando
                else:
                    self.error(lang(133), 70)  # el comando no existe
            try:
                del consola
            except Exception, exerr:
                print langError(351, exerr)

    def dibujarArmor(self):
        """
        Función para dibujar la armadura
        :return: void
        """
        # Borro todas las imágenes anteriores
        self.infoArmaduraArmaDerecha.config(
            image=self.images.image("no_rw"), state=DISABLED, cursor="arrow")
        self.infoArmaduraArmaIzquierda.config(
            image=self.images.image("no_lw"), state=DISABLED, cursor="arrow")
        self.infoArmaduraBotas.config(image=self.images.image(
            "no_botas"), state=DISABLED, cursor="arrow")
        self.infoArmaduraCasco.config(image=self.images.image(
            "no_casco"), state=DISABLED, cursor="arrow")
        self.infoArmaduraChaleco.config(image=self.images.image(
            "no_chaleco"), state=DISABLED, cursor="arrow")
        self.infoArmaduraPantalones.config(image=self.images.image(
            "no_pantalon"), state=DISABLED, cursor="arrow")
        # Cargo por item y dibujo (si existe)
        item = self.player.getCasco()
        if item is not None:
            self.infoArmaduraCasco.config(
                image=self.images.image(item.getImage() + "_32"),
                state=NORMAL, cursor="hand2")
        item = self.player.getLeftWeapon()
        if item is not None:
            self.infoArmaduraArmaIzquierda.config(
                image=self.images.image(item.getImage() + "_32"),
                state=NORMAL, cursor="hand2")
        item = self.player.getChaleco()
        if item is not None:
            self.infoArmaduraChaleco.config(
                image=self.images.image(item.getImage() + "_32"),
                state=NORMAL, cursor="hand2")
        item = self.player.getRightWeapon()
        if item is not None:
            self.infoArmaduraArmaDerecha.config(
                image=self.images.image(item.getImage() + "_32"),
                state=NORMAL, cursor="hand2")
        item = self.player.getPantalones()
        if item is not None:
            self.infoArmaduraPantalones.config(
                image=self.images.image(item.getImage() + "_32"),
                state=NORMAL, cursor="hand2")
        item = self.player.getBotas()
        if item is not None:
            self.infoArmaduraBotas.config(
                image=self.images.image(item.getImage() + "_32"),
                state=NORMAL, cursor="hand2")

    def dibujarItems(self):
        """
        Función para dibujar los items del jugador en el tablero de items
        :return: void
        """
        # Se eliminan las imágenes previas
        for bt in self.botonesItems:
            bt.config(image=self.images.image("vacio_16"), state=DISABLED,
                      command=None,
                      cursor="arrow")
        k = 0
        j = self.player.getItemAmount()
        if j != 0:  # Si el jugador tiene items
            if self.itemnumberlist == j != 0:
                # Si se borra el último elemento de una hoja activa esta se
                # devuelve
                self.itemnumberlist -= 20
            while True:
                bt = self.botonesItems[k]
                if k == 0 and self.itemnumberlist > 0:  # Si es el primer elemento se linkea la hoja anterior
                    bt.config(image=self.images.image("arrow_left"),
                              state=NORMAL,
                              cursor="hand2")  # se agrega al mapeado
                    k += 1
                else:  # Si no es el primer elemento
                    if self.itemnumberlist > 0:
                        # si ya hay mas de una pagina
                        item = self.player.getItem(k + self.itemnumberlist - 1)
                    else:
                        # si sólo es una pagina de items
                        item = self.player.getItem(k + self.itemnumberlist)
                    try:
                        bt.config(
                            image=self.images.image(item.getImage() + "_16"),
                            state=NORMAL,
                            cursor="hand2")  # se agrega textura a los botones
                    except:
                        print lang(378, item.getImage() + "_16")
                    k += 1
                    # Se dibuja la flecha hacia la otra pagina si cumple las
                    # condiciones de borde
                    if k + self.itemnumberlist < j and k == 20:
                        bt = self.botonesItems[k]
                        bt.config(image=self.images.image("arrow_right"),
                                  command=lambda: self.moverListaItems(
                                      "right"),
                                  state=NORMAL, cursor="hand2")
                        break
                    elif (
                                        k + self.itemnumberlist >= j and self.itemnumberlist == 0) or (
                                            k + self.itemnumberlist - 1 >= j and self.itemnumberlist != 0):
                        break

    def dibujarMundo(self, event=None):
        """
        Función que dibuja el mundo (más tableros de combate)
        :param event: Event
        :return: void
        """
        self.world.delete(ALL)  # Se borran todos los objetos
        if not (self.inBattle and (
                        self.tipoCombate == MODE_FIGHT_GROUP or self.tipoCombate == MODE_FIGHT_LINEAL)):
            # Se dibuja al jugador
            if self.player.getLeftWeapon() is not None:  # Arma segundaria
                self.world.create_image(
                    9 + 32 * self.playerPos[0] + self.canvasCorrecion[
                        1] + DRAW_CANVAS_OFFSET_X,
                    self.canvasCorrecion[
                        0] + 32 * self.playerPos[1] + 9 + DRAW_CANVAS_OFFSET_Y,
                    image=self.images.image(
                        self.player.getLeftWeapon().getImage() + "_16"),
                    tags="player:left_weapon")
            else:
                self.world.create_image(
                    9 + 32 * self.playerPos[0] + self.canvasCorrecion[
                        1] + DRAW_CANVAS_OFFSET_X,
                    self.canvasCorrecion[
                        0] + 32 * self.playerPos[1] + 9 + DRAW_CANVAS_OFFSET_Y,
                    image=self.images.image("None"), tags="player:left_weapon")
            # Textura del jugador
            if self.maplightning[self.playerPos[1]][self.playerPos[0]] == 0:
                self.world.create_image(
                    18 + 32 * self.playerPos[0] + self.canvasCorrecion[
                        1] + DRAW_CANVAS_OFFSET_X,
                    self.canvasCorrecion[
                        0] + 32 * self.playerPos[
                        1] + 18 + DRAW_CANVAS_OFFSET_Y,
                    image=self.images.image(self.player.getLinkImage() + "_0"),
                    tags="player")
            else:
                self.world.create_image(
                    18 + 32 * self.playerPos[0] + self.canvasCorrecion[
                        1] + DRAW_CANVAS_OFFSET_X,
                    self.canvasCorrecion[
                        0] + 32 * self.playerPos[
                        1] + 18 + DRAW_CANVAS_OFFSET_Y,
                    image=self.images.image(self.player.getLinkImage() + "_1"),
                    tags="player")
            if self.player.getRightWeapon() is not None:  # Arma primaria
                self.world.create_image(
                    28 + 32 * self.playerPos[0] + self.canvasCorrecion[
                        1] + DRAW_CANVAS_OFFSET_X,
                    self.canvasCorrecion[
                        0] + 32 * self.playerPos[
                        1] + 16 + DRAW_CANVAS_OFFSET_Y,
                    image=self.images.image(
                        self.player.getRightWeapon().getImage() + "_16"),
                    tags="player:right_weapon")
            else:
                self.world.create_image(
                    28 + 32 * self.playerPos[0] + self.canvasCorrecion[
                        1] + DRAW_CANVAS_OFFSET_X,
                    self.canvasCorrecion[
                        0] + 32 * self.playerPos[
                        1] + 16 + DRAW_CANVAS_OFFSET_Y,
                    image=self.images.image("None"),
                    tags="player:right_weapon")
            # Se dibujan los mobs
            k = 0  # id del mob para dejarlo como tag
            for i in self.mobs:  # Se recorre a los mobs
                if self.maplightning[i.getPosicionY()][i.getPosicionX()] == 0:
                    self.world.create_image(
                        18 + 32 * i.getPosicionX() + self.canvasCorrecion[
                            1] + DRAW_CANVAS_OFFSET_X,
                        self.canvasCorrecion[
                            0] + 32 * i.getPosicionY() + 18 + DRAW_CANVAS_OFFSET_Y,
                        image=self.images.image(
                            i.getImage() + "_0"),
                        tags="mob:" + str(k))  # Se dibujan los mobs
                else:
                    self.world.create_image(
                        18 + 32 * i.getPosicionX() + self.canvasCorrecion[
                            1] + DRAW_CANVAS_OFFSET_X,
                        self.canvasCorrecion[
                            0] + 32 * i.getPosicionY() + 18 + DRAW_CANVAS_OFFSET_Y,
                        image=self.images.image(i.getImage() + "_1"),
                        tags="mob:" + str(k))
                self.lifeBar(i.getLife(), i.getMaxLife(), i.getPosicionX(
                ), i.getPosicionY(), k)  # barra de vida
                # Si son varios se dibuja un icono de grupo en la esquina
                # inferior derecha
                if i.getTipoCombate() == MODE_FIGHT_GROUP and (
                                self.nivel_dificultad == DIFICULTAD_FACIL or self.nivel_dificultad == DIFICULTAD_MEDIO):
                    self.world.create_image(
                        26 + 32 * i.getPosicionX() + self.canvasCorrecion[
                            1] + DRAW_CANVAS_OFFSET_X,
                        self.canvasCorrecion[
                            0] + 32 * i.getPosicionY() + 26 + DRAW_CANVAS_OFFSET_Y,
                        image=self.images.image(
                            GROUP_TEXTURE_CREW),
                        tags="mob:icon:grupal:" + str(
                            k))  # Se dibujan los mobs
                k += 1
            # Se dibujan los npc
            k = 0  # id del mob para dejarlo como tag
            # Se recorren los npc que pueden ser dibujados (si el jugador tiene
            # la quest requerida)
            for i in self.npc:
                if i.canShowByQuest(self.player.getQuest()):
                    if self.maplightning[i.getPosicionY()][
                        i.getPosicionX()] == 0:
                        self.world.create_image(
                            18 + 32 * i.getPosicionX() +
                            self.canvasCorrecion[1] + DRAW_CANVAS_OFFSET_X,
                            self.canvasCorrecion[
                                0] + 32 * i.getPosicionY() + 18 + DRAW_CANVAS_OFFSET_Y,
                            image=self.images.image(i.getImage() + "_0"),
                            tags="npc:" + str(k))  # Se dibujan los mobs
                    else:
                        self.world.create_image(
                            18 + 32 * i.getPosicionX() +
                            self.canvasCorrecion[1] + DRAW_CANVAS_OFFSET_X,
                            self.canvasCorrecion[
                                0] + 32 * i.getPosicionY() + 18 + DRAW_CANVAS_OFFSET_Y,
                            image=self.images.image(i.getImage() + "_1"),
                            tags="npc:" + str(k))
                k += 1
            # Se dibujan los items
            for k in range(self.mapSize[1]):
                for j in range(self.mapSize[0]):
                    # Si hay una imagen que insertar
                    if self.mapItemsTextures[k][j] is not None:
                        i = self.world.create_image(
                            18 + self.canvasCorrecion[
                                1] + DRAW_CANVAS_OFFSET_X + 32 * j + textureMover(
                                self.images.image(self.mapItemsTextures[k][j]),
                                EJE_X),
                            18 + self.canvasCorrecion[
                                0] + 32 * k + textureMover(
                                self.images.image(self.mapItemsTextures[k][j]),
                                EJE_Y) + DRAW_CANVAS_OFFSET_Y,
                            image=self.images.image(
                                self.mapItemsTextures[k][j]),
                            tags="item:" + str(j) + "," + str(k))
                        # Compruebo la imagen para ver el zindex
                        if isIn(self.mapItemsTextures[k][j], LOWER_TEXTURES):
                            self.world.lower(i)
            # Inserto el fondo
            self.world.lower(
                self.world.create_image(306 + DRAW_CANVAS_OFFSET_X,
                                        290 + DRAW_CANVAS_OFFSET_Y,
                                        image=self.mapImage[0],
                                        tag="background"))
        elif self.tipoCombate == MODE_FIGHT_GROUP and self.inBattle:  # Si el modo de combate es grupal
            # Dibujo la sangre
            for blood in self.board.getBlood():
                self.world.create_image(
                    18 + 32 * blood[0] + self.board.getBoardCorreccionX(),
                    18 + 32 *
                    blood[1] +
                    self.board.getBoardCorreccionY(),
                    image=self.images.image(blood[2]))
            # Dibujo a los followers
            k = 0
            for i in self.board.getPlayers():
                self.world.create_image(
                    18 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                    18 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                    image=self.images.image(
                        i.getImage() + "_" + str(
                            self.board.getLight(i.getPosX(), i.getPosY()))),
                    tags="grupal:follower:actor:" + str(k))
                if i.getType() != "PL":  # Si no es el jugador al quien se dibuja
                    self.world.create_rectangle(
                        19 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                        4 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                        31 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                        13 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                        fill=RECT_CANT_COLOR_BG_F,
                        outline=RECT_CANT_COLOR_FG_F,
                        tags="grupal:follower:box:" + str(k))
                    self.world.create_text(
                        25 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                        9 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                        text=str(i.getCant()), fill=RECT_CANT_COLOR_TX_F,
                        font=self.fonts[1],
                        anchor=CENTER,
                        tags="grupal:follower:number:" + str(k))
                else:
                    self.world.create_rectangle(
                        14 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                        4 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                        31 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                        13 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                        fill=RECT_CANT_COLOR_BG_P,
                        outline=RECT_CANT_COLOR_FG_P,
                        tags="grupal:player:box")
                    self.world.create_text(
                        22 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                        9 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                        text=str(i.getVida()), fill=RECT_CANT_COLOR_TX_P,
                        font=self.fonts[1],
                        anchor=CENTER,
                        tags="grupal:player:number")
                k += 1
            # Dibujo a los mobs
            k = 0
            for i in self.board.getEnemies():
                self.world.create_image(
                    18 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                    18 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                    image=self.images.image(
                        i.getImage() + "_" + str(
                            self.board.getLight(i.getPosX(), i.getPosY()))),
                    tags="grupal:mob:actor:" + str(k))
                self.world.create_rectangle(
                    19 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                    4 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                    31 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                    13 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                    fill=RECT_CANT_COLOR_BG_M, outline=RECT_CANT_COLOR_FG_M,
                    tags="grupal:mob:box:" + str(k))
                self.world.create_text(
                    25 + 32 * i.getPosX() + self.board.getBoardCorreccionX(),
                    9 + 32 * i.getPosY() + self.board.getBoardCorreccionY(),
                    text=str(i.getCant()), fill=RECT_CANT_COLOR_TX_M,
                    font=self.fonts[1],
                    anchor=CENTER,
                    tags="grupal:mob:number:" + str(k))
                k += 1
            # Dibujo los obstáculos
            for k in range(self.board.getBoardSizeY()):
                for j in range(self.board.getBoardSizeX()):
                    self.world.create_image(
                        18 + self.board.getBoardCorreccionX() + 32 * j,
                        18 + self.board.getBoardCorreccionY() + 32 * k,
                        image=self.images.image(
                            self.board.getItemTexture(j, k)),
                        tags="grupal:item:" + str(j) + "," + str(k))
            # Dibujo los delimitadores
            for k in range(self.board.getBoardSizeY() - 1):
                self.world.create_line(self.board.getBoardCorreccionX() + 2,
                                       self.board.getBoardCorreccionY() + 32 * (
                                           k + 1) + 2,
                                       self.board.getBoardCorreccionX() + 32 * self.board.getBoardSizeX() + 2,
                                       self.board.getBoardCorreccionY() + 32 * (
                                           k + 1) + 2,
                                       fill=LINE_BOARD_COLOR_INACTIVE,
                                       dash=(4, 4))
            for j in range(self.board.getBoardSizeX() - 1):
                self.world.create_line(
                    32 * (j + 1) + self.board.getBoardCorreccionX() + 1,
                    5 + self.board.getBoardCorreccionY(),
                    32 * (j + 1) +
                    self.board.getBoardCorreccionX() + 1,
                    self.board.getBoardCorreccionY() + self.board.getBoardSizeY() * 32 + 5,
                    fill=LINE_BOARD_COLOR_INACTIVE, dash=(4, 4))
            self.world.create_line(self.board.getBoardCorreccionX() + 1,
                                   self.board.getBoardCorreccionY() + 2,
                                   self.board.getBoardCorreccionX() + self.board.getBoardSizeX() * 32 + 1,
                                   self.board.getBoardCorreccionY() + 2,
                                   fill=LINE_BOARD_COLOR_INACTIVE)
            self.world.create_line(self.board.getBoardCorreccionX() + 1,
                                   self.board.getBoardCorreccionY() + 2 + self.board.getBoardSizeY() * 32,
                                   self.board.getBoardCorreccionX() + 1 + self.board.getBoardSizeX() * 32 + 1,
                                   self.board.getBoardCorreccionY() + 2 + self.board.getBoardSizeY() * 32,
                                   fill=LINE_BOARD_COLOR_INACTIVE)
            self.world.create_line(self.board.getBoardCorreccionX() + 1,
                                   self.board.getBoardCorreccionY() + 2,
                                   self.board.getBoardCorreccionX() + 1,
                                   self.board.getBoardCorreccionY() + 2 + 32 * self.board.getBoardSizeY(),
                                   fill=LINE_BOARD_COLOR_INACTIVE)
            self.world.create_line(
                self.board.getBoardCorreccionX() + 1 + 32 * self.board.getBoardSizeX(),
                self.board.getBoardCorreccionY() + 2,
                self.board.getBoardCorreccionX() + 1 + 32 * self.board.getBoardSizeX(),
                self.board.getBoardCorreccionY() + 2 + 32 * self.board.getBoardSizeY(),
                fill=LINE_BOARD_COLOR_INACTIVE)
            # Se dibuja el fondo
            self.world.lower(
                self.world.create_image(306 + DRAW_CANVAS_OFFSET_X,
                                        290 + DRAW_CANVAS_OFFSET_Y,
                                        image=self.board.bgimage,
                                        tags="grupal:background"))
            self.combateGrupal("print")
            self.world.update()

    def dibujarPowers(self):
        """
        Función que dibuja los poderes del jugador en la lista de poderes
        :return: void
        """
        # Se eliminan las imágenes previas
        for bt in self.botonesPoderes:
            bt.config(image=self.images.image("vacio_16"), state=DISABLED,
                      command=None,
                      cursor="arrow")
        for i in range(min(self.player.getPowerAmount(), 7)):
            bt = self.botonesPoderes[i]
            power = self.player.getPower(i)
            if self.player.getLevel() >= power.getNivel():  # Se crea el botón en función del nivel del poder
                bt.config(image=self.images.image(power.getImage()),
                          state=NORMAL, cursor="hand2")
            else:
                bt.config(image=self.images.image(power.getImage()),
                          state=DISABLED, cursor="arrow")

    def error(self, text, h=70, w=300, icon=""):
        """
        Función que muestra un pop-up de error
        :param text: String
        :param h: Ancho de la ventana
        :param w: Alto de la ventana
        :param icon: String de icono
        :return:
        """
        if not isWindows():
            if h == 70:
                h = 75
        self.initialBg.config(cursor="arrow")
        st_error(text)
        if icon == "":
            e = pop([[lang(54), lang(173)], self.images.image(
                "alert_icon"), "aviso", h, w, text])
            e.w.mainloop(2)
            del e
        else:
            e = pop([[lang(54), lang(173)], self.images.image(
                icon), "aviso", h, w, text])
            e.w.mainloop(2)
            del e

    def escogerArmamento(self, e):
        """
        Escoger armamento y poderes
        :param e: Evento
        :return: void
        """
        if self.ingame:  # Si se encuentra jugando una partida
            if e == "automatic_bullet":  # Si bullet se escoge automaticamente
                armamento = []  # matriz que se usara para buscar armamento
                bulletid = 0  # id que se usara para reconocer al item
                for bullet in self.player.getItems():  # Si el item es una bala se agrega
                    if bullet.getType() == "bullet":
                        armamento.append(
                            [translate(bullet.getName()), bullet.getDamage(),
                             bullet.getUsos(), bulletid])
                    bulletid += 1  # aumenta el contador
                if len(armamento) > 1:  # Si hay mas de un armamento
                    self.setInfo(lang(264))
                    # Se arma una ventana con todos los bullets activos y se
                    # retorna un id
                    e = pop([[lang(254), lang(249), lang(256), "", "",
                              lang(255), lang(259), lang(260), lang(268)],
                             DATA_ICONS_ITEMS + self.player.getLeftWeapon().getImage() +
                             "_16.ico", "escogerArmamento",
                             130, 300, ["bullet"], [armamento, [], []]])
                    e.w.mainloop(1)
                    if e.sent:
                        if self.player.getActiveBullet() is not None:
                            self.player.addObject(
                                self.player.getActiveBullet())
                            self.player.dropObject(
                                self.player.getActiveBullet())
                        if e.values[
                            0] != -1:  # Si se mandó una respuesta válida
                            bullet = self.player.getItem(e.values[0])
                            if bullet.getType() == "bullet":
                                self.player.setActiveBullet(
                                    bullet)  # se define la bala
                                self.player.dropObject(
                                    e.values[
                                        0])  # se bota el item definido dado que ya existe una copia
                                self.setInfo(lang(262, translate(
                                    self.player.getActiveBullet().getName())))  # mensaje 'se ha definido'
                            else:  # Si el id cambió en el transcurso de definirlo
                                self.error(lang(272, translate(
                                    self.player.getLeftWeapon().getName())),
                                           85)  # mensaje de error inesperado
                                self.player.delActiveBullet()  # se borra el armamento
                        else:
                            self.player.delActiveBullet()  # se elimina lo que tenga
                    else:  # Si no fue recibida ninguna respuesta de la ventana
                        self.player.delActiveBullet()  # si no envió algo se elimina
                        self.setInfo(lang(269))  # no se eligió arma
                    del e
                elif len(armamento) == 1:  # Si sólo hay un armamento
                    self.player.setActiveBullet(
                        self.player.getItem(armamento[0][
                                                3]))  # se define la bala como bala principal
                    self.player.dropObject(
                        armamento[0][
                            3])  # se bota la bala desde los items (dado que existen dos copias)
                    self.setInfo(lang(250, armamento[0][0],
                                      translate(
                                          self.player.getLeftWeapon().getName())))  # se muestra mensaje
                else:  # Si no tiene armas
                    self.player.delActiveBullet()  # si no hay armamento se borra el actual
                    e = pop(
                        [[lang(271), lang(173)],
                         DATA_ICONS_ITEMS + self.player.getLeftWeapon().getImage() + "_16.ico",
                         "aviso", 85, 270, lang(270)])
                    e.w.mainloop(2)
                    del e
                del armamento
            self.dibujarItems()
            # Si se encuentra en dicho modo de combate y juega el usuario
            if self.inBattle and self.tipoCombate == MODE_FIGHT_GROUP:
                if self.board.returnControl():
                    self.combateGrupal("print")

    def getActivePowerId(self, i):
        """
        Función que retorna un poder en especifico
        :param i: Index
        :return: Boolean
        """
        try:
            # Si el poder corresponde al jugador
            if self.activePowers[0] == self.player.getName():
                if self.activePowers[1][i] == 1:
                    return True
                else:
                    return False
        except:
            print lang(390)

    def incrementarExperiencia(self, experiencia):
        """
        Aumenta la experiencia del jugador
        :param experiencia: Integer
        :return: void
        """
        while self.player.increaseExp(experiencia):  # Ganar experiencia
            # Si se juega en medio o fácil la vida y el mana aumentan al máximo
            # (tras subir de nivel)
            if self.nivel_dificultad == DIFICULTAD_FACIL or self.nivel_dificultad == DIFICULTAD_MEDIO:
                self.player.upgradeMana()
                self.player.upgradeLife()
                self.setInfo(lang(91))
                self.playerText("+", "verde", True)
            self.sfx(30)
            self.setInfo(lang(92))
            e = pop(
                [[lang(92), lang(173)], self.images.image("icon"), "aviso", 70,
                 270,
                 lang(93, str(self.player.getLevel()))])
            e.w.mainloop(1)
            del e
        self.setInfo(lang(94, str(experiencia)))

    def lifeBar(self, prev, tot, x, y, k=0):
        """
        Función que dibuja una barra bajo un mob indicando su vida
        :param prev: Vida previa
        :param tot: Vida total
        :param x: Posición x
        :param y: Posición y
        :param k: Index en el mapa
        :return: void
        """
        # se obtiene la imagen de acuerdo al nivel de vida
        img = "life{0}".format(int(math.ceil(max(prev * 100 / tot, 1) / 10.0)))
        try:
            self.world.create_image(32 * x + self.canvasCorrecion[1] + 18,
                                    32 * y + self.canvasCorrecion[0] - 9,
                                    image=self.images.image(img),
                                    tags="lifebar:" + str(k))
        except:
            print lang(366)

    def loadGame(self, e=None, b=""):
        """
        Función que carga una partida
        :param e: Event
        :param b: String de partida por argumento
        :return: void
        """
        global load, key1, console

        def _loadingScreen(image, e=None):
            """
            Pantalla de cargando
            :param image: String de imagen
            :param e: Evento
            :return: void
            """
            self.initialBg.create_image(405, 299, image=image)
            self.initialBg.update()
            time.sleep(0.025)

        if not self.isNewGameCreating:
            if self.multiplayer_isconected:  # Si el jugador está conectado a un servidor
                v = pop([[lang(795), lang(796), lang(797), lang(239)],
                         self.images.image("server_disconnect"),
                         "deseaDesconectarse",
                         75, 310, CONFIGURATION_DATA[
                             1]])  # Se consulta si cerrar o no la sesión activa
                v.w.mainloop(1)
                if v.sent:  # Se procede en función de la respuesta
                    if v.values[0] == "si":
                        print lang(798),
                        try:
                            self.multiplayer_desconnect(False)
                            print lang(310)
                        except:
                            print lang(398)
                    elif v.values[0] == "cancel":
                        del v
                        return
                del v
            totalerrors = 0
            print lang(407)
            if e != "argv":  # Si el archivo no se pasó por argumento
                print lang(406),
                archivo = str(
                    askopenfilename(title=lang(52), initialdir=DATA_SAVES,
                                    defaultextension=".save",
                                    filetypes=[(lang(563), ".save")])).encode(
                    "utf-8"). \
                    replace(u"\ufeff", "").replace("\xef\xbb\xbf", "")
            else:
                archivo = DATA_SAVES + b  # si se pasó se carga junto al directorio
            if len(archivo) > 0:  # Si el archivo existe
                if e != "argv":
                    print lang(310)
                self.ingame = True  # booleano que indica que se esta en juego o en proceso de cargado
                try:
                    self.menu.pack_forget()  # oculto todas las ventanas
                    self.menu2.pack_forget()
                    self.content.pack_forget()
                    self.initialBg.pack()
                except:
                    totalerrors += 1
                self.initialBg.create_rectangle(0, 0, 1000, 1000, fill="black")
                try:
                    self.initialBg.config(cursor="wait")
                except Exception, e:
                    print langError(829, e)
                self.root.title(lang(210))  # modifico el título con cargando
                # pantalla de cargado 1
                self.root.after(0, _loadingScreen(
                    self.images.image("loading0")))
                try:  # Se extrae el archivo de guardado
                    print lang(408),
                    loadfile = zipfile.ZipFile(archivo)
                    loadfile.extractall()
                    loadfile.close()
                    print lang(310)
                except:  # Error al extraer el archivo de guardado
                    print lang(398)
                    if e != "argv":
                        print lang(353)
                        self.abortGame()
                        self.error(lang(214))
                        return
                    else:
                        print lang(773)
                        self.abortGame()
                        self.error(lang(772))
                        return
                try:  # Se cargan los archivos de guardado
                    print lang(409),
                    load = loadFromArchive(archivo.replace(".save", ".sav"),
                                           lang(400),
                                           False)  # archivo principal de actor
                    console = loadFromArchive(archivo.replace(
                        ".save", ".hoacmd"), lang(400), False)  # consola
                    key1 = loadFromArchive(archivo.replace(
                        ".save", ".key1"), lang(400),
                        False)  # llaves de seguridad
                    key2 = loadFromArchive(archivo.replace(
                        ".save", ".key2"), lang(400),
                        False)  # llaves de seguridad
                    key3 = loadFromArchive(archivo.replace(
                        ".save", ".key3"), lang(400),
                        False)  # llaves de seguridad
                    key4 = loadFromArchive(archivo.replace(
                        ".save", ".key4"), lang(400),
                        False)  # llaves de seguridad
                    key5 = loadFromArchive(archivo.replace(
                        ".save", ".key5"), lang(400),
                        False)  # llaves de seguridad
                    loadmapmob = loadFromArchive(
                        archivo.replace(".save", ".mapmob"), lang(400),
                        False)  # información de los mobs del mapa actual
                    loadmapnpc = loadFromArchive(
                        archivo.replace(".save", ".mapnpc"), lang(400),
                        False)  # información de los npc del mapa actual
                    loadpowers = loadFromArchive(
                        archivo.replace(".save", ".powers"), lang(400),
                        False)  # poderes del jugador
                    loadquest = loadFromArchive(
                        archivo.replace(".save", ".quest"), lang(400),
                        False)  # quest del jugador
                    loadstatics = \
                        loadFromArchive(archivo.replace(".save", ".statics"),
                                        lang(400), False)[0].split(
                            self.static.getSeparator())  # estadísticas
                    loadmaplogic = loadFromArchive(
                        archivo.replace(".save", ".maplogic"), lang(400),
                        False)  # mapa lógico del guardado
                    loadmapitemtexture = loadFromArchive(
                        archivo.replace(".save", ".mapitemtexture"), lang(400),
                        False)  # texturas de items del mapa
                    console.reverse()  # se invierte el orden de los comandos
                    print lang(310)
                except:  # Error al cargar los archivos del guardado
                    print lang(398)
                    print lang(352)
                    self.abortGame()
                    self.error(lang(215), 85)
                if (amir(archivo.replace(".save", ".sav")).strip() == key1[
                    0] and amir(
                    archivo.replace(".save", ".statics")).strip() == key2[
                    0] and
                            amir(archivo.replace(".save",
                                                 ".maplogic")).strip() == key3[
                            0] and amir(
                    archivo.replace(".save", ".hoacmd")).strip() == key4[0] and
                            amir(
                                archivo.replace(".save", ".mapmob")).strip() ==
                            key5[
                                0]):  # Si el archivo no ha sido modificado
                    self.stopSound()  # se paran todos los sonidos
                    try:
                        self.delInfo()  # se borra la consola
                    except:
                        totalerrors += 1
                        print lang(351)
                    if console[
                        0] != "%NOCONSOLE%":  # Si la consola no está vacía
                        if len(console) < LIMIT_MESSAGES_CONSOLE:
                            for i in console:
                                self.console.insert(0, i)
                        else:
                            difr = len(console) - LIMIT_MESSAGES_CONSOLE
                            c = 0
                            for i in console:
                                if c > difr:
                                    # se carga la consola
                                    self.console.insert(0, i)
                                else:
                                    c += 1
                    try:
                        self.setInfo(False, False)
                    except:
                        totalerrors += 1
                    self.player.dropItems()  # boto los items cargados
                    self.player.dropArmor()  # boto la actual armadura
                    self.player.delQuest()  # elimino las quest
                    for j in range(2):
                        self.activePowers.pop()
                    self.activePowers.append("playername")
                    self.activePowers.append(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0])
                    self.itemnumberlist = 0  # pagina en 0
                    self.player = None  # borro al jugador
                    self.player = actors()  # nueva clase actor
                    delMatrix(self.dificultad)  # borro la dificultad
                    self.dibujarItems()  # redibujo los items
                    self.dibujarArmor()  # redibujo la armadura
                    self.namePartida = load[0]
                    try:  # se cargan los datos del usuario
                        print lang(410)
                        # pantalla de cargado
                        self.root.after(0, _loadingScreen(
                            self.images.image("loading1")))
                        self.nivel_dificultad = load[4]  # dificultad del juego
                        self.player.setLinkImage(load[9])  # textura
                        self.setDificultad()  # se define la dificultad
                        if load[11] == "%ERROR_LOADINGMAP%":
                            # si ocurre un error al cargar el mapa
                            raise Exception(lang(98))
                        self.player.setMap(load[11])  # mapa a cargar
                        self.setWorld()  # creo el mundo para generar el fondo y consultar los elementos lógicos
                        self.root.after(1, _loadingScreen(
                            self.images.image("loading2")))
                        # se define el nivel del jugador
                        self.player.setLevel(int(load[8]))
                        # se define el tipo de jugador
                        self.player.setType(load[12].lower())
                        self.player.setName(load[1])  # nombre del jugador
                        self.player.setEdad(int(load[2]))  # edad del jugador
                        self.player.setPais(load[3])  # país del jugador
                        self.player.setDamage(int(load[5]))  # daño del jugador
                        self.player.setExperience(int(load[6]))  # experiencia
                        self.player.setInfo(load[7])  # información
                        self.player.setMana(int(load[10]))  # mana
                        self.player.setVelocidad(int(load[13]))  # velocidad
                        self.itemnumberlist = int(load[16])  # pagina de items
                        self.activePowers[0] = load[1]  # nombre a los poderes
                        # se cargan los amigos
                        self.player.setFriends(load[17])
                    except:  # Error al cargar los datos del usuario
                        print lang(398)
                        print lang(350)
                        self.abortGame()
                        self.error(lang(145))
                        return
                    # se comprueba si el jugador es editor o no
                    editorkey = base64.b64encode(
                        md5.new(self.player.getName()).digest())
                    if editorkey == "NEp/Qn+3ZWEO+W63vOlSVw==" or editorkey == "Y/sQiCQbCs3XmHrwwfT35g==":
                        self.player.setEditor()
                    else:
                        self.player.setNotEditor()
                    self.enemy = None  # borro la información del enemigo
                    self.currentNpc = None
                    self.inBattle = False
                    self.inNpc = False
                    try:  # Se cargan los lógicos del mapa guardado
                        print lang(411),
                        y = 0
                        for i in loadmaplogic:
                            x = 0
                            j = i.split(";")
                            j.pop()
                            for logic in j:
                                # se define el nuevo lógico
                                self.mapLogic[y][x] = logic
                                x += 1
                            y += 1
                        print lang(310)
                    except:  # Error al cargar los elementos lógicos
                        print lang(398)
                        print lang(349)
                        self.abortGame()
                        self.error(lang(146), 85)
                        return
                    try:  # Se cargan las texturas de los items del mapa
                        print lang(412),
                        y = 0
                        for i in loadmapitemtexture:
                            x = 0
                            j = i.split(";")
                            j.pop()
                            for logic in j:
                                if logic == "None":
                                    logic = None
                                # se define la textura del item
                                self.mapItemsTextures[y][x] = logic
                                x += 1
                            y += 1
                        print lang(310)
                    except:  # Error al cargar las texturas de los items
                        print lang(398)
                        print lang(348)
                        self.abortGame()
                        self.error(lang(223), 85)
                        return
                    if len(
                            self.mobs) != 0:  # Si hay mobs en el mapa que se cargó
                        try:  # Se cargan los mob
                            print lang(413),
                            delMatrix(self.mobs)
                            self.enemyId = 0
                            if loadmapmob[
                                0] != "%NOMOBS%":  # Si hay mobs por cargar
                                for prop in loadmapmob:  # Se recorrren los mob
                                    prop = prop.split(MOB_SEPARATOR)
                                    # Se agrega el objeto a la lista de
                                    # enemigos
                                    self.mobs.append(
                                        mob(int(prop[0]), int(prop[1]),
                                            prop[2], int(prop[3]),
                                            int(prop[4]), prop[5],
                                            prop[6], int(prop[7]),
                                            int(prop[8]), int(
                                                prop[9]), int(prop[10]),
                                            int(prop[11]), int(prop[12]), prop[
                                                13], prop[14], prop[15],
                                            int(prop[16]),
                                            int(prop[17]), int(prop[18]),
                                            prop[19], prop[20], prop[21]))
                            try:
                                # se elimina el ultimo movimiento
                                self.root.after_cancel(self.lastmovementId)
                            except:
                                totalerrors += 1
                            if len(
                                    self.mobs) != 0:  # Activa el movimiento de los mobs
                                self.lastmovementId = self.root.after(
                                    self.dificultad[5], self.moveMobs)
                                self.movement = True
                            else:
                                self.movement = False
                            print lang(310)
                        except:  # Error al cargar los mob
                            print lang(398)
                            print lang(347)
                            self.abortGame()
                            self.error(lang(147), 85)
                            return
                    if len(self.npc) != 0:  # Si hay npc en el mapa actual
                        try:  # Cargo los npc
                            print lang(441),
                            delMatrix(self.npc)
                            self.npcId = -1
                            if loadmapnpc[
                                0] != "%NONPC%":  # Si hay npc por cargar
                                for elem in loadmapnpc:  # Se recorren los npc
                                    elem = elem.split(NPC_SEPARATOR)
                                    # Se agrega el elemento a la lista de npc
                                    self.npc.append(
                                        npc(elem[0], elem[1], elem[2], elem[3],
                                            elem[4], elem[5], int(elem[6]),
                                            elem[7],
                                            int(elem[8]), elem[9], int(
                                                elem[10]), int(elem[11]),
                                            elem[12],
                                            int(elem[13]),
                                            int(elem[14]), int(elem[15]),
                                            elem[16]))
                            movement = False
                            for elem in self.npc:
                                if elem.getMove():
                                    movement = True
                                    break
                            if movement:
                                try:
                                    self.root.after_cancel(
                                        self.lastnpcmovementid)
                                except:
                                    print lang(564)
                                self.lastnpcmovementid = self.root.after(
                                    NPC_TIME_MOVEMENT, self.moveNpc)
                                self.npcMovement = True
                            else:
                                self.npcMovement = False
                            del movement
                            print lang(310)
                        except:
                            print lang(398)
                            print lang(442)
                            self.abortGame()
                            self.error(lang(443), 85)
                            return
                    try:  # Se cargan las quest
                        print lang(583),
                        for quest in range(1, len(loadquest) - 1):
                            self.player.addQuest(
                                loadquest[quest].replace("\n", ""))
                        print lang(310)
                    except:
                        print lang(398)
                        print lang(581)
                        self.abortGame()
                        self.error(lang(582))
                        return
                    try:  # Se cargan las estadísticas
                        print lang(414),
                        self.static.restart()  # borro las estadíssticas anteriores
                        self.static.__init__(int(loadstatics[0]),
                                             int(loadstatics[1]),
                                             int(loadstatics[2]),
                                             int(loadstatics[3]),
                                             int(loadstatics[4]), int(
                                loadstatics[5]), int(loadstatics[6]),
                                             int(loadstatics[7]),
                                             int(loadstatics[8]), int(
                                loadstatics[9]), int(loadstatics[10]),
                                             int(loadstatics[11]),
                                             int(loadstatics[12]), int(
                                loadstatics[13]), int(loadstatics[14]),
                                             int(loadstatics[15]),
                                             int(loadstatics[16]), int(
                                loadstatics[17]), int(loadstatics[18]),
                                             int(loadstatics[19]))
                        print lang(310)
                    except:  # Error al cargar las estadísticas
                        print lang(398)
                        print lang(346)
                        self.error(lang(175), 70)
                        return
                    try:  # Se carga la posición y la textura
                        self.playerPos[0] = int(load[14])
                        self.playerPos[1] = int(load[15])
                        self.mapLogic[self.playerPos[1]][
                            self.playerPos[0]] = "player"
                    except:  # Error al cargar la posición y/o la textura
                        print lang(345)
                        self.abortGame()
                        self.error(lang(183), 70)
                        return
                    self.root.after(1, _loadingScreen(
                        self.images.image("loading3")))  # ventana de cargado
                    print lang(415),
                    try:  # Se cargan las balas y poderes
                        if load[18] != "%NULL%":
                            self.player.setActiveBullet(
                                Item(parseObject(
                                    load[18])))  # armamento predefinido
                        else:
                            self.player.delActiveBullet()
                        if load[19] != "%NULL%":
                            self.player.setFirstPower(load[19])  # primer poder
                        else:
                            self.player.delFirstPower()
                        if load[20] != "%NULL%":
                            self.player.setSecondPower(
                                load[20])  # segundo poder
                        else:
                            self.player.delSecondPower()
                    except:  # Error al cargar las balas y los poderes
                        print lang(398)
                        print lang(344)
                        self.player.delActiveBullet()
                        self.player.delFirstPower()
                        self.player.delSecondPower()
                        self.setInfo(lang(53))
                        self.error(lang(263))
                        return
                    try:  # Se cargan las armas
                        if load[22] != "%NULL%":
                            self.player.setLeftWeapon(
                                Item(parseObject(load[22])))
                        if load[23] != "%NULL%":
                            self.player.setRightWeapon(
                                Item(parseObject(load[23])))
                    except:  # Error al cargar las armas
                        print lang(398)
                        print lang(343)
                        self.error(lang(148))
                        return
                    try:  # Se carga la armadura
                        if load[25] != "%NULL%":
                            self.player.addCasco(Item(parseObject(load[25])))
                        if load[26] != "%NULL%":
                            self.player.addChaleco(Item(parseObject(load[26])))
                        if load[27] != "%NULL%":
                            self.player.addPantalones(
                                Item(parseObject(load[27])))
                        if load[28] != "%NULL%":
                            self.player.addBotas(Item(parseObject(load[28])))
                    except:  # Error al cargar la armadura
                        print lang(398)
                        print lang(342)
                        self.error(lang(149))
                        return
                    try:  # Se cargan los items
                        i = 0
                        while True:  # Se carga mientras no salga #end# en el archivo
                            if load[30 + i] != "#end#":
                                self.player.addObject(
                                    Item(parseObject(load[30 + i])))
                                i += 1
                                if i == 100:
                                    self.root.after(1, _loadingScreen(
                                        self.images.image("loading4")))
                                elif i == 200:
                                    self.root.after(1, _loadingScreen(
                                        self.images.image("loading5")))
                            else:
                                break
                        print lang(310)
                    except:  # Si ocurre un error al cargar
                        print lang(398)
                        print lang(341)
                        self.error(lang(150))
                        return
                    try:  # Se cargan los poderes
                        print lang(584),
                        for i in loadpowers:  # Recorro los poderes guardados
                            poder = i.split(POWERSEP)
                            self.player.addPower(Power(poder))
                        print lang(310)
                    except:
                        print lang(398)
                        print lang(387)
                        self.error(lang(388))
                        return
                    try:  # Borro las listas cargadas
                        del load
                        del key1
                        del key2
                        del key3
                        del key4
                        del key5
                        del console
                        del loadmapmob
                        del loadstatics
                        del loadmaplogic
                        del loadmapnpc
                        del loadpowers
                    except:  # Ocurre un error al borrar las listas
                        print lang(340)
                        self.setInfo(lang(53))
                        self.error(lang(176))
                    # Establezco las variables que indica que el mapa esta
                    # cargado
                    self.loaded = True
                    self.update()
                    # Muestro todas las ventanas y modifico el estado de los
                    # menús
                    self.menu.pack(side=LEFT, fill=Y)
                    self.menu2.pack(side=LEFT)
                    self.content.pack()
                    self.initialBg.pack_forget()
                    if CONFIGURATION_DATA[12]:
                        self.archivomenu.entryconfig(2, state=NORMAL)
                    self.archivomenu.entryconfig(3, state=NORMAL)
                    for k in range(5):
                        self.vermenu.entryconfig(k, state=NORMAL)
                    self.sfx(30)
                    # Mensaje de bienvenida
                    self.setInfo(lang(447, self.player.getName()))
                else:  # Si el archivo ha sido modificado
                    self.abortGame()
                    self.setInfo(lang(56))
                    self.error(lang(57), 85)
                print lang(416),
                borrarArchivosGuardado(archivo)
                print lang(310)  # borro los archivos extraidos
                print lang(417),
                if totalerrors == 0:
                    print lang(310)
                else:
                    print lang(762).format(str(totalerrors)).strip()
                del totalerrors
            else:
                print lang(398)
        self.initialBg.config(cursor="arrow")

    def move(self, x, y):
        """
        Función que mueve la imagen del jugador y modifica el campo lógico
        :param x: Posición x
        :param y: Posición y
        :return: void
        """
        try:

            def _allow():
                """
                Activa el movimiento
                :return: void
                """
                self.canmove = True

            self.canmove = False
            if self.maplightning[self.playerPos[1]][self.playerPos[0]] != \
                    self.maplightning[y][
                        x]:  # Si hay algún cambio en la iluminación
                # Modifico la iluminación de la textura
                if self.maplightning[y][x] == 0:
                    self.world.itemconfig("player", image=self.images.image(
                        self.player.getLinkImage() + "_0"))
                else:
                    self.world.itemconfig("player", image=self.images.image(
                        self.player.getLinkImage() + "_1"))
            self.mapLogic[self.playerPos[1]][self.playerPos[
                0]] = "none"  # Modifico el campo lógico
            # Actualizar la posición del jugador
            self.mapLogic[y][x] = "player"
            self.playerPos[0] = x
            self.playerPos[1] = y
            self.static.addMovimientos()

            def _moveNoAnimation():
                """
                Mueve la textura sin animación
                :return: void
                """
                self.world.coords("player", 18 + 32 * x + self.canvasCorrecion[
                    1] + DRAW_CANVAS_OFFSET_X,
                                  self.canvasCorrecion[
                                      0] + 32 * y + 18 + DRAW_CANVAS_OFFSET_Y)
                self.world.coords("player:left_weapon",
                                  9 + 32 * x + self.canvasCorrecion[
                                      1] + DRAW_CANVAS_OFFSET_X,
                                  self.canvasCorrecion[
                                      0] + 32 * y + 9 + DRAW_CANVAS_OFFSET_Y)
                self.world.coords("player:right_weapon",
                                  28 + 32 *
                                  self.playerPos[
                                      0] + self.canvasCorrecion[
                                      1] + DRAW_CANVAS_OFFSET_X,
                                  self.canvasCorrecion[0] + 32 *
                                  self.playerPos[
                                      1] + 16 + DRAW_CANVAS_OFFSET_Y)

            if MOVEMENT_ANIMATION[0]:  # Movimiento con animación
                try:
                    self.root.after(int(TEXDT / 4), makeCallable(
                        partial(arrastrarImagen, "player:left_weapon",
                                self.world,
                                9 + 32 * x +
                                self.canvasCorrecion[
                                    1] + DRAW_CANVAS_OFFSET_X,
                                self.canvasCorrecion[
                                    0] + 32 * y + 9 + DRAW_CANVAS_OFFSET_Y)))
                    self.root.after(int(TEXDT / 4), makeCallable(
                        partial(arrastrarImagen, "player", self.world,
                                18 + 32 * x +
                                self.canvasCorrecion[
                                    1] + DRAW_CANVAS_OFFSET_X,
                                self.canvasCorrecion[
                                    0] + 32 * y + 18 + DRAW_CANVAS_OFFSET_Y)))
                    self.root.after(int(TEXDT / 4), makeCallable(
                        partial(arrastrarImagen, "player:right_weapon",
                                self.world,
                                28 + 32 *
                                self.playerPos[
                                    0] + self.canvasCorrecion[
                                    1] + DRAW_CANVAS_OFFSET_X,
                                self.canvasCorrecion[0] + 32 * self.playerPos[
                                    1] + 16 + DRAW_CANVAS_OFFSET_Y)))
                except:
                    _moveNoAnimation()
                    print lang(389)
            else:  # Movimiento sin animación
                _moveNoAnimation()
            self.root.after(MOVETIME, _allow)
        except:  # Si ocurre algún error durante el proceso de movimiento
            self.error(lang(565))
            print lang(566, self.playerPos[1], self.playerPos[0])
            self.setInfo(lang(567))
            self.root.after(ERROR_DELAY, self.abortGame)

    def moveMobs(self):
        """
        Función para mover a los enemigos
        :return: void
        """
        try:
            # se borra el ultimo elemento
            self.root.after_cancel(self.lastmovementId)
        except:
            print lang(363)
        if not self.inBattle and self.movement and not self.inNpc and not self.getActivePowerId(
                0):  # Si no se encuentra en batalla y puede moverse
            # genero una matriz de identificadores para los mobs
            mob_id = range(len(self.mobs))
            random.shuffle(mob_id)  # desordeno la matriz
            for i_d in mob_id:  # Se van recorriendo los ids generados aleatoriamente
                mob = self.mobs[i_d]  # se carga el mob asociado a ese id
                x, y = mob.move(self.playerPos[0], self.playerPos[
                    1])  # se mueve el mob
                # Si las coordenadas estan dentro del mapa
                if 0 <= y < self.mapSize[1] and 0 <= x < self.mapSize[0]:
                    if self.mapLogic[y][x] == "none":  # Si el lugar esta vacío
                        if self.maplightning[mob.getPosicionY()][
                            mob.getPosicionX()] != self.maplightning[y][
                            x]:  # Si cambia la iluminación
                            if self.maplightning[y][x] == 0:
                                self.world.itemconfig(
                                    "mob:" + str(i_d), image=self.images.image(
                                        mob.getImage() + "_0"))
                            else:
                                self.world.itemconfig(
                                    "mob:" + str(i_d), image=self.images.image(
                                        mob.getImage() + "_1"))
                        # Actualizo el mapa lógico
                        self.mapLogic[mob.getPosicionY()][
                            mob.getPosicionX()] = "none"
                        self.mapLogic[y][x] = "mob"
                        mob.setPosicionX(x)
                        mob.setPosicionY(y)
                    # Si la siguiente combinación está vacía
                    elif self.mapLogic[y][mob.getPosicionX()] == "none":
                        if self.maplightning[mob.getPosicionY()][
                            mob.getPosicionX()] != self.maplightning[y][
                            mob.getPosicionX()]:  # Si cambia la iluminación
                            if self.maplightning[y][mob.getPosicionX()] == 0:
                                self.world.itemconfig(
                                    "mob:" + str(i_d), image=self.images.image(
                                        mob.getImage() + "_0"))
                            else:
                                self.world.itemconfig(
                                    "mob:" + str(i_d), image=self.images.image(
                                        mob.getImage() + "_1"))
                        # Actualizo el mapa lógico
                        self.mapLogic[mob.getPosicionY()][
                            mob.getPosicionX()] = "none"
                        self.mapLogic[y][mob.getPosicionX()] = "mob"
                        mob.setPosicionY(y)
                    # Si el lugar está vacío
                    elif self.mapLogic[mob.getPosicionY()][x] == "none":
                        if self.maplightning[mob.getPosicionY()][
                            mob.getPosicionX()] != \
                                self.maplightning[mob.getPosicionY()][
                                    x]:  # Si cambia la iluminación
                            if self.maplightning[mob.getPosicionY()][x] == 0:
                                self.world.itemconfig(
                                    "mob:" + str(i_d), image=self.images.image(
                                        mob.getImage() + "_0"))
                            else:
                                self.world.itemconfig(
                                    "mob:" + str(i_d), image=self.images.image(
                                        mob.getImage() + "_1"))
                        # Actualizo el mapa lógico
                        self.mapLogic[mob.getPosicionY()][
                            mob.getPosicionX()] = "none"
                        self.mapLogic[mob.getPosicionY()][x] = "mob"
                        mob.setPosicionX(x)
                    try:  # Se mueve la textura del mob
                        # Movimiento sin animación
                        if not MOVEMENT_ANIMATION[0]:
                            self.world.coords("mob:" + str(i_d),
                                              18 + 32 * mob.getPosicionX() +
                                              self.canvasCorrecion[
                                                  1] + DRAW_CANVAS_OFFSET_X,
                                              self.canvasCorrecion[
                                                  0] + 32 * mob.getPosicionY() + 18 + DRAW_CANVAS_OFFSET_Y)
                            self.world.coords("lifebar:" + str(i_d),
                                              32 * mob.getPosicionX() +
                                              self.canvasCorrecion[
                                                  1] + 18 + DRAW_CANVAS_OFFSET_X,
                                              32 * mob.getPosicionY() +
                                              self.canvasCorrecion[
                                                  0] - 9 + DRAW_CANVAS_OFFSET_Y)
                            if self.nivel_dificultad == DIFICULTAD_FACIL or self.nivel_dificultad == DIFICULTAD_MEDIO:
                                self.world.coords(
                                    "mob:icon:grupal:" + str(i_d),
                                    27 + 32 * mob.getPosicionX() +
                                    self.canvasCorrecion[
                                        1] + DRAW_CANVAS_OFFSET_X,
                                    self.canvasCorrecion[
                                        0] + 32 * mob.getPosicionY() + 26 + DRAW_CANVAS_OFFSET_Y)
                        else:  # Movimiento con animación
                            self.root.after(TEXDT, makeCallable(
                                partial(arrastrarImagen, "mob:" + str(i_d),
                                        self.world,
                                        17 + 32 * mob.getPosicionX() +
                                        self.canvasCorrecion[
                                            1] + DRAW_CANVAS_OFFSET_X,
                                        self.canvasCorrecion[
                                            0] + 32 * mob.getPosicionY() + 18 + DRAW_CANVAS_OFFSET_Y)))
                            self.root.after(TEXDT, makeCallable(
                                partial(arrastrarImagen, "lifebar:" + str(i_d),
                                        self.world,
                                        32 * mob.getPosicionX() +
                                        self.canvasCorrecion[
                                            1] + 17 + DRAW_CANVAS_OFFSET_X,
                                        32 * mob.getPosicionY() +
                                        self.canvasCorrecion[
                                            0] - 10 + DRAW_CANVAS_OFFSET_Y)))
                            if self.nivel_dificultad == DIFICULTAD_FACIL or self.nivel_dificultad == DIFICULTAD_MEDIO:
                                self.root.after(TEXDT, makeCallable(
                                    partial(arrastrarImagen,
                                            "mob:icon:grupal:" + str(i_d),
                                            self.world,
                                            32 * mob.getPosicionX() +
                                            self.canvasCorrecion[
                                                1] + 27 + DRAW_CANVAS_OFFSET_X,
                                            32 * mob.getPosicionY() +
                                            self.canvasCorrecion[
                                                0] + 26 + DRAW_CANVAS_OFFSET_Y)))
                    except:
                        print lang(328)
                    # Si el mob está encima, abajo, a la derecha o a la
                    # izquierda del jugador // no válido es en diagonal
                    if (abs(mob.getPosicionX() - self.playerPos[
                        0]) == 1 and mob.getPosicionY() == self.playerPos[
                        1]) or \
                            (abs(mob.getPosicionY() - self.playerPos[
                                1]) == 1 and mob.getPosicionX() ==
                                self.playerPos[
                                    0]):
                        self.setCombat(mob, i_d)
                        break
            del mob_id  # borro la matriz de ids
        if self.movement:  # Se ejecuta la funcion nuevamente
            try:
                self.lastmovementId = self.root.after(self.dificultad[5],
                                                      self.moveMobs)  # se establecen los movimientos
            except:
                print lang(363)

    def moveNpc(self):
        """
        Función que mueve a los npc
        :return: void
        """
        try:
            self.root.after_cancel(self.lastnpcmovementid)
        except:
            print lang(564)
        if not self.inNpc and not self.inBattle and self.npcMovement:  # Si no se encuentra interactuando con algo
            # genero una matriz de identificadores para los npc
            npc_id = range(len(self.npc))
            random.shuffle(npc_id)  # desordeno la matriz
            for i_d in npc_id:
                np = self.npc[i_d]
                if np.getMove():
                    x, y = np.moveNpc()
                    # Si el movimiento es valido
                    if 0 <= y < self.mapSize[1] and 0 <= x < self.mapSize[0]:
                        if self.mapLogic[y][
                            x] == "none":  # Si el lugar está vacío
                            if self.maplightning[np.getPosicionY()][
                                np.getPosicionX()] != self.maplightning[y][
                                x]:  # Si cambia la iluminación
                                if self.maplightning[y][x] == 0:
                                    self.world.itemconfig("npc:" + str(i_d),
                                                          image=self.images.image(
                                                              np.getImage() + "_0"))
                                else:
                                    self.world.itemconfig("npc:" + str(i_d),
                                                          image=self.images.image(
                                                              np.getImage() + "_1"))
                            # Actualizo el mapa lógico
                            self.mapLogic[np.getPosicionY()][
                                np.getPosicionX()] = "none"
                            self.mapLogic[y][x] = "npc"
                            np.setPosicionX(x)
                            np.setPosicionY(y)
                        # si la siguiente combinacion está vacía
                        elif self.mapLogic[y][np.getPosicionX()] == "none":
                            if self.maplightning[np.getPosicionY()][
                                np.getPosicionX()] != self.maplightning[y][
                                np.getPosicionX()]:  # Si cambia la iluminación
                                if self.maplightning[y][
                                    np.getPosicionX()] == 0:
                                    self.world.itemconfig("npc:" + str(i_d),
                                                          image=self.images.image(
                                                              np.getImage() + "_0"))
                                else:
                                    self.world.itemconfig("npc:" + str(i_d),
                                                          image=self.images.image(
                                                              np.getImage() + "_1"))
                            # Actualizo el mapa lógico
                            self.mapLogic[np.getPosicionY()][
                                np.getPosicionX()] = "none"
                            self.mapLogic[y][np.getPosicionX()] = "npc"
                            np.setPosicionY(y)
                        # Si el lugar está vacío
                        elif self.mapLogic[np.getPosicionY()][x] == "none":
                            if self.maplightning[np.getPosicionY()][
                                np.getPosicionX()] != \
                                    self.maplightning[np.getPosicionY()][
                                        x]:  # Si cambia la iluminación
                                if self.maplightning[np.getPosicionY()][
                                    x] == 0:
                                    self.world.itemconfig("npc:" + str(i_d),
                                                          image=self.images.image(
                                                              np.getImage() + "_0"))
                                else:
                                    self.world.itemconfig("npc:" + str(i_d),
                                                          image=self.images.image(
                                                              np.getImage() + "_1"))
                            # Actualizo el mapa lógico
                            self.mapLogic[np.getPosicionY()][
                                np.getPosicionX()] = "none"
                            self.mapLogic[np.getPosicionY()][x] = "npc"
                            np.setPosicionX(x)
                        try:  # Se mueve la textura del npc
                            # Movimiento sin animación
                            if not MOVEMENT_ANIMATION[0]:
                                self.world.coords("npc:" + str(i_d),
                                                  18 + 32 * np.getPosicionX() +
                                                  self.canvasCorrecion[1],
                                                  self.canvasCorrecion[
                                                      0] + 32 * np.getPosicionY() + 18)
                            else:  # Movimiento con animación
                                self.root.after(TEXDT, makeCallable(
                                    partial(arrastrarImagen, "npc:" + str(i_d),
                                            self.world,
                                            18 + 32 * np.getPosicionX() +
                                            self.canvasCorrecion[1],
                                            self.canvasCorrecion[
                                                0] + 32 * np.getPosicionY() + 18)))
                        except:
                            pass
            del npc_id
        if self.npcMovement:  # Genero nuevamente el movimiento
            try:
                self.lastnpcmovementid = self.root.after(
                    NPC_TIME_MOVEMENT, self.moveNpc)
            except:
                pass

    def movePlayer(self, direccion, e=None):
        """
        Función para mover al jugador
        :param direccion: Dirección de movimiento
        :param e: Evento
        :return: void
        """

        # Si se puede mover y no está en contacto con un mob y/o npc
        if (
                        not self.inBattle and not self.player.isDead() and not self.inNpc) and self.canmove:
            try:
                self.world.delete("textmsg")
                self.world.delete("textback")
            except:
                pass
            x = self.playerPos[0]
            y = self.playerPos[1]
            if direccion == "down":
                if y < self.mapSize[1] - 1:
                    y += 1
            elif direccion == "up":
                if y > 0:
                    y -= 1
            elif direccion == "left":
                if x > 0:
                    x -= 1
            else:
                if x < self.mapSize[0] - 1:
                    x += 1
            if x != self.playerPos[0] or y != self.playerPos[
                1]:  # Si hubo algún cambio (eso es cuando no se puede mover mas allá de los limites del mapa)
                action = self.mapLogic[y][x]
                logic = action.split(",")[0]
                if logic in AVAIABLE_WALK:  # Si no hay nada en el bloque que sigue
                    self.move(x, y)  # se mueve al jugador
                    self.sonido(self.mapSound[y][x])  # sonido del tile
                elif logic == "mob":  # Si es un mob, comienza la pelea
                    k = 0
                    for mob in self.mobs:  # Se busca el mob que comenzara la batalla
                        if mob.getPosicionX() == x and mob.getPosicionY() == y:  # Si las posiciones coinciden
                            self.setCombat(mob, k)
                            break  # establezco el combate
                        k += 1
                elif logic == "npc":  # Si es un npc comienza la interacción
                    k = 0
                    for npc in self.npc:  # Se busca al npc
                        if npc.getPosicionX() == x and npc.getPosicionY() == y and not npc.isEnded() and npc.canShowByQuest(
                                self.player.getQuest()):
                            self.currentNpc = npc  # objeto currentNpc
                            self.currentNpc.setName(
                                translate(self.currentNpc.getName()))
                            self.currentNpc.setDescripcion(
                                translate(self.currentNpc.getDescripcion()))
                            self.inNpc = True  # comienza la interacción
                            self.npcId = k  # id del npc para borrar despues
                            self.textMsg(self.currentNpc.getName(
                            ) + "\n" + self.currentNpc.getDescripcion(), "npc")
                            self.setInfo(lang(434, self.currentNpc.getName()))
                            self.setInfo(self.currentNpc.getDescripcion())
                        k += 1
                # Si es una puerta o un edificio
                elif logic in ["door", "building", "ladder"]:
                    action = action.split(",")
                    path = action[1]
                    key = action[2]
                    if path != "%NULL%" and path != "%SELF%":  # Si carga un mapa distinto
                        if key == "%NULL%":  # Si no precisa de llaves
                            if logic != "ladder":  # Si no es una escalera carga sonido
                                self.sfx(1)
                            else:
                                self.sfx(38)
                            prevmap = self.player.getMap()  # se obtiene el mapa previo en caso de error
                            self.player.setMap(path)
                            self.setWorld()
                            if self.player.getMap() == "%ERROR_LOADINGMAP%":  # Error inesperado al cargar el mapa (se devuelve)
                                self.player.setMap(prevmap)
                                self.setWorld()
                            self.static.addDoor()
                        else:  # Si necesita de una llave para abrir
                            opened = False  # booleano para comprobar si se abrió la puerta
                            im = 0
                            for k in self.player.getItems():  # Se revisan los items del jugador por las llaves
                                if "key" in k.getType():  # Si el jugador posee una llave
                                    if k.getName() == key:  # Si tiene la llave necesaria
                                        self.sfx(36)
                                        self.static.addDoor()
                                        prevmap = self.player.getMap()
                                        # se define el mapa actual del jugador
                                        self.player.setMap(path)
                                        self.setWorld()  # se carga el mapa definido
                                        # se bota la llave usada
                                        self.player.dropObject(im)
                                        if self.player.getMap() == "%ERROR_LOADINGMAP%":
                                            self.player.setMap(prevmap)
                                            self.setWorld()
                                        opened = True  # se realizó el proceso
                                        self.dibujarItems()  # se dibujan los items
                                        break  # termina de buscar llaves
                                im += 1
                            if not opened:  # Si la llave no se encuentra
                                self.sfx(2)
                                if "door" in action:
                                    self.setInfo(lang(65, translate(key)))
                                    self.textMsg(
                                        lang(65, translate(key)), "normal")
                                else:
                                    self.setInfo(lang(66, translate(key)))
                                    self.textMsg(
                                        lang(66, translate(key)), "normal")
                    elif path == "%SELF%":  # Si es una puerta al mismo mapa
                        if key == "%NULL%":  # Si no requiere de llaves
                            self.sfx(1)
                            self.world.delete("item:" + str(x) + "," + str(y))
                            self.move(x, y)
                            self.static.addDoor()
                            # se elimina la textura
                            self.mapItemsTextures[y][x] = None
                        else:  # Si requiere de una llave
                            opened = False  # booleano para comprobar si se abrio la puerta
                            im = 0
                            for k in self.player.getItems():  # Se revisan los items del jugador por las llaves
                                if "key" in k.getType():  # Si el jugador posee una llave
                                    if k.getName() == key:  # Si tiene la llave necesaria
                                        self.sfx(36)  # sonido de puerta
                                        self.static.addDoor()
                                        self.world.delete(
                                            "item:" + str(x) + "," + str(y))
                                        self.move(x, y)  # se mueve el jugador
                                        # se bota la llave usada
                                        self.player.dropObject(im)
                                        self.dibujarItems()  # se dibujan los items
                                        opened = True  # se realizo el proceso
                                        # se elimina la textura
                                        self.mapItemsTextures[y][x] = None
                                        break  # termina de buscar llaves
                                im += 1
                            if not opened:  # Si no se encuentra
                                self.sfx(2)
                                self.setInfo(lang(65, translate(key)), )
                                self.textMsg(
                                    lang(65, translate(key)), "normal")
                elif logic == "text":  # Si hay un texto
                    text = translate(putStrict(action.split(",")[1]))
                    self.setInfo(lang(67, text))
                    self.move(x, y)
                    self.textMsg(text, "text")
                elif logic == "sign":  # Si es un signo
                    text = translate(putStrict(action.split(",")[1]))
                    self.static.addCarteles()
                    self.setInfo(lang(choice([291, 292, 293, 294]), text))
                    self.sfx(31)
                    self.textMsg(text, "sign")
                elif logic == "nopass":  # Si el evento es no pasar
                    pass
                elif logic in ["plushp", "plusmana", "minushp",
                               "minusmana"]:  # Si hay un minushp, minusmana, plushp, plusmana
                    self.move(x, y)  # se mueve al jugador
                    # se obtiene la accion a realizar
                    event = action.split(",")[0]
                    # se obtiene el cambio que se realizara
                    cambio = action.split(",")[1]
                    porcentual = False  # si el cambio es porcentual
                    if "%" in cambio:  # Se pasa del porcentaje a un valor neto
                        porcentual = True
                        cambio = cambio.replace("%", "")
                        cambio = float(cambio) / 100
                    else:
                        cambio = int(cambio)
                    if event == "plushp":  # Aumenta el hp
                        if porcentual:
                            self.playerText(
                                "+" + action.split(",")[1], "verde")
                            self.setInfo(lang(68, action.split(",")[1]))
                            self.player.setDamage(
                                int(self.player.getDamage() * cambio))
                        else:
                            dam = max(0, self.player.getDamage() - cambio)
                            self.player.setDamage(dam)
                            self.setInfo(lang(69, str(dam)))
                            self.playerText("+" + str(dam), "verde")
                        self.sonidoFx(SOUND_ALERT + "new_level.wav")
                        self.textMsg(lang(454))
                    elif event == "plusmana":  # Aumenta el mana
                        if porcentual:
                            self.setInfo(lang(70, str(cambio)))
                            self.playerText("+" + str(cambio), "azul")
                            self.player.increaseMana(int(cambio))
                        else:
                            self.setInfo(lang(71, str(cambio)))
                            self.playerText("+" + str(cambio), "azul")
                            self.player.increaseMana(cambio)
                        self.sonidoFx(SOUND_ALERT + "new_level.wav")
                        self.textMsg(lang(455))
                    elif event == "minushp":  # Disminuye el HP
                        if porcentual:
                            hp = self.player.getDamage() * (cambio + 1)
                            if hp >= self.player.getActualMaximumLife():
                                hp = self.player.getActualMaximumLife() - 1
                            self.setInfo(lang(72, action.split(",")[1]))
                            self.playerText("-" + str(hp))
                            self.player.setDamage(int(hp))
                        else:
                            self.player.setDamage(
                                self.player.getDamage() + cambio)
                            if self.player.isDead():
                                self.player.setDamage(
                                    self.player.getActualMaximumLife() - 1)
                            self.setInfo(lang(73, str(cambio)))
                            self.playerText("-" + str(cambio), "rojo", True)
                        self.sonidoFx(SOUND_ALERT + "notificacion_2.wav")
                        self.textMsg(lang(456))
                    elif event == "minusmana":  # Disminuye el mana
                        if porcentual:
                            self.setInfo(lang(74, str(cambio * 100)))
                            self.playerText("-" + str(cambio * 100))
                            self.player.decreaseMana(int(cambio))
                        else:
                            self.player.decreaseMana(cambio)
                            self.setInfo(lang(75, str(cambio)))
                            self.playerText("-" + str(cambio))
                        self.sonidoFx(SOUND_ALERT + "notificacion_2.wav")
                        self.textMsg(lang(457))
                    self.updateInfoPlayer()  # se actualizan los estados
                elif logic == "moveto":  # Si el evento es moverse
                    def _allowmove():
                        self.canmove = True

                    # Se escoje la coordenada de viaje
                    coords = action.split(",")
                    self.mapLogic[y][x] = "none"
                    self.mapLogic[self.playerPos[1]][
                        self.playerPos[0]] = "none"
                    self.playerPos[0] = int(coords[1])
                    self.playerPos[1] = int(coords[2])
                    self.move(self.playerPos[0], self.playerPos[1])
                    self.sonido(SOUND_EFFECT + "move.wav")
                    self.canmove = False
                    # se permite el movimiento tras medio segundo
                    self.root.after(500, _allowmove)
                elif logic == "object":  # Si el evento es un objeto
                    objeto = action.split(",")[1]
                    object_prop = objeto.split(ITEMSEPARATOR)
                    self.move(x, y)
                    if object_prop[5] == "True":  # Si el objeto era stackable
                        self.setInfo(lang(76, str(object_prop[6]), translate(
                            str(object_prop[0]))).lower())
                    else:
                        self.setInfo(lang(77, translate(str(object_prop[0]))))
                    self.sfx(37)
                    self.player.addObject(Item(parseObject(objeto)))
                    self.playerText("+" + lang(143), "blanco", True)
                    self.dibujarItems()
                    self.textMsg(lang(choice([458, 459, 460, 461, 462])))
                elif logic == "teleport":  # Teletransportación
                    mapa = action.split(",")[1]
                    prevmap = self.player.getMap()
                    self.player.setMap(mapa)
                    self.setWorld()
                    if self.player.getMap() == "%ERROR_LOADINGMAP%":  # Si ocurre un error al cargar el mapa
                        self.player.setMap(prevmap)
                        self.setWorld()
                elif logic == "sound":  # Se reproduce un sonido
                    try:
                        self.sonidoFx(LEVEL_SOUND + action.split(",")[1])
                    except:
                        print lang(328)
                    self.move(x, y)
                elif logic == "mute":  # Se paran todos los sonidos
                    self.stopSound()
                    self.move(x, y)
                elif logic == "bed":  # si el evento es una cama
                    # mensaje al usuario
                    self.setInfo(lang(choice([295, 296, 297, 298, 299, 300])))
                    self.textMsg(lang(choice([295, 296, 297, 298, 299, 300])))
                    if self.nivel_dificultad in [DIFICULTAD_FACIL,
                                                 DIFICULTAD_MEDIO]:  # si la dificultad es fácil / medio se lleva el mana y la vida al máximo
                        self.player.setMaxMana()
                        self.player.setMaxLife()
                        self.setInfo(lang(91))
                        self.sfx(16)
                    else:
                        # mensaje al usuario (de que no subio nada)
                        self.setInfo(lang(choice([301, 302, 303])))
                    # la cama ha sido usada (se establece)
                    self.mapLogic[y][x] = "used_bed"
                elif logic == "used_bed":  # Si el evento es una cama usada
                    # mensaje al usuario (cama ya usada)
                    self.setInfo(lang(choice([304, 305, 306, 307])))
                    self.textMsg(lang(choice([304, 305, 306, 307])))
                    self.sfx(37)  # sonido de alerta
                elif logic == "longtext":  # Se carga un texto largo, similar a un libro
                    self.textMsg(lang(choice([463, 464, 465, 466, 467])))
                    self.sfx(37)
                    self.setInfo(lang(78))
                    self.move(x, y)
                    try:
                        k = pop([lang(79), self.images.image("text_icon"),
                                 "longtext", 400, 600,
                                 LEVELS_RES + action.split(",")[1],
                                 self.player.getName()])
                        k.w.mainloop(1)
                        del k
                    except:
                        print lang(355)
                elif logic == "autosave":  # Autoguardado
                    self.textMsg(lang(choice([468, 469, 470, 471, 472, 473])))
                    self.sfx(31)
                    self.move(x, y)
                    self.saveGame("autosave")
                    self.setInfo(lang(80))
                elif logic == "suddendeath":  # Muerte súbita
                    self.world.delete("player")
                    self.textMsg(lang(choice([474, 475, 476, 477, 478, 479])))
                    self.setInfo(lang(81))
                    self.setInfo(lang(82))
                    self.sfx(29)
                    e = pop([[lang(82), lang(173)], self.images.image(
                        "iconmuerte"), "aviso", 85, 270, lang(83)])
                    e.w.mainloop(1)
                    del e
                    self.abortGame()
                elif logic == "nopassalert":  # No pasar con alerta de sonido
                    self.sfx(37)
                    self.setInfo(lang(choice([84, 85, 315, 316, 317])))
                    self.textMsg(
                        lang(choice([451, 452, 453, 480, 481, 482, 483])))
        elif self.inNpc:
            self.setInfo(lang(choice([592, 593, 594, 595])))
        elif self.inBattle:
            if self.tipoCombate == MODE_FIGHT_NORMAL:  # Si el tipo de combate es normal
                self.setInfo(lang(choice([596, 597, 598, 599, 600])))

    def moverListaItems(self, direccion):
        """
        Función que mueve las páginas cambiando el parámetro de paginado
        :param direccion: Dirección de movimiento
        :return: void
        """
        if direccion == "left" and self.itemnumberlist > 0:
            self.itemnumberlist -= 20  # página anterior
        else:
            self.itemnumberlist += 20  # página siguiente
        self.dibujarItems()  # se dibujan los items

    # TODO:Conectarse al multiplayer
    def multiplayer_connect(self):
        """
        Conectar a un servidor
        :return: void
        """
        if self.ingame:
            if not self.inBattle:
                if not self.inNpc:
                    if not self.multiplayer_isconected:  # Si no está conectado a un servidor
                        ventana = pop(
                            [[lang(774), lang(775), lang(776), lang(777),
                              lang(778), lang(779), lang(780), lang(781)],
                             self.images.image("server_icon"),
                             "server_connect", 100, 290, DATA_CONFIG])
                        ventana.w.mainloop(1)
                        if ventana.sent:
                            try:
                                self.world.config(cursor="wait")
                                self.root.config(cursor="wait")
                                print lang(791),
                                self.multiplayer_me, self.multiplayer_me_conn = connect_server(
                                    ventana.values[0],
                                    ventana.values[1])
                                self.multiplayer_isconected = True
                                self.multiplayer_server = str(
                                    ventana.values[0]) + ":" + str(
                                    ventana.values[1])
                                self.setInfo(lang(792, ventana.values[
                                    0], str(ventana.values[1])), True)
                                print lang(310)
                            except:
                                print lang(398)
                                print lang(793)
                                self.multiplayer_desconnect(False, True)
                                self.setInfo(lang(804))
                                # no se pudo conectar a un servidor
                                self.error(lang(790), 70, 300, "server_error")
                            self.world.config(cursor='arrow')
                            self.root.config(cursor='arrow')

                            if self.multiplayer_isconected:  # Se obtienen los lobby del juego
                                # Inserto un lobby nulo
                                data = simplejson.dumps(
                                    [self.multiplayer_lobby,
                                     self.player.getName(),
                                     self.player.getMap()])
                                self.multiplayer_me_conn.send(data)
                                self.multiplayer_joinLobby()
                    else:
                        # ya se encuentra conectado a un servidor
                        self.error(lang(770), 70)
                else:
                    # se encuentra interactuando con un npc
                    self.error(lang(819), 82)
            else:
                self.error(lang(818), 82)  # se encuentra en una batalla

    # TODO:Desconectarse del multiplayer
    def multiplayer_desconnect(self, abort=False, error=False):
        """
        Desconectar de un servidor
        :param abort: Boolean
        :param error: Boolean
        :return: void
        """
        delMatrix(self.multiplayer_players)
        delMatrix(self.multiplayer_players_id)
        self.multiplayer_isconected = False
        self.multiplayer_lobby = "null"
        self.multiplayer_me, self.multiplayer_me_conn = NULL_CONECTION
        self.multiplayer_players = []
        self.multiplayer_players_id = []
        if abort:
            self.abortGame()
        if not error:
            self.setInfo(lang(803, self.multiplayer_server))
        self.multiplayer_server = "0.0.0.0:0"

    # TODO:Unirse a lobby
    def multiplayer_joinLobby(self):
        """
        Unirse a una partida multijugador
        :return: void
        """
        if self.multiplayer_isconected and self.ingame:  # Si está conectado
            data = simplejson.loads(self.multiplayer_me_conn.recv(2000))
            if len(data) != 0:  # Si existen entradas en el servidor
                ventana = pop(
                    [[lang(805), lang(806), lang(807), lang(808), lang(809),
                      lang(810), lang(811), lang(812), lang(813),
                      lang(54), lang(814), lang(817)],
                     self.images.image("door_in"), "server_joinlobby", 110,
                     330, data])
                ventana.w.mainloop(1)
                if ventana.sent:
                    if ventana.values[0] == "disconnect":
                        self.multiplayer_desconnect(False, False)
                    elif ventana.values[0] == "connect":
                        lobbyid = ventana.values[1]
                        if lobbyid in data.keys():
                            datalobby = data[lobbyid]
                            self.multiplayer_lobby = datalobby[0]
                            self.setInfo(lang(816, self.multiplayer_lobby))
                        else:
                            self.multiplayer_desconnect(False, True)
                            self.error(lang(815), 82)
                    elif ventana.values[0] == "create":
                        ventana1 = pop(
                            [[lang(808), lang(225), lang(820), lang(54)],
                             self.images.image("server_add"),
                             "server_create", 42, 280])
                        ventana1.w.mainloop(1)
                        if ventana1.sent:
                            if ventana.values[0] == "disconnect":
                                self.multiplayer_desconnect(False, False)
                            else:
                                try:
                                    lobbyname = ventana1.values[0]
                                    self.multiplayer_lobby = lobbyname
                                    newdata = simplejson.dumps(
                                        [self.multiplayer_lobby,
                                         self.player.getName(),
                                         self.player.getMap()])
                                    self.multiplayer_me_conn.send(newdata)
                                    self.setInfo(
                                        lang(822, self.multiplayer_lobby))
                                    self.setInfo(
                                        lang(816, self.multiplayer_lobby))
                                except:
                                    self.multiplayer_desconnect(False, False)
                                    self.error(
                                        lang(821))  # error al crear el lobby
                        del ventana1
                else:
                    self.multiplayer_desconnect(False, False)
                del ventana

    # TODO:Subir y actualizar jugadores del lobby
    def multiplayer_update(self):
        """
        Actualizar los datos del servidor
        :return: void
        """
        if self.multiplayer_isconected and self.ingame:  # Se ejecuta la funcion nuevamente
            try:
                # se borra el ultimo elemento
                self.root.after_cancel(self.lastmultiplayerId)
            except:
                print lang(823)
            # try: self.lastmovementId = self.root.after(self.dificultad[5], self.moveMobs)  # se establecen los movimientos
            # except: print lang(363)
            pass

    def newGame(self, e=None):
        """
        Función que genera una nueva partida
        :param e: Evento
        :return: void
        """
        if not self.isNewGameCreating:  # Si no hay otra ventana de creación abierta
            if self.multiplayer_isconected:  # Si el jugador está conectado a un servidor
                v = pop([[lang(795), lang(799), lang(797), lang(239)],
                         self.images.image("server_disconnect"),
                         "deseaDesconectarse",
                         75, 335, CONFIGURATION_DATA[
                             1]])  # Se consulta si cerrar o no la sesión activa
                v.w.mainloop(1)
                if v.sent:  # Se procede en función de la respuesta
                    if v.values[0] == "si":
                        print lang(798),
                        try:
                            self.multiplayer_desconnect(False)
                            print lang(310)
                        except:
                            print lang(398)
                    elif v.values[0] == "cancel":
                        del v
                        return
                del v
            self.isNewGameCreating = True
            if isWindows():
                _sizex = 354
                _sizey = 242
            else:
                _sizex = 455
                _sizey = 270
            ventana = pop(
                [[lang(46), lang(224), lang(225), lang(226), lang(227),
                  lang(228), lang(229), "[Fácil/Medio/Difícil]",
                  lang(245).replace(
                      ":", ""), "[Guerrero/Mago/Skaard/Ugraar]", lang(233),
                  lang(781), lang(782),
                  lang(783),
                  lang(784), lang(785), lang(786)],
                 self.images.image("new_user_icon"), "new_game", _sizey,
                 _sizex])
            ventana.w.mainloop(1)
            if ventana.sent:  # Si la ventana se envió
                try:  # Empiezo a crear la nueva partida
                    self.abortGame("newgame")  # aborto el juego
                    print lang(603),
                    info = ventana.values  # cargo la información
                    self.player.setType(info[4])  # tipo de jugador
                    self.player.setEdad(info[2])  # edad
                    self.player.setName(info[0])  # nombre
                    self.player.setPais(info[1])  # país
                    self.player.setLevel(1)  # nivel
                    self.player.setMaxMana()  # se define el nivel de mana máximo para el nivel 1
                    self.player.setMaxLife()  # se define la máxima vida para su nivel
                    # se establece la experiencia en 0
                    self.player.setExperience(0)
                    self.player.setAttack()  # defino el ataque
                    self.player.setDefensa()  # defino la defensa
                    self.player.setMaxExpLevel()  # defino el máximo nivel de experiencia del nivel 1
                    # nombre a los poderes
                    self.activePowers[0] = self.player.getName()
                    # cargo el mapa principal
                    self.player.setMap(DEFAULT_LEVEL)
                    self.nivel_dificultad = info[3]  # cargo la dificultad
                    self.setDificultad()  # establezco la dificultad
                    # Agrego items caracteristicos
                    if self.player.getType() == "guerrero":  # Si el tipo es guerrero
                        self.player.addObject(Item(ITEMS[73]))
                        self.player.addObject(Item(ITEMS[56]))
                    else:
                        self.player.addObject(Item(ITEMS[39]))
                        for w in range(25):  # @UnusedVariable
                            self.player.addObject(Item(ITEMS[24]))
                    self.ingame = True  # indica que el mundo se ha cargado
                    self.setWorld()  # cargo el mundo inicial
                    self.setInfo(lang(50))  # mensajes al jugador de bienvenida
                    self.setInfo("", False)
                    self.setInfo(lang(51), False)
                    self.setInfo(lang(49), False)
                    self.update()  # se actualiza la UI
                    self.sfx(30)  # se carga el sonido de comienzo
                    editorkey = base64.b64encode(
                        md5.new(
                            self.player.getName()).digest())  # se comprueba si el jugador es editor o no
                    if editorkey == "NEp/Qn+3ZWEO+W63vOlSVw==" or editorkey == "Y/sQiCQbCs3XmHrwwfT35g==":
                        self.player.setEditor()
                    self.menu.pack(side=LEFT, fill=Y)
                    self.menu2.pack(side=LEFT)
                    self.content.pack()
                    self.initialBg.pack_forget()
                    if CONFIGURATION_DATA[12]:
                        self.archivomenu.entryconfig(2, state=NORMAL)
                    self.archivomenu.entryconfig(3, state=NORMAL)
                    self.vermenu.entryconfig(0, state=NORMAL)
                    self.vermenu.entryconfig(1, state=NORMAL)
                    self.vermenu.entryconfig(2, state=NORMAL)
                    self.vermenu.entryconfig(3, state=NORMAL)
                    self.vermenu.entryconfig(4, state=NORMAL)
                except:  # Error al crear la nueva partida
                    print lang(398)
                    print lang(604)
                    self.isNewGameCreating = False  # termina el estado creativo
                    self.ingame = False
                    self.abortGame()
                    self.error(lang(605))
                    return
            self.isNewGameCreating = False  # termina el estado creativo
            del ventana

    # TODO: Interacción con NPC
    def npcInteract(self, action, e=None):
        """
        Interactuar con un npc
        :param action: Acción del npc
        :param e: Event
        :return: void
        """
        if self.ingame:  # Si hay un juego en proceso
            if self.inNpc:  # Si hay un npc en proceso
                try:
                    line = self.currentNpc.getCurrentString()  # obtengo el string
                    adv = True
                    if line != "{end}":
                        if action == "yes":
                            if "{yes}" in line:
                                line = translate(line.replace(
                                    "{yes}", "").split("%"))
                                self.textMsg(line[0], "normal")
                                self.setInfo(
                                    lang(436, self.currentNpc.getName(),
                                         line[0]))
                            else:
                                adv = False
                        elif action == "no":
                            if "{no}" in line:
                                line = line.replace("{no}", "")
                                line = translate(line.replace(
                                    "{yes}", "").split("%"))
                                self.textMsg(line[1], "normal")
                                self.setInfo(
                                    lang(436, self.currentNpc.getName(),
                                         line[1]))
                            else:
                                adv = False
                        elif action == "accept":  # Avanzar en el string
                            if "{yes}" in line or "{no}" in line:
                                adv = False
                            else:
                                def _quest():
                                    line = translate(line.replace(
                                        "{setquest ", "").replace("}", ""))
                                    self.setInfo(
                                        lang(choice(
                                            [571, 575, 577, 578, 579, 580])))
                                    self.world.delete("textmsg")
                                    self.world.delete("textback")
                                    self.playerText(
                                        "+" + lang(576), "blanco", True)
                                    self.player.addQuest(line)

                                if line == "{give}":  # Si se da un objeto al jugador
                                    if self.currentNpc.getObject() != "%NULL%":
                                        self.static.addObj()
                                        self.player.addObject(Item(parseObject(
                                            self.currentNpc.getObject())))  # Se agrega nuevo objeto al jugador
                                        self.dibujarItems()
                                        self.setInfo(
                                            lang(435,
                                                 self.currentNpc.getName()))
                                        self.playerText(
                                            "+" + lang(143), "blanco", True)
                                        if not self.currentNpc.getStringAmount() == self.currentNpc.getCount():
                                            self.currentNpc.addCount()
                                            line = translate(
                                                self.currentNpc.getCurrentString())
                                            self.textMsg(line, "normal")
                                            self.setInfo(
                                                lang(436,
                                                     self.currentNpc.getName(),
                                                     line))
                                # Si se pide un objeto al jugador
                                elif line == "{request}":
                                    object_id = self.currentNpc.getRequest()
                                    if object_id.isdigit():
                                        object_id = int(object_id)
                                        finded = False
                                        k = 0
                                        for obj in self.player.getItems():
                                            if obj.getId() == object_id:
                                                finded = True
                                                break
                                            k += 1
                                        if finded:
                                            req = self.player.getItem(k)
                                            self.textMsg(
                                                lang(560,
                                                     translate(req.getName())))
                                        else:
                                            self.textMsg(
                                                lang(choice([561, 562])))
                                            self.inNpc = False
                                            self.npcId = -1
                                            self.currentNpc = None
                                elif ("{setquest" in line) and ("}" in line):
                                    line = translate(line.replace(
                                        "{setquest ", "").replace("}", ""))
                                    self.setInfo(
                                        lang(choice(
                                            [571, 575, 577, 578, 579, 580])))
                                    self.world.delete("textmsg")
                                    self.world.delete("textback")
                                    self.playerText(
                                        "+" + lang(576), "blanco", True)
                                    self.player.addQuest(line)
                                    self.static.addQuest()
                                elif "{follower" in line:
                                    line = translate(line.replace(
                                        "{follower ", "").replace("}",
                                                                  "").split(
                                        " "))
                                    tipo = line[0].upper()
                                    cant = line[1].strip()
                                    if cant.isdigit():  # Si la cantidad de followers es numérica
                                        cant = int(cant)
                                        if tipo == "LIV":
                                            self.player.addLightFriend(cant)
                                        elif tipo == "MED":
                                            self.player.addMediumFriend(cant)
                                        elif tipo == "STR":
                                            self.player.addStrongFriend(cant)
                                        else:
                                            print lang(714)
                                        if tipo == "LIV" or tipo == "MED" or tipo == "STR":
                                            self.setInfo(lang(715, str(cant)))
                                            self.textMsg(
                                                lang(choice(
                                                    [716, 717, 718, 719,
                                                     720])))
                                            self.playerText(
                                                "+" + lang(721), "naranja",
                                                True, False)
                                            self.static.addFollower(cant)
                                        if not self.currentNpc.getStringAmount() == self.currentNpc.getCount():
                                            self.currentNpc.addCount()
                                            line = translate(
                                                self.currentNpc.getCurrentString())
                                            self.textMsg(line, "normal")
                                            self.setInfo(
                                                lang(436,
                                                     self.currentNpc.getName(),
                                                     line))
                                    else:
                                        print lang(713)
                                else:
                                    line = translate(line)
                                    self.textMsg(line, "normal")
                                    self.setInfo(
                                        lang(436, self.currentNpc.getName(),
                                             line))
                                    try:
                                        if "{setquest" in self.currentNpc.NextString():
                                            self.currentNpc.addCount()
                                            line = self.currentNpc.getCurrentString()  # obtengo el string
                                            line = translate(line.replace(
                                                "{setquest ", "").replace("}",
                                                                          ""))
                                            self.setInfo(
                                                lang(choice(
                                                    [571, 575, 577, 578, 579,
                                                     580])))
                                            self.playerText(
                                                "+" + lang(576), "blanco",
                                                True, True)
                                            self.player.addQuest(line)
                                            self.static.addQuest()
                                    except:
                                        pass
                        else:
                            adv = True
                    if adv:  # Si termina el diálogo con el npc
                        if (
                                            self.currentNpc.getStringAmount() == self.currentNpc.getCount() and self.npcId >= 0 and adv) or line == "{end}":
                            def _setnonpc():  # Elimina al npc activo
                                self.inNpc = False
                                self.npcId = -1

                            self.static.addNpc()
                            if self.currentNpc.isFade():
                                self.mapLogic[self.currentNpc.getPosicionY()][
                                    self.currentNpc.getPosicionX()] = "none"
                                # elimino al npc de las matrices
                                self.npc.pop(self.npcId)
                                self.root.after(
                                    SHOWMESSAGESTIME / 2, self.dibujarMundo)
                                self.root.after(
                                    SHOWMESSAGESTIME / 2, _setnonpc)
                            else:
                                def _delnpc():
                                    self.dibujarMundo()
                                    self.moveNpc()  # elimina al npc

                                self.currentNpc.end()
                                self.root.after(
                                    SHOWMESSAGESTIME / 2, _setnonpc)
                                if "{setquest" in self.currentNpc.getStrings():
                                    self.root.after(SHOWMESSAGESTIME / 2,
                                                    _delnpc)
                            self.currentNpc = None
                        else:
                            self.currentNpc.addCount()
                except AttributeError:
                    pass

    def playerText(self, msg, c="rojo", player=True, bold=True):
        """
        Función que escribe un mensaje sobre el jugador (o enemigo) y lo borra al segundo
        :param msg: String
        :param c: Color
        :param player: Jugador o enemigo
        :param bold: Bold
        :return: void
        """
        if not self.tipoCombate == MODE_FIGHT_GROUP:
            if c == "azul":
                color = "#0000ff"
            elif c == "blanco":
                color = "#ffffff"
            elif c == "morado":
                color = "#9400D3"
            elif c == "naranja":
                color = "#FF8C00"
            elif c == "rojo":
                color = "#ff0000"
            elif c == "verde":
                color = "#48db0f"
            else:
                color = c
            try:
                if bold:
                    if player:
                        msgid = self.world.create_text(
                            self.playerPos[0] * 32 + self.canvasCorrecion[
                                1] + 22,
                            self.playerPos[1] * 32 + self.canvasCorrecion[
                                0] + 3, text=msg,
                            fill=color, font=self.fonts[3])
                    else:
                        msgid = self.world.create_text(
                            self.enemy.getPosicionX() * 32 +
                            self.canvasCorrecion[1] + 22,
                            self.enemy.getPosicionY() * 32 +
                            self.canvasCorrecion[
                                0] + 3,
                            text=msg, fill=color, font=self.fonts[3])
                    if msg.replace("+", "").replace("-", "").isdigit():
                        self.root.after(PLAYER_TEXT_TIME,
                                        lambda: self.world.delete(
                                            msgid))  # se borra el mensaje tras medio segundo
                    else:
                        self.root.after(PLAYER_TEXT_TIME * 3,
                                        lambda: self.world.delete(msgid))
                else:
                    if player:
                        msgid = self.world.create_text(
                            self.playerPos[0] * 32 + self.canvasCorrecion[
                                1] + 22,
                            self.playerPos[1] * 32 + self.canvasCorrecion[
                                0] + 3, text=msg,
                            fill=color, font=self.fonts[2])
                    else:
                        msgid = self.world.create_text(
                            self.enemy.getPosicionX() * 32 +
                            self.canvasCorrecion[1] + 22,
                            self.enemy.getPosicionY() * 32 +
                            self.canvasCorrecion[
                                0] + 3,
                            text=msg, fill=color, font=self.fonts[2])
                    if msg.replace("+", "").replace("-", "").isdigit():
                        self.root.after(PLAYER_TEXT_TIME,
                                        lambda: self.world.delete(
                                            msgid))  # se borra el mensaje tras medio segundo
                    else:
                        self.root.after(PLAYER_TEXT_TIME * 3,
                                        lambda: self.world.delete(msgid))
                self.world.update()
            except:
                print lang(367)

    def salir(self, e=None):
        """
        Función para salir del juego
        :param e: Event
        :return: void
        """
        print lang(402),
        if (
                            self.ingame and e != "command" and not self.inBattle and not self.inNpc) and \
                CONFIGURATION_DATA[
                    12]:  # Si hay una partida en curso y no está en una batalla
            # Si está habilitado guardar al salir
            if CONFIGURATION_DATA[2] and self.namePartida != "":
                print lang(403)
                self.saveGame("exit")
            else:  # Si no está habilitado guardar al salir
                e = pop(
                    [[lang(64), lang(236), lang(237), lang(238), lang(239)],
                     self.images.image("save_icon"),
                     "deseaGuardar",
                     75, 250, CONFIGURATION_DATA[
                         1]])  # Se pregunta si quiere guardar o no
                e.w.mainloop(1)
                if e.sent:  # Se procede en función de la respuesta
                    if e.values[0] == "si":
                        print lang(403)
                        self.saveGame("exit")
                    elif e.values[0] == "no":
                        print lang(310)
                    else:
                        print lang(398)
                        return
                del e
        else:
            print lang(310)
        print lang(745),
        print "",
        if self.multiplayer_isconected:
            self.multiplayer_desconnect(False)
        if isWindows():
            os.system("taskkill /PID " + str(os.getpid()) + " /F")
        else:
            import signal

            os.kill(os.getpid(), signal.SIGKILL)  # @UndefinedVariable

    def saveGame(self, tipo=None):
        """
        Función que guarda una partida
        :param tipo: Tipo de guardado
        :return: void
        """
        if (self.ingame and not self.player.isDead()) and CONFIGURATION_DATA[
            12]:  # Si se esta jugando (esto evita que se pueda guardar sin hacer nada
            if not self.inBattle and not self.inNpc:  # Si no se encuentra peleando ni interactuando con un npc
                nameSav = ""
                continuar = False
                # Si no se ha cargado (es una nueva partida) se pregunta por un
                # nombre
                if not self.loaded:
                    ventana = pop([[lang(60), lang(234), lang(235), lang(64),
                                    lang(781), lang(787), lang(788)],
                                   self.images.image("save_icon"),
                                   "save_game_name", 120, 280])
                    ventana.w.mainloop(1)
                    if ventana.sent:
                        nameSav = ventana.values[0]
                        continuar = True
                        self.namePartida = nameSav
                    del ventana
                else:
                    nameSav = self.namePartida
                    continuar = True
                if len(nameSav) > 0 and continuar:  # Si está listo
                    nameSav = nameSav.replace(u"\ufeff",
                                              "")  # reemplazo caracteres no válidos para el nombre del archivo
                    self.static.addJuegosGuardados()
                    archivo = open(DATA_SAVES + nameSav + ".sav",
                                   "w")  # se abre el archivo
                    try:  # Información del jugador
                        print lang(418),
                        archivo.write(nameSav.decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getName()).decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getEdad()).decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getPais()).decode('utf-8') + "\n")
                        archivo.write(
                            self.nivel_dificultad.decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getDamage()).decode(
                                'utf-8') + "\n")
                        archivo.write(
                            str(self.player.getExperience()).decode(
                                'utf-8') + "\n")
                        archivo.write(
                            str(self.player.getInfo()).decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getLevel()).decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getLinkImage()).decode(
                                'utf-8') + "\n")
                        archivo.write(
                            str(self.player.getMana()).decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getMap()).decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getType()).decode('utf-8') + "\n")
                        archivo.write(
                            str(self.player.getVelocidad()).decode(
                                'utf-8') + "\n")
                        archivo.write(str(self.playerPos[0]) + "\n")
                        archivo.write(str(self.playerPos[1]) + "\n")
                        archivo.write(str(self.itemnumberlist) + "\n")
                        archivo.write(str(self.player.getFriends()) + "\n")
                        if self.player.getActiveBullet() is not None:
                            archivo.write(
                                str(self.player.getActiveBullet().export()))
                        else:
                            archivo.write("%NULL%\n")
                        if self.player.getFirstPower() is not None:
                            archivo.write(
                                str(self.player.getFirstPower()) + "\n")
                        else:
                            archivo.write("%NULL%\n")
                        if self.player.getSecondPower() is not None:
                            archivo.write(
                                str(self.player.getSecondPower()) + "\n")
                        else:
                            archivo.write("%NULL%\n")
                        print lang(310)
                    except:  # Error al guardar la información básica del jugador
                        print lang(398)
                        print lang(339)
                        self.setInfo(lang(63))
                        self.error(lang(151))
                        return
                    try:  # Información de las armas
                        print lang(419),
                        archivo.write("#weapons#\n")
                        try:
                            archivo.write(
                                self.player.getLeftWeapon().export().decode(
                                    'utf-8'))
                        except:
                            archivo.write("%NULL%\n")
                        try:
                            archivo.write(
                                self.player.getRightWeapon().export().decode(
                                    'utf-8'))
                        except:
                            archivo.write("%NULL%\n")
                        print lang(310)
                    except:  # Error al escribir la información de las armas
                        print lang(398)
                        print lang(338)
                        self.setInfo(lang(63))
                        self.error(lang(152))
                        return
                    try:  # Información de la armadura
                        print lang(420),
                        archivo.write("#armor#\n")
                        try:
                            archivo.write(
                                self.player.getCasco().export().decode(
                                    'utf-8'))
                        except:
                            archivo.write("%NULL%\n")
                        try:
                            archivo.write(
                                self.player.getChaleco().export().decode(
                                    'utf-8'))
                        except:
                            archivo.write("%NULL%\n")
                        try:
                            archivo.write(
                                self.player.getPantalones().export().decode(
                                    'utf-8'))
                        except:
                            archivo.write("%NULL%\n")
                        try:
                            archivo.write(
                                self.player.getBotas().export().decode(
                                    'utf-8'))
                        except:
                            archivo.write("%NULL%\n")
                        print lang(310)
                    except:  # Error al escribir la información de la armadura
                        print lang(398)
                        print lang(337)
                        self.setInfo(lang(63))
                        self.error(lang(153))
                        return
                    try:  # Items del jugador
                        print lang(421),
                        archivo.write("#items#\n")
                        for item in self.player.getItems()[::-1]:
                            archivo.write(item.export().decode('utf-8'))
                        archivo.write("#end#\n")
                        archivo.close()
                        print lang(310)
                    except:  # Error al escribir los items del jugador
                        print lang(398)
                        print lang(336)
                        self.setInfo(lang(63))
                        self.error(lang(154))
                        return
                    try:  # Quest del jugador
                        print lang(569),
                        archivo14 = open(DATA_SAVES + nameSav + ".quest", "w")
                        archivo14.write("#quest#\n")
                        if self.player.hasQuest():  # Si existen quest para guardar
                            for quest in self.player.getQuest()[::-1]:
                                archivo14.write(quest + "\n")
                        archivo14.write("#end#\n")
                        archivo14.close()
                        print lang(310)
                    except:  # Error al escribir las quest del jugador
                        print lang(398)
                        print lang(568)
                        self.setInfo(lang(63))
                        self.error(lang(570))
                        return
                    try:  # Poderes del jugador
                        print lang(430),
                        archivo12 = open(DATA_SAVES + nameSav + ".powers", "w")
                        for pod in self.player.getPowers():  # Recorro los poderes del jugador
                            # escribo el poder exportado
                            archivo12.write(pod.export() + "\n")
                        archivo12.close()
                        print lang(310)
                    except:  # Error al escribir los poderes del jugador
                        print lang(398)
                        print lang(385)
                        self.setInfo(lang(63))
                        self.error(lang(386))
                        return
                    try:  # Archivo de comandos
                        print lang(422),
                        archivo3 = open(DATA_SAVES + nameSav + ".hoacmd", "w")
                        if len(self.console) != 0:
                            for i in self.console:
                                archivo3.write(i + "\n")
                        else:
                            archivo3.write("%NOCONSOLE%")
                        archivo3.close()
                        print lang(310)
                    except:  # Error al exportar los comandos
                        print lang(398)
                        print lang(335)
                        self.setInfo(lang(63))
                        self.error(lang(156))
                        return
                    try:  # Archivo del mapa lógico
                        print lang(423),
                        archivo4 = open(
                            DATA_SAVES + nameSav + ".maplogic", "w")
                        for j in self.mapLogic:
                            k = ""
                            for i in j:
                                k += i + ";"
                            archivo4.write(k + "\n")
                        archivo4.close()
                        print lang(310)
                    except:  # Error al guardar el mapa lógico
                        print lang(398)
                        print lang(334)
                        self.setInfo(lang(63))
                        self.error(lang(157))
                        return
                    try:  # Archivo de mobs del mapa actual
                        print lang(424),
                        archivo5 = open(DATA_SAVES + nameSav + ".mapmob", "w")
                        if len(self.mobs) > 0:  # Si existen mobs
                            for mob in self.mobs:
                                # se exporta el mob
                                archivo5.write(mob.export())
                        else:
                            archivo5.write("%NOMOBS%")
                        archivo5.close()
                        print lang(310)
                    except:  # Error al crear el mapa actual
                        print lang(398)
                        print lang(333)
                        self.setInfo(lang(63))
                        self.error(lang(158))
                        return
                    try:  # Archivo de estadísticas
                        print lang(425),
                        archivo6 = open(DATA_SAVES + nameSav + ".statics", "w")
                        archivo6.write(self.static.export())
                        archivo6.close()
                        print lang(310)
                    except:  # Error al exportar las estadísticas del jugador
                        print lang(398)
                        print lang(332)
                        self.setInfo(lang(63))
                        self.error(lang(174))
                        return
                    try:  # Archivo de npc del mapa actual
                        print lang(437),
                        archivo13 = open(DATA_SAVES + nameSav + ".mapnpc", "w")
                        if len(self.npc) > 0:  # Si existen npc
                            for it in self.npc:
                                # se exporta el npc
                                archivo13.write(it.export())
                        else:
                            archivo13.write("%NONPC%")
                        archivo13.close()
                        print lang(310)
                    except:  # Error al exportar npc
                        print lang(398)
                        print lang(438)
                        self.setInfo(lang(63))
                        self.error(lang(439))
                        return
                    try:  # Archivos de seguridad
                        print lang(426)
                        archivo2 = open(DATA_SAVES + nameSav + ".key1", "w")
                        archivo2.write(
                            amir(DATA_SAVES + nameSav + ".sav") + "\n")
                        archivo2.close()
                        archivo7 = open(DATA_SAVES + nameSav + ".key2", "w")
                        archivo7.write(
                            amir(DATA_SAVES + nameSav + ".statics") + "\n")
                        archivo7.close()
                        archivo8 = open(DATA_SAVES + nameSav + ".key3", "w")
                        archivo8.write(
                            amir(DATA_SAVES + nameSav + ".maplogic") + "\n")
                        archivo8.close()
                        archivo9 = open(DATA_SAVES + nameSav + ".key4", "w")
                        archivo9.write(
                            amir(DATA_SAVES + nameSav + ".hoacmd") + "\n")
                        archivo9.close()
                        archivo10 = open(DATA_SAVES + nameSav + ".key5", "w")
                        archivo10.write(
                            amir(DATA_SAVES + nameSav + ".mapmob") + "\n")
                        archivo10.close()
                    except:  # Error al crear archivos de seguridad
                        print lang(398)
                        print lang(331)
                        self.setInfo(lang(63))
                        self.error(lang(155))
                        return
                    try:  # Archivo de texturas lógicas
                        print lang(427),
                        archivo11 = open(
                            DATA_SAVES + nameSav + ".mapitemtexture", "w")
                        for j in self.mapItemsTextures:
                            k = ""
                            for i in j:
                                if i is None:
                                    i = "None"
                                k += i + ";"
                            archivo11.write(k + "\n")
                        archivo11.close()
                        print lang(310)
                    except:  # Error al crear el archivo de texturas lógicas
                        print lang(398)
                        print lang(330)
                        self.setInfo(lang(63))
                        self.error(lang(222), 85)
                    try:  # Archivo de guardado
                        print lang(428)
                        print lang(401).format(
                            "(...)" + (DATA_SAVES + nameSav + ".save")[-44:]),
                        filesave = zipfile.ZipFile(
                            DATA_SAVES + nameSav + ".save",
                            mode='w')  # archivo final de guardado
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".hoacmd",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de comandos
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".key1",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de seguridad
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".key2",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de seguridad
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".key3",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de seguridad
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".key4",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de seguridad
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".key5",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de seguridad
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".mapitemtexture",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de texturas
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".maplogic",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega los elementos lógicos del mapa
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".mapmob",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega los mobs del mapa
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".mapnpc",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de npc del mapa actual
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".powers",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de los poderes
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".quest",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo de las quest
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".sav",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agrega el archivo principal
                        filesave.write(
                            DATA_SAVES_NO_DIRECTORY + nameSav + ".statics",
                            compress_type=zipfile.ZIP_DEFLATED)  # se agregan las estadísticas del jugador
                        filesave.close()  # cierro el archivo generado
                        print lang(310)
                    except:  # Error al crear el archivo de guardado
                        self.setInfo(lang(63))
                        self.error(lang(213))
                        print lang(440)
                    self.loaded = True  # se establece como cargada la partida
                    if tipo not in [
                        "shorcut"]:  # Si no fue por atajo de teclado
                        # La partida fue guardada exitosamente
                        if tipo not in ["exit", "autosave", "command"]:
                            self.sfx(37)
                            e = pop([[lang(61), lang(173)], self.images.image(
                                "save_icon"), "aviso", 70, 270, lang(62)])
                            e.w.mainloop(2)
                            del e
                            self.setInfo(lang(61))
                        else:
                            self.setInfo(lang(169))
                    else:
                        self.setInfo(lang(61))
                # Elimino los archivos generados
                print lang(429),
                borrarArchivosGenerados(DATA_SAVES + nameSav)
                print lang(310)
                print lang(431)
            else:  # Si se encuentra peleando
                self.setInfo(lang(278))
                self.sfx(28)

    def setCombat(self, mob, i_d):
        """
        Establece el combate entre el mob y el jugador
        :param mob: Mob
        :param i_d: ID del mob
        :return: void
        """
        self.enemy = mob  # objeto mob
        self.enemy.setName(translate(self.enemy.getName()))
        self.enemy.setInfo(translate(self.enemy.getInformacion()))
        self.enemy.setDefensa(int(self.enemy.getDefensa() * (
            self.dificultad[
                1] + 1)))  # se define la defensa basal mob en funcion de la dificultad
        self.enemyId = i_d  # se obtiene el id del mob
        self.inBattle = True  # modo batalla (loop)
        try:
            # se borra el ultimo elemento
            self.root.after_cancel(self.lastmovementId)
        except:
            print lang(363)
        self.tipoCombate = self.enemy.getTipoCombate()  # se define el tipo de combate
        # Si es un combate normal o no se tienen amigos para luchar
        if self.tipoCombate == MODE_FIGHT_NORMAL or self.player.getTotalFriends() == 0:
            self.tipoCombate = MODE_FIGHT_NORMAL
            self.enemy.setPosAbs(self.playerPos[0],
                                 self.playerPos[
                                     1])  # se define la posición absoluta con respecto al jugador
            self.textMsg(self.enemy.getName() + "\n" +
                         self.enemy.getInformacion(), "combat")
            try:  # Si el mob posee un sonido caracteristico se le reproduce
                if self.enemy.getSound() != "%NOSOUND%":
                    self.sonidoFx(
                        SOUND_MOB + self.enemy.getSound() + ".wav")  # sonido característico del mob
            except:
                print lang(328)
        elif self.tipoCombate == MODE_FIGHT_GROUP:  # Si es un combate grupal
            self.sfx(29)  # sonido del combate grupal
            self.board = board(self.player, self.enemy,
                               self.mapTextures[self.playerPos[1]][
                                   self.playerPos[0]],
                               self.mapTextures[self.enemy.getPosicionY()][
                                   self.enemy.getPosicionX()],
                               choice(TEXTURE_OBSTACLES),
                               self.maplightning[self.playerPos[1]][
                                   self.playerPos[0]],
                               self.maplightning[self.enemy.getPosicionY()][
                                   self.enemy.getPosicionX()],
                               self.nivel_dificultad, self.dificultad[
                                   7], self.images,
                               self.mapSound[self.playerPos[1]][
                                   self.playerPos[0]],
                               self.mapSound[self.enemy.getPosicionY()][
                                   self.enemy.getPosicionX()],
                               self.player.getArrowTexture(),
                               self.player.getWeaponTexture())
            print lang(726),
            try:
                self.board.generate()  # genero un tablero al azar
            except:  # Si ocurre un error genero otro tablero
                self.board.deleteAll()
                self.board.generate()
            print lang(310)
            for i in self.board.players:
                i.setMaxDistance(
                    int(
                        self.board.getBoardSizeX() * MAX_1ST_MOVEMENT))  # establezco el máximo movimiento de los grupos
            self.board.setTotalExp()
            self.board.modifyBoardCorreccionX(DRAW_CANVAS_OFFSET_X)
            self.board.modifyBoardCorreccionY(DRAW_CANVAS_OFFSET_Y)
            self.dibujarMundo()
            self.combateGrupal("print")
            self.setInfo(lang(725, str(
                int(self.enemy.getLife() * (2 - self.dificultad[7]) * 0.12)),
                              str(int(self.enemy.getAtaque() *
                                      (2 - self.dificultad[7]) * 0.4)),
                              str(int(self.enemy.getDefensa() * (
                                  2 - self.dificultad[7]) * 0.3))), False)
        self.setInfo(self.enemy.getName() + "\n" +
                     lang(87, self.enemy.getInformacion()), False)
        if self.tipoCombate == MODE_FIGHT_GROUP:
            self.setInfo(lang(724))

    def setDificultad(self):
        """
        Define la dificultad del juego
        :return: void
        """
        if self.nivel_dificultad == DIFICULTAD_FACIL:
            self.dificultad = [-0.25, -0.25, 0.25, -0.25, 0.25,
                               int(TIME_MOVE_MOBS_NORMAL * 1.25), -0.5, 1.25]
        elif self.nivel_dificultad == DIFICULTAD_MEDIO:
            self.dificultad = [0, 0, 0, 0, 0, int(
                TIME_MOVE_MOBS_NORMAL * 1), 0, 1]
        elif self.nivel_dificultad == DIFICULTAD_DIFICIL:
            self.dificultad = [0.25, 0.25, -0.25, 0.25, -0.25,
                               int(TIME_MOVE_MOBS_NORMAL * 0.75), 0.5, 0.75]

    def setInfo(self, text, hour=True):
        """
        Función que escribe un texto en la consola
        :param text: Texto
        :param hour: Boolean
        :return: void
        """
        if text:  # Agrego texto a consola
            if hour:
                # se agrega mensaje con hora
                self.console.insert(0, getHour() + " " + putStrict(text))
            else:
                self.console.insert(0, putStrict(text))
        # Si la consola alcanza el límite de mensajes luego se elimina el
        # último
        if len(self.console) > LIMIT_MESSAGES_CONSOLE:
            self.console.pop()
        self.info.config(text=consoled(self.console))
        self.infoSlider.canv.yview_scroll(-1000, "units")

    def setWorld(self):
        """
        Función que carga el mundo desde un archivo
        :return: void
        """
        try:
            mapa = loadFromArchive(
                DATA_LEVELS + self.player.getMap(),
                lang(400))  # carga del mapa
            self.root.title(self.programTitle + " - " +
                            str(translate(mapa[0])).replace("'", ""))
            size = mapa[2].split(",")
            self.mapSize = int(size[0]), int(size[1])
            delMatrix(self.mapItemsTextures)
            delMatrix(self.mapLogic)
            delMatrix(self.mapSound)
            delMatrix(self.mapTextures)
            delMatrix(self.maplightning)
            delMatrix(self.mobs)
            delMatrix(self.npc)
            k = 0
            # se crea la imágen de fondo
            im = Image.new(
                "RGB", (self.mapSize[0] * 32, self.mapSize[1] * 32), "#000000")
            # se crea la imágen de fondo
            fim = Image.new("RGB", (CANVAS_SIZE[0], CANVAS_SIZE[1]), "#000000")
            self.mapBackgroundSound[0] = SOUND_AMBIENCE + \
                                         mapa[4]  # establezco el sonido
            for i in range(6, len(mapa)):  # Se agregan datos al mapa
                self.mapItemsTextures.append([0] * self.mapSize[0])
                self.mapLogic.append([0] * self.mapSize[0])
                self.mapSound.append([0] * self.mapSize[0])
                self.mapTextures.append([0] * self.mapSize[0])
                self.maplightning.append([0] * self.mapSize[0])
                fila = mapa[i].split(";")
                for f in range(self.mapSize[0]):
                    fila[f] = fila[f].split(":")
                for j in range(self.mapSize[0]):
                    light = int(fila[j][0])
                    item = fila[j][1]
                    self.maplightning[k][j] = light
                    (texture, sound, terrainlog) = textureTerrainAnalysis(
                        int(fila[j][2]),  # @UnusedVariable
                        light)  # cargo la textura y el sonido @UnusedVariable
                    im.paste(self.images.image(texture),
                             (32 * j, 32 * k, 32 * (j + 1),
                              32 * (k + 1)))  # se agrega imagen al fondo
                    self.mapSound[k][j] = SOUND_WALK + \
                                          sound + SOUND_FORMAT  # se agrega sonido
                    self.mapTextures[k][j] = texture  # se agrega la textura
                    item = item.split("-")
                    logic = int(item[0])
                    # Reviso los elementos lógicos
                    if logic == 1:  # Jugador
                        log = "player"
                        self.playerPos[0] = j
                        self.playerPos[1] = k
                    elif logic == 2:
                        log = "tree"  # �?rbol
                    elif logic == 3:
                        log = "chest"  # Cofre
                    elif logic == 4:
                        log = "water"  # Agua
                    elif logic == 5:
                        log = "rock"  # Roca
                    elif logic == 6:
                        log = "door," + item[2]  # Puerta
                    elif logic == 7:
                        try:
                            log = "building," + item[2]  # Edificio
                        except:
                            log = "nopass"
                    elif logic == 8:  # Mob
                        log = "mob"
                        prop = item[2].split(",")
                        if len(prop) == 17:
                            prop += ["%NOSOUND%"]
                        self.mobs.append(mob(int(prop[0]), int(prop[1]),
                                             textureMobAnalysis(int(prop[2])),
                                             int(prop[3]), int(prop[4]), prop[
                                                 5], prop[6], j, k,
                                             int(prop[7]),
                                             int(prop[8]), int(prop[9]), int(
                                prop[10]), prop[11], prop[12], prop[13],
                                             int(prop[14]),
                                             j, k, prop[15], prop[16],
                                             prop[17]))
                    elif logic == 9:
                        log = "people"  # Mob lógico - persona que realiza metodos sobre el jugador
                    elif logic == 10:
                        log = "empty"  # Espacio vacío al que no se puede acceder
                    elif logic == 11:
                        log = "item"  # Item
                    elif logic == 12:
                        log = "decoration"  # Decoración
                    elif logic == 13:
                        log = "text," + item[2]  # Texto al usuario
                    elif logic == 14:
                        log = "torch"  # Antorcha
                    elif logic == 15:
                        log = "object," + item[2]  # Objeto
                    elif logic == 16:
                        log = "library"  # Librería / estante
                    elif logic == 17:
                        log = "minushp," + item[2]  # Quitar vida al jugador
                    elif logic == 18:
                        log = "minusmana," + item[2]  # Quitar mana al jugador
                    elif logic == 19:
                        # Moverse a un (x,y) determinado
                        log = "moveto," + item[2]
                    elif logic == 20:
                        log = "nopass"  # No pasar
                    elif logic == 21:
                        log = "pass"  # Pasar
                    elif logic == 22:
                        log = "plushp," + item[2]  # Dar vida al jugador
                    elif logic == 23:
                        log = "plusmana," + item[2]  # Dar mana al jugador
                    elif logic == 24:
                        log = "teleport," + item[2]  # Teletransportarse
                    elif logic == 25:
                        # Moverse desde (no hace nada)
                        log = "movefrom," + item[2]
                    elif logic == 26:
                        log = "bed"  # Cama
                    elif logic == 27:
                        log = "vehicle"  # Vehículo
                    elif logic == 28:
                        log = "sound," + item[2]  # Si es sound
                    elif logic == 29:
                        log = "mute"  # Si es mute
                    elif logic == 30:
                        log = "longtext," + item[2]  # Si es longtext
                    elif logic == 31:
                        log = "autosave"  # Si es autosave
                    elif logic == 32:
                        log = "suddendeath"  # Si es suddendeath
                    elif logic == 33:
                        log = "nopassalert"  # Si es nopassalert
                    elif logic == 34:
                        log = "nature"  # objetos naturales
                    elif logic == 35:
                        log = "cactus"  # cactus #objeto natural
                    elif logic == 36:
                        log = "hongo"  # hongo #algunos son usables
                    elif logic == 37:
                        log = "estatua"  # hongo #algunos son usables
                    elif logic == 38:
                        log = "sign," + item[2]  # Si es un signo
                    elif logic == 39:
                        log = "ambientEffect"  # efecto de ambiente, puede causar daño o algún otro efecto
                    elif logic == 40:
                        log = "grass"  # efecto de ambiente, puede causar daño o algún otro efecto
                    elif logic == 41:
                        log = "wall/pilar"  # efecto de ambiente, puede causar daño o algún otro efecto
                    elif logic == 42:
                        log = "ladder," + item[2]  # Si es una escalera
                    elif logic == 43:  # Npc
                        log = "npc"
                        prop = item[2].split(",")
                        self.npc.append(
                            npc(prop[0], textureMobAnalysis(int(prop[1])),
                                prop[2], prop[3], prop[4],
                                prop[5], int(prop[6]), prop[7], int(
                                    prop[8]), prop[9], j, k, "FALSE", 0, j,
                                k, prop[10]))
                    elif logic == 44:
                        log = "alfombra"
                    else:
                        log = "none"
                    self.mapLogic[k][j] = log
                    self.mapItemsTextures[k][
                        j] = textureItemAnalysis(item[1], light)
                k += 1
            if CANVAS_MAX_SIZE[0] > self.mapSize[1]:
                self.canvasCorrecion[0] = (
                                              CANVAS_MAX_SIZE[0] -
                                              self.mapSize[
                                                  1]) * 16  # Horizontal
            else:
                self.canvasCorrecion[0] = 0
            if CANVAS_MAX_SIZE[1] > self.mapSize[0]:
                self.canvasCorrecion[1] = (
                                              CANVAS_MAX_SIZE[1] -
                                              self.mapSize[0]) * 16  # Vertical
            else:
                self.canvasCorrecion[1] = 0
            self.canvasCorrecion[0] += DRAW_CANVAS_OFFSET_X
            self.canvasCorrecion[1] += DRAW_CANVAS_OFFSET_Y
            if len(self.mobs) != 0:  # Activa el movimiento de los mobs
                try:
                    # se intenta eliminar la ultima ejecución de la funcion
                    self.root.after_cancel(self.lastmovementId)
                except:
                    print lang(363)
                self.lastmovementId = self.root.after(
                    self.dificultad[5], self.moveMobs)
                self.movement = True
            else:
                self.movement = False
            if len(self.npc) != 0:  # Activa el movimiento de los npc
                movement = False
                for elem in self.npc:
                    if elem.getMove():
                        movement = True
                        break
                if movement:
                    try:
                        self.root.after_cancel(self.lastnpcmovementid)
                    except:
                        print lang(564)
                    self.lastnpcmovementid = self.root.after(
                        NPC_TIME_MOVEMENT, self.moveNpc)
                    self.npcMovement = True
                else:
                    self.npcMovement = False
                del movement
            self.static.addMapas()
            fim.paste(im,
                      (self.canvasCorrecion[1], self.canvasCorrecion[0],
                       32 * self.mapSize[0] + self.canvasCorrecion[1],
                       32 * self.mapSize[1] + self.canvasCorrecion[0]))
            self.mapImage.pop()  # borro la ultima imagen de fondo
            # agrego imagen de fondo
            self.mapImage.append(ImageTk.PhotoImage(fim))
            self.dibujarMundo()
            try:  # Elimino los sonidos anteriores
                if self.mapBackgroundSound[1] is not None:
                    self.root.after_cancel(self.mapBackgroundSound[1])
            except:
                print lang(362)
            self.stopSound()  # Paro los sonidos
            # Cargo el sonido de fondo
            self.sonidoBg(self.mapBackgroundSound[0])
            self.sfxBackgroundRepeat()  # Repito indefinidamente el sonido
            del im
            del fim  # Borro las imágenes generadas
        except:  # Si ocurre algún error durante la carga del mapa
            print lang(361)
            self.player.setMap("%ERROR_LOADINGMAP%")
            self.stopSound()
            self.setInfo(lang(97))
            self.movement = False
            self.npcMovement = False
            self.error(lang(98))

    def sfx(self, t):
        """
        Función que reproduce un archivo de musica desde la libreria
        :param t: Index
        :return: void
        """
        self.sonidoFx(
            choice(SONIDO[
                       t]))  # carga el sonido desde la lista eligiendo un sonido al azar

    def sfxBackgroundRepeat(self, e=None):
        """
        Función que repite un sonido
        :param e: Event
        :return: void
        """
        if CONFIGURATION_DATA[1] and TKSNACK[
            0]:  # Si los sonidos están activados
            self.sndBg.play()
            if self.mapBackgroundSound[1] is not None:
                self.root.after_cancel(self.mapBackgroundSound[1])

            def _play(e=None):
                self.sndBg.play()

            self.mapBackgroundSound[1] = self.root.after(
                self.mapBackgroundSound[2], _play)

    def sfxSpecial(self, n, t):
        """
        Función que reproduce un archivo especifico desde la librería de musica
        :param n: Index
        :param t: Sub-Index
        :return: void
        """
        self.sonido(SONIDO[n][t])  # carga y reproduce el sonido

    def sonido(self, archivo):
        """
        Función que reproduce un archivo
        :param archivo: Archivo de sonido
        :return: void
        """
        # Si el sonido existe y los sonidos están activados
        if archivo != "" and CONFIGURATION_DATA[1] and TKSNACK[0]:
            try:
                self.snd.read(archivo)
                self.snd.play()
            except:
                print st_error(lang(404, "(...)" + archivo[CONSOLE_WRAP:]))

    def sonidoBg(self, archivo):
        """
        Función que reproduce un archivo
        :param archivo: String de sonido
        :return: void
        """
        # Si el archivo existe y los sonidos están activados
        if archivo != "" and CONFIGURATION_DATA[
            1] and archivo != SOUND_AMBIENCE + "%MAPSOUND%" and TKSNACK[0]:
            try:
                print lang(670).format(
                    "(...)" + (self.mapBackgroundSound[0])[-37:]),
                self.sndBg.read(archivo)
                self.mapBackgroundSound[2] = self.sndBg.length(
                    unit="SECONDS") * 1000
                print lang(310)
            except:
                print lang(398)
                print st_error(lang(404, "(...)" + archivo[CONSOLE_WRAP:]))

    def sonidoFx(self, archivo):
        """
        Función que reproduce un archivo
        :param archivo: String de sonido
        :return: void
        """
        # Si el archivo existe y los sonidos están activados
        if archivo != "" and CONFIGURATION_DATA[1] and TKSNACK[0]:
            try:
                self.sndFx.stop()
                self.sndFx.read(archivo)
                self.sndFx.play()
            except:
                print st_error(lang(404, "(...)" + archivo[CONSOLE_WRAP:]))

    def stopSound(self, mode="normal"):
        """
        Función que detiene todos los sonidos
        :param mode: Modo de reproducción
        :return: void
        """
        if (CONFIGURATION_DATA[1] or mode == "silent") and TKSNACK[
            0]:  # Si los sonidos están activados
            if mode != "silent":
                print lang(432),
            try:
                self.snd.stop()
                self.sndBg.stop()
                self.sndFx.stop()
            except:
                pass
            try:  # Se borran de la memoria todos los sonidos
                self.snd.flush()
                self.sndBg.flush()
                self.sndFx.flush()
            except:
                if mode != "silent":
                    print lang(364)
            if mode != "silent":
                print lang(310)

    def textMsg(self, txt, mode="normal"):
        """
        Escribe un texto en el mapa
        :param txt: Texto
        :param mode: Modo de dibujo
        :return: void
        """
        try:
            self.world.delete("textmsg")
            self.world.delete("textback")
        except:
            pass
        if not self.tipoCombate == MODE_FIGHT_GROUP:
            tfont = self.fonts[2]
            if mode == "combat" or mode == "npc":
                txta = txt.split("\n")
                width = max(tfont.measure(
                    txta[0]), tfont.measure(txta[1])) + 10
                height = 32
                corr = -4
                time = 2
            else:
                txt = putStrict(txt.strip())
                width = min(tfont.measure(txt) + 10, WIDTHMESSAGES)
                height = (tfont.measure(txt) / WIDTHMESSAGES + 1) * 16
                corr = 0
                time = 1
            try:
                if self.playerPos[0] <= self.mapSize[1] / 2:
                    bloq = self.world.create_rectangle(
                        self.playerPos[0] * 32 + self.canvasCorrecion[1] + 37,
                        self.playerPos[
                            1] * 32 + self.canvasCorrecion[0] - height,
                        self.playerPos[0] * 32 + self.canvasCorrecion[
                            1] + 32 + width + 5, self.playerPos[1] * 32 +
                        self.canvasCorrecion[0] + 3, fill="#FFFFE1",
                        outline="#646464",
                        tags="textback")
                    msg = self.world.create_text(
                        self.playerPos[0] * 32 + self.canvasCorrecion[1] + 42,
                        self.playerPos[
                            1] * 32 + self.canvasCorrecion[0] + 3 - height,
                        text=txt, fill="#000000", font=tfont, width=width,
                        anchor=NW,
                        tags="textmsg")
                else:
                    bloq = self.world.create_rectangle(
                        self.playerPos[0] * 32 + self.canvasCorrecion[
                            1] - width + 5,
                        self.playerPos[1] * 32 + self.canvasCorrecion[0] -
                        height + corr,
                        self.playerPos[
                            0] * 32 + self.canvasCorrecion[1] + 5,
                        self.playerPos[1] * 32 +
                        self.canvasCorrecion[0] + 3 + corr, fill="#FFFFE1",
                        outline="#646464", tags="textback")
                    msg = self.world.create_text(
                        self.playerPos[0] * 32 + self.canvasCorrecion[1],
                        self.playerPos[
                            1] * 32 + self.canvasCorrecion[
                            0] + 3 - height + corr,
                        text=txt, fill="#000000", font=tfont, width=width,
                        anchor=NE,
                        tags="textmsg")
                self.root.after(SHOWMESSAGESTIME * time,
                                lambda: self.world.delete(msg))
                self.root.after(SHOWMESSAGESTIME * time,
                                lambda: self.world.delete(bloq))
            except:
                print lang(433)
            self.world.update()

    def update(self, e=None):
        """
        Función que actualiza el juego
        :param e: Event
        :return: void
        """
        if self.ingame:  # Si se encuentra jugando
            self.checkItems()
            self.dibujarArmor()
            self.dibujarItems()
            self.dibujarMundo()
            self.dibujarPowers()
            self.updateInfoPlayer()

    def updateInfoPlayer(self):
        """
        Función que actualiza los contadores del jugador
        :return: void
        """
        life = self.player.getLife()
        maxl = self.player.getActualMaximumLife()
        barras = min(100 * BAR_POND_COEF,
                     int((life * 100 * BAR_POND_COEF) / max(1, maxl)))
        self.infoVidaCanv.delete(ALL)
        self.infoVidaCanv.create_rectangle(
            0, 0, barras + 1, 18, fill="#008000", outline="#008000")
        self.infoVida.config(text=str(life).zfill(3) +
                                  "/" + str(maxl).zfill(3))
        barras = min(100 * BAR_POND_COEF,
                     int((
                             self.player.getExperience() - self.player.getPrevExp()) * 100 * BAR_POND_COEF / max(
                         1,
                         self.player.getMaxExperience() - self.player.getPrevExp())))
        self.infoExpCanv.delete(ALL)
        self.infoExpCanv.create_rectangle(
            0, 0, barras + 1, 18, fill="#000080", outline="#000080")
        if 0 <= self.player.getExperience() < 10000000:
            msg = str(self.player.getExperience())
        elif 10000000 <= self.player.getExperience() < 100000000:
            msg = str(self.player.getExperience())[0:4] + "m"
        elif 100000000 <= self.player.getExperience() < 1000000000:
            msg = str(self.player.getExperience())[0:5] + "M"
        else:
            msg = "∞"
        self.infoExp.config(text=msg)
        mana = self.player.getMana()
        maxm = self.player.getMaxMana()
        barras = int((mana * 100 * BAR_POND_COEF) / max(1, maxm))
        self.infoManaCanv.delete(ALL)
        self.infoManaCanv.create_rectangle(
            0, 0, barras + 1, 18, fill="#6F7116", outline="#6F7116")
        self.infoMana.config(text=str(mana).zfill(3) +
                                  "/" + str(maxm).zfill(3))
