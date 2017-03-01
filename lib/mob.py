#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MOB
Actores (mob), entidades lógicas hostiles del juego.

Autor: PABLO PIZARRO @ ppizarror
Fecha: 2013-2015, 2017
Licencia: GPLv2
"""

# Importación de librerías
from lib import *  # @UnusedWildImport

# Constantes del programa
MOB_SEPARATOR = "/__/"
# tiempo en milisegundos que se usara para mover a los mobs
TIME_MOVE_MOBS_NORMAL = 4000


def _positive(a):
    """
    Función que retorna solo si el valor ingresado da positivo, caso contrario devuelve 0
    :param a: Integer
    :return: Integer, 0
    """
    if a > 0:
        return a
    else:
        return 0


class mob(object):
    """Clase mob, enemigo"""

    def __init__(self, ataque, vida, imagen, target, velocidad, nombre,
                 informacion, posx,
                 posy, regeneracion, movimiento, defensa, exp, obj="",
                 escapa="FALSE", persigue="FALSE", distance=0,
                 initposx=-1, initposy=-1,
                 tipocombate="NORMAL", tipoataque="NORMAL",
                 sonido="%NOSOUND%"):
        """
        Función constructora
        :param ataque: Ataque
        :param vida: Vida total
        :param imagen: Textura
        :param target: Target
        :param velocidad: Velocidad
        :param nombre: Nombre
        :param informacion: Descripción del mob
        :param posx: Posición X
        :param posy: Posición Y
        :param regeneracion: Regeneración
        :param movimiento: �?ndice de movimiento
        :param defensa: Defensa del mob
        :param exp: Experiencia-drop
        :param obj: Objeto-drop
        :param escapa: Booleano escapa o no
        :param persigue: Booleano persigue o no
        :param distance: Distancia máxima de alcance
        :param initposx: Posición Original X
        :param initposy: Posición Original Y
        :param tipocombate: Tipo de combate
        :param tipoataque: Tipo de ataque
        :param sonido: Sonido
        :return: void
        """
        # Formateo de variables
        if escapa.upper() == "FALSE":
            escapa = False
        else:
            escapa = True
        if persigue.upper() == "FALSE":
            persigue = False
        else:
            persigue = True
        if int(initposx) == -1:
            initposx = posx
        if int(initposy) == -1:
            initposx = posy
        self.ataque = ataque  # ataque del mob
        self.defensa = defensa  # defensa del mob
        # máxima distancia que puede avanzar el mob por movimiento unitario
        self.distance = int(distance)
        self.escapa = escapa  # define si el mob escapa al tener poca vida
        self.expDrown = exp  # define la experiencia dada al morir
        self.imagen = imagen  # imagen del mob
        self.informacion = putStrict(informacion)  # descripción del mob
        # posición inicial del mob
        self.initPos = [int(initposx), int(initposy)]
        self.maxvida = vida  # vida máxima del mob
        # define la taza de movimiento en porcentaje, 0: no se mueve, 100:
        # siempre se mueve
        self.movimiento = movimiento
        self.nombre = putStrict(nombre)  # nombre del mob
        # define el objeto que arroja el mob tras su muerte
        self.objDrown = putStrict(obj)
        # define si el mob persigue al jugador en sus movimientos
        self.persigue = persigue
        self.posicion = [posx, posy]  # posición inmediata del mob
        # posición con respecto al jugador
        self.posicionConRespectoJugador = ""
        # define la regeneración por turno del mob
        self.regeneracion = regeneracion
        self.sonido = sonido  # sonido del mob cuando se enfrenta a él
        self.target = target  # define la presición de los ataques
        self.tipoataque = tipoataque.strip()  # define el tipo de ataque
        self.tipocombate = tipocombate.strip()  # define el tipo de combate
        # define la velocidad que tendrá al moverse y atacar
        self.velocidad = velocidad
        self.vida = vida  # vida instantánea del mob

    def getName(self):
        """
        Obtener el nombre
        :return: String
        """
        return self.nombre

    def getInformacion(self):
        """
        Obtener la información
        :return: String
        """
        return self.informacion

    def getAtaque(self):
        """
        Obtener el ataque
        :return: Integer
        """
        return self.ataque

    def getImage(self):
        """
        Obtener la imagen
        :return: String
        """
        return self.imagen

    def getPosicionX(self):
        """
        Obtener la posición X
        :return: Integer
        """
        return self.posicion[0]

    def getPosicionY(self):
        """
        Obtener la posición Y
        :return: Integer
        """
        return self.posicion[1]

    def getTarget(self):
        """
        Retorna el target del mob
        :return: Integer
        """
        return self.target

    def move(self, px, py):
        """
        Mover al mob, recibe como parámetros la posición del jugador
        :param px: Pos X
        :param py: Pos Y
        :return: void
        """
        # Primero se calcula la probabilidad del movimiento
        if 0 < random.randint(1, 100) <= self.movimiento:
            if self.distance == 0:  # Si se muede mover infinitamente
                if self.persigue:  # Si el mob persigue al jugador
                    # Se comprueba en el eje x
                    if px > self.posicion[0]:
                        p_x = self.posicion[0] + self.velocidad
                    elif px < self.posicion[0]:
                        p_x = self.posicion[0] - self.velocidad
                    else:
                        p_x = self.posicion[0]
                    # Se comprueba en el eje y
                    if py > self.posicion[1]:
                        p_y = self.posicion[1] + self.velocidad
                    elif py < self.posicion[1]:
                        p_y = self.posicion[1] - self.velocidad
                    else:
                        p_y = self.posicion[1]
                else:  # Si se mueve al azar
                    p_x = self.posicion[
                              0] + random.randint(-self.velocidad,
                                                  self.velocidad)
                    p_y = self.posicion[
                              1] + random.randint(-self.velocidad,
                                                  self.velocidad)
            else:  # Si no se mueden mover infinitamente
                if self.persigue:  # Si el mob persigue al jugador
                    if abs(px - self.initPos[0]) <= self.distance and abs(
                                    py - self.initPos[1]) <= self.distance:
                        if px > self.posicion[0]:
                            p_x = min(
                                self.posicion[0] + self.velocidad,
                                self.initPos[0] + self.distance)
                        elif px < self.posicion[0]:
                            p_x = max(
                                self.posicion[0] - self.velocidad,
                                self.initPos[0] - self.distance)
                        else:
                            p_x = self.posicion[0]
                        if py > self.posicion[1]:
                            p_y = min(
                                self.posicion[1] + self.velocidad,
                                self.initPos[1] + self.distance)
                        elif py < self.posicion[1]:
                            p_y = max(
                                self.posicion[1] - self.velocidad,
                                self.initPos[1] - self.distance)
                        else:
                            p_y = self.posicion[1]
                    else:
                        rannewposx = random.randint(-self.velocidad,
                                                    self.velocidad) + \
                                     self.posicion[0]
                        rannewposy = random.randint(-self.velocidad,
                                                    self.velocidad) + \
                                     self.posicion[1]
                        if abs(rannewposx - self.initPos[0]) <= self.distance:
                            p_x = rannewposx
                        else:
                            p_x = self.posicion[0]
                        if abs(rannewposy - self.initPos[1]) <= self.distance:
                            p_y = rannewposy
                        else:
                            p_y = self.posicion[1]
                else:  # Si no persigue
                    rannewposx = random.randint(-self.velocidad,
                                                self.velocidad) + \
                                 self.posicion[0]
                    rannewposy = random.randint(-self.velocidad,
                                                self.velocidad) + \
                                 self.posicion[1]
                    if abs(rannewposx - self.initPos[0]) <= self.distance:
                        p_x = rannewposx
                    else:
                        p_x = self.posicion[0]
                    if abs(rannewposy - self.initPos[1]) <= self.distance:
                        p_y = rannewposy
                    else:
                        p_y = self.posicion[1]
            return p_x, p_y
        else:
            return -1, -1  # indica que el movimiento no se gesto

    def setPosicionX(self, x):
        """
        Definir la posición X
        :param x: Integer
        :return:
        """
        self.posicion[0] = x

    def setPosicionY(self, y):
        """
        Definir la posición Y
        :param y:
        :return:
        """
        self.posicion[1] = y

    def golpear(self, attack):
        """
        Atacar
        :param attack: Ataque total
        :return: Ataque, Defensa
        """
        if (attack - self.defensa - self.regeneracion) > 0:
            self.vida = min(
                self.maxvida, self.vida - _positive(
                    attack - self.defensa - self.regeneracion))
        return attack, self.regeneracion + self.defensa

    def getLife(self):
        """
        Devolver la vida actual
        :return: Integer
        """
        return self.vida

    def getMaxLife(self):
        """
        Devolver la vida maxima
        :return: Integer
        """
        return self.maxvida

    def atacar(self):
        """
        Atacar
        :return: Integer
        """
        return abs(self.ataque + random.randint(-self.target, self.target))

    def isDead(self):
        """
        Preguntar si esta muerto o no
        :return: Boolean
        """
        if self.vida <= 0:
            return True
        else:
            return False

    def setDefensa(self, defmob):
        """
        Definir la defensa
        :param defmob: Defensa nueva
        :return: void
        """
        self.defensa = defmob

    def getDefensa(self):
        """
        Obtener la defensa
        :return: Integer
        """
        return self.defensa

    def getExp(self):
        """
        Obtener la experiencia que deja el mob tras morir
        :return: Integer
        """
        return self.expDrown

    def getObjDrown(self):
        """
        Obtener el objeto del mob tras morir
        :return: Integer
        """
        return self.objDrown

    def getTipoCombate(self):
        """
        Retorna el tipo de combate
        :return: String
        """
        return self.tipocombate

    def getTipoAtaque(self):
        """
        Retorna el tipo de ataque
        :return: String
        """
        return self.tipoataque

    def setName(self, nombre):
        """
        Define el nombre del mob
        :param nombre: String
        :return: void
        """
        self.nombre = nombre

    def setInfo(self, info):
        """
        Define la información del mob
        :param info: String
        :return: void
        """
        self.informacion = info

    def setPosAbs(self, posx, posy):
        """
        Definir la posición absoluta con respecto al jugador
        :param posx: Pos x
        :param posy: Pos y
        :return: void
        """
        if posx == self.posicion[0]:  # Si estan en el mismo x
            if posy > self.posicion[1]:
                self.posicionConRespectoJugador = "arriba"
            else:
                self.posicionConRespectoJugador = "abajo"
        elif posy == self.posicion[1]:  # Si estan en el mismo y
            if posx > self.posicion[0]:
                self.posicionConRespectoJugador = "izquierda"
            else:
                self.posicionConRespectoJugador = "derecha"

    def getPosAbs(self):
        """
        Retorna la posición absoluta con respecto al jugador
        :return: String
        """
        return self.posicionConRespectoJugador

    def getSound(self):
        """
        Obtiene el sonido caracteristico del mob
        :return: String
        """
        return self.sonido

    def export(self):
        """
        Función que exporta un mob
        :return: String
        """
        return replaceStrict(str(self.ataque)) + MOB_SEPARATOR + replaceStrict(
            str(self.vida)) + MOB_SEPARATOR + \
               replaceStrict(str(self.imagen)) + MOB_SEPARATOR + replaceStrict(
            str(self.target)) + MOB_SEPARATOR + \
               replaceStrict(
                   str(self.velocidad)) + MOB_SEPARATOR + replaceStrict(
            str(self.nombre)) + MOB_SEPARATOR + \
               replaceStrict(
                   str(self.informacion)) + MOB_SEPARATOR + replaceStrict(
            str(self.posicion[0])) + MOB_SEPARATOR + \
               replaceStrict(
                   str(self.posicion[1])) + MOB_SEPARATOR + replaceStrict(
            str(self.regeneracion)) + MOB_SEPARATOR + \
               replaceStrict(
                   str(self.movimiento)) + MOB_SEPARATOR + replaceStrict(
            str(self.defensa)) + MOB_SEPARATOR + \
               replaceStrict(
                   str(self.expDrown)) + MOB_SEPARATOR + replaceStrict(
            str(self.objDrown)) + MOB_SEPARATOR + \
               replaceStrict(str(self.escapa)) + MOB_SEPARATOR + replaceStrict(
            str(self.persigue)) + MOB_SEPARATOR + \
               str(self.distance) + MOB_SEPARATOR + str(
            self.initPos[0]) + MOB_SEPARATOR + str(self.initPos[1]) + \
               MOB_SEPARATOR + str(self.tipocombate) + MOB_SEPARATOR + \
               str(self.tipoataque) + MOB_SEPARATOR + str(self.sonido) + "\n"
