#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Actor, entidad lógica manejada por el usuario

# ACTORS
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2013-2015
# Licencia: GPLv2

# Importación de librerías
import random

# Constantes del programa
MAX_FRIENDS = 1152  # número máximo de seguidores


class actors:
    """Actores"""

    def __init__(self):
        """
        Función constructora
        :return: void
        """
        self.activebullet = None  # armamento activo
        self.activefirstpower = None  # primer poder activo
        self.activesecondpower = None  # segundo poder activo
        self.armor = [None, None, None, None]  # armadura
        self.ataque = 0  # ataque instantáneo
        self.atkLevels = []  # ataque por niveles
        self.damage = 0  # daño instantáneo del jugador
        self.defLevels = []  # defensa por niveles
        self.defensa = 0  # defensa instantánea
        self.edad = "%ACTOR_EDAD%"  # edad del jugador
        # define si el jugador tiene los derechos para ejecutar comandos
        # privilegiados
        self.editor = False
        self.expLevels = []  # define la experiencia por niveles
        self.experiencia = 0  # experiencia inmediata
        # define los followers, livianos, medios, pesados
        self.friends = [0, 0, 0]
        self.info = ""  # descripción del jugador
        self.images = []  # imágenes por niveles del jugador
        # imágenes de los followers, liv, med y pesado
        self.images_friends = ["", "", ""]
        # imágenes de las flechas y del armamento
        self.images_friends_arrow = ["", ""]
        self.items = []  # items del jugador
        self.level = 1  # nivel instantáneo del jugador
        self.linkImage = "%ACTOR_IMAGE_URL"  # imágen instantánea del jugador
        self.magic = []  # magia del jugador
        self.mana = 0  # maná instantáneo del jugador
        self.map = "%LEVEL_MAP%"  # mapa actual del jugador
        self.maxExpLevel = 0  # define la máxima experiencia por nivel
        self.maxItems = 0  # define la máxima cantidad de items
        self.maxLife = 0  # define la máxima vida del nivel actual
        self.maxLifeLevels = []  # define la máxima vida por niveles
        self.maxMana = 0  # define el máximo mana del nivel actual
        self.maxManaLevels = []  # define el máximo mana por niveles
        self.name = "%ACTOR_NAME%"  # nombre del jugador
        self.pais = "%ACTOR_PAIS%"  # país del jugador
        self.playerquest = []  # quest o trabajos del jugador
        self.powers = []  # poderes del jugador
        self.target = 0  # puntería con las armas izquierdas en el nivel actual
        self.targetLevels = []  # presición por niveles
        self.tipo = ""  # tipo de jugador
        self.velocidad = 0  # velocidad del jugador
        self.weapons = [None, None]  # armas del jugador

    def setName(self, name):
        """
        Asignar un nombre al actor
        :param name: Nombre
        :return:
        """
        if len(name) > 0:
            self.name = name

    def setPais(self, pais):
        """
        Asignar un país al actor
        :param pais: Pais
        :return: void
        """
        if len(pais) > 0:
            self.pais = pais

    def setEdad(self, edad):
        """
        Asignar una edad al actor
        :param edad: Edad
        :return: void
        """
        edad = str(edad)
        if edad.isdigit():
            self.edad = int(edad)

    def setType(self, tipo):
        """
        Asignar un tipo al actor
        :param tipo: Tipo de jugador
        :return: void
        """
        # Se definen los tipos de actores, pueden agregarse más
        if tipo == "guerrero":
            self.atkLevels = [5, 20, 40, 60, 80,
                              110, 130, 170, 210, 240, 270, 300]
            self.defLevels = [2, 6, 10, 20, 25, 40, 60, 80, 100, 120, 150, 200]
            self.expLevels = [0, 700, 3000, 7000, 12500, 22500,
                              45000, 90000, 250000, 450000, 1000000, 4000000]
            self.images = ["actor127", "actor127", "actor113", "actor113", "actor103", "actor103", "actor8", "actor40",
                           "actor46", "actor7", "actor7", "actor107"]
            self.images_friends = ["actor111", "actor66", "actor8"]
            self.images_friends_arrow = ["flecha_hierro_16", "arco_umbral_16"]
            self.info = "El guerrero es súmamente hábil en combates cuerpo a cuerpo, posee un gran ataque y vida, pero poca defensa, puntería y mana." + \
                        " Es conocido por su gran habilidad en el uso de espadas y mazas."
            self.maxLifeLevels = [100, 120, 150, 190,
                                  240, 300, 370, 450, 540, 650, 800, 999]
            self.maxManaLevels = [10, 15, 20, 25,
                                  30, 40, 50, 60, 70, 80, 90, 100]
            self.targetLevels = [0, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
            self.tipo = "Guerrero"
            self.velocidad = 2
        elif tipo == "mago":
            self.atkLevels = [5, 10, 20, 30, 50,
                              80, 100, 120, 150, 180, 210, 250]
            self.defLevels = [2, 6, 10, 20, 25, 40, 60, 80, 100, 120, 150, 200]
            self.expLevels = [0, 1000, 2500, 5000, 10000, 25000,
                              50000, 100000, 250000, 500000, 1000000, 2500000]
            self.images = ["actor127", "actor127", "actor68", "actor68", "actor68", "actor41", "actor41", "actor42",
                           "actor42", "actor13", "actor13", "actor135"]
            self.images_friends = ["actor113", "actor1", "actor8"]
            self.images_friends_arrow = [
                "magic_ball_5", "mazo_snake_gods_sceptre_16"]
            self.info = "Un sabio de las artes oscuras, súmamente hábil en todo tipo de magias, de gran mana y mediana vida, pero poco ataque. " + \
                        "Es conocido por su gran manejo de los arcos y las varas mágicas."
            self.maxLifeLevels = [150, 160, 170, 180,
                                  190, 200, 220, 250, 270, 320, 390, 500]
            self.maxManaLevels = [100, 120, 150, 190,
                                  240, 300, 370, 450, 540, 650, 800, 999]
            self.targetLevels = [10, 15, 20, 25,
                                 30, 40, 50, 60, 70, 80, 90, 100]
            self.tipo = "Mago"
            self.velocidad = 1
        elif tipo == "skaard":
            self.atkLevels = [2, 6, 10, 20, 25, 40, 60, 80, 100, 120, 150, 200]
            self.defLevels = [4, 10, 20, 40, 55,
                              70, 100, 140, 180, 220, 280, 350]
            self.expLevels = [0, 1000, 2500, 5000, 15000, 30000,
                              100000, 175000, 250000, 500000, 1000000, 1500000]
            self.images = ["actor76", "actor76", "actor77", "actor77", "actor78", "actor78", "actor75", "actor75",
                           "actor20", "actor12", "actor12", "actor64"]
            self.images_friends = ["actor111", "actor75", "actor20"]
            self.images_friends_arrow = [
                "flecha_hierro_16", "arco_silkweaver_16"]
            self.info = "Originario de las tierras de Okwainth, conocido por su gran habilidad en el uso de flechas y lanzas. Posee una gran puntería," + \
                        " una gran defensa y una mediana vida."
            self.maxLifeLevels = [10, 20, 40, 70, 100,
                                  180, 220, 250, 300, 340, 360, 400]
            self.maxManaLevels = [5, 20, 40, 60, 80,
                                  110, 130, 170, 210, 240, 270, 300]
            self.targetLevels = [5, 20, 40, 60, 80,
                                 110, 130, 170, 210, 240, 270, 300]
            self.tipo = "Skaard"
            self.velocidad = 2
        elif tipo == "ugraar":
            self.atkLevels = [5, 10, 20, 30, 50,
                              80, 100, 120, 150, 180, 210, 250]
            self.defLevels = [2, 6, 10, 20, 25, 40, 60, 80, 100, 120, 150, 200]
            self.expLevels = [0, 2000, 4500, 8000, 17000, 35000,
                              140000, 290000, 550000, 900000, 1500000, 3400000]
            self.images = ["actor115", "actor115", "actor119", "actor119", "actor116", "actor116", "actor117",
                           "actor117", "actor121", "actor121", "actor120", "actor120"]
            self.images_friends = ["actor119", "actor117", "actor120"]
            self.images_friends_arrow = [
                "lanza_hunting_spear_16", "lanza_hunting_spear_16"]
            self.info = "Originario de Myraleem los Ugraar son conocidos por su gran resistencia y su verde piel, además de ser muy hábiles en el manejo" + \
                        "de las armas de filo."
            self.maxLifeLevels = [20, 40, 70, 100,
                                  140, 190, 250, 310, 380, 460, 580, 690]
            self.maxManaLevels = [2, 6, 10, 20,
                                  25, 40, 60, 80, 100, 120, 150, 200]
            self.targetLevels = [10, 15, 20, 25,
                                 30, 40, 50, 60, 70, 80, 90, 100]
            self.tipo = "Ugraar"
            self.velocidad = 1
        self.mana = self.maxManaLevels[self.level - 1]
        self.setAttack()
        self.setDefensa()
        self.setImage()
        self.setMaxExpLevel()
        self.setMaxLife()
        self.setMaxMana()
        self.setTarget()

    def getActualMaximumLife(self):
        """
        Obtener vida máxima actual
        :return: Integer
        """
        return self.maxLife

    def getLife(self):
        """
        Obtener vida menos el damage actual
        :return: Integer
        """
        return self.maxLife - self.damage

    def getExperience(self):
        """
        Obtener experiencia
        :return: Integer
        """
        return self.experiencia

    def getMaxExperience(self):
        """
        Obtener la maxima experiencia
        :return: Integer
        """
        return self.maxExpLevel

    def getMana(self):
        """
        Obtener mana
        :return: Integer
        """
        return self.mana

    def increaseMana(self, mana):
        """
        Aumentar el mana
        :param mana: Nuevo mana
        :return: void
        """
        self.mana = min(self.mana + mana, self.maxMana)

    def decreaseMana(self, mana):
        """
        Usar mana
        :param mana: Cantidad de mana a usar
        :return: void
        """
        self.mana = max(self.mana - mana, 0)

    def dropObject(self, obj):
        """
        Soltar objeto
        :param obj: Objeto a eliminar
        :return: void
        """
        self.items.pop(obj)

    def dropPower(self, power):
        """
        Eliminar un poder específico
        :param power: Poder a eliminar
        :return: void
        """
        self.powers.pop(power)

    def addObject(self, obj=None):
        """
        Agregar objeto
        :param obj: Objeto a agregar <Item>
        :return: void
        """
        if obj.isStackable():
            k = 0
            for i in self.items:
                if i.getId() == obj.getId():
                    self.items[k].subirUsos(obj.getUsos())
                    k = -1
                    return
                k += 1
            if k != -1:
                self.items.insert(0, obj)
        else:
            self.items.insert(0, obj)

    def addPower(self, power):
        """
        Agregar un poder
        :param power: Poder a agregar
        :return: void
        """
        self.powers.insert(0, power)

    def addCasco(self, obj):
        """
        Agregar un casco
        :param obj: Casco a agregar
        :return: void
        """
        self.armor.pop(0)
        self.armor.insert(0, obj)

    def getCasco(self):
        """
        Obtener el casco
        :return: Item
        """
        return self.armor[0]

    def dropCasco(self):
        """
        Eliminar el casco
        :return: void
        """
        self.armor.pop(0)
        self.armor.insert(0, None)

    def addChaleco(self, obj):
        """
        Agregar un chaleco
        :param obj: Item
        :return: void
        """
        self.armor.pop(1)
        self.armor.insert(1, obj)

    def getChaleco(self):
        """
        Obtener el chaleco
        :return: Item
        """
        return self.armor[1]

    def dropChaleco(self):
        """
        Eliminar el chaleco
        :return: void
        """
        self.armor.pop(1)
        self.armor.insert(1, None)

    def addPantalones(self, obj):
        """
        Agregar pantalones
        :param obj: Item
        :return: void
        """
        self.armor.pop(2)
        self.armor.insert(2, obj)

    def getPantalones(self):
        """
        Obtener los pantalones
        :return: void
        """
        return self.armor[2]

    def dropPantalones(self):
        """
        Eliminar el pantalón
        :return: void
        """
        self.armor.pop(2)
        self.armor.insert(2, None)

    def addBotas(self, obj):
        """
        Agregar zapatos
        :param obj: Item
        :return: void
        """
        self.armor.pop(3)
        self.armor.insert(3, obj)

    def getBotas(self):
        """
        Obtener las botas
        :return: Item
        """
        return self.armor[3]

    def dropBotas(self):
        """
        Eliminar las botas
        :return: void
        """
        self.armor.pop(3)
        self.armor.insert(3, None)

    def dropArmor(self):
        """
        Quitar armadura completa
        :return: void
        """
        for i in range(4):
            self.armor.pop(0)
        for i in range(4):
            self.armor.append(None)

    def dropItems(self):
        """
        Eliminar todos los items del jugador
        :return: void
        """
        l = len(self.items)
        if l > 0:
            for i in range(l):
                self.items.pop(0)

    def dropPowers(self):
        """
        Elimina todos los poderes del jugador
        :return: void
        """
        l = len(self.powers)
        if l > 0:
            for i in range(l):
                self.powers.pop(0)

    def dropMagics(self):
        """
        Elimina todas las magias
        :return: void
        """
        l = len(self.magic)
        if l > 0:
            for i in range(l):
                self.magic.pop(0)

    def kill(self):
        """
        Matar a un actor
        :return: void
        """
        self.damage = self.maxLife

    def setRightWeapon(self, obj):
        """
        Definir el arma derecha
        :param obj: Item
        :return: void
        """
        self.weapons[1] = obj

    def dropRightWeapon(self):
        """
        Eliminar el arma derecha
        :return: void
        """
        self.weapons[1] = None

    def getRightWeapon(self):
        """
        Obtener el arma derecha
        :return: void
        """
        return self.weapons[1]

    def setLeftWeapon(self, obj):
        """
        Definir el arma izquierda
        :param obj: void
        :return:
        """
        self.weapons[0] = obj

    def dropLeftWeapon(self):
        """
        Eliminar el arma izquierda
        :return: void
        """
        self.weapons[0] = None

    def getLeftWeapon(self):
        """
        Obtener el arma izquierda
        :return: Item
        """
        return self.weapons[0]

    def setVelocidad(self, vel):
        """
        Definir la velocidad del actor
        :param vel: Integer
        :return: void
        """
        self.velocidad = vel

    def getVelocidad(self):
        """
        Obtejer la velocidad del actor
        :return: Integer
        """
        return self.velocidad

    def setInfo(self, info):
        """
        Definir la información
        :param info: String
        :return: void
        """
        self.info = info

    def getInfo(self):
        """
        Obtener la información
        :return: void
        """
        return self.info

    def getName(self):
        """
        Obtener el nombre
        :return: String
        """
        return self.name

    def getType(self):
        """
        Obtejer el tipo
        :return: void
        """
        return self.tipo

    def increaseDamage(self, damage):
        """
        Incrementar el daño
        :param damage: Integer
        :return: void
        """
        defn = self.defensa
        try:
            defn += self.getBotas().getDefense()
            self.getBotas().usar()
        except:
            pass
        try:
            defn += self.getCasco().getDefense()
            self.getCasco().usar()
        except:
            pass
        try:
            defn += self.getPantalones().getDefense()
            self.getPantalones().usar()
        except:
            pass
        try:
            defn += self.getChaleco().getDefense()
            self.getChaleco().usar()
        except:
            pass
        if damage > defn:
            self.damage = min(self.damage + (damage - defn), self.maxLife)
        return damage, defn

    def increaseDamageNODEFN(self, damage):
        """
        Incrementar el daño sin defensa
        :param damage: Integer
        :return: void
        """
        self.damage += damage

    def setDamage(self, damage):
        """
        Establecer el daño
        :param damage: Integer
        :return: void
        """
        self.damage = min(damage, self.maxLife)

    def curar(self, hp):
        """
        Curar al jugador
        :param hp: Integer
        :return: void
        """
        self.damage = max(0, self.damage - abs(hp))

    def getDamage(self):
        """
        Obtener el daño
        :return: Integer
        """
        return self.damage

    def getMaxLife(self):
        """
        Obtener la máxima vida
        :return: Integer
        """
        return self.maxLife

    def getMaxMana(self):
        """
        Obtener el máximo mana
        :return: Integer
        """
        return self.maxMana

    def getPrevMana(self):
        """
        Obtener el mana del nivel anterior
        :return: Integer
        """
        return self.maxManaLevels[self.level]

    def getPrevExp(self):
        """
        Obtener la experiencia anterior
        :return: Integer
        """
        if self.level > 1:
            return self.expLevels[self.level - 1]
        else:
            return 0

    def getLevel(self):
        """
        Obtener el nivel
        :return: Integer
        """
        return self.level

    def increaseExp(self, exp):
        """
        Incrementar la experiencia
        :param exp: Integer
        :return: Boolean
        """
        if self.level != 12:
            self.experiencia += exp
            if self.experiencia >= self.getMaxExperience():
                self.level += 1
                self.setAttack()
                self.setDefensa()
                self.setImage()
                self.setMaxExpLevel()
                self.setMaxLife()
                self.setMaxMana()
                self.setTarget()
                return True
        return False

    def upgradeMana(self):
        """
        Aumentar el mana al subir de nivel
        :return: void
        """
        self.mana = self.maxManaLevels[self.level - 1]
        self.maxMana = self.maxManaLevels[self.level - 1]

    def upgradeLife(self):
        """
        Aumentar el la vida al subir de nivel
        :return: void
        """
        self.damage = 0
        self.maxLife = self.maxLifeLevels[self.level - 1]

    def upgradeExp(self):
        """
        Aumentar la experiencia al subir de nivel
        :return: void
        """
        self.experiencia = self.expLevels[self.level - 1]
        self.setMaxExpLevel()

    def setMap(self, mapa):
        """
        Definir mapa
        :param mapa: String
        :return: void
        """
        self.map = mapa

    def getMap(self):
        """
        Obtener mapa
        :return: String
        """
        return self.map

    def getEdad(self):
        """
        Obtener la edad del jugador
        :return: Integer
        """
        return self.edad

    def getPais(self):
        """
        Obtener el pais
        :return: String
        """
        return self.pais

    def getLinkImage(self):
        """
        Obtener el link de la imagen
        :return: String
        """
        return self.linkImage

    def getImages(self):
        """
        Obtener las imágenes
        :return: List
        """
        return self.images

    def setExperience(self, exp):
        """
        Definir la experiencia
        :param exp: Integer
        :return: void
        """
        self.experiencia = exp

    def setLevel(self, level):
        """
        Definir el nivel
        :param level: Integer
        :return: void
        """
        if level <= 12:
            self.level = level

    def setLinkImage(self, img):
        """
        Definir el link de la imagen del jugador
        :param img: String
        :return: void
        """
        self.linkImage = img

    def setMana(self, mana):
        """
        Definir el mana
        :param mana: Integer
        :return: void
        """
        self.mana = mana

    def setMaxExpLevel(self):
        """
        Definir el máximo de experiencia por nivel
        :return: void
        """
        if self.level < 12:
            self.maxExpLevel = self.expLevels[self.level]

    def setMaxLife(self):
        """
        Definir el máximo de vida
        :return: void
        """
        self.maxLife = self.maxLifeLevels[self.level - 1]

    def setMaxMana(self):
        """
        Definir el máximo de mana
        :return: void
        """
        self.maxMana = self.maxManaLevels[self.level - 1]

    def setImage(self):
        """
        Define la imagen del actor en función de su nivel
        :return: void
        """
        self.linkImage = self.images[self.level - 1]

    def setTypeDef(self, t):
        """
        Definir el tipo de actor
        :param t: Integer
        :return: void
        """
        self.tipo = t

    def atacar(self, mano):
        """
        Atacar
        :param mano: String {izquierda, derecha, fp, sp}
        :return: Integer
        """
        if mano == "izquierda":  # atacar con la mano izquierda
            if self.weapons[0] is not None:  # Si posee un arma
                self.weapons[0].usar()
                return max(0, self.ataque + random.randint(0, self.target) + self.weapons[
                    0].getDamage() + self.getActiveBullet().getDamage())
            else:
                return max(0, self.ataque + random.randint(0, self.target))
        elif mano == "derecha":  # atacar con la mano derecha
            if self.weapons[1] is not None:
                self.weapons[1].usar()
                return max(0, self.ataque + self.weapons[1].getDamage() + random.randint(-self.target / 2,
                                                                                         self.target / 2))
            else:
                return max(0, self.ataque + random.randint(-self.target / 2, self.target / 2))
        elif mano == "fp":  # atacar con el primer poder
            print "ataque con primer poder"
            return -1
        elif mano == "sp":  # atacar con el segundo poder
            print "ataque con segundo poder"
            return -1
        else:
            return 0  # ataque no valido

    def getAttack(self):
        """
        Obtener el ataque
        :return: Integer
        """
        return self.ataque

    def getDefensa(self):
        """
        Obtener la defensa
        :return: Integer
        """
        return self.defensa

    def getTarget(self):
        """
        Obtener el target
        :return: Integer
        """
        return self.target

    def setAttack(self, cant=0):
        """
        Definir el ataque, si cant==0 se define el ataque segun el nivel, si no se establece cant como ataque definido
        :param cant: Integer
        :return: void
        """
        if cant == 0:
            self.ataque = self.atkLevels[self.level - 1]
        else:
            self.ataque = cant

    def setDefensa(self, cant=0):
        """
        Definir la defensa, si cant==0 se define la defensa segun el nivel, si no se establece cant como defensa definido
        :param cant: Integer
        :return: void
        """
        if cant == 0:
            self.defensa = self.defLevels[self.level - 1]
        else:
            self.defensa = cant

    def setTarget(self, cant=0):
        """
        Definir el target segun el nivel del jugador, si se define cant se deja como target
        :param cant: Integer
        :return: void
        """
        if cant == 0:
            self.target = self.defLevels[self.level - 1]
        else:
            self.target = cant

    def isDead(self):
        """
        Devuelve si esta vivo o muerto
        :return: Boolean
        """
        if self.damage >= self.maxLife:
            return True
        else:
            return False

    def isEditor(self):
        """
        Devuelve si el player es editor
        :return: Boolean
        """
        return self.editor

    def setEditor(self):
        """
        Define al jugador como editor
        :return: void
        """
        self.editor = True

    def setNotEditor(self):
        """
        Define al jugador como no editor
        :return: void
        """
        self.editor = False

    def getItems(self):
        """
        Devuelve los items
        :return: List
        """
        return self.items

    def getPowers(self):
        """
        Devuelve los poderes
        :return: List
        """
        return self.powers

    def getMagics(self):
        """
        Devuelve la magia
        :return: List
        """
        return self.magic

    def getItem(self, item):
        """
        Devuelve un cierto item
        :param item: String
        :return: Item
        """
        return self.items[item]

    def getPower(self, power):
        """
        Devuelve un cierto poder
        :param power: String
        :return: Item
        """
        return self.powers[power]

    def setPower(self, i, power):
        """
        Define un poder
        :param i: Integer
        :param power: Power
        :return: void
        """
        self.powers[i] = power

    def setItem(self, i, item):
        """
        Define un item
        :param i: Integer
        :param item: Item
        :return: void
        """
        self.items[i] = item

    def getItemAmount(self):
        """
        Retorna la cantidad de items que tiene el jugador
        :return: Integer
        """
        return len(self.items)

    def getPowerAmount(self):
        """
        Retorna la cantidad de poderes que tiene el jugador
        :return: Integer
        """
        return len(self.powers)

    def getMagicAmount(self):
        """
        Retorna la cantidad de magias
        :return: Integer
        """
        return len(self.magic)

    def setActiveBullet(self, obj):
        """
        Define el armamento activo
        :param obj: Item
        :return: void
        """
        if obj == "None":
            obj = None
        self.activebullet = obj

    def setFirstPower(self, power):
        """
        Define el primer poder
        :param power: Power
        :return: void
        """
        if power == "None":
            power = None
        self.activefirstpower = power

    def setSecondPower(self, power):
        """
        Define el poder secundario
        :param power: Power
        :return: void
        """
        if power == "None":
            power = None
        self.activesecondpower = power

    def getActiveBullet(self):
        """
        Retorna el armamento
        :return: Item
        """
        return self.activebullet

    def getFirstPower(self):
        """
        Retorna el primer poder
        :return: Power
        """
        return self.activefirstpower

    def getSecondPower(self):
        """
        Retorna el poder secundario
        :return: Power
        """
        return self.activesecondpower

    def delActiveBullet(self):
        """
        Elimina el armamento
        :return: void
        """
        self.setActiveBullet(None)

    def delFirstPower(self):
        """
        Elimina el primer poder
        :return: void
        """
        self.setFirstPower(None)

    def delSecondPower(self):
        """
        Elimina el poder secundario
        :return: void
        """
        self.setSecondPower(None)

    def addQuest(self, quest):
        """
        Agrega una quest
        :param quest: Quest
        :return: void
        """
        if quest not in self.playerquest:
            self.playerquest.insert(0, quest)

    def getQuest(self):
        """
        Retorna las quest
        :return: Quest
        """
        return self.playerquest

    def delQuest(self):
        """
        Elimina las quest
        :return: void
        """
        l = len(self.playerquest)
        if l > 0:
            for i in range(l):
                self.playerquest.pop()

    def getTotalQuest(self):
        """
        Retorna la cantidad de quest
        :return: Integer
        """
        return len(self.playerquest)

    def hasQuest(self):
        """
        Retorna si existen quest
        :return: Boolean
        """
        if len(self.playerquest) > 0:
            return True
        else:
            return False

    def getFriends(self):
        """
        Obtener seguidores del actor
        :return: List
        """
        return self.friends

    def setFriends(self, friends):
        """
        Definir los amigos
        :param friends: String
        :return: void
        """
        friends = str(friends).replace("[", "").replace("]", "").split(",")
        friends_archer = friends[0].strip()
        friends_medium = friends[1].strip()
        friends_strong = friends[2].strip()
        if friends_archer.isdigit() and friends_medium.isdigit() and friends_strong.isdigit():
            friends_archer = int(friends_archer)
            friends_medium = int(friends_medium)
            friends_strong = int(friends_strong)
            self.friends[0] = friends_archer
            self.friends[1] = friends_medium
            self.friends[2] = friends_strong

    def getLightFriends(self):
        """
        Retorna los seguidores arqueros
        :return: Integer
        """
        return self.friends[0]

    def getMediumFriends(self):
        """
        Retorna los seguidores medios
        :return: Integer
        """
        return self.friends[1]

    def getStrongFriends(self):
        """
        Retorna los seguidores pesados
        :return: Integer
        """
        return self.friends[2]

    def dropFollowers(self):
        """
        Elimina a los seguidores
        :return: void
        """
        self.friends = [0, 0, 0]

    def addLightFriend(self, liv):
        """
        Agrega un amigo liviano
        :param liv: Integer
        :return: void
        """
        self.friends[0] = min(self.friends[0] + liv,
                              MAX_FRIENDS - self.friends[1] - self.friends[2])

    def addMediumFriend(self, mdf):
        """
        Agrega un amigo medio
        :param mdf: Integer
        :return: void
        """
        self.friends[1] = min(self.friends[1] + mdf,
                              MAX_FRIENDS - self.friends[0] - self.friends[2])

    def addStrongFriend(self, strf):
        """
        Agrega un amigo pesado
        :param strf: Integer
        :return: void
        """
        self.friends[2] = min(self.friends[2] + strf,
                              MAX_FRIENDS - self.friends[0] - self.friends[1])

    def getLightImageFriend(self):
        """
        Retorna la imagen de los seguidores arqueros
        :return: String
        """
        return self.images_friends[0]

    def getMediumImageFriend(self):
        """
        Retorna la imagen del seguidor medio
        :return: String
        """
        return self.images_friends[1]

    def getStrongImageFriend(self):
        """
        Retorna la imagen del seguidor pesado
        :return: String
        """
        return self.images_friends[2]

    def getTotalFriends(self):
        """
        Retorna la cantidad total de friends
        :return: Integer
        """
        return sum(self.friends)

    def getArrowTexture(self):
        """
        Retorna la textura de las flechas
        :return: String
        """
        return self.images_friends_arrow[0]

    def getWeaponTexture(self):
        """
        Retorna la textura del arma del follower
        :return: String
        """
        return self.images_friends_arrow[1]
