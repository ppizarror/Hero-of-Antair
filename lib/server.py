#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Servidor para jugar online

# SERVER
# Autor: PABLO PIZARRO @ ppizarro
# Fecha: 2014-2015
# Licencia: GPLv2

import select
import uuid
from lib import *  # @UnusedWildImport

# Importación de librerías
# Constantes del programa
AUTOR_NAME = "Pablo Pizarro"
BUFFER_SIZE = 2000
DELAY = 0
IP_WEB = 'http://httpbin.org/ip'
RESTRICTED_LOBBYNAMES = ['create', 'connect', 'disconnect',
                         'null', '', 'name', 'server', 'ip', 'protocol', 'ping', 'lobby']
SERVER_VERSION = '1.0'

# Variables del programa
online = False
players = {}
public_ip = '0.0.0.0'
server_ip = '0.0.0.0'
local_ip = []

# Funciones principales


def getIPAddresses():
    """
    Obtiene la dirección IP
    :return: void
    """
    from ctypes import Structure, windll, sizeof
    from ctypes import POINTER, byref
    from ctypes import c_ulong, c_uint, c_ubyte, c_char

    MAX_ADAPTER_DESCRIPTION_LENGTH = 128
    MAX_ADAPTER_NAME_LENGTH = 256
    MAX_ADAPTER_ADDRESS_LENGTH = 8

    class IP_ADDR_STRING(Structure):
        pass

    LP_IP_ADDR_STRING = POINTER(IP_ADDR_STRING)
    IP_ADDR_STRING._fields_ = [
        ("next", LP_IP_ADDR_STRING),
        ("ipAddress", c_char * 16),
        ("ipMask", c_char * 16),
        ("context", c_ulong)]

    class IP_ADAPTER_INFO(Structure):
        pass

    LP_IP_ADAPTER_INFO = POINTER(IP_ADAPTER_INFO)
    IP_ADAPTER_INFO._fields_ = [
        ("next", LP_IP_ADAPTER_INFO),
        ("comboIndex", c_ulong),
        ("adapterName", c_char * (MAX_ADAPTER_NAME_LENGTH + 4)),
        ("description", c_char * (MAX_ADAPTER_DESCRIPTION_LENGTH + 4)),
        ("addressLength", c_uint),
        ("address", c_ubyte * MAX_ADAPTER_ADDRESS_LENGTH),
        ("index", c_ulong),
        ("type", c_uint),
        ("dhcpEnabled", c_uint),
        ("currentIpAddress", LP_IP_ADDR_STRING),
        ("ipAddressList", IP_ADDR_STRING),
        ("gatewayList", IP_ADDR_STRING),
        ("dhcpServer", IP_ADDR_STRING),
        ("haveWins", c_uint),
        ("primaryWinsServer", IP_ADDR_STRING),
        ("secondaryWinsServer", IP_ADDR_STRING),
        ("leaseObtained", c_ulong),
        ("leaseExpires", c_ulong)]
    GetAdaptersInfo = windll.iphlpapi.GetAdaptersInfo
    GetAdaptersInfo.restype = c_ulong
    GetAdaptersInfo.argtypes = [LP_IP_ADAPTER_INFO, POINTER(c_ulong)]
    # noinspection PyCallingNonCallable
    adapterList = (IP_ADAPTER_INFO * 10)()
    buflen = c_ulong(sizeof(adapterList))
    rc = GetAdaptersInfo(byref(adapterList[0]), byref(buflen))
    if rc == 0:
        for a in adapterList:
            adNode = a.ipAddressList
            while True:
                ipAddr = adNode.ipAddress
                if ipAddr:
                    yield ipAddr
                adNode = adNode.next
                if not adNode:
                    break


class Server:
    """
    Clase server
    """

    def __init__(self, host, port):
        """
        Función constructora, toma por parámetro un host y un puerto
        :param host: Host
        :param port: Puerto
        :return: void
        """
        self.channel = {}
        self.input_list = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(200)

    def main_loop(self):
        """
        Bucle principal
        :return: void
        """
        self.input_list.append(self.server)
        while True:
            time.sleep(DELAY)
            inputr, outputr, exceptr = select.select(self.input_list, [], [])  # @UnusedVariable
            for self.s in inputr:
                if self.s == self.server:
                    self.on_accept()
                    break
                else:
                    try:
                        # noinspection PyAttributeOutsideInit
                        self.data = self.s.recv(BUFFER_SIZE)
                    except:
                        pass
                if len(self.data) == 0:
                    self.on_close()
                else:
                    self.on_recv()

    def on_accept(self):
        """
        Acepta a un cliente
        :return: void
        """
        clientsock, clientaddr = self.server.accept()
        print "\t" + str(clientaddr) + " se ha conectado"
        players[clientaddr[1]] = {}
        self.input_list.append(clientsock)

    def on_close(self):
        """
        Cierra la conexión con un cliente
        :return: void
        """
        clientaddr = self.s.getpeername()
        print "\tEl usuario %s se ha desconectado" % clientaddr[1]
        del (players[clientaddr[1]])
        self.input_list.remove(self.s)

    def on_recv(self):
        """
        Recibe la consulta de un cliente
        :return:
        """
        _id = self.s.getpeername()[1]
        print "\tUsuario %s realizo una consulta" % _id
        try:
            players[_id] = simplejson.loads(self.data)
            self.s.send(simplejson.dumps(players))
        except:
            print "\tEl usuario %s ha cerrado la conexion" % _id
            self.s.getpeername()
            del (players[_id])
            self.input_list.remove(self.s)


class Lobby:
    """
    Clase lobby
    """

    def __init__(self, lobbyname, lobbyhost, lobbyid, lobbymap, lobbymobs, lobbynpc, lobbytextures, lobbyplayers):
        """
        Función constructora
        :param lobbyname: Nombre
        :param lobbyhost: Host
        :param lobbyid: ID
        :param lobbymap: Mapa
        :param lobbymobs: Mobs
        :param lobbynpc: Ncpc's
        :param lobbytextures: Texturas
        :param lobbyplayers: Jugadores
        :return: void
        """
        self.lobbyhost = lobbyhost  # host del lobby, str
        self.lobbyid = lobbyid  # id del lobby (hex), str
        self.lobbymap = lobbymap  # mapa del lobby, str
        self.lobbymobs = lobbymobs  # mobs del lobby, list
        self.lobbyname = lobbyname  # nombre del loby, str
        self.lobbynpc = lobbynpc  # npc's del lobbby, list
        self.lobbyplayers = lobbyplayers  # jugadores del lobby, list
        self.lobbytextures = lobbytextures  # texturas del lobby, list

    def __cmp__(self, lobby):
        """
        Compara un lobby con otro
        :param lobby: Lobby secundario
        :return: Boolean
        """
        if self.lobbyhost == lobby.lobbyhost:
            if self.lobbyid == lobby.lobbyid:
                if self.lobbymap == lobby.lobbymap:
                    if self.lobbymobs == lobby.lobbymobs:
                        if self.lobbyname == lobby.lobbyname:
                            if self.lobbynpc == lobby.lobbynpc:
                                if self.lobbytextures == lobby.lobbytextures:
                                    if self.lobbyplayers == lobby.lobbyplayers:
                                        return True
        return False

    def generateId(self):
        """
        Genera un nuevo id
        :return: void
        """
        self.lobbyid = uuid.uuid4().hex

    def getHost(self):
        """
        Retorna el host del lobby
        :return: String
        """
        return self.lobbyhost

    def getId(self):
        """
        Retorna el id del lobby
        :return: String
        """
        return self.lobbyid

    def getMap(self):
        """
        Retorna el mapa del lobby
        :return: String
        """
        return self.lobbymap

    def getMobs(self):
        """
        Retorna los mobs del lobby
        :return: List
        """
        return self.lobbymobs

    def getName(self):
        """
        Retorna el nombre del lobby
        :return: String
        """
        return self.lobbyname

    def getNpc(self):
        """
        Retorna los npc del lobby
        :return: List
        """
        return self.lobbynpc

    def getTextures(self):
        """
        Retorna las texturas del lobby
        :return: List
        """
        return self.lobbytextures


def returnNullLobby():
    """
    Retorna el lobby null
    :return: Lobby nulo
    """
    return Lobby("null", "null", "0", "null", [], [], [], [])


def isNullLobby(lobby):
    """
    Retorna si es un lobby nulo
    :param lobby: Boolean
    :return:
    """
    nulllby = returnNullLobby()
    return nulllby.__cmp__(lobby)


if __name__ == '__main__':
    printAsciiArtServer()  # logo del programa
    colorcmd("\nHOA Server - version: " + SERVER_VERSION, "red")
    print "\nAutor: " + AUTOR_NAME
    print "Pulse Ctrl-C para cerrar el servidor\n"
    try:
        print "Obtiendo ip local ...",
        for addr in getIPAddresses():
            if addr != "0.0.0.0":
                local_ip.append(addr)
        if len(local_ip) != 0:
            print "ok"
        else:
            print "error, definiendo ip del servidor: 127.0.0.1"
            server_ip == "127.0.0.1"  # @NoEffect
    except:
        print "error, definiendo ip del servidor: 127.0.0.1"
        server_ip == "127.0.0.1"  # @NoEffect
    try:
        print "Obteniendo ip publica ...",
        public_ip = json.load(urlopen(IP_WEB))['origin']
        print "ok"
        online = True
    except:
        print "sin conexion"

    # Se configura la ip del servidor
    if server_ip != "127.0.0.1":
        if online:
            print "\nElija modo de servidor:\n\t1) Local\n\t2) Publico\t"
            while True:
                modo = raw_input("\tOpcion: ")
                if modo.isdigit():
                    if modo == "1":
                        if len(local_ip) == 1:
                            server_ip = local_ip[0]
                            break
                        else:
                            print "\n\tElija ip local:"
                            for i in range(len(local_ip)):
                                print "\t\t" + str(i + 1) + ") " + local_ip[i]
                            print "\t\t" + str(len(local_ip) + 1) + ") Volver"
                            while True:
                                modo = raw_input("\t\tOpcion: ")
                                if modo.isdigit():
                                    modo = int(modo)
                                    if 0 <= modo - 1 < len(local_ip):
                                        server_ip = local_ip[modo - 1]
                                        break
                                    elif modo == len(local_ip) + 1:
                                        break
                                    else:
                                        print "\t\t\tError :: Opcion no valida"
                                else:
                                    print "\t\t\tError :: La opcion solo es numerica"
                            if server_ip != "0.0.0.0":
                                break
                    elif modo == "2":
                        server_ip = public_ip
                        break
                    else:
                        print "\tError :: Opcion no valida"
                else:
                    print "\t\tError :: La opcion solo es numerica"
        else:
            if len(local_ip) == 1:
                server_ip = local_ip[0]
            else:
                print "\nElija ip local:"
                for i in range(len(local_ip)):
                    print "\t" + str(i + 1) + ") " + local_ip[i]
                while True:
                    modo = raw_input("\tOpcion: ")
                    if modo.isdigit():
                        modo = int(modo)
                        if 0 <= modo - 1 < len(local_ip):
                            server_ip = local_ip[modo - 1]
                            break
                        else:
                            print "\t\tError :: Opcion no valida"
                    else:
                        print "\t\tError :: La opcion solo es numerica"
    print ""

    # Se obtiene el puerto de la conexión
    while True:
        port = raw_input("Ingrese el puerto: ")
        if port.isdigit():
            port = int(port)
            if 0 <= port:
                break
            else:
                print "\tError :: El puerto no puede ser negativo"
        else:
            print "\tError :: El puerto es un digito mayor o igual que 0"

    # Se inicia el servidor
    print "\nIniciando servidor en '{0}:{1}' ...".format(server_ip, str(port)),
    try:
        server = Server(server_ip, port)
        print "ok"
    except:
        print "error"
        exit()
    print "Escuchando:"
    try:
        server.main_loop()
    except KeyboardInterrupt:
        print "Ctrl C - deteniendo servidor"
        sys.exit(1)
