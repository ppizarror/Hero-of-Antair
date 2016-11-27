# coding=utf-8
#
# Poderes del jugador

# POWERS
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2014-2015
# Licencia: GPLv2

# Constantes del programa
POWERSEP = ";"
_POWERID = -1

# Poderes del juego
POWERLIST = {
    # ID     NOMBRE SHORT DESCRIPCION ID IMAGEN NIVEL TIEMPO MANA (0=UNICO)
    0: ["Escape rápido", "escrap",
        "Permite escapar rápidamente de cualquier enemigo", _POWERID,
        "fastescape", 1, 0,
        10],
    1: ["Regenerar vida", "revida",
        "Tu vida se regenerará en un periodo de tiempo", _POWERID, "regvida",
        3, 3, 15],
    2: ["Regenerar mana", "remana",
        "Tu mana se regenerará en un periodo de tiempo", _POWERID, "regmana",
        3, 3, 0],
    3: ["Doblar XP", "dobxp", "Ganarás el doble de xp en un periodo de tiempo",
        _POWERID, "doblxp", 4, 2, 20],
    4: ["Doble daño", "dobdam",
        "Tus ataques se duplicarán en un periodo de tiempo", _POWERID,
        "dobdam", 5, 2, 25],
    5: ["Doble defensa", "dobdef",
        "Tu defensa se duplicará en un periodo de tiempo", _POWERID, "dobdef",
        5, 3, 25],
    6: ["Muerte instantánea", "instkill", "El enemigo morirá instantáneamente",
        _POWERID, "inskill", 6, 0, 50],
    7: ["50% de descuento", "halfdesc",
        "Los precios de las tiendas bajarán a la mitad por un periodo de tiempo",
        _POWERID, "halfdesc", 6, 1, 50],
    8: ["Congelar enemigos", "freeze",
        "Los enemigos no se moverán por un periodo de tiempo", _POWERID,
        "freeze", 5, 2,
        50],
    9: ["Armas extra duras", "infweapon",
        "Las armas no sufrirán de daños por un periodo de tiempo", _POWERID,
        "infweapon", 4, 3, 50],
    10: ["Robar y matar", "robym",
         "Qué tal si le robamos, y lo desaparecemos?", _POWERID, "robym", 2, 0,
         50],
    11: ["Como un dios", "god",
         "Serás un dios en la tierra por un periodo de tiempo", _POWERID,
         "god", 12, 4, 100],
    12: ["Reparar armas", "repwep", "Armas reparadas, qué mejor?", _POWERID,
         "repwep", 2, 0, 75],
    13: ["Reparar armadura", "reparm", "Armadura reparada, nada mejor",
         _POWERID, "reparm", 2, 0, 75],
    14: ["Reparar todo", "repall", "Todo se repara al instante, y sin costo",
         _POWERID, "repall", 7, 0, 100],
    15: ["Super regeneración", "fullreg", "Tu vida al máximo", _POWERID,
         "fullreg", 4, 0, 80],
    16: ["Super mana", "fullmana", "Tu mana al máximo", _POWERID, "fullmana",
         4, 0, 0],
    17: ["Subir de nivel", "uplevel", "Ganar xp es para los débiles", _POWERID,
         "upexp", 1, 0, 100],
    18: ["Cambiar de forma", "newform", "Tu forma cambiará a una aleatoria",
         _POWERID, "newform", 1, 0, 100]
}
for i in POWERLIST.keys():
    POWERLIST[i][3] = i  # se agrega el id a cada poder


class Power(object):
    """Poderes"""

    def __init__(self, data):
        """
        Función constructora
        :param data: Datos del poder
        :return:
        """
        (nombre, short, descripcion, i_d, imagen, nivel, tiempo, mana) = data
        self.descripcion = descripcion  # descripción del poder
        self.id = int(i_d)  # identificador del poder
        self.imagen = imagen  # imagen del poder
        self.mana = int(mana)  # mana del poder
        self.nivel = int(nivel)  # nivel requerido del poder
        self.nombre = nombre  # tiempo del poder
        self.short = short  # nombre clave del poder
        self.tiempo = int(tiempo)  # tiempo máximo del poder

    def getName(self):
        """
        Obtener el nombre
        :return: String
        """
        return self.nombre

    def getShort(self):
        """
        Obtener la identificación por nombre
        :return: String
        """
        return self.short

    def getDescripcion(self):
        """
        Obtener la descripción
        :return: String
        """
        return self.descripcion

    def getId(self):
        """
        Obtener la id
        :return: Integer
        """
        return self.id

    def getImage(self):
        """
        Obtener la imagen
        :return: String
        """
        return self.imagen

    def getNivel(self):
        """
        Obtener el nivel del poder
        :return: Integer
        """
        return self.nivel

    def getTime(self):
        """
        Obtener el tiempo de utilidad del poder
        :return: Integer
        """
        return self.tiempo

    # noinspection PyMethodMayBeStatic
    def getSeparator(self):
        """
        Obtener el separador de la información por defecto
        :return: String
        """
        return POWERSEP

    def getReqMana(self):
        """
        Obtener el porcentaje de mana requerido
        :return: Integer
        """
        return self.mana

    def export(self):
        """
        Exportar la información
        :return: String
        """
        return str(self.nombre) + POWERSEP + str(self.short) + POWERSEP + str(
            self.descripcion) + POWERSEP + \
               str(self.id) + POWERSEP + str(self.imagen) + POWERSEP + str(
            self.nivel) + POWERSEP + \
               str(self.tiempo) + POWERSEP + str(self.mana)
