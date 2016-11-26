# coding=utf-8
#
# Tablero para el combate grupal

# BOARD
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2013-2015
# Licencia: GPLv2

# Importación de librerías
from group import *  # @UnusedWildImport
from lib import *  # @UnusedWildImport

# Constantes del programa
BASE_ENEMIES = {"FACIL": 0, "MEDIO": 5, "DIFICIL": 10}
BOARD_LIMIT = [16, 17]  # tamaño máximo del board en (alto,ancho)
CANVAS_SIZE = 608, 576  # tamaño de la ventana de dibujo
COEF_ATK = {"L": 0.5, "M": 0.4, "S": 0.3}  # coeficiente de ataque por tipo
COEF_DEF = {"L": 0.1, "M": 0.3, "S": 0.5}  # coeficiente de defensa por tipo
COEF_MOB = {"HP": 0.12, "TAR": 0.23, "ATK": 0.4,
            "DEF": 0.3, "VEL": 1}  # coeficiente de los mobs
COEF_PLAYER = {"HP": 0.5, "TAR": 0.35, "ATK": 0.4,
               "DEF": 0.5, "VEL": 0}  # coeficiente del jugador
COEF_TAR = {"L": 0.35, "M": 0.22, "S": 0.12}  # coeficiente del target por tipo
COEF_VEL = {"L": {"FACIL": 5, "MEDIO": 4, "DIFICIL": 3}, "M": {"FACIL": 4, "MEDIO": 3, "DIFICIL": 2},
            "S": {"FACIL": 3, "MEDIO": 2, "DIFICIL": 1},
            "P": {"FACIL": 5, "MEDIO": 4, "DIFICIL": 3}}  # indica la cantidad máxima de tiles por movimiento
COEF_VIDA = {"L": 0.1, "M": 0.13, "S": 0.15}  # coeficiente de vida por tipo
ENEMY_COEFICIENT = {"FACIL": 0.875, "MEDIO": 1.050,
                    "DIFICIL": 1.275}  # indica la proporción de enemigos en función de la dificultad
ENEMY_MOVEMENT = {"FACIL": 1, "MEDIO": 2,
                  "DIFICIL": 4}  # movimiento de los mobs
# máxima cantidad de objetos por agrupación
GROUP_MAX_SIZE = {"FACIL": 36, "MEDIO": 27, "DIFICIL": 18}
GROUP_TEXTURE_ARROW = "actor_arrow"  # textura del arco modo ataque flecha
GROUP_TEXTURE_CREW = "actor_groupal_3"  # textura del grupo
LINE_BOARD_COLOR_ACTIVE = "#837A77"  # color activo del board
LINE_BOARD_COLOR_INACTIVE = "#6F6662"  # color inactivo del board
# indica el largo del mapa donde se puede mover por primera vez (el player
# siempre tiene este coeficiente)
MAX_1ST_MOVEMENT = 0.5
MAX_OBSTACLES = 25  # número máximo de obstáculos que puede tener un board
# partición de los grupos por dificultad
PARTITION_PLAYER = {"FACIL": 1.000, "MEDIO": 0.770, "DIFICIL": 0.680}
RECT_CANT_COLOR_BG_F = "#554C49"  # color del fondo del box de los follower
RECT_CANT_COLOR_BG_M = "#553F38"  # color del fondo del box de los mob
RECT_CANT_COLOR_BG_P = "#385944"  # color del fondo del box del jugador
RECT_CANT_COLOR_FG_A = "#542E22"  # color de ataque de fondo del mob
RECT_CANT_COLOR_FG_F = "#ACA4A1"  # color del borde del box de los follower
RECT_CANT_COLOR_FG_M = "#A98E85"  # color del borde del box de los mob
RECT_CANT_COLOR_FG_P = "#A4ABA1"  # color del borde del box del jugador
RECT_CANT_COLOR_TX_F = "#ACA4A1"  # color del texto del box de los follower
RECT_CANT_COLOR_TX_M = "#A98E85"  # color del texto del box de los mob
RECT_CANT_COLOR_TX_P = "#A4ABA1"  # color del texto del box del jugador
TIME_ALERT = 1000  # tiempo en milisegundos donde se muestran los estados numéricos
TURN_AI = 0  # turno de la computadora
TURN_HN = 1  # turno del humano


class board:
    """Clase board"""

    def __init__(self, player, enemies, textureA, textureB, obstacle, iluminacionA, iluminacionB, dificultad,
                 dificultad_coef,
                 image, soundA, soundB, arrowtexture, weapontexture):
        """
        Función constructora
        :param player: Jugador
        :param enemies: Enemigo
        :param textureA: Textura sector A
        :param textureB: Textura sector B
        :param obstacle: Textura de obstáculo
        :param iluminacionA: Luz sector A
        :param iluminacionB: Luz sector B
        :param dificultad: Dificultad
        :param dificultad_coef: Coeficientes dificultad
        :param image: Imagen
        :param soundA: Sonido sector a
        :param soundB: Sonido sector b
        :param arrowtexture: Textura de las flechas
        :param weapontexture: Textura de las armas
        :return:
        """
        self.ai = False  # indica que la computadora controla
        self.aiturno = 0  # indica de quien es el turno para la computadora
        self.bgimage = None  # imagen de fondo del board
        self.blood = []  # mapa de sangre
        self.boardArrow = arrowtexture  # indica la textura de las flechas
        self.boardCorrecion = [0, 0]  # corrección en pixeles del board
        self.boardSize = [0, 0]  # tamaño del board
        self.boardWeapon = weapontexture  # indica la textura del arco
        self.cache = [[], [], [],
                      []]  # almacena el caché de los movimientos válidos, los tags y los ataques con flechas
        self.dificultad = dificultad.upper()  # dificultad del tablero
        self.dificultad_coef = dificultad_coef  # coeficiente de la dificultad
        self.enemies = enemies  # propiedades del enemigo
        self.images = image  # imagen del host
        self.lightA = iluminacionA  # iluminación de la zona player
        self.lightB = iluminacionB  # iluminación de la zona mob
        self.mapitems = []  # mapa de items
        self.maplight = []  # mapa de iluminación
        self.maplogics = []  # mapa de lógicos
        self.mapsound = []  # mapa de sonidos
        self.mobs = []  # lista de enemigos que se generarán
        self.obstacle = obstacle  # textura del obstáculo
        self.player = player  # objeto player
        self.players = []  # lista de amigos que se generarán
        self.soundA = soundA  # sonido textura A
        self.soundB = soundB  # sonido textura B
        self.textureA = textureA.replace("_0", "").replace(
            "_1", "")  # textura de la zona player
        self.textureB = textureB.replace("_0", "").replace(
            "_1", "")  # textura de la zona mob
        self.totalexp = 0  # indica la cantidad de experiencia a recibir tras terminar la partida
        self.turno = 0  # indica de quién es el turno para jugar

    def generate(self):
        """
        Función que genera un board random
        :return: void
        """
        self.generatePlayers()
        self.generateMobs()
        self.generateBoard()
        self.lightBoard()
        self.paintBoard()
        self.putObstacles()
        self.placeFriends()
        self.placeMobs()

    def generatePlayers(self):
        """
        Función que genera las agrupaciones de followers al azar
        :return: void
        """
        # Se obtienen los followers
        light_friends = self.player.getLightFriends()
        medium_friends = self.player.getMediumFriends()
        strong_friends = self.player.getStrongFriends()
        # Se agrega al jugador
        self.players.append(group("PL", 1, self.player.getMaxLife() - self.player.getDamage(),
                                  self.player.getAttack() *
                                  COEF_PLAYER["ATK"] *
                                  (2 - self.dificultad_coef),
                                  self.player.getDefensa(), self.player.getLinkImage(),
                                  True, self.player.getTarget(), COEF_VEL["P"][self.dificultad], "Player"))
        while light_friends > 0:  # Genero grupos de followers livianos
            followers = min(light_friends,
                            random.randint(int(PARTITION_PLAYER[self.dificultad] * GROUP_MAX_SIZE[self.dificultad]),
                                           GROUP_MAX_SIZE[self.dificultad]))
            if followers > 0:
                self.players.append(
                    group("FL", followers, self.player.getMaxLife() * COEF_VIDA["L"] * self.dificultad_coef,
                          self.player.getAttack() *
                          COEF_ATK["L"] * self.dificultad_coef,
                          self.player.getDefensa() *
                          COEF_DEF["L"] * self.dificultad_coef,
                          self.player.getLightImageFriend(), False,
                          self.player.getTarget() *
                          COEF_TAR["L"] * self.dificultad_coef,
                          COEF_VEL["L"][self.dificultad], "Normal"))
                light_friends -= followers
        while medium_friends > 0:  # Genero grupos de followers medios
            followers = min(medium_friends,
                            random.randint(int(PARTITION_PLAYER[self.dificultad] * GROUP_MAX_SIZE[self.dificultad]),
                                           GROUP_MAX_SIZE[self.dificultad]))
            if followers > 0:
                self.players.append(
                    group("FM", followers, self.player.getMaxLife() * COEF_VIDA["M"] * self.dificultad_coef,
                          self.player.getAttack() *
                          COEF_ATK["M"] * self.dificultad_coef,
                          self.player.getDefensa() *
                          COEF_DEF["M"] * self.dificultad_coef,
                          self.player.getMediumImageFriend(), False,
                          self.player.getTarget() *
                          COEF_TAR["M"] * self.dificultad_coef,
                          COEF_VEL["M"][self.dificultad], "Normal"))
                medium_friends -= followers
        while strong_friends > 0:  # Genero grupos de followers pesados
            followers = min(strong_friends,
                            random.randint(int(PARTITION_PLAYER[self.dificultad] * GROUP_MAX_SIZE[self.dificultad]),
                                           GROUP_MAX_SIZE[self.dificultad]))
            if followers > 0:
                self.players.append(
                    group("FS", followers, self.player.getMaxLife() * COEF_VIDA["S"] * self.dificultad_coef,
                          self.player.getAttack() *
                          COEF_ATK["S"] * self.dificultad_coef,
                          self.player.getDefensa() *
                          COEF_DEF["S"] * self.dificultad_coef,
                          self.player.getStrongImageFriend(), False,
                          self.player.getTarget() *
                          COEF_TAR["S"] * self.dificultad_coef,
                          COEF_VEL["S"][self.dificultad], "Normal"))
                strong_friends -= followers

    def generateMobs(self):
        """
        Función que genera las agrupaciones de mobs al azar
        :return: void
        """
        total_friends = (
            self.player.getLightFriends() + self.player.getMediumFriends() + self.player.getStrongFriends()) + \
            BASE_ENEMIES[self.dificultad]
        total_mobs = int(total_friends * ENEMY_COEFICIENT[self.dificultad])
        if self.enemies.getTipoAtaque() == "LARGO":
            large = True
        else:
            large = False
        while total_mobs > 0:  # Genero grupos de followers pesados
            mobs = min(total_mobs,
                       random.randint(int(PARTITION_PLAYER[self.dificultad] * GROUP_MAX_SIZE[self.dificultad]),
                                      GROUP_MAX_SIZE[self.dificultad]))
            self.mobs.append(group("MB", mobs,
                                   self.enemies.getLife() *
                                   COEF_MOB["HP"] * (2 - self.dificultad_coef),
                                   self.enemies.getAtaque() *
                                   COEF_MOB["ATK"] *
                                   (2 - self.dificultad_coef),
                                   self.enemies.getDefensa() *
                                   COEF_MOB["DEF"] *
                                   (2 - self.dificultad_coef),
                                   self.enemies.getImage(), large,
                                   self.enemies.getTarget() *
                                   COEF_MOB["TAR"] *
                                   (2 - self.dificultad_coef),
                                   ENEMY_MOVEMENT[self.dificultad],
                                   self.enemies.getTipoAtaque()))
            total_mobs -= mobs

    def generateBoard(self):
        """
        Función que genera un tablero al azar
        :return: void
        """
        alto = min(BOARD_LIMIT[0], 3 + int(3.00 * int(len(self.players) / 4)) - 2 * int(len(self.players) / 8) - int(
            len(self.players) / 16))
        ancho = min(BOARD_LIMIT[1],
                    2 + int(2.00 * int(len(self.players) / 2)) - int(int(len(self.players) / 4) / 4) - int(
                        len(self.players) / 8) -
                    int(len(self.players) / 16))
        for i in range(alto):  # Creo las matrices del mundo @UnusedVariable
            self.mapitems.append(["None"] * ancho)
            self.maplight.append([0] * ancho)
            self.maplogics.append(["none"] * ancho)
        for i in range(alto + 2):  # @UnusedVariable
            self.mapsound.append([0] * (ancho + 2))
        # se disminuye en 1 dado que ahora se trabaja en matrices
        self.boardSize[0] = alto - 1
        # se disminuye en 1 dado que ahora se trabaja en matrices
        self.boardSize[1] = ancho - 1
        if BOARD_LIMIT[1] > (self.boardSize[1] + 1):
            self.boardCorrecion[0] = (
                BOARD_LIMIT[1] - self.boardSize[1] - 1) * 16 + 32  # Horizontal
        else:
            self.boardCorrecion[0] = 32
        if BOARD_LIMIT[0] > (self.boardSize[0] + 1):
            self.boardCorrecion[1] = (
                BOARD_LIMIT[0] - self.boardSize[0] - 1) * 16 + 32  # Vertical
        else:
            self.boardCorrecion[1] = 32

    def lightBoard(self):
        """
        Función que ilumina el tablero
        :return: void
        """
        last_pos = min(
            int(self.boardSize[1] / 2) + random.randint(-2, 2), self.boardSize[1])
        for i in range(self.boardSize[0] + 1):
            for k in range(0, last_pos):  # Se ilumina el bloque A
                self.maplight[i][k] = self.lightA
            # Se ilumina el bloque B
            for k in range(last_pos, self.boardSize[1] + 1):
                self.maplight[i][k] = self.lightB
            last_pos += random.randint(-2, 2)
            last_pos = min(last_pos, self.boardSize[1])

    def paintBoard(self):
        """
        Función que pinta el tablero
        :return: void
        """
        last_pos = min(
            int(self.boardSize[1] / 2) + random.randint(-2, 2), self.boardSize[1])
        im = Image.new("RGB", ((self.boardSize[1] + 3) * 32, (self.boardSize[0] + 3) * 32),
                       "#000000")  # se crea la imágen de fondo
        # se crea la imágen de fondo
        fim = Image.new("RGB", (CANVAS_SIZE[0], CANVAS_SIZE[1]), "#000000")
        for i in range(self.boardSize[0] + 3):
            for k in range(0, last_pos + 1):  # Se colorea el bloque A
                try:
                    light = str(self.maplight[i][k])
                except:
                    light = str(self.maplight[self.boardSize[0]][k])
                finally:
                    light = str(
                        sum(self.maplight[0]) / (self.boardSize[1] + 1))
                self.mapsound[i][k] = self.soundA
                im.paste(self.images.image(self.textureA + "_" + light),
                         (32 * k, 32 * i, 32 * (k + 1), 32 * (i + 1)))  # se agrega imagen al fondo
            # Se colorea el bloque B
            for k in range(last_pos + 1, self.boardSize[1] + 3):
                try:
                    light = str(self.maplight[i][k])
                except:
                    if i == self.boardSize[0] + 1:
                        light = str(self.maplight[i - 1][k - 2])
                    elif i == self.boardSize[0] + 2:
                        light = str(self.maplight[i - 2][k - 2])
                    else:
                        light = str(self.maplight[i][k - 2])
                self.mapsound[i][k] = self.soundB
                im.paste(self.images.image(self.textureB + "_" + light),
                         (32 * k, 32 * i, 32 * (k + 1), 32 * (i + 1)))  # se agrega imagen al fondo
            last_pos += random.randint(-2, 2)
            last_pos = min(last_pos, self.boardSize[1])
        fim.paste(im, (
            self.boardCorrecion[0] - 32, self.boardCorrecion[1] - 32,
            32 * (self.boardSize[1] + 2) + self.boardCorrecion[0],
            32 * (self.boardSize[0] + 2) + self.boardCorrecion[1]))
        self.bgimage = ImageTk.PhotoImage(fim)
        del fim
        del im

    def putObstacles(self):
        """
        Función que pone obstáculos en el mapa
        :return: void
        """
        if self.dificultad == "FACIL":
            cant = min(MAX_OBSTACLES,
                       int(len(self.players) / 3) + 2 * int(len(self.players) / 8) + int(len(self.players) / 16))
        elif self.dificultad == "MEDIO":
            cant = min(MAX_OBSTACLES, int(len(self.players) / 3) + 2 * int((len(self.players) - 1) / 4) +
                       int(len(self.players) / 8) + int(len(self.players) / 16))
        elif self.dificultad == "DIFICIL":
            cant = min(MAX_OBSTACLES, int(len(self.players) / 3) + 4 * int((len(self.players) - 1) / 4) +
                       2 * int(len(self.players) / 8) + int(len(self.players) / 16))
        pos_obstacles = []
        # noinspection PyUnboundLocalVariable
        for i in range(cant):  # Se agregan cant posiciones @UnusedVariable
            pos_obstacles.append([random.randint(2 + int(len(self.mobs) / 16),
                                                 max(2, self.boardSize[1] - (2 + int(len(self.mobs) / 16)))),
                                  random.randint(0, self.boardSize[0])])
        for pos in pos_obstacles:  # Se agregan elementos a los mapas lógicos y gráficos
            self.maplogics[pos[1]][pos[0]] = "obs"
            self.mapitems[pos[1]][pos[0]] = self.obstacle + \
                "_" + str(self.maplight[pos[1]][pos[0]])
        del pos_obstacles

    def placeFriends(self):
        """
        Función que pega a los followers en el board
        :return: void
        """
        friends_pos = []
        while True:  # genero las posiciones
            if self.dificultad == "FACIL":
                random_pos = [random.randint(0, 1 + int(len(self.mobs) / 16) + int(self.boardSize[1] / 8)),
                              random.randint(0, self.boardSize[0])]
            elif self.dificultad == "MEDIO":
                random_pos = [random.randint(0, 1 + int(len(self.mobs) / 16) + int(self.boardSize[1] / 6)),
                              random.randint(0, self.boardSize[0])]
            elif self.dificultad == "DIFICIL":
                random_pos = [random.randint(0, 1 + int(len(self.mobs) / 16) + int(self.boardSize[1] / 4)),
                              random.randint(0, self.boardSize[0])]
            if random_pos not in friends_pos and self.maplogics[random_pos[1]][
                    random_pos[0]] == "none":
                    # Si la posición random es válida
                    friends_pos.append(random_pos)
            if len(friends_pos) == len(self.players):
                break
        k = 0
        for pos in friends_pos:  # Recorro dichas posiciones y las agrego a la matriz
            follower = self.players[k]
            follower.setPos(pos[0], pos[1])
            self.maplogics[pos[1]][pos[0]] = "player"
            k += 1

    def placeMobs(self):
        """
        Función que pega a los mobs en el board
        :return: void
        """
        mobs_pos = []
        while True:  # genero las posiciones
            if self.dificultad == "FACIL":
                random_pos = [random.randint(self.boardSize[1] - (1 + int(len(self.mobs) / 16)), self.boardSize[1]),
                              random.randint(0, self.boardSize[0])]
            elif self.dificultad == "MEDIO":
                random_pos = [random.randint(self.boardSize[1] - (1 + int(len(self.mobs) / 8)), self.boardSize[1]),
                              random.randint(0, self.boardSize[0])]
            elif self.dificultad == "DIFICIL":
                random_pos = [random.randint(self.boardSize[1] - (1 + int(len(self.mobs) / 4)), self.boardSize[1]),
                              random.randint(0, self.boardSize[0])]
            if random_pos not in mobs_pos and self.maplogics[random_pos[1]][random_pos[0]] == "none":
                mobs_pos.append(
                    random_pos)  # Si la posición random es válida
            if len(mobs_pos) == len(self.mobs):
                break
        k = 0
        for pos in mobs_pos:  # Recorro dichas posiciones y las agrego a la matriz
            mob = self.mobs[k]
            mob.setPos(pos[0], pos[1])
            self.maplogics[pos[1]][pos[0]] = "mob"
            k += 1

    def getBoardSizeX(self):
        """
        Función que retorna el largo del mapa
        :return: Integer
        """
        return self.boardSize[1] + 1

    def getBoardSizeY(self):
        """
        Función que retorna el alto del mapa
        :return: Integer
        """
        return self.boardSize[0] + 1

    def getBoardCorreccionX(self):
        """
        Función que retorna la corrección en X
        :return: Integer
        """
        return self.boardCorrecion[0]

    def modifyBoardCorreccionX(self, val):
        """
        Modifica la corrección en X
        :param val: valor a corregir
        :return:
        """
        self.boardCorrecion[0] += val

    def getBoardCorreccionY(self):
        """
        Función que retorna la corrección en Y
        :return: Integer
        """
        return self.boardCorrecion[1]

    def modifyBoardCorreccionY(self, val):
        """
        Modifica la corrección en Y
        :param val: valor a corregir
        :return:
        """
        self.boardCorrecion[1] += val

    def getItemTexture(self, j, k):
        """
        Retorna la textura del item
        :param j: Pos X
        :param k: Pos Y
        :return: String
        """
        return self.mapitems[k][j]

    def getLight(self, j, k):
        """
        Retorna la iluminación en (j,k)
        :param j: Pos X
        :param k: Pos Y
        :return: 1/0
        """
        return self.maplight[k][j]

    def getLogic(self, j, k):
        """
        Retorna el lógico en (j,k)
        :param j: Pos x
        :param k: Pos Y
        :return: Logic
        """
        return self.maplogics[k][j]

    def setLogic(self, j, k, log):
        """
        Retorna el lógico en (j,k)
        :param j: Pos X
        :param k: Pos Y
        :param log: Logic
        :return: void
        """
        self.maplogics[k][j] = log

    def addTurno(self):
        """
        Aumenta el turno para el jugador
        :return: Boolean
        """
        self.turno += 1
        if self.turno >= len(self.players):
            self.turno = 0
            return True
        else:
            return False

    def addAITurno(self):
        """
        Aumenta el turno para la maquina
        :return: Boolean
        """
        self.aiturno += 1
        if self.aiturno >= len(self.mobs):
            self.aiturno = 0
            self.disableAI()
            return True
        else:
            return False

    def restartTurno(self):
        """
        Reinicia el turno
        :return: void
        """
        self.turno = 0

    def getTurno(self):
        """
        Retorna el turno
        :return: Integer
        """
        return self.turno

    def dropCache(self):
        """
        Destruye el caché
        :return: void
        """
        del self.cache
        self.cache = [[], [], [], []]

    def addCache(self, pos, tag, arrow, arrow_tag):
        """
        Almacena el caché
        :param pos: Posición
        :param tag: Tag del tile
        :param arrow: Flecha
        :param arrow_tag: Tag de la flecha
        :return:
        """
        self.dropCache()
        self.cache[0] = pos
        self.cache[1] = tag
        self.cache[2] = arrow
        self.cache[3] = arrow_tag

    def getAvaiablePos(self):
        """
        Retorna las posiciones válidas del turno
        :return: Pos list
        """
        return self.cache[0]

    def getAvaiableTags(self):
        """
        Retorna el tag de las imágenes de las posiciones válidas
        :return: Tag list
        """
        return self.cache[1]

    def getAvaiableArrow(self):
        """
        Retorna las posiciones válidas del ataque secundario
        :return: Boolean list
        """
        return self.cache[2]

    def getAvaiableArrowTag(self):
        """
        Retorna el tag de las imágens de los ataques secundarios
        :return: Tag list
        """
        return self.cache[3]

    def getEnemies(self):
        """
        Retorna a los enemigos
        :return: List
        """
        return self.mobs

    def getPlayers(self):
        """
        Retorna los players
        :return: List
        """
        return self.players

    def deleteAll(self):
        """
        Se elimina el tablero completo
        :return: void
        """
        self.bgimage = None  # imagen de fondo del board
        self.boardCorrecion = [0, 0]  # corrección en pixeles del board
        self.boardSize = [0, 0]  # tamaño del board
        # almacena el caché de los movimientos válidos y los tags
        self.cache = [[], [], [], []]
        self.mapitems = []  # mapa de items
        self.maplight = []  # mapa de iluminación
        self.maplogics = []  # mapa de lógicos
        self.mapsound = []  # mapa de sonidos
        self.mobs = []  # lista de enemigos que se generarán
        self.players = []  # lista de amigos que se generarán
        self.totalexp = 0  # indica la cantidad de experiencia a recibir tras terminar la partida
        self.turno = 0  # indica de quién es el turno para jugar

    def setTotalExp(self):
        """
        Define la cantidad máxima exp
        :return: void
        """
        self.totalexp = len(self.mobs) * self.enemies.getExp()

    def getTotalExp(self):
        """
        Retorna la cantidad máxima de exp
        :return: Integer
        """
        return self.totalexp

    def getBlood(self):
        """
        Retorna la sangre
        :return: String
        """
        return self.blood

    def addBlood(self, texture, posx, posy):
        """
        Agrega sangre
        :param texture: String
        :param posx: Pos X
        :param posy: Pos Y
        :return: void
        """
        self.blood.append([posx, posy, texture])

    def returnOriginalEnemy(self):
        """
        Retorna el enemigo original
        :return: List
        """
        return self.enemies

    def getAITurno(self):
        """
        Retorna el turno de la computadora
        :return: Boolean
        """
        return self.aiturno

    def enableAI(self):
        """
        Activa a la computadora
        :return: void
        """
        self.ai = True

    def disableAI(self):
        """
        Desactiva la computadora
        :return: void
        """
        self.ai = False

    def returnControl(self):
        """
        Retorna el control del tablero
        :return: Boolean
        """
        return not self.ai

    def getSound(self, i, j):
        """
        Retorna el sonido de el tile (i,j)
        :param i: Pos X
        :param j: Pos Y
        :return: Boolean
        """
        return self.mapsound[j + 1][i + 1]

    def getLeader(self):
        """
        Retorna al lider (personaje principal)
        :return: Player
        """
        return self.players[0]

    def getArrow(self):
        """
        Retorna la textura de las flechas
        :return: String
        """
        return self.boardArrow

    def getWeapon(self):
        """
        Retorna la textura del arma
        :return: String
        """
        return self.boardWeapon
