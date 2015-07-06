#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Npc's
# Pablo Pizarro, 2015

# Importación de librerías
from lib import *

# Constantes del programa
NPC_SEPARATOR = "{npcsep}"
NPC_TIME_MOVEMENT = 6000
STRING_SEP = "/"


class npc:  # Objetos npc

    def __init__(self, nombre, imagen, descripcion, strings, obj, req, oro, move, dist,
                 fade, posx, posy, ended="FALSE", count=0, initposx=-1, initposy=-1, needquest="None"):  # Función constructora
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

    def getName(self):  # Función para obtener el nombre
        return self.nombre

    def setName(self, name):  # Función que defiene el nombre del npc
        self.nombre = name

    def getImage(self):  # Función para obtener la imagen
        return self.imagen

    def getDescripcion(self):  # Función para obtener la descripcion
        return self.descripcion

    # Función que define la descripción del npc
    def setDescripcion(self, desc):
        self.descripcion = desc

    def getStrings(self):  # Función para obtener los strings
        return self.strings

    def getCurrentString(self):  # Función para obtener el string actual
        return self.string[self.stringCount]

    def getStringAmount(self):  # Obtener la cantidad de strings
        return len(self.string) - 1

    def getObject(self):  # Función para obtener los objetos
        return self.obj

    def getRequest(self):  # Función para obtener el objeto pedido
        return self.req

    def getOro(self):  # Función para obtener el oro del npc
        return self.oro

    def getMove(self):  # Función que retorna si se mueve o no
        return self.move

    # Función para obtener la máxima distancia que puede alcanzar desde el
    # punto de inicio
    def getDistance(self):
        return self.distance

    # Función que retorna si desaparece al terminar el string o no
    def isFade(self):
        return self.fade

    def getPosicion(self):  # Función que retorna la posición del npc
        return self.posicion

    def getPosicionY(self):  # Obtener la posición y
        return self.posicion[1]

    def getPosicionX(self):  # Obtener la posición x
        return self.posicion[0]

    def getCount(self):  # Obtener el contador
        return self.stringCount

    def addCount(self):  # Incrementa el contador
        self.stringCount += 1

    def NextString(self):  # Retorna el siguiente string
        return self.string[self.stringCount + 1]

    def isEnded(self):  # Retorna si esta disponible o no
        return self.ended

    def end(self):  # Termina con el npc, pero no lo destruye
        self.ended = True

    def setPosicionX(self, x):  # Define la posición en x
        self.posicion[0] = x

    def setPosicionY(self, y):  # Define la posición en y
        self.posicion[1] = y

    def needQuest(self):  # Retornan los quest que se necesitan
        return self.needquest

    # Retorna si se muede mostrar al npc o no
    def canShowByQuest(self, playerquest):
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

    def moveNpc(self):  # Mueve al npc
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

    def export(self):  # Exportar los datos
        return replaceStrict(str(self.nombre)) + NPC_SEPARATOR + replaceStrict(str(self.imagen)) + \
            NPC_SEPARATOR + replaceStrict(str(self.descripcion)) + NPC_SEPARATOR + replaceStrict(str(self.strings)) + \
            NPC_SEPARATOR + replaceStrict(str(self.obj)) + NPC_SEPARATOR + replaceStrict(str(self.req)) + NPC_SEPARATOR + \
            replaceStrict(str(self.oro)) + NPC_SEPARATOR + replaceStrict(str(self.move)) + NPC_SEPARATOR + replaceStrict(str(self.distance)) + \
            NPC_SEPARATOR + replaceStrict(str(self.fade)) + NPC_SEPARATOR + str(self.posicion[0]) + NPC_SEPARATOR + str(self.posicion[1]) + NPC_SEPARATOR + \
            str(self.ended) + NPC_SEPARATOR + str(self.stringCount) + NPC_SEPARATOR + str(self.initPos[0]) + NPC_SEPARATOR + str(self.initPos[1]) + \
            NPC_SEPARATOR + str(self.needquest) + "\n"
