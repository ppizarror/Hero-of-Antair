#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Statics
# Pablo Pizarro, 2014-2015

# Constantes del programa
_STATIC = ";"


class Statics:  # Statics

    def __init__(self, muertes=0, obj=0, mapas=0, trucos=0, droppedweapon=0, droppeditem=0,
                 orogastado=0, oroganado=0, escapes=0, librosleidos=0, movimientos=0, pociones=0,
                 saved=0, droppedarmor=0, doors=0, npc=0, usedpowers=0, cartelesleidos=0, questhechas=0, followers=0):  # Función constructora
        self.carteles = cartelesleidos
        self.droppedarmor = droppedarmor
        self.droppeditem = droppeditem
        self.droppedweapon = droppedweapon
        self.escapes = escapes
        self.followers = followers
        self.interactnpc = npc
        self.librosleidos = librosleidos
        self.mapas = mapas
        self.movimientos = movimientos
        self.muertes = muertes
        self.obj = obj
        self.opendoors = doors
        self.oroganado = oroganado
        self.orogastado = orogastado
        self.pociones = pociones
        self.poderesuados = usedpowers
        self.questhechas = questhechas
        self.saved = saved
        self.trucos = trucos

    def addMuerte(self):  # Aumenta el número de muertes
        self.muertes += 1

    def addObj(self):  # Aumenta el número de objetos
        self.obj += 1

    def addMapas(self):  # Aumenta el número de mapas reiniciados
        self.mapas += 1

    def addTrucos(self):  # Aumenta el número de trucos
        self.trucos += 1

    def addDroppedWeapon(self):  # Aumenta el número de armas botadas
        self.droppedweapon += 1

    def addDroppedItem(self):  # Aumenta el número de items botados
        self.droppeditem += 1

    def addDroppedArmor(self):  # Aumenta el número de armaduras botadas
        self.droppedarmor += 1

    def addOroGanado(self, i):  # Aumenta el número de oro ganado
        self.oroganado += i

    def addOroGastado(self, i):  # Aumenta el número de oro gastado
        self.orogastado += 1

    def addEscapes(self):  # Aumenta el número de escapes
        self.escapes += 1

    def addLibros(self):  # Aumenta el número de libros leidos
        self.librosleidos += 1

    def addMovimientos(self):  # Aumenta el número de movimientos
        self.movimientos += 1

    def addPociones(self):  # Aumenta el número de pociones usadas
        self.pociones += 1

    # Aumenta el número de veces en que el jugador ha guardado el juego
    def addJuegosGuardados(self):
        self.saved += 1

    def addDoor(self):  # Aumenta el número de puertas abiertas
        self.opendoors += 1

    # Aumenta el número de npc's que han interactuado con el jugador
    def addNpc(self):
        self.interactnpc += 1

    def addPower(self):  # Aumenta el número de poderes usados
        self.poderesuados += 1

    def addCarteles(self):  # Aumenta el número de carteles leidos
        self.carteles += 1

    def addQuest(self):  # Aumenta el número de Quest
        self.questhechas += 1

    def addFollower(self, cant):  # Aumenta el número de Followers
        self.followers += cant

    def getSeparator(self):  # Retorna el separador
        return _STATIC

    def restart(self):  # Devuelve todos los contadores a 0
        self.carteles = 0
        self.droppedarmor = 0
        self.droppeditem = 0
        self.droppedweapon = 0
        self.escapes = 0
        self.followers = 0
        self.interactnpc = 0
        self.librosleidos = 0
        self.mapas = 0
        self.movimientos = 0
        self.muertes = 0
        self.obj = 0
        self.opendoors = 0
        self.oroganado = 0
        self.orogastado = 0
        self.pociones = 0
        self.poderesuados = 0
        self.questhechas = 0
        self.saved = 0
        self.trucos = 0

    def export(self):  # Exporta los datos
        return str(self.muertes) + _STATIC + str(self.obj) + _STATIC + str(self.mapas) + _STATIC + str(self.trucos) + \
            _STATIC + str(self.droppedweapon) + _STATIC + str(self.droppeditem) + _STATIC + str(self.orogastado) + \
            _STATIC + str(self.oroganado) + _STATIC + str(self.escapes) + _STATIC + str(self.librosleidos) + \
            _STATIC + str(self.movimientos) + _STATIC + str(self.pociones) + _STATIC + str(self.saved) + \
            _STATIC + str(self.droppedarmor) + _STATIC + str(self.opendoors) + _STATIC + str(self.interactnpc) + \
            _STATIC + str(self.poderesuados) + _STATIC + str(self.carteles) + _STATIC + str(self.questhechas) + \
            _STATIC + str(self.followers) + "\n"

    def get(self):  # Envía los datos por una matriz
        return [self.muertes, self.obj, self.mapas, self.trucos, self.droppedweapon, self.droppeditem,
                self.orogastado, self.oroganado, self.escapes, self.librosleidos, self.movimientos,
                self.pociones, self.saved, self.droppedarmor, self.opendoors, self.interactnpc,
                self.poderesuados, self.carteles, self.questhechas, self.followers]
