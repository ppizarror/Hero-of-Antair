# coding=utf-8
#
# Items usables por el jugador

# ITEM
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2013-2015
# Licencia: GPLv2

# Importación de librerías de alto nivel
from lib import *  # @UnusedWildImport

# Constantes del programa
ITEMSEPARATOR = "/_/"
_ITEMID = -1

# Items del juego, matriz global que contiene los objetos que se usaran en partidas, estos son predefinidos.
# Ver documentacion (objetos.txt)
ITEMS = {
    # ID
    # NOMBRE,DESCRIPCION,TEXTURA,TIPO,_ITEMID,STACKABLE,VIDA/USOS,PROPIEDADES
    1: ["Espada de diamantes", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right", _ITEMID,
        False, 25, [100, 0]], \
    2: ["Espada de diamantes", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right", _ITEMID,
        False, 50, [100, 0]], \
    3: ["Espada de diamantes", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right", _ITEMID,
        False, 75, [100, 0]], \
    4: ["Espada de diamantes", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right", _ITEMID,
        False, 100, [100, 0]], \
    5: ["Espada de diamantes", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right", _ITEMID,
        False, 150, [100, 0]], \
    6: ["Espada de diamantes", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right", _ITEMID,
        False, 200, [100, 0]], \
    7: ["Espada de diamantes", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right", _ITEMID,
        False, 250, [100, 0]], \
    10: ["Espada de diamantes superior", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 25, [200, 0]], \
    11: ["Espada de diamantes superior", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 50, [200, 0]], \
    12: ["Espada de diamantes superior", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 75, [200, 0]], \
    13: ["Espada de diamantes superior", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 100, [200, 0]], \
    14: ["Espada de diamantes superior", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 150, [200, 0]], \
    15: ["Espada de diamantes debil", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 25, [50, 0]], \
    16: ["Espada de diamantes debil", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 50, [50, 0]], \
    17: ["Espada de diamantes debil", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 75, [50, 0]], \
    18: ["Espada de diamantes debil", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 100, [50, 0]], \
    19: ["Espada de diamantes debil", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 150, [50, 0]], \
    20: ["Espada de diamantes debil", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 200, [50, 0]], \
    21: ["Espada de diamantes debil", "Potente espada forjada en finos diamantes", "espada_diamante", "weapon/right",
         _ITEMID, False, 250, [50, 0]], \
    23: ["Flecha de Hierro debil", "Flecha compuesta por una gruesa punta de hierro forjado, muy util a distancia",
         "flecha_hierro", "bullet", _ITEMID, True, 1, [10, 0]], \
    24: ["Flecha de Hierro", "Flecha compuesta por una gruesa punta de hierro forjado, muy util a distancia",
         "flecha_hierro", "bullet", _ITEMID, True, 1, [20, 0]], \
    25: ["Flecha de Hierro", "Flecha compuesta por una gruesa punta de hierro forjado, muy util a distancia",
         "flecha_hierro", "bullet", _ITEMID, True, 1, [30, 0]], \
    26: ["Flecha de Hierro superior", "Flecha compuesta por una gruesa punta de hierro forjado, muy util a distancia",
         "flecha_hierro", "bullet", _ITEMID, True, 1, [40, 0]], \
    27: ["Flecha de Hierro superior", "Flecha compuesta por una gruesa punta de hierro forjado, muy util a distancia",
         "flecha_hierro", "bullet", _ITEMID, True, 1, [50, 0]], \
    28: ["Flecha de Diamante debil", "Flecha compuesta por extraños y muy filudos diamantes, mortifero a distancia",
         "flecha_diamante", "bullet", _ITEMID, True, 1, [40, 0]], \
    29: ["Flecha de Diamante", "Flecha compuesta por extraños y muy filudos diamantes, mortifero a distancia",
         "flecha_diamante", "bullet", _ITEMID, True, 1, [50, 0]], \
    30: ["Flecha de Diamante", "Flecha compuesta por extraños y muy filudos diamantes, mortifero a distancia",
         "flecha_diamante", "bullet", _ITEMID, True, 1, [60, 0]], \
    31: ["Flecha de Diamante", "Flecha compuesta por extraños y muy filudos diamantes, mortifero a distancia",
         "flecha_diamante", "bullet", _ITEMID, True, 1, [70, 0]], \
    32: ["Flecha de Diamante superior", "Flecha compuesta por extraños y muy filudos diamantes, mortifero a distancia",
         "flecha_diamante", "bullet", _ITEMID, True, 1, [80, 0]], \
    33: ["Manzana podrida", "Sabrosas manzanas de Antair", "manzana_simple", "potion/apple", _ITEMID, True, 1, [10, 0]], \
    34: ["Manzana comun", "Sabrosas manzanas de Antair", "manzana_simple", "potion/apple", _ITEMID, True, 1, [25, 0]], \
    35: ["Manzana exquisita", "Sabrosas manzanas de Antair", "manzana_simple", "potion/apple", _ITEMID, True, 1,
         [50, 0]], \
    36: ["Manzana superior", "Sabrosas manzanas de Antair", "manzana_simple", "potion/apple", _ITEMID, True, 1,
         [100, 0]], \
    37: ["Arco", "Principal arma del pueblo de Hag, gran alcance pero realiza poco daño", "arco_madera", "weapon/left",
         _ITEMID, False, 50, [40, 0]], \
    38: ["Arco", "Principal arma del pueblo de Hag, gran alcance pero realiza poco daño", "arco_madera", "weapon/left",
         _ITEMID, False, 100, [40, 0]], \
    39: ["Arco", "Principal arma del pueblo de Hag, gran alcance pero realiza poco daño", "arco_madera", "weapon/left",
         _ITEMID, False, 25, [40, 0]], \
    40: ["Arco", "Principal arma del pueblo de Hag, gran alcance pero realiza poco daño", "arco_madera", "weapon/left",
         _ITEMID, False, 75, [40, 0]], \
    41: ["Arco superior", "Principal arma del pueblo de Hag, gran alcance pero realiza poco daño", "arco_madera",
         "weapon/left", _ITEMID, False, 50, [80, 0]], \
    42: ["Arco superior", "Principal arma del pueblo de Hag, gran alcance pero realiza poco daño", "arco_madera",
         "weapon/left", _ITEMID, False, 100, [80, 0]], \
    43: ["Arco superior", "Principal arma del pueblo de Hag, gran alcance pero realiza poco daño", "arco_madera",
         "weapon/left", _ITEMID, False, 25, [80, 0]], \
    44: ["Arco superior", "Principal arma del pueblo de Hag, gran alcance pero realiza poco daño", "arco_madera",
         "weapon/left", _ITEMID, False, 75, [80, 0]], \
    45: ["Ballesta",
         "La ballesta, originaria de Fieregarr, muy poderosa y efectiva, aunque generalmente de poca duración",
         "ballesta_oro", "weapon/left", _ITEMID, False, 25, [50, 0]], \
    46: ["Ballesta",
         "La ballesta, originaria de Fieregarr, muy poderosa y efectiva, aunque generalmente de poca duración",
         "ballesta_oro", "weapon/left", _ITEMID, False, 25, [60, 0]], \
    47: ["Ballesta",
         "La ballesta, originaria de Fieregarr, muy poderosa y efectiva, aunque generalmente de poca duración",
         "ballesta_oro", "weapon/left", _ITEMID, False, 25, [70, 0]], \
    48: ["Ballesta superior",
         "La ballesta, originaria de Fieregarr, muy poderosa y efectiva, aunque generalmente de poca duración",
         "ballesta_oro", "weapon/left", _ITEMID, False, 25, [80, 0]], \
    49: ["Ballesta superior",
         "La ballesta, originaria de Fieregarr, muy poderosa y efectiva, aunque generalmente de poca duración",
         "ballesta_oro", "weapon/left", _ITEMID, False, 25, [90, 0]], \
    50: ["Ballesta superior",
         "La ballesta, originaria de Fieregarr, muy poderosa y efectiva, aunque generalmente de poca duración",
         "ballesta_oro", "weapon/left", _ITEMID, False, 25, [100, 0]], \
    51: ["Biblia", "Texto sagrado", "biblia_1", "object/holy", _ITEMID, False, 1, ["Libro", "Mana"]], \
    52: ["Biblia eterna", "Texto sagrado", "biblia_1", "object/holy", _ITEMID, False, 1, ["Libro", "Mana"]], \
    53: ["Biblia destruida", "Texto sagrado, posiblemente ha sufrido daños por la guerra", "biblia_1", "object/holy",
         _ITEMID, False, 1, ["Libro", "Mana"]], \
    54: ["Botas de cuero dañadas",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_cuero", "armor/botas", _ITEMID, False, 25, [0, 10]], \
    55: ["Botas de cuero dañadas",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_cuero", "armor/botas", _ITEMID, False, 25, [0, 20]], \
    56: ["Botas de cuero",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_cuero", "armor/botas", _ITEMID, False, 50, [0, 30]], \
    57: ["Botas de cuero",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_cuero", "armor/botas", _ITEMID, False, 50, [0, 50]], \
    58: ["Botas de cuero superiores",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_cuero", "armor/botas", _ITEMID, False, 100, [0, 60]], \
    59: ["Botas de cuero superiores",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_cuero", "armor/botas", _ITEMID, False, 100, [0, 90]], \
    60: ["Botas de diamante dañadas",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_diamante", "armor/botas", _ITEMID, False, 25, [0, 40]], \
    61: ["Botas de diamante dañadas",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_diamante", "armor/botas", _ITEMID, False, 25, [0, 50]], \
    62: ["Botas de diamante",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_diamante", "armor/botas", _ITEMID, False, 50, [0, 90]], \
    63: ["Botas de diamante",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_diamante", "armor/botas", _ITEMID, False, 50, [0, 100]], \
    64: ["Botas de diamante superiores",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_diamante", "armor/botas", _ITEMID, False, 100, [0, 150]], \
    65: ["Botas de diamante superiores",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_diamante", "armor/botas", _ITEMID, False, 100, [0, 175]], \
    66: ["Botas de hierro dañadas",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_hierro", "armor/botas", _ITEMID, False, 25, [0, 20]], \
    67: ["Botas de hierro dañadas",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_hierro", "armor/botas", _ITEMID, False, 25, [0, 40]], \
    68: ["Botas de hierro",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_hierro", "armor/botas", _ITEMID, False, 50, [0, 60]], \
    69: ["Botas de hierro",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_hierro", "armor/botas", _ITEMID, False, 90, [0, 70]], \
    70: ["Botas de hierro superiores",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_hierro", "armor/botas", _ITEMID, False, 100, [0, 100]], \
    71: ["Botas de hierro superiores",
         "Las botas permiten caminar más comodo, protegerse de los enemigos terrestres y evitar daños por flechas",
         "botas_hierro", "armor/botas", _ITEMID, False, 100, [0, 110]], \
    72: ["Espada de Madera", "Una simple espada, construida en madera de roble", "espada_madera", "weapon/right",
         _ITEMID, False, 25, [25, 0]], \
    73: ["Espada de Madera", "Una simple espada, construida en madera de roble", "espada_madera", "weapon/right",
         _ITEMID, False, 25, [50, 0]], \
    74: ["Espada de Madera", "Una simple espada, construida en madera de roble", "espada_madera", "weapon/right",
         _ITEMID, False, 25, [75, 0]], \
    75: ["Espada de Madera", "Una simple espada, construida en madera de roble", "espada_madera", "weapon/right",
         _ITEMID, False, 25, [100, 0]], \
    76: ["Espada de Madera superior", "Una simple espada, construida en madera de roble", "espada_madera",
         "weapon/right", _ITEMID, False, 50, [25, 0]], \
    77: ["Espada de Madera superior", "Una simple espada, construida en madera de roble", "espada_madera",
         "weapon/right", _ITEMID, False, 50, [50, 0]], \
    78: ["Espada de Madera superior", "Una simple espada, construida en madera de roble", "espada_madera",
         "weapon/right", _ITEMID, False, 50, [75, 0]], \
    79: ["Espada de Madera superior", "Una simple espada, construida en madera de roble", "espada_madera",
         "weapon/right", _ITEMID, False, 50, [100, 0]], \
}

for i in ITEMS.keys():
    ITEMS[i][4] = i  # se agrega el id a cada item


def lookType(a):
    """
    Función interna que reconoce el tipo de dato y devuelve un patron interno
    :param a: String
    :return: String formateado
    """
    a = str(a)
    if a == "True" or a == "False":
        return "boo_" + a  # Comprueba si el dato es booleano
    elif a.isdigit():
        return "int_" + a  # comprueba si es un dato numerico
    elif a.replace(".", "").isdigit():
        return "flt_" + a  # comprueba si es un numero flotante
    else:
        return "str_" + replaceStrict(a)  # si no es solo texto


class Item:
    """Items"""

    def __init__(self, prop):
        """
        Función constructora
        :param prop: Propiedades del item
        :return: void
        """
        (nombre, descripcion, imagen, tipo, id_item,
         stackable, life, propiedades) = prop
        self.descripcion = descripcion  # descripción del item
        self.id = id_item  # identificador del item
        self.imagen = imagen  # imágen del item
        self.nombre = nombre  # nombre del item
        self.propiedades = propiedades  # propiedades del item
        self.stack = stackable  # define si el item es apilable
        self.tipo = tipo  # define el tipo de item
        self.usos = life  # usos (vida) del item

    def getImage(self):
        """
        Devolver la imagen
        :return: String
        """
        return self.imagen

    def getName(self):
        """
        Devolver el nombre
        :return: String
        """
        return self.nombre

    def getDescription(self):
        """
        Devolver la descripción
        :return: String
        """
        return self.descripcion

    def getId(self):
        """
        Devolver el id
        :return: Integer
        """
        return self.id

    def getPropiedades(self):
        """
        Devolver las propiedades
        :return: List
        """
        return self.propiedades

    def isStackable(self):
        """
        Preguntar si es apilable
        :return: Boolean
        """
        return self.stack

    def getType(self):
        """
        Devolver el tipo
        :return: String
        """
        return self.tipo

    def getUsos(self):
        """
        Devolver los usos restantes
        :return: Integer
        """
        return self.usos

    def subirUsos(self, usos):
        """
        Aumentar la cantidad de usos disponibles
        :param usos: Usos
        :return: void
        """
        self.usos += usos

    def usar(self):
        """
        Usar unitariamente el objeto
        :return: void
        """
        self.usos -= 1

    def estaDestruido(self):
        """
        Pregunta si el objeto ya está destruido
        :return: Boolean
        """
        if self.usos <= 0:
            return True
        else:
            return False

    def getDamage(self):
        """
        Devolver el damage
        :return: Integer 0, +inf
        """
        if not self.estaDestruido():
            return self.propiedades[0]
        else:
            return 0

    def getDefense(self):
        """
        Obtener la protección
        :return: Integer 0, +inf
        """
        if not self.estaDestruido():
            return self.propiedades[1]
        else:
            return 0

    def getPDV(self):
        """
        Obtener los puntos de restauración de una poción
        :return: Integer
        """
        return self.propiedades[0]

    def getTypePotion(self):
        """
        Obtener el tipo de pocion
        :return: String
        """
        return self.propiedades[1]

    def getTipoObjeto(self):
        """
        Obtener el tipo de objeto
        :return: String
        """
        return self.propiedades[0]

    def getBookLink(self):
        """
        Obtener el tipo de objeto
        :return: String
        """
        return self.propiedades[0]

    def getUtilidad(self):
        """
        Obtener el uso de algún objeto
        :return: String
        """
        return self.propiedades[1]

    def export(self):
        """
        Función que exporta todos los datos de objeto
        :return: String
        """
        return replaceStrict(str(self.nombre)) + ITEMSEPARATOR + replaceStrict(
            str(self.descripcion)) + ITEMSEPARATOR + str(self.imagen) + \
            ITEMSEPARATOR + str(self.tipo) + ITEMSEPARATOR + str(self.id) + ITEMSEPARATOR + str(
            self.stack) + ITEMSEPARATOR + \
            str(self.usos) + ITEMSEPARATOR + lookType(self.propiedades[0]) + ITEMSEPARATOR + lookType(
            self.propiedades[1]) + "\n"
