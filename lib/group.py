# coding=utf-8
"""
GROUP
Se define la agrupación de actores para el modo de combate grupal donde
se explicitan métodos y cantidades.

Tipos: (pueden agregarse más)
FL: seguidor liviano
FM: seguidor medio
FS: seguidor fuerte
PL: jugador
MB: mob

Autor: PABLO PIZARRO @ ppizarror
Fecha: JULIO 2015, 2017
Licencia: GPLv2
"""

# Importación de librerías
import random

# Constantes del programa
TARGET = False


class group(object):
    """Grupo"""

    def __init__(self, tipo, cantidad, vida, ataque, defensa, textura,
                 largadistancia, target, maxmovement,
                 tattack):
        """
        Función constructora
        :param tipo: Tipo de grupo
        :param cantidad: Cantidad de integrantes
        :param vida: Vida del grupo
        :param ataque: Ataque del grupo
        :param defensa: Defensa del grupo
        :param textura: Textura del grupo
        :param largadistancia: Booleano que representa el ataque de larga distancia
        :param target: Target del grupo
        :param maxmovement: Máximo movimiento de gruppo
        :param tattack: Tipo de ataque
        :return:
        """
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

    def setPos(self, x, y):
        """
        Define la posición del grupo
        :param x: Pos X
        :param y: Pos Y
        :return: void
        """
        self.pos[0] = int(x)
        self.pos[1] = int(y)

    def getPosX(self):
        """
        Retorna la posición en X del grupo
        :return: Integer
        """
        return self.pos[0]

    def getPosY(self):
        """
        Retorna la posición en Y del grupo
        :return: Integer
        """
        return self.pos[1]

    def getImage(self):
        """
        Retorna la imágen del grupo
        :return: String
        """
        return self.textura

    def getCant(self):
        """
        Retorna la cantidad del grupo
        :return: String
        """
        return self.cantidad

    def getType(self):
        """
        Retorna el tipo de jugador
        :return: String
        """
        return self.tipo

    def getVida(self):
        """
        Retorna la vida total del grupo
        :return: Integer
        """
        return self.vida * self.cantidad

    def setMaxDistance(self, dist):
        """
        Define la máxima distancia
        :param dist: Integer
        :return: void
        """
        self.maxdistance = dist

    def getMaxMovement(self):
        """
        Retorna la cantidad máxima de movimientos
        :return: Integer
        """
        if not self.moved1st and self.tipo == "PL":  # Si no se ha movido por primera vez
            return self.maxdistance
        else:
            return self.maxmovement

    def attack(self):
        """
        Atacar
        :return: Integer del ataque final
        """
        if TARGET:
            return (self.ataque + random.randint(-int(self.target / 2), int(
                self.target / 2))) * self.cantidad
        else:
            return self.ataque * self.cantidad

    def defend(self):
        """
        Defensa
        :return: Integer de defensa total
        """
        return self.defensa * self.cantidad

    def getLifeUnit(self):
        """
        Retornar la vida unitaria
        :return: Integer
        """
        return self.vida

    def getTotal(self):
        """
        Retornar la cantidad de elementos en el grupo
        :return: Integer
        """
        return self.cantidad

    def disminuir(self, cant):
        """
        Disminuir la cantidad en el grupo
        :param cant: Integer
        :return: void
        """
        self.cantidad = self.cantidad - cant

    def setVida(self, cant):
        """
        Definir la cantidad de vida
        :param cant: Integer
        :return: void
        """
        self.vida = cant

    def getAtk(self):
        """
        Retorna el ataque
        :return: Integer
        """
        return self.ataque

    def getTipoAtaque(self):
        """
        Retorna el tipo de ataque
        :return: String
        """
        return self.tipoAtaque
