# coding=utf-8
"""
NPC
NPC (Not player character) entidades lógicas que proveen de quest e
items al jugador.

Autor: PABLO PIZARRO @ ppizarror
Fecha: 2013-2015, 2017
Licencia: GPLv2
"""

# Importación de librerías
from lib import *

# Constantes del programa
NPC_SEPARATOR = "{npcsep}"
NPC_TIME_MOVEMENT = 6000
STRING_SEP = "/"


class npc(object):
    """
    Objetos npc
    """

    def __init__(self, nombre, imagen, descripcion, strings, obj, req, oro,
                 move, dist,
                 fade, posx, posy, ended="FALSE", count=0, initposx=-1,
                 initposy=-1,
                 needquest="None"):
        """
        Función constructora
        :param nombre: Nombre
        :param imagen: Imagen
        :param descripcion: Descripción
        :param strings: Lineas de diálogo del npc
        :param obj: Objeto-drop
        :param req: Objeto requerido
        :param oro: Oro-drop
        :param move: Boolean
        :param dist: Distancia maxima desde el origen
        :param fade: Boolean - desaparecer tras dialogar
        :param posx: Pos X
        :param posy: Pos Y
        :param ended: Boolean - finalizado o no
        :param count: Indice del diálogo
        :param initposx: Posición inicial en X
        :param initposy: Posición inicial en Y
        :param needquest: Quest requerida
        :return:
        """
        if fade.upper() == "FALSE":
            fade = False
        else:
            fade = True
        if move.upper() == "FALSE":
            move = False
        else:
            move = True
        if str(ended).upper() == "FALSE":
            ended = False
        else:
            ended = True
        if int(initposx) == -1:
            initposx = posx
        if int(initposy) == -1:
            initposx = posy
        self.descripcion = putStrict(descripcion)  # descripción del npc
        self.distance = int(dist)  # distancia máxima de desplazamiento
        # define si el npc está activo para su interacción o no
        self.ended = ended
        self.fade = fade  # define si el npc desaparece tras interactuar con él
        self.imagen = imagen  # imagen del npc
        # posición inicial del npc
        self.initPos = [int(initposx), int(initposy)]
        self.move = move  # define si el npc se mueve o no
        # define si el npc necesita un cierto quest para mostrarse o no
        self.needquest = needquest
        self.neededquest = needquest.split("/")
        self.nombre = putStrict(nombre)  # nombre del npc
        # objeto que entrega el npc con la sentencia {give}
        self.obj = putStrict(obj)
        self.oro = oro  # oro del npc (para vender)
        self.posicion = [posx, posy]  # posición instantánea del npc
        self.req = req  # objeto requerido
        self.stringCount = int(count)  # cantidad de strings
        self.strings = putStrict(strings)  # string del npc
        self.string = str(self.strings).split(STRING_SEP)  # matriz de string
        # total de quest requeridas
        self.totalneededquest = len(self.neededquest)

    def getName(self):
        """
        Función para obtener el nombre
        :return: String
        """
        return self.nombre

    def setName(self, name):
        """
        Función que defiene el nombre del npc
        :param name: String
        :return: void
        """
        self.nombre = name

    def getImage(self):
        """
        Función para obtener la imagen
        :return: String
        """
        return self.imagen

    def getDescripcion(self):
        """
        Función para obtener la descripcion
        :return: String
        """
        return self.descripcion

    def setDescripcion(self, desc):
        """
        Función que define la descripción del npc
        :param desc: String
        :return: void
        """
        self.descripcion = desc

    def getStrings(self):
        """
        Función para obtener los strings
        :return: List
        """
        return self.strings

    def getCurrentString(self):
        """
        Función para obtener el string actual
        :return: String
        """
        return self.string[self.stringCount]

    def getStringAmount(self):
        """
        Obtener la cantidad de strings
        :return: Integer
        """
        return len(self.string) - 1

    def getObject(self):
        """
        Función para obtener los objetos
        :return: Item
        """
        return self.obj

    def getRequest(self):
        """
        Función para obtener el objeto pedido
        :return: Item
        """
        return self.req

    def getOro(self):
        """
        Función para obtener el oro del npc
        :return: Integer
        """
        return self.oro

    def getMove(self):
        """
        Función que retorna si se mueve o no
        :return: Boolean
        """
        return self.move

    def getDistance(self):
        """
        Función para obtener la máxima distancia que puede alcanzar desde el punto de inicio
        :return: Integer
        """
        return self.distance

    def isFade(self):
        """
        Función que retorna si desaparece al terminar el string o no
        :return: Boolean
        """
        return self.fade

    def getPosicion(self):
        """
        Función que retorna la posición del npc
        :return: List
        """
        return self.posicion

    def getPosicionY(self):
        """
        Obtener la posición y
        :return: Integer
        """
        return self.posicion[1]

    def getPosicionX(self):
        """
        Obtener la posición x
        :return: Integer
        """
        return self.posicion[0]

    def getCount(self):
        """
        Obtener el contador
        :return: Integer
        """
        return self.stringCount

    def addCount(self):
        """
        Incrementa el contador
        :return: void
        """
        self.stringCount += 1

    def NextString(self):
        """
        Retorna el siguiente string
        :return: String
        """
        return self.string[self.stringCount + 1]

    def isEnded(self):
        """
        Retorna si esta disponible o no
        :return: Boolean
        """
        return self.ended

    def end(self):
        """
        Termina con el npc, pero no lo destruye
        :return: void
        """
        self.ended = True

    def setPosicionX(self, x):
        """
        Define la posición en x
        :param x: Integer
        :return: void
        """
        self.posicion[0] = x

    def setPosicionY(self, y):
        """
        Define la posición en y
        :param y: Integer
        :return: void
        """
        self.posicion[1] = y

    def needQuest(self):
        """
        Retornan los quest que se necesitan
        :return: List
        """
        return self.needquest

    def canShowByQuest(self, playerquest):
        """
        Retorna si se muede mostrar al npc o no
        :param playerquest: List
        :return: void
        """
        if self.needquest == "None":
            return True
        else:
            total = 0
            for nedquest in self.neededquest:
                for quest in playerquest:
                    if nedquest in quest.split("%")[0]:
                        total += 1
                        break
            if total == self.totalneededquest:
                return True
            else:
                return False

    def moveNpc(self):
        """
        Mueve al npc
        :return: (x,y) Integer
        """
        rannewposx = random.randint(-1, 1) + self.posicion[0]
        rannewposy = random.randint(-1, 1) + self.posicion[1]
        if abs(rannewposx - self.initPos[0]) <= self.distance:
            newx = rannewposx
        else:
            newx = self.posicion[0]
        if abs(rannewposy - self.initPos[1]) <= self.distance:
            newy = rannewposy
        else:
            newy = self.posicion[1]
        return newx, newy

    def export(self):
        """
        Exportar los datos
        :return: String
        """
        return replaceStrict(str(self.nombre)) + NPC_SEPARATOR + replaceStrict(
            str(self.imagen)) + \
               NPC_SEPARATOR + replaceStrict(
            str(self.descripcion)) + NPC_SEPARATOR + replaceStrict(
            str(self.strings)) + \
               NPC_SEPARATOR + replaceStrict(
            str(self.obj)) + NPC_SEPARATOR + replaceStrict(
            str(self.req)) + NPC_SEPARATOR + \
               replaceStrict(str(self.oro)) + NPC_SEPARATOR + replaceStrict(
            str(self.move)) + NPC_SEPARATOR + replaceStrict(
            str(self.distance)) + \
               NPC_SEPARATOR + replaceStrict(
            str(self.fade)) + NPC_SEPARATOR + str(
            self.posicion[0]) + NPC_SEPARATOR + str(
            self.posicion[1]) + NPC_SEPARATOR + \
               str(self.ended) + NPC_SEPARATOR + str(
            self.stringCount) + NPC_SEPARATOR + str(
            self.initPos[0]) + NPC_SEPARATOR + str(self.initPos[1]) + \
               NPC_SEPARATOR + str(self.needquest) + "\n"
