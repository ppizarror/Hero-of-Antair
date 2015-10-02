#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Editor de mapas

# MEDT
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2013-2015
# Licencia: GPLv2

# Importación de librerías de alto nivel
from lib import *

# Información del programa
PROGRAM_TITLE = "Editor de mapas"
PROGRAM_VERSION = 1.8
printAsciiArtME()  # imprimo el logo del programa en ascii
print "\nMap editor version: " + str(PROGRAM_VERSION)
print "\nCargando librerias ...",

# Importación de librerías
try:
    from mpop import pop
    from textures_editor import *
    import gc
except:
    print "error"
    exit()
print "ok"

# Configuración de librerías
gc.enable()
try:
    os.remove("mapeditor.pyc")
except:
    pass

# Constantes del programa
_libdir = "lib"
ACTUAL_FOLDER = str(os.getcwd()).replace(
    "\\", "/").replace(_libdir, "") + "/"  # se dfine el directorio actual
AUTOR = "Pablo Pizarro"  # nombre mio
AUTOR_EMAIL = "pablo@ppizarror.com"  # mi correo
COLOR_INFO = "#FFFFFF"  # color de las informaciones
# colores para los elementos lógicos, g:rojo, c:naranjo
COLOR_MOVEMENT = ["g_mov", "c_mov"]
COLOR_LINE = "#CCCCCC"  # color del grid
DATA_FOLDER = ACTUAL_FOLDER + "data/"  # directorio de los archivos
DATA_DOCUMENTS = DATA_FOLDER + "doc/"  # directorio de la documentación
DATA_LEVELS = DATA_FOLDER + "levels/"  # directorio de los niveles
DATA_SOUND = DATA_FOLDER + "sound/"  # directorio de sonidos
DATA_SOUNDS_AMBIENCE = DATA_SOUND + "ambience/"  # sonidos de ambiente
EVENTS_LOGIC = ["1", "8", "11", "13", "15", "16", "17", "18", "20", "21", "22", "23", "24", "28", "29", "30", "31",
                "32", "33", "43"]  # logicos
EVENT_MOVE = ["19", "25"]  # eventos de movimiento
LEVEL_PROP = DATA_LEVELS + "prop/"  # propiedades de los niveles
LEVEL_RES = DATA_LEVELS + "res/"  # recursos de los niveles
LEVEL_SOUND = DATA_LEVELS + "sound/"  # sonidos de los niveles
LOGICS = {"0": "vacío", "1": "jugador", "2": "árbol", "3": "cofre", "4": "líquido", "5": "roca",
          "6": "puerta", "7": "edificio", "8": "enemigo", "9": "ciudadano", "10": "vacio",
          "11": "item", "12": "decorado", "13": "text", "14": "antorcha", "15": "object",
          "16": "librería", "17": "minushp", "18": "minusmana", "19": "move(to)",
          "20": "nopass", "21": "pass", "22": "plushp", "23": "plusmana", "24": "teleport",
          "25": "move(from)", "26": "bed", "27": "vehicle", "28": "sound", "29": "mute",
          "30": "longtext", "31": "autosave", "32": "death", "33": "nopass(al)",
          "34": "nature", "35": "cactus", "36": "hongo", "37": "estatua", "38": "sign",
          "39": "effect", "40": "grass", "41": "wall", "42": "ladder", "43": "npc",
          "44": "alfombra"}
TILE_BUILDING = ["7", "14", "39"]  # lógicos de la edificación
TILE_EDIT = ["3", "6", "7", "8", "11", "13", "15", "16", "17", "18", "19", "22", "23", "24", "25", "27", "28", "30",
             "38", "42", "43"]  # tiles disponibles para la edición
TILE_EVENT = ["1", "8", "11", "13", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
              "25", "28", "29", "30", "31", "32", "33"]

if isWindows():
    PROGRAM_SIZE = 918, 601  # tamaño de la ventana
else:
    PROGRAM_SIZE = 931, 581  # tamaño de la ventana


class mapeditor:
    """Editor de mapas"""

    def __init__(self):
        """
        Función constructora
        :return: void
        """

        # Métodos del constructor
        def _saveas(event=None):
            """
            Guardar como
            :param event: Event
            :return: void
            """
            self.saveMap("save_as")

        def _changeSound(event=None):
            """
            Escoger sonido de fondo
            :param event: Event
            :return: void
            """
            if self.isEvent:
                q = pop(['Escoger sonido de fondo', self.images["sound_icon"], 'new_sound_background', 120, 380,
                         DATA_SOUNDS_AMBIENCE])
                q.w.mainloop(1)
                if q.sent:
                    self.isMapEditing = True
                    self.core.title(PROGRAM_TITLE + " - " +
                                    self.mapName + " (" + self.mapFile + ") *")
                    self.mapSound = q.values[0]
                    if self.mapSound == "-Sin sonido":
                        self.mapSound = "%MAPSOUND%"
                del q
                self.setSoundMap()

        def _numbers(event=None):
            """
            Ocultar/Mostrar números
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.showNumbers = not self.showNumbers
                self.drawTiles()

        def _lines(event=None):
            """
            Ocultar/Mostrar líneas
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.showLines = not self.showLines
                self.drawTiles()

        def _redib(event=None):
            """
            Redibujar
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.drawTiles()

        def _logics(event=None):
            """
            Ocultar/Mostrar eventos lógicos
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.showLogics = not self.showLogics
                self.drawTiles()

        def _movements(event=None):
            """
            Ocultar/Mostrar movimientos
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.showMovement = not self.showMovement
                self.drawTiles()

        def _terrain(event=None):
            """
            Ocultar/Mostrar terreno
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.showTerrain = not self.showTerrain
                self.drawTiles()

        def _events(event=None):
            """
            Ocultar/Mostrar eventos
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.showEvents = not self.showEvents
                self.drawTiles()

        def _items(event=None):
            """
            Ocultar/Mostrar Ítems
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.showItems = not self.showItems
                self.drawTiles()

        def _delactor(event=None):
            """
            Eliminar actor
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.delActive()
                self.actualActor = "", "", "delete"

        def _delterrain(event=None):
            """
            Eliminar terreno
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.delActive()
                self.actualTexture = 0, "noneterrain"

        def _deldecoration(event=None):
            """
            Eliminar decoración
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.delActive()
                self.actualEnvironment = "delete", -1

        def _infoTile_info(event=None):
            """
            Acción del menu que muestra la información
            :param event: Event
            :return: void
            """
            if self.isEvent:
                if sum(self.workTile) != -2:
                    if isWindows():
                        ysize = 169
                    else:
                        ysize = 175
                    e = pop(['Información', self.images['mapinfo'], 'infoTile_info', ysize, 330, self.workTile,
                             self.worldLogic[self.workTile[0]][
                                 self.workTile[1]],
                             self.worldTextures[self.workTile[0]][
                                 self.workTile[1]],
                             self.worldLight[self.workTile[0]][self.workTile[1]]])
                    e.w.mainloop(1)
                    del e

        # TODO: Modificar copia de luz
        def _copyTile(event=None):
            """
            Copia la información de un tile
            :param event: Event
            :return: void
            """
            if self.isEvent:
                self.clipboard = [self.worldLogic[self.workTile[0]][self.workTile[1]],
                                  self.worldTextures[self.workTile[0]][
                                      self.workTile[1]],
                                  self.worldGraph[self.workTile[0]][
                                      self.workTile[1]],
                                  self.worldItems[self.workTile[0]][self.workTile[1]]]

        def _pasteTile(event=None):
            """
            Pega la información de un tile
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Pego la información
                light = "_" + \
                    str(self.worldLight[self.workTile[0]][self.workTile[1]])
                self.worldLogic[self.workTile[0]][
                    self.workTile[1]] = self.clipboard[0]
                self.worldTextures[self.workTile[0]][
                    self.workTile[1]] = self.clipboard[1]
                self.worldGraph[self.workTile[0]][self.workTile[1]] = self.clipboard[2].replace("_0", light).replace(
                    "_1", light)
                self.worldItems[self.workTile[0]][self.workTile[1]] = self.clipboard[3].replace("_0", light).replace(
                    "_1", light)
                self.drawTiles()
                self.core.title(PROGRAM_TITLE + " - " +
                                self.mapName + " (" + self.mapFile + ") *")
                self.isMapEditing = True

        def _infoTile_delete(event=None):
            """
            Acción del menu que borra
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Borro el vecindario
                delTileLogicNeighbor(self.worldLogic[self.workTile[0]][self.workTile[1]],
                                     self.workTile[0], self.workTile[1], self.worldLogic, self.worldItems)
                # borro los vectores luminicos
                if "14" or "7-407" or "39-961" in self.worldLogic[self.workTile[0]][self.workTile[1]]:
                    self.removeLightVector(self.workTile[1], self.workTile[0])
                logic = self.worldLogic[self.workTile[0]][
                    self.workTile[1]].split("-")
                # Establezco los lógicos
                if logic[0] == "4":
                    self.worldLogic[self.workTile[0]][self.workTile[1]] = "4-0"
                else:
                    self.worldLogic[self.workTile[0]][self.workTile[1]] = "0-0"
                self.worldItems[self.workTile[0]][
                    self.workTile[1]] = "None"  # elimino las texturas
                self.drawTiles()  # Redibujo el mapa
                self.isMapEditing = True
                self.core.title(PROGRAM_TITLE + " - " +
                                self.mapName + " (" + self.mapFile + ") *")

        def _infoTile_edit(event=None):
            """
            Acción para editar
            :param event: Event
            :return: void
            """
            if self.isEvent:
                logic = self.worldLogic[self.workTile[0]][
                    self.workTile[1]].split("-")
                main_logic = logic[0]
                sec_logic = logic[1]
                prop = logic[2].split(",")
                if main_logic == "3":  # Chest
                    pass
                elif main_logic == "6":  # Puerta
                    p = pop(['Nueva puerta', self.images['door'],
                             'new_door', 145, 290, prop[0], prop[1]])
                    p.w.mainloop(1)
                    if p.sent:
                        self.worldLogic[self.workTile[0]][
                            self.workTile[1]] = main_logic + "-" + sec_logic + "-" + p.values[0] + ',' + replaceStrict(
                            p.values[1])
                    del p
                elif main_logic == "7":  # Edificio
                    pass
                elif main_logic == "8":  # Mob
                    # Se agrega vector para evitar errores
                    if len(prop) == 18:
                        pass
                    elif len(prop) == 17:
                        prop += ["%NOSOUND%"]
                    elif len(prop) == 15:
                        prop += ["NORMAL", "NORMAL", "%NOSOUND%"]
                    elif len(prop) == 14:
                        prop += [0, "NORMAL", "NORMAL", "%NOSOUND%"]
                    tex = prop[2]
                    if isWindows():
                        p = pop(
                            ['Editar mob', self.images['group'], 'edit_mob', 398, 290, putStrict(prop[5]), prop[1],
                             prop[7],
                             prop[0], prop[9],
                             prop[3], prop[4], prop[8], prop[9], prop[
                                 14], putStrict(prop[6]), putStrict(prop[11]),
                             prop[12], prop[13], prop[15], prop[16], prop[17]])
                    else:
                        p = pop(
                            ['Editar mob', self.images['group'], 'edit_mob', 460, 350, putStrict(prop[5]), prop[1],
                             prop[7],
                             prop[0], prop[9],
                             prop[3], prop[4], prop[8], prop[9], prop[
                                 14], putStrict(prop[6]), putStrict(prop[11]),
                             prop[12], prop[13], prop[15], prop[16], prop[17]])
                    p.w.mainloop(1)
                    if p.sent:
                        data = p.values
                        properties = '8-0-' + data[0] + ',' + data[1] + ',' + tex + ',' + data[3] + ',' + data[4] + ',' \
                                     + replaceStrict(data[5]) + ',' + replaceStrict(data[6]) + ',' + data[7] + ',' + \
                                     data[8] + ',' + data[9] + ',' + \
                                     data[10] + ','
                        if data[11] != '':
                            # Si el mob porta un objeto se agrega
                            properties += replaceStrict(data[11]) + ','
                        else:
                            properties += '%NULL%,'
                        properties += data[12] + ',' + data[13] + ',' + data[14] + ',' + data[15] + ',' + data[
                            16]  # se agregan propiedades de perseguir y escapar
                        properties += ',' + data[17]  # se agrega sonido
                        self.worldLogic[self.workTile[0]][
                            self.workTile[1]] = properties
                    del p
                    self.drawTiles()
                elif main_logic == "11":  # Item
                    pass
                elif main_logic == "13":  # Text
                    q = pop(['Text', self.images['text_ico'],
                             'edit_text', 77, 280, putStrict(prop[0])])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = "13-0-" + replaceStrict(
                            q.values[0])
                    del q
                elif main_logic == "15":  # Object
                    pass
                elif main_logic == "16":  # Libreria
                    pass
                elif main_logic == "17":  # Minushp
                    q = pop(['Minus HP', self.images['minushp_ico'],
                             'edit_absdigit', 77, 280, "Hp:", prop[0]])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = "17-0-" + replaceStrict(
                            q.values[0])
                    del q
                elif main_logic == "18":  # Minusmana
                    q = pop(['Minus mana', self.images['minusmana_ico'],
                             'edit_absdigit', 77, 280, "Mana:", prop[0]])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = "18-0-" + replaceStrict(
                            q.values[0])
                    del q
                elif main_logic == "19" or main_logic == "25":  # Move
                    pass
                elif main_logic == "22":  # Plushp
                    q = pop(['Plus HP', self.images['plushp_ico'],
                             'edit_absdigit', 77, 280, "Hp:", prop[0]])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = "22-0-" + replaceStrict(
                            q.values[0])
                    del q
                elif main_logic == "23":  # Plusmana
                    q = pop(['Plus mana', self.images['plusmana_ico'],
                             'edit_absdigit', 77, 280, "Mana:", prop[0]])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = "23-0-" + replaceStrict(
                            q.values[0])
                    del q
                elif main_logic == "24":  # Teleport
                    q = pop(['Teleport', self.images['teleport_ico'],
                             'edit_maplink', 77, 280, prop[0]])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = "24-0-" + replaceStrict(
                            q.values[0])
                    del q
                elif main_logic == "27":  # Vehicle
                    pass
                elif main_logic == "28":  # Sound
                    q = pop(['Sound', self.images['sound_ico'],
                             'edit_sound', 77, 280, prop[0]])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = "28-0-" + replaceStrict(
                            q.values[0])
                    del q
                elif main_logic == "30":  # Longtext
                    q = pop(['Longtext', self.images['longtext_ico'],
                             'edit_longtext', 77, 280, putStrict(prop[0])])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = "30-0-" + replaceStrict(
                            q.values[0])
                    del q
                elif main_logic == "38":  # Sign
                    q = pop(['Sign', self.images['sign_ico'],
                             'edit_text', 75, 280, putStrict(prop[0])])
                    q.w.mainloop(1)
                    if q.sent:
                        self.worldLogic[self.workTile[0]][
                            self.workTile[1]] = "38-" + sec_logic + "-" + replaceStrict(q.values[0])
                    del q
                elif main_logic == "42":  # Ladder
                    p = pop(['Nueva escalera', self.images['stair_icon'],
                             'edit_stair', 96, 290, putStrict(prop[0])])
                    p.w.mainloop(1)
                    if p.sent:
                        self.worldLogic[self.workTile[0]][self.workTile[1]] = '42-' + sec_logic + '-' + p.values[
                            0] + ',' + replaceStrict(p.values[1])
                    del p
                elif main_logic == "43":  # Npc
                    prop += ["None"]  # se agrega vector para evitar errores
                    tex = prop[1]
                    if isWindows():
                        k = pop(['Editar npc', self.images['group'], 'edit_npc', 307, 290, putStrict(prop[0]),
                                 putStrict(prop[2]), putStrict(
                                     prop[3]), prop[6], prop[8],
                                 putStrict(prop[4]), putStrict(prop[5]), prop[7], prop[9], prop[10]])
                    else:
                        k = pop(['Editar npc', self.images['group'], 'edit_npc', 350, 350, putStrict(prop[0]),
                                 putStrict(prop[2]), putStrict(
                                     prop[3]), prop[6], prop[8],
                                 putStrict(prop[4]), putStrict(prop[5]), prop[7], prop[9], prop[10]])
                    k.w.mainloop(1)
                    if k.sent:
                        npc = k.values
                        properties = "43-0-" + replaceStrict(npc[0]) + ',' + tex + ',' + replaceStrict(
                            npc[2]) + ',' + replaceStrict(npc[3]) + \
                            ',' + replaceStrict(npc[4]) + ',' + replaceStrict(npc[5]) + ',' + npc[6] + ',' + \
                            npc[7] + ',' + npc[8] + ',' + \
                            npc[9] + ',' + npc[10]
                        self.worldLogic[self.workTile[0]][
                            self.workTile[1]] = properties
                    del k
                    self.drawTiles()
                self.isMapEditing = True
                self.core.title(PROGRAM_TITLE + " - " +
                                self.mapName + " (" + self.mapFile + ") *")

        def _item_mousewheel(event):
            """
            Función que atrapa el evento del scrolling y mueve los items
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Si se encuentra en edición
                if 0 <= event.x < 307 and 0 <= event.y < 580:
                    # Se recoge la dirección
                    if isWindows():
                        if -1 * (event.delta / 100) < 0:
                            move = -1
                        else:
                            move = 2
                    else:
                        if -1 * event.delta < 0:
                            move = -1
                        else:
                            move = 2
                    self.menu1.canv.yview_scroll(move, "units")

        def _item_moveup(event):
            """
            Mover hacia arriba la lista de ítems
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Si se encuentra en edición
                self.menu1.canv.yview_scroll(-1, "units")

        def _item_movedown(event):
            """
            Mover hacia abajo la lista de ítems
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Si se encuentra en edición
                self.menu1.canv.yview_scroll(2, "units")

        def _item_moveend(event):
            """
            Mover hasta el final la lista de ítems
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Si se encuentra en edición
                self.menu1.canv.yview_scroll(256, "units")

        def _item_movetop(event):
            """
            Mover hasta el principio la lista de ítems
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Si se encuentra en edición
                self.menu1.canv.yview_scroll(-256, "units")

        def _item_movenext(event):
            """
            Deslizamiento pequeño lista de ítems
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Si se encuentra en edición
                self.menu1.canv.yview_scroll(10, "units")

        def _item_moveprior(event):
            """
            Deslizamiento pequeño lista de ítems
            :param event: Event
            :return: void
            """
            if self.isEvent:  # Si se encuentra en edición
                self.menu1.canv.yview_scroll(-10, "units")

        def _help_actors(e=None):
            """
            Cargar la ayuda de los actores
            :param e: Event
            :return: void
            """
            pop([["Help Actors"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/documentation/actors.txt"])

        def _help_buildings(e=None):
            """
            Cargar la ayuda de los actores
            :param e: Event
            :return: void
            """
            pop([["Help Buildings"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/documentation/buildings.txt"])

        def _help_items(e=None):
            """
            Cargar la ayuda de los items
            :param e: Event
            :return: void
            """
            pop([["Help Items"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/documentation/items.txt"])

        def _help_levelformat(e=None):
            """
            Cargar la ayuda de los formatos de nivel
            :param e: Event
            :return: void
            """
            pop([["Help LevelFormat"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/documentation/levelformat.txt"])

        def _help_logic(e=None):
            """
            Cargar la ayuda de los elementos logicos
            :param e: Event
            :return: void
            """
            pop([["Help Logic"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/documentation/logic.txt"])

        def _help_objetos(e=None):
            """
            Cargar la ayuda de los objetos
            :param e: Event
            :return: void
            """
            pop([["Help Objetos"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/documentation/objetos.txt"])

        def _help_sfx(e=None):
            """
            Cargar la ayuda del sfx (sonido)
            :param e: Event
            :return: void
            """
            pop([["Help Sfx"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/documentation/sfx.txt"])

        def _help_textures(e=None):
            """
            Cargar la ayuda de los elementos de texturas
            :param e: Event
            :return: void
            """
            pop([["Help Textures"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/documentation/textures.txt"])

        def _acercaDe(e=None):
            """
            Cargar el acerca de
            :param e: Event
            :return: void
            """
            pop([["Acerca de", "Creador: ", "Mail: ", "Versión: ", "Cerrar"], self.images["mapeditoricon"], "about",
                 115, 220, AUTOR, AUTOR_EMAIL, PROGRAM_VERSION])

        def _ayuda(e=None):
            """
            Cargar la ayuda
            :param e: Event
            :return: void
            """
            pop([["Ayuda"], self.images["text_icon"], "license",
                 400, 600, DATA_DOCUMENTS + "/mapeditor/ayuda.txt"])

        def _changelog(e=None):
            """
            Cargar la lista de cambios
            :param e: Event
            :return: void
            """
            pop([["Changelog"], self.images["text_icon"], "license", 400, 600,
                 DATA_DOCUMENTS + "/mapeditor/changelog.txt"])

        def _licencia(e=None):
            """
            Cargar la licencia del programa
            :param e: Event
            :return: void
            """
            pop([["Licencia"], self.images["text_icon"],
                 "license", 400, 600, "LICENSE"])

        # Ventana de programa
        self.core = Tk()
        self.core.title(PROGRAM_TITLE)
        self.core.minsize(width=PROGRAM_SIZE[0], height=PROGRAM_SIZE[1])
        self.core.resizable(width=False, height=False)
        self.core.geometry(
            '%dx%d+%d+%d' % (PROGRAM_SIZE[0], PROGRAM_SIZE[1], (self.core.winfo_screenwidth() - PROGRAM_SIZE[0]) / 2,
                             (self.core.winfo_screenheight() - PROGRAM_SIZE[1] - 50) / 2))
        self.core.focus_force()

        # Variables del programa
        self.actualActor = -1
        self.actualEnvironment = -1
        self.actualTexture = -1
        self.botones = list()
        # almacena la información copiada y pegada
        self.clipboard = ["", "", "", ""]
        self.font = tkFont.Font(family="ansi", size=5)
        self.isEvent = False
        self.isMapEditing = False
        self.isNewMapCreating = False
        self.mapAutor = "%MAPAUTOR%"
        self.mapDescription = "%MAPDESCRIPTION"
        self.mapFile = ""
        self.mapName = "%MAPNAME%"
        self.mapSize = [0, 0]  # columnas, filas
        self.mapSound = "%MAPSOUND%"
        self.maxLength = [19, 18]  # máximo largo del mapa
        self.showEvents = True
        self.showItems = True
        self.showLines = False
        self.showLogics = False
        self.showMovement = True
        self.showNumbers = False
        self.showTerrain = True
        self.workTile = [-1, -1]  # tile de trabajo
        self.worldDay = 0
        self.worldGraph = list()
        self.worldItems = list()
        self.worldLight = list()
        self.worldLightVectors = list()
        self.worldLogic = list()
        self.worldTextures = list()
        print "Cargando texturas ...",
        self.images = mapEditorTextures().images
        print "ok"

        # Se carga la interfaz
        print "Cargando interfaz ...",
        # icono del programa
        self.core.iconbitmap(self.images["mapeditoricon"])
        menu = Menu(self.core)
        self.core.config(menu=menu)
        self.archivomenu = Menu(menu, tearoff=0)
        self.archivomenu.add_command(
            label="Nuevo Mapa", accelerator="Ctrl+N", command=self.newMap)
        self.archivomenu.add_command(
            label="Cargar Mapa", accelerator="Ctrl+L", command=self.loadMap)
        self.archivomenu.add_separator()
        self.archivomenu.add_command(
            label="Guardar Mapa", accelerator="Ctrl+S", command=self.saveMap)
        self.archivomenu.add_command(
            label="Guardar Como", accelerator="Ctrl+G", command=_saveas)
        self.archivomenu.add_separator()
        self.archivomenu.add_command(
            label="Cerrar Mapa", accelerator="Ctrl+Q", command=self.showOn)
        self.archivomenu.add_command(
            label="Salir", accelerator="Ctrl+E", command=self.endCoreMap)
        menu.add_cascade(label="Archivo", menu=self.archivomenu)
        self.archivomenu.entryconfig(3, state=DISABLED)
        self.archivomenu.entryconfig(4, state=DISABLED)
        self.archivomenu.entryconfig(6, state=DISABLED)
        self.herrammenu = Menu(menu, tearoff=0)
        self.herrammenu.add_command(
            label='Borrar actor', accelerator="Ctrl+J", command=_delactor)
        self.herrammenu.add_command(
            label='Borrar decoración', accelerator="Ctrl+U", command=_deldecoration)
        self.herrammenu.add_command(
            label='Borrar terreno', accelerator="Ctrl+K", command=_delterrain)
        self.herrammenu.add_command(
            label='Borrar seleción actual', accelerator="Esc", command=self.delActive)
        self.herrammenu.add_command(
            label='Establecer sonido de fondo', accelerator="Ctrl+M", command=_changeSound)
        for k in range(5):
            self.herrammenu.entryconfig(k, state=DISABLED)
        menu.add_cascade(label='Herramientas', menu=self.herrammenu)
        self.visualmenu = Menu(menu, tearoff=0)
        self.visualmenu.add_command(
            label='Mostrar/Ocultar eventos', accelerator="F6", command=_events)
        self.visualmenu.add_command(
            label='Mostrar/Ocultar items', accelerator="F7", command=_items)
        self.visualmenu.add_command(
            label='Mostrar/Ocultar lineas', accelerator="F1", command=_lines)
        self.visualmenu.add_command(
            label='Mostrar/Ocultar lógicos', accelerator="F3", command=_logics)
        self.visualmenu.add_command(
            label='Mostrar/Ocultar movimientos', accelerator="F4", command=_movements)
        self.visualmenu.add_command(
            label='Mostrar/Ocultar posiciones', accelerator="F2", command=_numbers)
        self.visualmenu.add_command(
            label='Mostrar/Ocultar terreno', accelerator="F8", command=_terrain)
        self.visualmenu.add_command(
            label='Redibujar mapa', accelerator="F5", command=_redib)
        for k in range(8):
            self.visualmenu.entryconfig(k, state=DISABLED)
        menu.add_cascade(label='Visualización', menu=self.visualmenu)
        ayudamenu = Menu(menu, tearoff=0)
        ayudamenu.add_command(label='Acerca de', command=_acercaDe)
        ayudamenu.add_command(
            label='Ayuda', command=_ayuda, accelerator="Ctrl+A")
        ayudamenu.add_command(label='Changelog', command=_changelog)
        ayudamenu.add_command(label='Licencia', command=_licencia)
        ayudamenu.add_separator()
        ayudamenu.add_command(
            label='Actors', command=_help_actors, accelerator="Ctrl+1")
        ayudamenu.add_command(
            label='Buildings', command=_help_buildings, accelerator="Ctrl+2")
        ayudamenu.add_command(
            label='Items', command=_help_items, accelerator="Ctrl+3")
        ayudamenu.add_command(label='Level format',
                              command=_help_levelformat, accelerator="Ctrl+4")
        ayudamenu.add_command(
            label='Logic', command=_help_logic, accelerator="Ctrl+5")
        ayudamenu.add_command(
            label='Objetos', command=_help_objetos, accelerator="Ctrl+6")
        ayudamenu.add_command(
            label='Sfx', command=_help_sfx, accelerator="Ctrl+7")
        ayudamenu.add_command(
            label='Textures', command=_help_textures, accelerator="Ctrl+8")
        menu.add_cascade(label="Ayuda", menu=ayudamenu)
        self.infoMenu = Menu(self.core, tearoff=0)  # menú normal
        self.infoMenu.add_command(label="Información", command=_infoTile_info)
        self.infoMenu.add_separator()
        self.infoMenu.add_command(label="Borrar", command=_infoTile_delete)
        self.infoMenu.add_command(label="Copiar", command=_copyTile)
        self.infoMenu.add_command(label="Pegar", command=_pasteTile)
        self.infoEditMenu = Menu(self.core, tearoff=0)  # menú editable
        self.infoEditMenu.add_command(
            label="Información", command=_infoTile_info)
        self.infoEditMenu.add_separator()
        self.infoEditMenu.add_command(label="Borrar", command=_infoTile_delete)
        self.infoEditMenu.add_command(label="Copiar", command=_copyTile)
        self.infoEditMenu.add_command(label="Editar", command=_infoTile_edit)
        self.infoEditMenu.add_command(label="Pegar", command=_pasteTile)
        self.blackBackground = Canvas(
            self.core, width=1500, height=1000, bg="black", bd=-2, highlightthickness=0)
        self.blackBackground.pack(padx=0, pady=0)
        text_color_title = "#1F1F1F"
        self.menu1 = VerticalScrolledFrame(self.core)
        l1 = LabelFrame(self.menu1.interior, text="Nombre del mapa",
                        foreground=text_color_title, padx=3, pady=2)
        l1.pack(padx=0, pady=3)
        self.infoNameMap = Label(
            l1, width=38, justify=LEFT, anchor=W, wraplength=380)
        self.infoNameMap.pack(anchor=NW)
        l5 = LabelFrame(self.menu1.interior, text="Autor del mapa",
                        foreground=text_color_title, padx=3, pady=2)
        l5.pack(padx=0, pady=3)
        self.infoAutorMap = Label(
            l5, width=38, justify=LEFT, anchor=W, wraplength=380)
        self.infoAutorMap.pack(anchor=NW)
        l2 = LabelFrame(self.menu1.interior, text="Descripción",
                        foreground=text_color_title, padx=3, pady=2)
        l2.pack(padx=0, pady=5)
        self.infoDescriptionMap = Label(
            l2, width=38, wraplength=270, justify=LEFT, anchor=W)
        self.infoDescriptionMap.pack(anchor=NW)
        l14 = LabelFrame(self.menu1.interior, text="Sonido de fondo",
                         foreground=text_color_title, padx=3, pady=2)
        l14.pack(padx=0, pady=5)
        self.infoSoundMap = Label(
            l14, width=38, wraplength=270, justify=LEFT, anchor=W)
        self.infoSoundMap.pack(anchor=NW)
        l14.config(cursor="hand2")
        l14.bind("<Button-1>", _changeSound)
        self.infoSoundMap.bind("<Button-1>", _changeSound)
        bpf = 8
        bpfg = bpf / 2
        bbpfg = bpfg / 2
        l3 = LabelFrame(self.menu1.interior, text="Actores - Eventos de usuario", foreground=text_color_title, padx=3,
                        pady=3, relief=GROOVE)
        l3.pack(padx=3, pady=5, anchor=NW)
        j = 0
        for i in range(redondear(len(actores), bpf)):
            f = Frame(l3)
            f.pack()
            for k in range(bpf):
                cmd = partial(self.setActive, 1, actores[j][0], actores[j][1])
                bt = Button(f, image=self.images[actores[j][
                            0]], command=cmd, relief=GROOVE, border=0, cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT)
                else:
                    bt.pack()
                j += 1
                if j == len(actores):
                    break
        if isWindows():
            labeltitle = "Terreno\t\t\t\t             [32x32]"
        else:
            labeltitle = "Terreno\t\t\t                 [32x32]"
        l4 = LabelFrame(self.menu1.interior, text=labeltitle, foreground=text_color_title,
                        padx=3, pady=3, relief=GROOVE)
        l4.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(terrain), bpf)):
            f = Frame(l4)
            f.pack()
            for k in range(bpf):
                cmd = partial(self.setActive, 2, terrain[j][
                              0], terrain[j][1])  # Boton del objeto
                bt = Button(f, image=self.images[terrain[j][
                            0]], command=cmd, relief=GROOVE, border=0, cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT)
                else:
                    bt.pack()
                j += 1
                if j == len(terrain):
                    break
        if isWindows():
            labeltitle = "Ambientación\t\t\t             [32x32]"
        else:
            labeltitle = "Ambientación\t\t                 [32x32]"
        l6 = LabelFrame(self.menu1.interior, text=labeltitle, foreground=text_color_title,
                        padx=3, pady=3, relief=GROOVE)
        l6.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(environment), bpf)):
            f = Frame(l6)
            f.pack()
            for k in range(bpf):
                cmd = partial(self.setActive, 3, environment[j][
                              0], environment[j][1], environment[j][2])
                bt = Button(f, image=self.images[environment[j][0]], command=cmd, relief=GROOVE, border=0,
                            cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT)
                else:
                    bt.pack()
                j += 1
                if j == len(environment):
                    break
        if isWindows():
            labeltitle = "Ambientación\t\t\t             [64x64]"
        else:
            labeltitle = "Ambientación\t\t                    [64x64]"
        l10 = LabelFrame(self.menu1.interior, text=labeltitle,
                         foreground=text_color_title, padx=6, pady=3, relief=GROOVE)
        l10.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(benvironment), bpfg)):
            f = Frame(l10)
            f.pack()
            for k in range(bpfg):
                cmd = partial(self.setActive, 3, benvironment[j][
                              0], benvironment[j][1], benvironment[j][2])
                bt = Button(f, image=self.images[benvironment[j][0]], command=cmd, relief=GROOVE, border=0,
                            cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT)
                else:
                    bt.pack()
                j += 1
                if j == len(benvironment):
                    break
        if isWindows():
            labeltitle = "Decoración - Interior \t\t             [32x32]"
        else:
            labeltitle = "Decoración - Interior \t                 [32x32]"
        l7 = LabelFrame(self.menu1.interior, text=labeltitle,
                        foreground=text_color_title, padx=3, pady=5, relief=GROOVE)
        l7.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(interior), bpf)):
            f = Frame(l7)
            f.pack()
            for k in range(bpf):
                cmd = partial(self.setActive, 3, interior[j][
                              0], interior[j][1], interior[j][2])
                bt = Button(f, image=self.images[interior[j][
                            0]], command=cmd, relief=GROOVE, border=0, cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT)
                else:
                    bt.pack()
                j += 1
                if j == len(interior):
                    break
        if isWindows():
            labeltitle = "Decoración - Interior \t\t             [64x64]"
        else:
            labeltitle = "Decoración - Interior \t                    [64x64]"
        l12 = LabelFrame(self.menu1.interior, text=labeltitle,
                         foreground=text_color_title, padx=3, pady=5, relief=GROOVE)
        l12.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(binterior), bpfg)):
            f = Frame(l12)
            f.pack()
            for k in range(bpfg):
                cmd = partial(self.setActive, 3, binterior[j][
                              0], binterior[j][1], binterior[j][2])
                bt = Button(f, image=self.images[binterior[j][
                            0]], command=cmd, relief=GROOVE, border=0, cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT)
                else:
                    bt.pack()
                j += 1
                if j == len(binterior):
                    break
        if isWindows():
            labeltitle = "Construcción \t\t\t             [32x32]"
        else:
            labeltitle = "Construcción \t\t                 [32x32]"
        l9 = LabelFrame(self.menu1.interior, text=labeltitle,
                        foreground=text_color_title, padx=3, pady=5, relief=GROOVE)
        l9.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(construccion), bpf)):
            f = Frame(l9)
            f.pack()
            for k in range(bpf):
                cmd = partial(self.setActive, 3, construccion[j][0], construccion[j][1],
                              construccion[j][2])  # Boton del objeto
                bt = Button(f, image=self.images[construccion[j][0]], command=cmd, relief=GROOVE, border=0,
                            cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT, anchor=W)
                else:
                    bt.pack()
                j += 1
                if j == len(construccion):
                    break
        if isWindows():
            labeltitle = "Construcción \t\t\t             [64x64]"
        else:
            labeltitle = "Construcción \t\t                    [64x64]"
        l11 = LabelFrame(self.menu1.interior, text=labeltitle,
                         foreground=text_color_title, padx=3, pady=5, relief=GROOVE)
        l11.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(bconstruccion), bpfg)):
            f = Frame(l11)
            f.pack()
            for k in range(bpfg):
                cmd = partial(self.setActive, 3, bconstruccion[j][
                              0], bconstruccion[j][1], bconstruccion[j][2])
                bt = Button(f, image=self.images[bconstruccion[j][0]], command=cmd, relief=GROOVE, border=0,
                            cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT, anchor=W)
                else:
                    bt.pack()
                j += 1
                if j == len(bconstruccion):
                    break
        if isWindows():
            labeltitle = "Edificios\t\t\t\t         [128x128]"
        else:
            labeltitle = "Edificios\t\t\t                [128x128]"
        l13 = LabelFrame(self.menu1.interior, text=labeltitle, foreground=text_color_title,
                         padx=3, pady=5, relief=GROOVE)
        l13.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(bbuilding), bbpfg)):
            f = Frame(l13)
            f.pack()
            for k in range(bbpfg):
                cmd = partial(self.setActive, 3, bbuilding[j][
                              0], bbuilding[j][1], bbuilding[j][2])
                bt = Button(f, image=self.images[bbuilding[j][
                            0]], command=cmd, relief=GROOVE, border=0, cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT)
                else:
                    bt.pack()
                j += 1
                if j == len(bbuilding):
                    break
        if isWindows():
            labeltitle = "Edificios\t\t\t\t             [32x32]"
        else:
            labeltitle = "Edificios\t\t\t               [32x32]"
        l8 = LabelFrame(self.menu1.interior, text=labeltitle, foreground=text_color_title,
                        padx=3, pady=5, relief=GROOVE)
        l8.pack(padx=3, pady=6, anchor=NW)
        j = 0
        for i in range(redondear(len(building), bpf)):
            f = Frame(l8)
            f.pack()
            for k in range(bpf):
                cmd = partial(self.setActive, 3, building[j][
                              0], building[j][1], building[j][2])
                bt = Button(f, image=self.images[building[j][
                            0]], command=cmd, relief=GROOVE, border=0, cursor="hand2")
                if k != bpf - 1:
                    bt.pack(side=LEFT, anchor=W)
                else:
                    bt.pack(anchor=W)
                j += 1
                if j == len(building):
                    break
        self.menu2 = Frame(self.core, border=0)
        self.mapTile = Canvas(self.menu2, width=608, height=576, bg="#000000")
        self.mapTile.pack(pady=0, padx=0)

        # Eventos del programa
        print "ok"
        print "Cargando eventos ...",
        self.core.bind("<MouseWheel>", _item_mousewheel)
        self.core.bind("<Up>", _item_moveup)
        self.core.bind("<Down>", _item_movedown)
        self.core.bind("<Down>", _item_movedown)
        self.core.bind("<End>", _item_moveend)
        self.core.bind("<Home>", _item_movetop)
        self.core.bind("<Next>", _item_movenext)
        self.core.bind("<Prior>", _item_moveprior)
        self.core.bind("<Control-1>", _help_actors)
        self.core.bind("<Control-2>", _help_buildings)
        self.core.bind("<Control-3>", _help_items)
        self.core.bind("<Control-4>", _help_levelformat)
        self.core.bind("<Control-5>", _help_logic)
        self.core.bind("<Control-6>", _help_actors)
        self.core.bind("<Control-7>", _help_sfx)
        self.core.bind("<Control-8>", _help_textures)
        self.core.bind("<Control-N>", self.newMap)
        self.core.bind("<Control-n>", self.newMap)
        self.core.bind("<Control-L>", self.loadMap)
        self.core.bind("<Control-l>", self.loadMap)
        self.core.bind("<Control-A>", _ayuda)
        self.core.bind("<Control-a>", _ayuda)
        self.core.bind("<Control-S>", self.saveMap)
        self.core.bind("<Control-s>", self.saveMap)
        self.core.bind("<Control-G>", _saveas)
        self.core.bind("<Control-g>", _saveas)
        self.core.bind("<Control-Q>", self.showOn)
        self.core.bind("<Control-q>", self.showOn)
        self.core.bind("<Control-E>", self.endCoreMap)
        self.core.bind("<Control-e>", self.endCoreMap)
        self.core.bind("<Control-M>", _changeSound)
        self.core.bind("<Control-m>", _changeSound)
        self.core.bind("<Control-M>", _changeSound)
        self.core.bind("<Control-m>", _changeSound)
        self.core.bind("<Control-J>", _delactor)
        self.core.bind("<Control-j>", _delactor)
        self.core.bind("<Control-K>", _delterrain)
        self.core.bind("<Control-k>", _delterrain)
        self.core.bind("<Control-U>", _deldecoration)
        self.core.bind("<Control-u>", _deldecoration)
        self.core.bind("<Escape>", self.delActive)
        self.core.bind("<F1>", _lines)
        self.core.bind("<F2>", _numbers)
        self.core.bind("<F3>", _logics)
        self.core.bind("<F4>", _movements)
        self.core.bind("<F5>", _redib)
        self.core.bind("<F6>", _events)
        self.core.bind("<F7>", _items)
        self.core.bind("<F8>", _terrain)
        self.core.protocol("WM_DELETE_WINDOW", self.endCoreMap)
        print "ok"
        print "Estado ... ok"

    def endCoreMap(self, e=None):
        """
        Salir del programa, y destruirlo
        :param e: Event
        :return: void
        """
        if self.isMapEditing:
            e = pop(["Guardar", self.images["alert_icon"],
                     "deseaGuardar", 75, 250, "Error al guardar el mapa"])
            e.w.mainloop(1)
            if e.sent:
                if e.values[0] == "si":
                    self.saveMap()
                elif e.values[0] == "no":
                    pass
                else:
                    return
            del e
        if isWindows():
            os.system("taskkill /PID " + str(os.getpid()) + " /F")
        else:
            import signal

            os.kill(os.getpid(), signal.SIGKILL)

    def drawTiles(self):
        """
        Dibuja los tiles del mapa
        :return: void
        """
        self.mapTile.delete(ALL)
        if self.showItems:
            for j in range(self.mapSize[1]):  # Items
                for i in range(self.mapSize[0]):
                    # Si existe una imagen la agrego al mundo
                    if self.worldItems[j][i] != "None" and not isIn(self.worldItems[j][i], EVENT_IMAGE_EDITOR):
                        imagen = self.mapTile.create_image(
                            18 + 32 * i +
                            textureMover(
                                self.images[self.worldItems[j][i]], EJE_X),
                            18 + 32 * j +
                            textureMover(
                                self.images[self.worldItems[j][i]], EJE_Y),
                            image=self.images[self.worldItems[j][i]])
                        # Compruebo la imagen para ver el zindex
                        if isIn(self.worldItems[j][i], LOWER_TEXTURES):
                            self.mapTile.lower(imagen)
        if self.showEvents:  # Si se pueden dibujar los eventos
            for j in range(self.mapSize[1]):  # Eventos
                for i in range(self.mapSize[0]):
                    if isIn(self.worldItems[j][i], EVENT_IMAGE_EDITOR):
                        self.mapTile.create_image(18 + 32 * i + textureMover(self.images[self.worldItems[j][i]], EJE_X),
                                                  18 + 32 * j +
                                                  textureMover(
                                                      self.images[self.worldItems[j][i]], EJE_Y),
                                                  image=self.images[self.worldItems[j][i]])
        if self.showTerrain:  # Si se pueden dibujar las texturas de terreno
            for j in range(self.mapSize[1]):  # Texturas de terreno
                for i in range(self.mapSize[0]):
                    self.mapTile.lower(self.mapTile.create_image(18 + 32 * i, 18 + 32 * j, image=self.images[
                        self.worldGraph[j][i]]))  # @UndefinedVariable
        # Dibujo la información de los tiles
        if self.showLines != False or self.showNumbers != False or self.showLogics != False:
            for i in range(0, self.mapSize[1]):
                if self.showLines:
                    self.mapTile.create_line(32 * (i + 1) + 1, 0, 32 * (i + 1) + 1,
                                             self.mapSize[1] * 32 + 2, fill=COLOR_LINE)
                k = -32
                for j in range(0, self.mapSize[0]):
                    k += 32
                    if self.showLines:
                        self.mapTile.create_line(0, 32 * (i + 1) + 1, self.mapSize[0] * 32 + 2,
                                                 32 * (i + 1) + 1, fill=COLOR_LINE)
                    if self.showNumbers:
                        if i < 10 <= j or i >= 10 > j:
                            add = "  "
                        elif i < 10 and j < 10:
                            add = "    "
                        else:
                            add = ""
                        self.mapTile.create_text(k + 14, 32 * (i + 1) - 27, text=add + str(j) + "," + str(i), anchor=W,
                                                 font=self.font, fill=COLOR_INFO)
                    if self.showLogics:
                        try:
                            logic = LOGICS[self.worldLogic[i][j].split("-")[0]]
                        except:
                            logic = ""
                        self.mapTile.create_text(
                            k + 17, 32 * (i + 1) - 3, text=logic, font=self.font, fill=COLOR_INFO)
        if self.showMovement:  # Dibujo el movimiento de los npc y mob
            for j in range(self.mapSize[1]):
                for i in range(self.mapSize[0]):
                    # Si se encuentra un actor (mob o npc)
                    if "actor" in self.worldItems[j][i]:
                        actor = self.worldLogic[j][i].split("-")
                        if actor[0] == "8":  # Si es un mob
                            prop = actor[2].split(",")
                            velocidad = int(prop[4])
                            mov = int(prop[8])
                            try:
                                maxdist = int(prop[14])
                            except:
                                maxdist = 0
                            if velocidad > 0 and mov > 0 and maxdist != 0:
                                self.setImageSquare(i, j, maxdist,
                                                    COLOR_MOVEMENT[0])
                        elif actor[0] == "43":  # Si es un npc
                            prop = actor[2].split(",")
                            move = prop[7]
                            dist = int(prop[8])
                            if move.upper() == "TRUE":
                                self.setImageSquare(
                                    i, j, dist, COLOR_MOVEMENT[1])

    def showOff(self, e=None):
        """
        Ocultar la pantalle de negro
        :param e: Event
        :return: void
        """
        self.blackBackground.pack_forget()
        self.menu1.pack(side=LEFT, fill=Y)
        self.menu2.pack()
        self.archivomenu.entryconfig(3, state=NORMAL)
        self.archivomenu.entryconfig(4, state=NORMAL)
        self.archivomenu.entryconfig(6, state=NORMAL)
        for k in range(5):
            self.herrammenu.entryconfig(k, state=NORMAL)
        for k in range(8):
            self.visualmenu.entryconfig(k, state=NORMAL)
        self.mapTile.bind("<Button-1>", self.editTile)
        if isWindows():
            self.mapTile.bind("<ButtonRelease-3>", self.infoTile)
        else:
            self.mapTile.bind("<ButtonRelease-2>", self.infoTile)

    def showOn(self, e=None):
        """
        Muestra la pantalla de negro
        :param e: Event
        :return: void
        """
        if self.isEvent:
            self.isEvent = False
            self.isMapEditing = False
            delMatrix(self.worldTextures)
            delMatrix(self.worldLight)
            delMatrix(self.worldLogic)
            delMatrix(self.worldGraph)
            delMatrix(self.worldItems)
            delMatrix(self.worldLightVectors)
            self.delActive()
            self.menu1.pack_forget()
            self.menu2.pack_forget()
            self.archivomenu.entryconfig(3, state=DISABLED)
            self.archivomenu.entryconfig(4, state=DISABLED)
            self.archivomenu.entryconfig(6, state=DISABLED)
            for k in range(5):
                self.herrammenu.entryconfig(k, state=DISABLED)
            for k in range(8):
                self.visualmenu.entryconfig(k, state=DISABLED)
            self.blackBackground.pack()
            self.core.title(PROGRAM_TITLE)
            self.mapTile.bind("<Button-1>", self.breakpoint)
            if isWindows():
                self.mapTile.bind("<ButtonRelease-3>", self.breakpoint)
            else:
                self.mapTile.bind("<ButtonRelease-2>", self.breakpoint)

    def newMap(self, e=None):
        """
        Nuevo mapa
        :param e: Event
        :return: void
        """
        if not self.isNewMapCreating:  # Si no hay una ventana abierta
            self.isNewMapCreating = True  # Se establece que hay una ventana abierta
            vpop = pop(
                ["Nuevo Mapa", self.images["mapeditoricon"], "new_map", 280, 300])  # Ventana consultora de información
            vpop.w.mainloop(1)
            if vpop.sent:  # Si los datos fueron enviados
                datos = vpop.values
                self.mapName = datos[0]  # cargo los datos
                self.mapDescription = datos[1]
                self.mapSize[0] = datos[4]
                self.mapSize[1] = datos[5]
                self.mapAutor = datos[6]
                self.mapSound = "%MAPSOUND%"
                self.setMapName()  # escribo la información en el frame
                self.setDescriptionMap()
                self.setAutorMap()
                self.setSoundMap()
                self.setMapTiles(datos[2], datos[3])  # creo el mundo
                self.drawTiles()  # dibujo el mundo
                self.showOff()  # oculto la ventana negra inicial
                self.isMapEditing = True  # variables lógicas del programa
                self.isEvent = True  # comienzan los eventos de ventana
                self.clipboard = ["", "", "", ""]
                # se mueven los items al principio
                self.menu1.canv.yview_scroll(-256, "units")
                self.worldDay = datos[2]  # si es de dia / noche
                self.mapFile = self.mapName.replace(
                    " ", "").strip().lower() + ".lvl"
            del vpop
            self.isNewMapCreating = False  # termina la ventana abierta

    def saveMap(self, e=None):
        """
        Guardar un mapa
        :param e: Event
        :return: void
        """
        try:
            if self.isMapEditing or e == "save_as":  # Si se han realizado cambios para guardar
                if e == "save_as" or self.mapFile == "":
                    nameFile = asksaveasfilename(title="Guardar mapa", initialdir=DATA_LEVELS,
                                                 initialfile=self.mapFile, defaultextension=".lvl",
                                                 filetypes=[("Archivo de mapa de HOA", ".lvl")])
                else:
                    nameFile = DATA_LEVELS + self.mapFile
                if len(nameFile) > 0:  # Si el nombre del archivo es valido
                    archivo = open(nameFile, "w")  # creo nuevo archivo
                    archivo.write(self.mapName + "\n")
                    archivo.write(self.mapAutor + "\n")
                    archivo.write(
                        str(self.mapSize[0]) + "," + str(self.mapSize[1]) + "\n")
                    archivo.write(self.mapDescription + "\n")
                    archivo.write(self.mapSound + "\n\n")
                    for k in range(self.mapSize[1]):  # Contenido
                        l = ""
                        for j in range(self.mapSize[0]):
                            # Agrego la información de cada matriz
                            if j != self.mapSize[0] - 1:
                                l += str(self.worldLight[k][j]) + ":" + str(self.worldLogic[k][j]) + ":" + str(
                                    self.worldTextures[k][j]) + ";"
                            else:
                                l += str(self.worldLight[k][j]) + ":" + str(self.worldLogic[k][j]) + ":" + str(
                                    self.worldTextures[k][j])
                        archivo.write(l + "\n")
                    archivo.flush()
                    archivo.close()
                    namefile = str(nameFile).replace(
                        DATA_LEVELS, LEVEL_PROP).replace(".lvl", ".prop")
                    # archivo de vectores luminicos
                    archivo2 = open(namefile, "w")
                    archivo2.write(str(self.worldDay) + "\n")
                    self.worldLightVectors.sort()
                    for vector in self.worldLightVectors:
                        archivo2.write(vector + "\n")
                    archivo2.close()
                    self.isMapEditing = False  # no hay cambios sin guardar
                    self.core.title(PROGRAM_TITLE + " - " +
                                    self.mapName + " (" + self.mapFile + ")")
        except:  # Si ocurre algún error en el proceso de guardado
            self.core.title(PROGRAM_TITLE + " - " + self.mapName + "!")
            pop(["Error", self.images["alert_icon"], "error",
                 70, 270, "Error al guardar el mapa"])

    def editTile(self, e=None):
        """
        Editar un tile
        :param e: Event
        :return: void
        """
        if self.isMapEditing == False and (
                self.actualActor != -1 or self.actualEnvironment != -1 or self.actualTexture != -1):
            self.isMapEditing = True
        tile = whatTile(e.x, e.y)
        if 0 <= tile[0] < self.mapSize[1] and 0 <= tile[1] < self.mapSize[
                0]:  # Compruebo el tile si esta dentro del mapa
            if self.isMapEditing:
                self.core.title(PROGRAM_TITLE + " - " +
                                self.mapName + " (" + self.mapFile + ") *")
            if self.actualTexture != -1:  # Si lo seleccionado es una textura
                t = self.actualTexture[0]  # se aplica lógica
                obj = self.worldLogic[tile[0]][
                    tile[1]].split("-")  # objeto en el tile
                if t in TEXTURE_WATER or t in TEXTURE_LAVA and obj[
                        0] != "12":  # Si la textura es agua o lava y el tile no tiene un objeto
                    obj[0] = "4"  # si agrega la información lógica
                    if t in TEXTURE_LAVA:
                        self.addLightVector(tile[1], tile[0], 1)  # Si era lava
                else:
                    if obj[0] == "4":  # Si el objeto previo era un tile de agua o liquido
                        obj[0] = "0"  # no tiene lógica
                        prevTex = self.worldTextures[tile[0]][
                            tile[1]]  # se almacena la textura previa
                        if prevTex in TEXTURE_LAVA:
                            self.removeLightVector(tile[1],
                                                   tile[0])  # si la textura contenia lava
                # actualización de la matriz lógica
                self.worldLogic[tile[0]][tile[1]] = "-".join(obj)
                self.worldTextures[tile[0]][tile[1]] = self.actualTexture[
                    0]  # se actualiza la matriz de texturas
                if self.worldLight[tile[0]][tile[1]] == 0:
                    self.worldGraph[tile[0]][tile[1]] = self.actualTexture[1]
                else:
                    self.worldGraph[tile[0]][tile[1]] = self.actualTexture[
                        1].replace("_0", "_1")
            elif self.actualEnvironment != -1:  # Si lo seleccionado es una decoracion o edificio
                item = self.worldLogic[tile[0]][tile[1]].split("-")
                if item[0] not in TILE_EVENT:  # Si el tile seleccionado no tiene un mob o evento
                    delTileLogicNeighbor(self.worldLogic[tile[0]][tile[1]], tile[0], tile[1], self.worldLogic,
                                         self.worldItems)
                    if item[1] in BUILD_TORCHES_ID:
                        self.removeLightVector(tile[1], tile[0])
                    # Si el item es algo especial, una llave o puerta, etc
                    if self.actualEnvironment[0] == "special":
                        tipo = self.actualEnvironment[3]
                        if tipo == "door" or tipo == "building":
                            self.worldLogic[tile[0]][
                                tile[1]] = self.actualEnvironment[2]
                            if self.worldLight[tile[0]][tile[1]] == 0:
                                self.worldItems[tile[0]][
                                    tile[1]] = self.actualEnvironment[1]
                            else:
                                self.worldItems[tile[0]][tile[1]] = self.actualEnvironment[
                                    1].replace("_0", "_1")
                        elif tipo == "volcan":
                            if "14" or "7-407" or "39-961" in self.worldLogic[tile[0]][
                                    tile[1]]:  # Si había una antorcha antes se elimina
                                self.removeLightVector(tile[1], tile[0])
                            self.worldLogic[tile[0]][
                                tile[1]] = self.actualEnvironment[2]
                            self.worldItems[tile[0]][
                                tile[1]] = self.actualEnvironment[1]
                            self.addLightVector(tile[1], tile[0], 1)
                        elif tipo == "antorcha":
                            if "14" or "7-407" or "39-961" in self.worldLogic[tile[0]][
                                    tile[1]]:  # Si había una antorcha antes se elimina
                                self.removeLightVector(tile[1], tile[0])
                            self.worldLogic[tile[0]][
                                tile[1]] = self.actualEnvironment[2]
                            self.worldItems[tile[0]][
                                tile[1]] = self.actualEnvironment[1]
                            self.addLightVector(
                                tile[1], tile[0], self.actualEnvironment[4])
                        elif tipo == "sign":
                            self.worldLogic[tile[0]][tile[1]] = self.actualEnvironment[2] + "-" + \
                                self.actualEnvironment[4]
                            if self.worldLight[tile[0]][tile[1]] == 0:
                                self.worldItems[tile[0]][
                                    tile[1]] = self.actualEnvironment[1]
                            else:
                                self.worldItems[tile[0]][tile[1]] = self.actualEnvironment[
                                    1].replace("_0", "_1")
                    # Si el item es "trash" para borrar el item
                    elif self.actualEnvironment[0] == "delete":
                        if item[0] == "4":
                            self.worldLogic[tile[0]][
                                tile[1]] = "4-0"  # Si es agua
                        self.worldLogic[tile[0]][tile[1]] = "0-0"
                        self.worldItems[tile[0]][tile[1]] = "None"
                    else:  # Si es un item normal
                        self.worldLogic[tile[0]][
                            tile[1]] = self.actualEnvironment[0]
                        if self.worldLight[tile[0]][tile[1]] == 0:
                            self.worldItems[tile[0]][
                                tile[1]] = self.actualEnvironment[1]
                        else:
                            self.worldItems[tile[0]][tile[1]] = self.actualEnvironment[
                                1].replace("_0", "_1")
                    logicTileCorrection(self.worldLogic[tile[0]][tile[1]], tile[0], tile[1], self.worldLogic,
                                        self.worldItems)
            elif self.actualActor != -1:  # Si es un mob o evento de jugador
                tipo = self.actualActor[2]
                if tipo == "mob":
                    if self.worldLight[tile[0]][tile[1]] == 0:
                        self.worldItems[tile[0]][tile[1]] = self.actualActor[0]
                    else:
                        self.worldItems[tile[0]][tile[1]] = self.actualActor[
                            0].replace("_0", "_1")
                    self.worldLogic[tile[0]][tile[1]] = self.actualActor[1]
                elif tipo == "npc":
                    if self.worldLight[tile[0]][tile[1]] == 0:
                        self.worldItems[tile[0]][tile[1]] = self.actualActor[0]
                    else:
                        self.worldItems[tile[0]][tile[1]] = self.actualActor[
                            0].replace("_0", "_1")
                    self.worldLogic[tile[0]][tile[1]] = self.actualActor[1]
                elif tipo == "text":
                    self.worldLogic[tile[0]][
                        tile[1]] = "13-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "text"
                elif tipo == "minushp":
                    self.worldLogic[tile[0]][
                        tile[1]] = "17-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "minushp"
                elif tipo == "minusmana":
                    self.worldLogic[tile[0]][
                        tile[1]] = "18-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "minusmana"
                elif tipo == "plushp":
                    self.worldLogic[tile[0]][
                        tile[1]] = "22-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "plushp"
                elif tipo == "pass":
                    self.worldLogic[tile[0]][tile[1]] = "21-0-0"
                    self.worldItems[tile[0]][tile[1]] = "pass"
                elif tipo == "nopass":
                    self.worldLogic[tile[0]][tile[1]] = "20-0-0"
                    self.worldItems[tile[0]][tile[1]] = "nopass"
                elif tipo == "plusmana":
                    self.worldLogic[tile[0]][
                        tile[1]] = "23-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "plusmana"
                elif tipo == "playerpos":
                    # Busco el playerpos anterior
                    for j in range(self.mapSize[1]):
                        for i in range(self.mapSize[0]):
                            if self.worldLogic[j][i] == "1-999":
                                self.worldLogic[j][i] = "0-0"
                                self.worldItems[j][i] = "None"
                    self.worldLogic[tile[0]][tile[1]] = "1-999"
                    self.worldItems[tile[0]][tile[1]] = "playerpos"
                elif tipo == "object":
                    self.worldLogic[tile[0]][
                        tile[1]] = "15-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "object"
                elif tipo == "teleport":
                    self.worldLogic[tile[0]][
                        tile[1]] = "24-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "teleport"
                elif tipo == "sound":
                    self.worldLogic[tile[0]][
                        tile[1]] = "28-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "sound"
                elif tipo == "mute":
                    self.worldLogic[tile[0]][tile[1]] = "29-0-0"
                    self.worldItems[tile[0]][tile[1]] = "mute"
                elif tipo == "longtext":
                    self.worldLogic[tile[0]][
                        tile[1]] = "30-0-" + self.actualActor[0]
                    self.worldItems[tile[0]][tile[1]] = "longtext"
                elif tipo == "autosave":
                    self.worldLogic[tile[0]][tile[1]] = "31-0-0"
                    self.worldItems[tile[0]][tile[1]] = "autosave"
                elif tipo == "suddendeath":
                    self.worldLogic[tile[0]][tile[1]] = "32-0-0"
                    self.worldItems[tile[0]][tile[1]] = "suddendeath"
                elif tipo == "nopassalert":
                    self.worldLogic[tile[0]][tile[1]] = "33-0-0"
                    self.worldItems[tile[0]][tile[1]] = "nopassalert"
                elif tipo == "delete":
                    item = self.worldLogic[tile[0]][tile[1]].split("-")
                    if item[0] in EVENTS_LOGIC:  # Si es un mob, un playerpos o un texto
                        self.worldLogic[tile[0]][tile[1]] = "0-0"
                        self.worldItems[tile[0]][tile[1]] = "None"
                    elif item[0] in EVENT_MOVE:  # Si es un movimiento busco el companero y lo borro
                        self.worldLogic[tile[0]][tile[1]] = "0-0"
                        self.worldItems[tile[0]][tile[1]] = "None"
                        # Busco al companero y lo borro
                        for j in range(self.mapSize[1]):
                            for i in range(self.mapSize[0]):
                                if self.worldLogic[j][i] == "25-0-" + str(tile[1]) + "," + str(tile[0]) or \
                                        self.worldLogic[j][i] == "19-0-" + str(tile[1]) + "," + str(tile[0]):
                                    self.worldLogic[j][i] = "0-0"
                                    self.worldItems[j][i] = "None"
        self.drawTiles()

    def infoTile(self, e=None):
        """
        Información de un tile
        :param e: Event
        :return: void
        """
        tile = whatTile(e.x, e.y)  # Recuadro a trabajar
        # Compruebo el tile si esta dentro del mapa
        if tile[0] < self.mapSize[1] and tile[1] < self.mapSize[0]:
            self.workTile[0] = tile[0]
            self.workTile[1] = tile[1]
            logic = self.worldLogic[tile[0]][tile[1]].split("-")[0]
            if logic in TILE_EDIT:
                self.infoEditMenu.post(e.x_root, e.y_root)
            else:
                self.infoMenu.post(e.x_root, e.y_root)
        else:  # Si el tile no está dentro del mapa
            self.workTile = [-1, -1]

    def setActive(self, tipo, tex, idItem, prop=""):
        """
        Definir el objeto actual para trabajar
        :param tipo: Tipo de objeto
        :param tex: Textura de objeto
        :param idItem: id del objeto
        :param prop: Propiedades del objeto
        :return: void
        """
        if tipo == 1:  # Actors
            if idItem == 999:  # Si es el jugador
                self.actualActor = "", "", "playerpos"
                self.actualEnvironment = -1
                self.actualTexture = -1
            elif idItem == "events":  # Si es un evento del tipo texto a usuario
                if isWindows():
                    p = pop(['Insertar Evento', self.images[
                            'event_ico'], 'new_event', 315, 270, 0])
                else:
                    p = pop(['Insertar Evento', self.images[
                            'event_ico'], 'new_event', 330, 270, 0])
                p.w.mainloop(1)
                if p.sent:
                    evento = p.values[0]
                    # Insertar texto (mostrar un texto al jugador)
                    if evento == "text":
                        q = pop(
                            ['Text', self.images['text_ico'], 'new_text', 77, 280])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = replaceStrict(
                                q.values[0]), "", "text"
                        del q
                    elif evento == "move":  # Mover al jugador desde un punto A al punto B
                        q = pop(['Move', self.images['move_ico'],
                                 'new_move', 180, 290])
                        q.w.mainloop(1)
                        if q.sent:
                            coords = q.values[0].split(",")
                            # Si las coordenadas ingresadas son válidas
                            if (0 <= int(coords[1]) <= self.mapSize[0] and 0 <= int(coords[3]) <= self.mapSize[0]) and \
                                    (0 <= int(coords[0]) <= self.mapSize[1] and 0 <= int(coords[2]) <= self.mapSize[1]):
                                self.worldLogic[int(coords[1])][int(coords[0])] = "19-0-" + str(coords[2]) + "," + str(
                                    coords[3])
                                self.worldLogic[int(coords[3])][int(coords[2])] = "25-0-" + str(coords[0]) + "," + str(
                                    coords[1])
                                self.worldItems[int(coords[1])][
                                    int(coords[0])] = "amove"
                                self.worldItems[int(coords[3])][
                                    int(coords[2])] = "bmove"
                                self.drawTiles()
                                self.delActive()
                                self.isMapEditing = True
                                self.core.title(
                                    PROGRAM_TITLE + " - " + self.mapName + " (" + self.mapFile + ") *")
                            del q
                    # Disminuir la vida (HP) al jugador
                    elif evento == "minushp":
                        q = pop(['Minus HP', self.images['minushp_ico'],
                                 'new_absdigit', 77, 280, "Hp:"])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = replaceStrict(
                                q.values[0]), "", "minushp"
                        del q
                    elif evento == "minusmana":  # Disminuir mana
                        q = pop(['Minus mana', self.images[
                                'minusmana_ico'], 'new_absdigit', 77, 280, "Mana:"])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = replaceStrict(
                                q.values[0]), "", "minusmana"
                        del q
                    elif evento == "nopass":  # No pasar
                        self.actualActor = "", "", "nopass"
                    elif evento == "object":  # Dar un objeto al jugador
                        q = pop(['Object', self.images['new_object'],
                                 'new_object', 280, 320])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = q.values[0], "", "object"
                        del q
                    elif evento == "pass":  # Pasar
                        self.actualActor = "", "", "pass"
                    elif evento == "plushp":  # Aumentar la vida del jugador
                        q = pop(['Plus HP', self.images['plushp_ico'],
                                 'new_absdigit', 77, 280, "Hp:"])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = replaceStrict(
                                q.values[0]), "", "plushp"
                        del q
                    elif evento == "plusmana":  # Aumentar mana del jugador
                        q = pop(['Plus mana', self.images['plusmana_ico'],
                                 'new_absdigit', 77, 280, "Mana:"])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = replaceStrict(
                                q.values[0]), "", "plusmana"
                        del q
                    elif evento == "teleport":  # Teleport
                        q = pop(['Teleport', self.images[
                                'teleport_ico'], 'new_maplink', 77, 280])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = replaceStrict(
                                q.values[0]), "", "teleport"
                        del q
                    elif evento == "sound":  # Sonido
                        q = pop(['Sound', self.images['sound_ico'],
                                 'new_sound', 77, 280])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = replaceStrict(
                                q.values[0]), "", "sound"
                        del q
                    elif evento == "mute":  # Mute
                        self.actualActor = "", "", "mute"
                    elif evento == "longtext":  # Long text
                        q = pop(['Longtext', self.images[
                                'longtext_ico'], 'new_longtext', 77, 280])
                        q.w.mainloop(1)
                        if q.sent:
                            self.actualActor = replaceStrict(
                                q.values[0]), "", "longtext"
                        del q
                    elif evento == "autosave":  # Autoguardar
                        self.actualActor = "", "", "autosave"
                    elif evento == "suddendeath":  # Muerte subita
                        self.actualActor = "", "", "suddendeath"
                    elif evento == "nopassalert":  # no pasar con alerta
                        self.actualActor = "", "", "nopassalert"
                del p
            elif idItem == "delete":  # Si es un elemento de borrar
                self.actualActor = "", "", "delete"
            else:  # Si es un mob normal
                if isWindows():
                    p = pop(['Nuevo mob', self.images[
                            'group'], 'new_mob', 442, 295])
                else:
                    p = pop(['Nuevo mob', self.images[
                            'group'], 'new_mob', 500, 350])
                p.w.mainloop(1)
                if p.sent:
                    data = p.values
                    if data[0] == "create-new-npc":  # Si se crea un npc en vez de un mob
                        if isWindows():
                            k = pop(['Nuevo npc', self.images[
                                    'group'], 'new_npc', 307, 290])
                        else:
                            k = pop(['Nuevo npc', self.images[
                                    'group'], 'new_npc', 360, 360])
                        k.w.mainloop(1)
                        if k.sent:
                            npc = k.values
                            properties = "43-0-" + replaceStrict(npc[0]) + ',' + str(idItem) + ',' + replaceStrict(
                                npc[2]) + ',' + replaceStrict(npc[3]) + \
                                ',' + replaceStrict(npc[4]) + ',' + replaceStrict(npc[5]) + ',' + npc[
                                6] + ',' + npc[7] + ',' + npc[8] + ',' + npc[9] + ',' + npc[10]
                            self.actualActor = tex, properties, "npc"
                        del k
                    else:
                        properties = '8-0-' + data[0] + ',' + data[1] + ',' + str(idItem) + ',' + data[3] + ',' + data[
                            4] + ',' \
                            + replaceStrict(data[5]) + ',' + replaceStrict(data[6]) + ',' + data[7] + ',' + \
                            data[8] + ',' + data[9] + ',' + \
                            data[10] + ','
                        if data[11] != '':
                            # Si el mob porta un objeto se agrega
                            properties += replaceStrict(data[11]) + ','
                        else:
                            properties += '%NULL%,'
                        properties += data[12] + ',' + data[13] + ',' + data[14] + ',' + data[15] + ',' + data[
                            16]  # se agregan propiedades de perseguir y escapar
                        # se agrega sonido del mob
                        properties += ',' + data[17]
                        self.actualActor = tex, properties, "mob"
                del p
            self.actualEnvironment = -1
            self.actualTexture = -1
            self.mapTile.bind("<B1-Motion>", self.breakpoint)
        elif tipo == 2:  # Texturas
            self.actualTexture = idItem, tex
            self.actualActor = -1
            self.actualEnvironment = -1
            self.mapTile.bind("<B1-Motion>", self.editTile)
        elif tipo == 3:  # Environment & Building
            if prop == 1:  # Si el objeto es una puerta
                if isWindows():
                    p = pop(['Nueva puerta', self.images[
                            'door'], 'new_door', 145, 290])
                else:
                    p = pop(['Nueva puerta', self.images[
                            'door'], 'new_door', 160, 320])
                p.w.mainloop(1)
                if p.sent:
                    self.actualEnvironment = "special", tex, '6-' + str(idItem) + '-' + p.values[
                        0] + ',' + replaceStrict(p.values[1]), "door"
                del p
            elif prop == 2:  # Si el objeto es un edificio
                if tex in BUILD_LINKS_KEY:  # Link - door - key
                    p = pop(['Nuevo edificio', self.images[
                            'building_add'], 'new_key_building', 190, 290])
                    p.w.mainloop(1)
                    if p.sent:
                        self.actualEnvironment = "special", tex, idItem + "-" + p.values[
                            0] + "," + replaceStrict(p.values[1]), "building"
                    del p
                elif tex in BUILD_LINKS_NOKEY:  # Link - door - no key
                    p = pop(['Nuevo edificio', self.images[
                            'building_add'], 'new_nokey_building', 150, 290])
                    p.w.mainloop(1)
                    if p.sent:
                        self.actualEnvironment = "special", tex, idItem + "-" + p.values[
                            0] + "," + "%NULL%", "volcan"
                    del p
                elif tex in BUILD_TORCHES:  # Antorcha
                    if tex == "ambient_effect2_0":
                        self.actualEnvironment = "special", tex, idItem, "antorcha", 1
                    else:
                        p = pop(['Insertar antorcha', self.images[
                                'lightbulb_add'], 'new_torch', 120, 260])
                        p.w.mainloop(1)
                        if p.sent:
                            self.actualEnvironment = "special", tex, idItem, "antorcha", p.values[
                                0]
                        del p
            # TODO: Objeto usable
            elif prop == 3:  # Si es un objeto usable
                pass
            # TODO: Cofre
            elif prop == 4:  # Si es un cofre
                pass
            # TODO: Librero
            elif prop == 5:  # Si es un librero
                pass
            # TODO: Vehículo
            elif prop == 6:  # Si es un vehiculo
                pass
            elif prop == 7:  # Si es una escalera
                p = pop(['Nueva escalera', self.images[
                        'stair_icon'], 'new_stair', 96, 290])
                p.w.mainloop(1)
                if p.sent:
                    self.actualEnvironment = "special", tex, '42-' + str(idItem) + '-' + p.values[
                        0] + ',' + replaceStrict(p.values[1]), "door"
                del p
            elif prop == 38:  # Si es un mensaje de signo
                q = pop(['Sign', self.images['sign_ico'], 'new_text', 75, 280])
                q.w.mainloop(1)
                if q.sent:
                    self.actualEnvironment = "special", tex, idItem, "sign", replaceStrict(q.values[
                                                                                           0])
                del q
            else:
                self.actualEnvironment = idItem, tex  # Objeto no valido
            self.actualActor = -1
            self.actualTexture = -1
            self.mapTile.bind("<B1-Motion>", self.editTile)

    def setMapName(self):
        """
        Función que escribe el nombre del mapa
        :return: void
        """
        self.infoNameMap.config(text=self.mapName)

    def setDescriptionMap(self):
        """
        Función que escribe la descripcion del mapa
        :return: void
        """
        self.infoDescriptionMap.config(text=self.mapDescription)

    def setAutorMap(self):
        """
        Función que escribe el autor del mapa
        :return: void
        """
        self.infoAutorMap.config(text=self.mapAutor)

    def setSoundMap(self):
        """
        Función que escribe el autor del mapa
        :return: void
        """
        if self.mapSound == "%MAPSOUND%":
            msg = "sin sonido"
        else:
            msg = self.mapSound.replace("_", " ").replace(".wav", "")
        self.infoSoundMap.config(text=msg.capitalize())

    def delActive(self, e=None):
        """
        Borrar todos los objetos actuales
        :param e: Event
        :return: void
        """
        if self.isEvent:
            self.actualActor = -1
            self.actualEnvironment = -1
            self.actualTexture = -1

    def setLightVector(self, x, y, z, o):
        """
        Función que establece un vector en el mapa luminico, de coordenadas (x,y), iluminosidad z y tipo o
        :param x: Pos x
        :param y: Pos y
        :param z: Alcance
        :param o: Luz
        :return: void
        """
        if z == 0:
            return
        else:
            for k in range(-z + y, z + 1 + y):  # Se recorren los lados
                for i in range(-z + x, z + 1 + x):
                    # Si la posicion de la matriz calza
                    if 0 <= k < self.mapSize[1]:
                        if 0 <= i < self.mapSize[0]:
                            self.worldLight[k][i] = o
            self.setLightVector(x, y, z - 1, o)

    def setImageSquare(self, x, y, z, image):
        """
        Función que inserta una imagen de modo análogo al mapa luminico
        :param x: Pos X
        :param y: Pos Y
        :param z: Alcance
        :param image: String de imagen
        :return: void
        """
        if z == 0:
            self.mapTile.create_image(
                17 + 32 * x, 17 + 32 * y, image=self.images[image])
            return
        else:
            for j in range(-z + y, z + 1 + y):  # Se recorren los lados
                for i in range(-z + x, z + 1 + x):
                    # Si la posicion de la matriz calza
                    if 0 <= j < self.mapSize[1]:
                        if 0 <= i < self.mapSize[0]:
                            self.mapTile.create_image(17 + 32 * i, 17 + 32 * j,
                                                      image=self.images[image])
            self.setImageSquare(x, y, z - 1, image)

    def updateLightTiles(self):
        """
        Función que actualiza las matrices graficas tras agregar vectores lumínicos
        :return: void
        """
        for j in range(self.mapSize[1]):  # Texturas
            for i in range(self.mapSize[0]):
                if "_1" in self.worldGraph[j][i] and self.worldLight[j][i] == 0:
                    self.worldGraph[j][i] = str(self.worldGraph[j][i]).replace(
                        "_1", "_0")  # matrices gráficas
                elif "_0" in self.worldGraph[j][i] and self.worldLight[j][i] == 1:
                    self.worldGraph[j][i] = str(
                        self.worldGraph[j][i]).replace("_0", "_1")
                if self.worldItems[j][i] is not None and ("_1" in self.worldItems[j][i] and self.worldLight[j][i] == 0):
                    self.worldItems[j][i] = str(self.worldItems[j][i]).replace(
                        "_1", "_0")  # matrices de items
                elif self.worldItems[j][i] is not None and (
                        "_0" in self.worldItems[j][i] and self.worldLight[j][i] == 1):
                    self.worldItems[j][i] = str(
                        self.worldItems[j][i]).replace("_0", "_1")

    def addLightVector(self, x, y, z):
        """
        Función que agrega un vector luminico en posicion x,y con rango z de luminosidad
        :param x: Posición X
        :param y: Posición Y
        :param z: Luminosidad
        :return: void
        """
        self.worldLightVectors.append(str(x) + "," + str(y) + "," + str(z))
        # se ordena el vector segun crecimiento de x,y
        self.worldLightVectors = list(set(self.worldLightVectors))
        # se actualiza la matriz luminica
        self.setLightVector(int(x), int(y), int(z), 0)
        self.updateLightTiles()

    def removeLightVector(self, x, y):
        """
        Función que elimina un vector luminico en posicion x,y
        :param x: Pos X
        :param y: Pos Y
        :return: void
        """
        pos = str(x) + "," + str(y)
        # Se elimina el vector de la matriz
        for vector in range(len(self.worldLightVectors)):
            # Si el vector contiene la posicion buscada
            if pos in self.worldLightVectors[vector]:
                # obtengo la luminosidad del vector a borrar
                lum = self.worldLightVectors[vector].split(",")[2]
                self.worldLightVectors.pop(vector)
                if self.worldDay == 1:
                    self.setLightVector(int(x), int(y), int(lum), 1)
                    # noinspection PyAssignmentToLoopOrWithParameter
                    # Recorro todos los vectores cercanos para establecer
                    # nuevamente la luminosidad
                    for vector in self.worldLightVectors:
                        vector = vector.split(",")
                        self.setLightVector(int(vector[0]), int(
                            vector[1]), int(vector[2]), 0)
                self.updateLightTiles()
                break

    def setMapTiles(self, light, tex):
        """
        Dibujar el mapa y crear las matrices respectivas
        :param light: Luz
        :param tex: Textura
        :return: void
        """
        try:
            self.core.title(PROGRAM_TITLE + " - " + self.mapName)
            delMatrix(self.worldTextures)
            delMatrix(self.worldLight)
            delMatrix(self.worldLogic)
            delMatrix(self.worldGraph)
            delMatrix(self.worldGraph)
            delMatrix(self.worldLightVectors)
            delMatrix(self.worldItems)
            for i in range(self.mapSize[1]):
                self.worldTextures.append([tex] * self.mapSize[0])
                self.worldLight.append([light] * self.mapSize[0])
                self.worldItems.append(["None"] * self.mapSize[0])
                (texture, sound, log) = textureTerrainAnalysis(
                    tex, light, True)  # Cargo la información
                self.worldGraph.append([texture] * self.mapSize[0])
                self.worldLogic.append([log] * self.mapSize[0])
        except:
            e = pop(["Error", self.images["alert_icon"], "error", 75, 270,
                     "Error al crear el mapa"])  # si ocurre algun error
            e.w.mainloop(1)
            del e

    def loadMap(self, e=None):
        """
        Cargar un mapa
        :param e: Event
        :return: void
        """
        try:
            if not self.isNewMapCreating:  # Si no hay una creacion de nuevo mapa en curso
                lvl = askopenfilename(title="Cargar mapa", initialdir=DATA_LEVELS, defaultextension=".lvl",
                                      filetypes=[("Archivo de mapa de HOA", ".lvl")])
                proplvl = str(lvl).replace(
                    DATA_LEVELS, LEVEL_PROP).replace(".lvl", ".prop")
                if len(lvl) > 0:
                    self.mapFile = lvl.split("/").pop()
                    mapa = loadFromArchive(lvl)  # Carga del mapa
                    self.mapAutor = mapa[1]
                    self.mapDescription = mapa[3]
                    self.mapName = mapa[0]
                    self.mapSound = mapa[4]
                    self.core.title(PROGRAM_TITLE + " - " +
                                    self.mapName + " (" + self.mapFile + ")")
                    size = mapa[2].split(",")
                    self.mapSize[0] = int(size[0])
                    self.mapSize[1] = int(size[1])
                    delMatrix(self.worldTextures)
                    delMatrix(self.worldLight)
                    delMatrix(self.worldLogic)
                    delMatrix(self.worldGraph)
                    delMatrix(self.worldItems)
                    delMatrix(self.worldLightVectors)
                    self.delActive()
                    self.clipboard = ["", "", "", ""]
                    k = 0
                    for i in range(6, len(mapa)):
                        self.worldLight.append([0] * self.mapSize[0])
                        self.worldLogic.append([0] * self.mapSize[0])
                        self.worldTextures.append([0] * self.mapSize[0])
                        self.worldGraph.append([0] * self.mapSize[0])
                        self.worldItems.append([0] * self.mapSize[0])
                        fila = mapa[i].split(";")
                        for f in range(self.mapSize[0]):
                            fila[f] = fila[f].split(":")
                        for j in range(self.mapSize[0]):
                            light = int(fila[j][0])
                            item = fila[j][1]
                            self.worldLight[k][j] = light  # Luz del tile
                            # Cargo el terreno
                            (tex, sound, terrainlog) = textureTerrainAnalysis(
                                int(fila[j][2]), light, True)
                            self.worldGraph[k][j] = tex
                            self.worldTextures[k][j] = int(fila[j][2])
                            # Cargo las texturas
                            self.worldLogic[k][j] = item
                            item = item.split("-")
                            tex = textureItemAnalysis(
                                item[1], light, True)  # Textura
                            if tex == "None":  # Si la textura no pertenece a las decoraciones entonces es logico
                                logic = int(item[0])
                                if logic == 1:
                                    tex = "playerpos"  # Si el es jugador
                                elif logic == 8:  # Si el item es un mob
                                    prop = item[2].split(",")
                                    tex = etextureMobAnalysis(
                                        int(prop[2]), light)
                                elif logic == 13:
                                    tex = "text"  # Si es un texto
                                elif logic == 15:
                                    tex = "object"  # Si es un objeto
                                elif logic == 17:
                                    tex = "minushp"  # Si es un minushp
                                elif logic == 18:
                                    tex = "minusmana"  # Si es un minusmana
                                elif logic == 19:
                                    tex = "amove"  # Si es un moveto
                                elif logic == 20:
                                    tex = "nopass"  # Si es un nopass
                                elif logic == 21:
                                    tex = "pass"  # Si es un pass
                                elif logic == 22:
                                    tex = "plushp"  # Si es unplushp
                                elif logic == 23:
                                    tex = "plusmana"  # Si es un plusmana
                                elif logic == 24:
                                    tex = "teleport"  # Si es un teleport
                                elif logic == 25:
                                    tex = "bmove"  # Si es un movefrom
                                elif logic == 28:
                                    tex = "sound"  # Si es un sound
                                elif logic == 29:
                                    tex = "mute"  # Si es un mute
                                elif logic == 30:
                                    tex = "longtext"  # Si es un longtext
                                elif logic == 31:
                                    tex = "autosave"  # Si es un autosave
                                elif logic == 32:
                                    tex = "suddendeath"  # Si es un suddendeath
                                elif logic == 33:
                                    tex = "nopassalert"  # Si es un nopassalert
                                elif logic == 43:
                                    prop = item[2].split(",")
                                    tex = etextureMobAnalysis(
                                        int(prop[1]), light)
                                else:
                                    tex = "None"
                            self.worldItems[k][j] = tex
                        k += 1
                    try:  # Cargo las propiedades del mapa
                        propmapa = loadFromArchive(proplvl)
                        self.worldDay = int(propmapa.pop(0))
                        # Agrego vector a la matriz vectorial
                        for i in propmapa:
                            self.worldLightVectors.append(
                                i.decode('utf-8').replace("\ufeff", ""))
                    except:
                        pass
                    self.updateLightTiles()
                    self.showOff()
                    self.drawTiles()
                    self.setDescriptionMap()
                    self.setAutorMap()
                    self.setSoundMap()
                    self.setMapName()
                    self.isMapEditing = False  # No hay cambios
                    self.isEvent = True  # Comienzan los eventos de programa
                    # Se mueven los items al principio
                    self.menu1.canv.yview_scroll(-256, "units")
        except:  # Si ocurre algún error durante la carga del mapa
            self.isMapEditing = False  # No hay cambios
            self.isEvent = False  # Se detienen los eventos
            self.showOn()
            self.core.title(PROGRAM_TITLE)
            pop([["Error"], self.images["alert_icon"],
                 "error", 75, 270, "Error al cargar el mapa"])

    # noinspection PyMethodMayBeStatic
    def breakpoint(self, e=None):  # Función que retorna nulo
        return
