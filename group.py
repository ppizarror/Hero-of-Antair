#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GROUP
# Pablo Pizarro, 2014-2015
# Se define la agrupación de actores para el modo de combate grupal
# Donde se explicitan métodos y cantidades
# Tipos: (pueden agregarse más)
# FL: seguidor liviano
# FM: seguidor medio
# FS: seguidor fuerte
# PL: jugador
# MB: mob

# Importación de librerías
import random
import pygame

# Constantes del programa
TARGET = False

class group:  # Clase group

    def __init__(self, tipo, cantidad, vida, ataque, defensa, textura, largadistancia, target, maxmovement, tattack):  # Constructor
        self.ataque = int(ataque)  # ataque unitario por agrupación
        self.cantidad = cantidad  # cantidad de elementos en el grupo
        self.defensa = int(defensa)  # defensa de la agrupación
        self.largadistancia = largadistancia  # puede atacar a larga distancia
        self.maxdistance = 0  # máxima distancia del grupo a la que puede alcanzar
        self.maxmovement = maxmovement  # máximo movimiento
        self.moved1st = False  # indica si se ha movido por primera vez
        self.pos = [0, 0]  # posición del grupo
        self.target = int(target)  # indica el target del group
        self.textura = textura.replace(".gif", "")  # textura de la agrupación
        self.tipo = tipo  # tipo de grupo
        self.tipoAtaque = tattack
        self.vida = int(vida)  # vida unitaria por agrupación

    def setPos(self, x, y):  # Define la posición del grupo
        self.pos[0] = int(x)
        self.pos[1] = int(y)

    def getPosX(self):  # Retorna la posición en X del grupo
        return self.pos[0]

    def getPosY(self):  # Retorna la posición en Y del grupo
        return self.pos[1]

    def getImage(self):  # Retorna la imágen del grupo
        return self.textura

    def getCant(self):  # Retorna la cantidad del grupo
        return self.cantidad

    def getType(self):  # Retorna el tipo de jugador
        return self.tipo

    def getVida(self):  # Retorna la vida total del grupo
        return self.vida * self.cantidad

    def setMaxDistance(self, dist):  # Define la máxima distancia
        self.maxdistance = dist

    def getMaxMovement(self):  # Retorna la cantidad máxima de movimientos
        if not self.moved1st and self.tipo == "PL":  # Si no se ha movido por primera vez
            return self.maxdistance
        else:
            return self.maxmovement

    def attack(self):  # Atacar
        if TARGET: return (self.ataque + random.randint(-int(self.target / 2), int(self.target / 2))) * self.cantidad
        else: return self.ataque * self.cantidad

    def defend(self):  # Defensa
        return self.defensa * self.cantidad

    def getLifeUnit(self):  # Retornar la vida unitaria
        return self.vida

    def getTotal(self):  # Retornar la cantidad de elementos en el grupo
        return self.cantidad

    def disminuir(self, cant):  # Disminuir la cantidad en el grupo
        self.cantidad = self.cantidad - cant

    def setVida(self, cant):  # Definir la cantidad de vida
        self.vida = cant

    def getAtk(self):  # Retorna el ataque
        return self.ataque

    def getTipoAtaque(self):  # Retorna el tipo de ataque
        return self.tipoAtaque
